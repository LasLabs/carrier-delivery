# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class DeliveryCarrier(models.Model):

    _inherit = 'delivery.carrier'

    partner_id = fields.Many2one(
        string='Transporter Company',
        comodel_name='res.partner',
        help='The partner that is doing the delivery service.'
    )
