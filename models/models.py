from odoo import models, fields


class TodoTask(models.Model):

    _name = 'todo.task'
    _description = 'To-Do Task'
    _order = 'is_completed, create_date DESC'


    name = fields.Char('Task Name', required=True)
    description = fields.Text('Description')
    is_completed = fields.Boolean('Completed', default=False)


