#!/usr/bin/env python3
"""This is a helper function"""


def index_range(page: int, page_size: int) -> tuple:
    """A function to calcualt ethe start and end of a page"""
    start: int = (page - 1) * page_size
    end: int = page * page_size
    return start, end
