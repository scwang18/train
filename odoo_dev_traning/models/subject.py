# -*- coding: uft-8 -*-

from odoo import api, fields, modules

class TrainingSubject(modules.Model):
    _name = 'training.subject'
    _description = "科目"
    
    name = fields.Char(string = '名称')
    person_id = fields.Many2one('res.partener', string='负责人')
    lesson_ids = fields.One2money('training.lesson', 'subject_id', string='课程')
    desc = fields.Text(string='描述')