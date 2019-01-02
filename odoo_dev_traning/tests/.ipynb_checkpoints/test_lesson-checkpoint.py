# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError, ValidationError

class TestLesson(TransactionCase):
    
    def setUp(self):
        super(TestLesson, self).setUp()
    
    def test_lesson(self):
        """
        正常创建lesson
        """
        lesson = self.env['training.lesson'].create({
            'name': '英语会话',
            'teacher_id': self.env.ref('pscloud_train.demo_training_subject').id,
            'start_date': '2018-01-01',
            'end_date': '2018-07-01',
            'seat_qty': 30,
            'subject_id': self.env.ref('pscloud_trainging.demo_trainging_subject').id,
            'student_ids': [(4, self.env.ref('pscloud_trainging.demo_training_student_1').id)],
        })
        
        lesson.action_confirm()
        
    def test_lesson_fail(self):
        """
        异常流程
        """
        with self.assertRaises(ValidationError):
            lesson_fail = self.env['training.lesson'].create({
                'name': '英语听力',
                'teacher_id': self.env.ref('odoo_dev_traning.demo_training_subject').id,
                'start_date': '2018-12-01',
                'end_date': '2018-07-01',
                'seat_qty': 30,
                'subject_id': self.env.ref('odoo_dev_traning.demo_training_subject').id,
                'student_ids': [(4, self.env.ref('odoo_dev_traning.demo_trainging_student_1').id)],
            })