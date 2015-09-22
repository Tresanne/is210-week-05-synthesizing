#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01"""

import datetime

CURDATE = None


def get_current_date():
    """Docstring explaining the get_current_date function.

    Args:
        func(): get_current_date function will be used to give the current date.

    Returns:
         int(): returns the current date.

    Examples:
        >>>import task_01
        >>>print task_01.CURDATE
        None
        >>> print task_01.get_current_date()
        2015-09-22
    """
    return datetime.date.today()

if __name__ == '__main__':
    CURDATE = get_current_date()
    print CURDATE
