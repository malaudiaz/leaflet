# -*- coding: utf-8 -*-
{
    'name': "leaflet",
    "description": "Leaflet Map View",    
    'version': '17.0.1.0.0',
    'summary': """ Table Summary Leaflet Map """,
    'author': '',
    'website': '',
    'category': '',
    'depends': ['base', 'web'],
    'assets': {
        'web.assets_backend': [
            'leaflet/static/src/**/*'
        ],
    },
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3'
}
