# -*- coding: utf-8 -*-
"""
    Main entry point
"""

from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.scan("simple_calculator.api.views")
    config.add_route('calculator', 'calculator/')

    return config.make_wsgi_app()
