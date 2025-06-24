{
    'name': 'Intervention',
    'version': '1.0',
    'depends': ['base'],
    'author': 'NetC',
    'category': 'Custom',
    'summary': 'Module de gestion des interventions terrain',
    'data': [
        'security/ir.model.access.csv',
        'views/terrain_views.xml',
        'views/intervention_menu.xml',
        
    ],
    'installable': True,
    'application': True,
}