# -*- coding: utf-8 -*-

from .base import DoubanApiBase, DEFAULT_START, DEFAULT_COUNT

class Book(DoubanApiBase):

    def __repr__(self):
        return '<DoubanAPI Book>'


