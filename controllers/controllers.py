import base64
from odoo import http
from odoo.http import request


class TodoTaskController(http.Controller):


    @http.route('/todo/tasks', auth='public', website=True)
    def show_tasks(self):
        tasks = http.request.env['todo.task'].sudo().search([])
        return http.request.render(
            'todotask.task_template_id', {'tasks': tasks}
            )


    @http.route('/todo/task/create', type='http', auth='user', website=True, csrf="False", methods=['GET', 'POST'])
    def create_task(self, **post):
        if http.request.httprequest.method == 'POST':
            name = post.get('name')
            description = post.get('description')
            if name:
                request.env['todo.task'].sudo().create({'name': name, 'description': description})
                return 'yes'
        return http.request.render('todotask.todo_task_form_template')


    # @http.route('/todo/task/<int:self_id>/edit', type='http', auth='user', website=True, methods=['GET', 'POST'])
    # def edit_task(self, self_id, **post):
    #     if http.request.httprequest.method == 'POST':
    #         name = post.get('name')
    #         description = post.get('description')
    #         if name:
    #             self_id.write({'name': name, 'description': description})
    #             return http.redirect_with_hash('/todo/tasks')
    #     return http.request.render('todotask.view_todo_task_form_edit', {'task': self_id})


    @http.route('/todo/task/<string:record_id>/edit', type='http', auth='user', website=True, methods=['GET', 'POST'])
    def edit_task(self, record_id, **post):
        record = request.env['todo.task'].browse(record_id)

        if request.httprequest.method == 'POST':
            # Update the task with the form data
            name = post.get('name')
            description = post.get('description')
            # Update other task fields as needed

            if name:
                record.write({'name': name, 'description': description})
                # Write other field updates here

                return "Task updated successfully!"

        return request.render('todotask.view_todo_task_form_edit', {'record': record})


    # @http.route('/todo/task/<int:record_id>/edit', type='http', auth='user', website=True, methods=['GET', 'POST'])
    # def edit_task(self, record_id):
    #     record = self.env['todo.task'].browse(record_id)
    #     return self.render('todotask.view_todo_task_form_edit', {'record': record})


    @http.route('/todo/task/<model("todo.task"):task>/delete', type='http', auth='user', website=True)
    def delete_task(self, task, **post):
        task.unlink()
        return http.redirect_with_hash('/todo/tasks')


    @http.route("/user/create", type='http', auth='user', website=True, csrf='False', methods=['GET', 'POST'])
    def create_user(self, **post):
        if http.request.httprequest.method == 'POST':
            name = post.get('name')
            login = post.get('login')
            image_1920 = post.get('image_1920')
            if image_1920:
                image_data = image_1920.read()
                encoded_image = base64.b64encode(image_data).decode('utf-8')
            else:
                image_data = None
            if name:
                request.env['res.users'].sudo().create({'name': name, 'login': login, 'image_1920': encoded_image})
                return "User created successfully!"
        return http.request.render('todotask.user_form_template')

    # @http.route("/partner/create", type='http', auth='user', website=True, csrf='False', methods=['GET', 'POST'])
    # def create_partner(self, **post):
    #     if http.request.httprequest.method == 'POST':
    #         name = post.get('name')
    #         email = post.get('email')
    #         if name:
    #             request.env['res.partner'].sudo().create({'name': name, 'email': email})
    #             return http.redirect_with_hash('/')
    #     return http.request.render('todotask.partner_form_template')

    # @http.route(['/appointment/new'], type='http', auth="user", website=True)
    # def appointment(self):
    #     partners = request.env['res.email'].sudo().search([])
    #     values = {}
    #     values.update({
    #         'partners': partners
    #     })
    #     return request.render("todotask.online_appointment_form", values)


    # @http.route('/todo/task/create', type='http', auth='user', website=True)
    # def create_task(self, **post):
    #     if post.get('name'):
    #         request.env['todo.task'].sudo().create({'name': post.get('name'), 'description': post.get('description')})
    #     return http.redirect_with_hash('/todo/tasks')

    # @http.route('/todo/task/<model("todo.task"):task>/edit', type='http', auth='user', website=True)
    # def edit_task(self, task, **post):
    #     if post.get('name'):
    #         task.write({'name': post.get('name'), 'description': post.get('description')})
    #     return http.redirect_with_hash('/todo/tasks')

# tail -f -n 100 /var/log/odoo/odoo-server.log