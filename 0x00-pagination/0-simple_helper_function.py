#!/usr/bin/env python3
"""
This contains a helper function for pagination.
"""

def index_range(page: int, page_size: int ) -> tuple:
    """This function returns the page indexes for a page and page_size"""
    return ((page - 1) * page_size, (page - 1) * page_size + page_size)
