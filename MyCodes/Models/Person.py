from odoo import api, fields, models

class ResPartner(models.Model):inherit='res.partner'
    IsTeacher=fields.Boolean(string='教师')
    IsStudent=fields.Boolean(string='学生')