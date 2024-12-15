# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import UserError


class ResUsers(models.Model):
    _inherit = "res.users"

    def compute_has_purchase_groups(self):
        for rec in self:
            rec.national_purchase = self.sudo(rec).has_group(
                "coinsamatik_supplier_buyer.national_purchase"
            )
            rec.foreign_purchase = self.sudo(rec).has_group(
                "coinsamatik_supplier_buyer.foreign_purchase"
            )

    national_purchase = fields.Boolean(
        compute="compute_has_purchase_groups", store=True
    )
    foreign_purchase = fields.Boolean(compute="compute_has_purchase_groups", store=True)
