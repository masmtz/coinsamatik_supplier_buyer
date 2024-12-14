# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import UserError


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    current_user_id = fields.Many2one("res.users", default=lambda self: self.env.user)

    @api.onchange("partner_id")
    def onchange_partner_id(self):
        if self.partner_id:
            self.user_id = self.partner_id.purchase_user_id or False
