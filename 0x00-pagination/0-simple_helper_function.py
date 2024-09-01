"""
This contains a helper function for pagination.
"""

def index_range(page, page_size):
    return ((page - 1) * page_size, (page - 1) * page_size + page_size)

print(index_range(1, 7))
