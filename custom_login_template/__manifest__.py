{
    'name': 'Custom Login Template',
    'version': '1.0',
    'author': 'Amir',
    'category': 'Website',
    'depends': ['web'],
    'data': [
        'views/custom_login_template.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'custom_login_template/static/src/img/logo-sac.png',
        ],
    },
    'installable': True,
    'application': False,

}