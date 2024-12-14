# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import UserError


class ResUsers(models.Model):
    _inherit = "res.users"

    def compute_has_purchase_groups(self):
        self.has_purchase_groups = self.has_group(
            "purchase.group_purchase_manager"
        ) or self.has_group("purchase.group_warning_purchase")

    national_purchase = fields.Boolean()
    foreign_purchase = fields.Boolean()
    has_purchase_groups = fields.Boolean(compute="compute_has_purchase_groups")
