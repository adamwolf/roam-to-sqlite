import json
from typing import Iterable

BLOCK_EXTRACTS = {"create-email": "emails", "edit-email": "emails"}
PAGE_EXTRACTS = {"create-email": "emails", "edit-email": "emails"}


def order_generator(iterable: Iterable[dict], order_attr=None):
    """Wrap an iterable of dicts, while setting an incrementing 'order' key on each item"""
    if order_attr is None:
        order_attr = "order"
    order: int = 0

    for i in iterable:
        i[order_attr] = order
        order += 1
        yield i


def add_blocks(db, blocks, parent_block_id=None, parent_page_id=None):
    """Given a sqlite-utils database connection, an ordered list of blocks, and the blocks' parent page or block ID,
    add them to the database.

    @type db: sqlite-utils.Table
    @type blocks: list
    @type parent_page_id: Optional[str]
    @type parent_block_id: Optional[str]
    """
    if not blocks:
        return

    if (parent_page_id is None and parent_block_id is None) or \
            (parent_page_id is not None and parent_block_id is not None):
        raise Exception("Either parent_page_id or parent_block_id must be set.")

    for block in blocks:
        if parent_page_id is not None:
            block['parent_page_id'] = parent_page_id
            block['parent_block_id'] = None
        else:
            block['parent_block_id'] = parent_block_id
            block['parent_page_id'] = None

        if 'children' in block:
            children = block['children']
            del block['children']
            add_blocks(db, children, parent_block_id=block['uid'])
    db["blocks"].upsert_all(order_generator(blocks), pk="uid", extracts=BLOCK_EXTRACTS, alter=True)


def add_page(db, page):
    if 'children' in page:
        children = page['children']
        del page['children']
    else:
        children = None

    pages = db["pages"]
    pages.upsert(page, pk="title", extracts=PAGE_EXTRACTS, alter=True)

    add_blocks(db, children, parent_page_id=pages.last_pk)


def save_roam(db, json_file):
    pages_created = "pages" not in db.table_names()
    blocks_created = "blocks" not in db.table_names()

    if pages_created:
        db["pages"].create({
            "title": str,
            "create-time": int,
            "edit-time": int,
        }, pk="title")

    if blocks_created:
        db["blocks"].create({
            "uid": str,
            "string": str,
            "create-time": int,
            "edit-time": int,
            "heading": int,
            "text-align": str,
            "order": int,
            "parent_block_id": str,
            "parent_page_id": str,
        }, pk="uid",
            foreign_keys=[
                ("parent_page_id", "pages"),
                # ("parent_block_id", "blocks"), # I was not able to add this at table creation time, not sure why.
            ])

        db["blocks"].add_foreign_key("parent_block_id", "blocks", "uid",
                                     ignore=True)

    for page in json.load(json_file):
        add_page(db, page)

    if pages_created:
        db["pages"].enable_fts(["title", ], create_triggers=True)
    if blocks_created:
        db["blocks"].enable_fts(["string", ], create_triggers=True)
