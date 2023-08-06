{
    'name': 'To do Task',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/task_template_id.xml',
        'views/todo_task_form_template.xml',
        'views/user_form_template.xml',
        'views/partner_form_template.xml',
        "views/online_appointment_form.xml",
        'views/view_todo_task_form_edit.xml',
        'views/menu.xml',
    ],
    'demo': [],
    'icon': "todotask/static/done.png",
    'application': True,
    'installable': True,
    'sequence': 6,
    
}
