# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import UserError


class ResUsers(models.Model):
    _inherit = "res.users"

    def compute_has_purchase_groups(self):
        self.national_purchase = self.has_group(
            "coinsamatik_supplier_buyer.national_purchase"
        )
        self.foreign_purchase = self.has_group(
            "coinsamatik_supplier_buyer.foreign_purchase"
        )

    national_purchase = fields.Boolean(compute="compute_has_purchase_groups")
    foreign_purchase = fields.Boolean(compute="compute_has_purchase_groups")
