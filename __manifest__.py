{
    'name': 'Türkiye Ulusal Adres Veritabanı (TR UAVT)',
    'version': '1.0',
    'category': 'Localization',
    'summary': 'Manage Turkish National Address Database',
    'description': 'Module to manage Turkish National Address Database including cities, counties, districts, villages, neighborhoods, and streets.',
    'author': 'Fime Bilisim Ltd. Sti.',
    'website': 'https://fimeltd.com',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/uavt_ilce_data.xml',
        'views/uavt_ilce_views.xml',
        'views/uavt_koy_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'i18n': ['i18n/tr.po'],
}
