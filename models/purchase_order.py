# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import UserError


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.onchange("partner_id")
    def onchange_partner_id(self):
        if self.partner_id:
            self.user_id = self.partner_id.purchase_user_id
