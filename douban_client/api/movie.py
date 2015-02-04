# -*- coding: utf-8 -*-

from .subject import Subject


class Movie(Subject):

    target = 'movie'

    def __repr__(self):
        return '<DoubanAPI Movie>'

    def celebrity(self, celebrity_id):
        return self._get('/v2/movie/celebrity/%s' % celebrity_id)

    def imdb(self, imdb_id):
        return self._get('/v2/movie/imdb/%s' % imdb_id)

    #/v2/movie/nowplaying
    def nowplaying(self):
        return self._get('/v2/movie/nowplaying')

    #/v2/movie/coming

    def coming(self):
        reuturn self._get('/v2/movie/coming')
