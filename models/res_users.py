# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import UserError


class ResUsers(models.Model):
    _inherit = "res.users"

    national_purchase = fields.Boolean()
    foreign_purchase = fields.Boolean()
