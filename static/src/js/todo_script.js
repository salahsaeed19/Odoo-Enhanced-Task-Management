odoo.define('todotask.todo_script', function (require) {
    "use strict";

    var core = require('web.core');
    var ListController = require('web.ListController');
    var ListRenderer = require('web.ListRenderer');

    var qweb = core.qweb;

    ListController.include({
        /**
         * Override the init function to add custom event listeners
         */
        init: function () {
            this._super.apply(this, arguments);
            this._bindEditButton();
        },

        /**
         * Bind the "Edit" button click event to open the task edit form
         */
        _bindEditButton: function () {
            var self = this;
            this.$el.on('click', '.edit-task-btn', function (event) {
                var taskId = $(event.currentTarget).data('task-id');
                self.do_action({
                    type: 'ir.actions.act_window',
                    name: 'Edit Task',
                    res_model: 'todo.task',
                    res_id: taskId,
                    views: [[false, 'form']],
                    target: 'new',
                });
            });
        },
    });

    ListRenderer.include({
        /**
         * Override the _renderBodyCell function to add "Edit" button to the task name field
         */
        _renderBodyCell: function (record, node, colIndex, options) {
            var $cell = this._super.apply(this, arguments);
            if (node.attrs.name === 'name' && !record.data.is_completed) {
                var taskId = record.data.id;
                var $editButton = $(qweb.render('TodoTaskEditButton', { taskId: taskId }));
                $cell.append($editButton);
            }
            return $cell;
        },
    });

    core.action_registry.add('todo_task_form_edit', {
        controller: 'todo.task',
        renderer: 'todo.task',
    });

    return {
        ListController: ListController,
        ListRenderer: ListRenderer,
    };

});
