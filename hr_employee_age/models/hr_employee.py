# -*- coding: utf-8 -*-
###############################################################################
#
#    Copyright (C) 2015 Salton Massally (<smassally@idtlabs.sl>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from odoo import api, fields, models
from dateutil.relativedelta import relativedelta


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    age = fields.Integer(
        string='Age',
        readonly=True,
        compute='_compute_age'
    )
    complete_age = fields.Char(
        string='Edad Completa',
        readonly=True,
        compute='_compute_age'
    )

    @api.multi
    @api.depends('birthday')
    def _compute_age(self):
        for record in self:
            if record.birthday:
                resultado = relativedelta(
                    fields.Date.from_string(fields.Date.today()),
                    fields.Date.from_string(record.birthday))
                record.age = resultado.years
                record.complete_age = '{years} A {months} M {days} D'.format(
                    years=resultado.years,
                    months=resultado.months,
                    days=resultado.days
                )
            else:
                record.age = 0
                record.complete_age = '*'
