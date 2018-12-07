from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    is_teacher = fields.Boolean(string='教师')
    is_student = fields.Boolean(string='学生')