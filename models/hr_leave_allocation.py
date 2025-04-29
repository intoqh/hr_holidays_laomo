from odoo import api, fields, models, tools
import xlrd
import base64
from odoo.exceptions import ValidationError
from datetime import datetime, date, timedelta
from odoo.tools.translate import _

class HolidaysAllocation(models.Model):
    _inherit = 'hr.leave.allocation'

    @api.constrains('date_from', 'date_to', 'employee_id')
    def _check_date(self):
        # 增加时间约束
        if self.env.context.get('leave_skip_date_check', False):
            return
        for holiday in self.filtered('employee_id'):
            domain = [
                ('date_from', '<', holiday.date_to),
                ('date_to', '>', holiday.date_from),
                ('employee_id', '=', holiday.employee_id.id),
                ('id', '!=', holiday.id),
                ('state', 'not in', ['cancel', 'refuse']),
            ]
            nholidays = self.search_count(domain)
            if nholidays:
                raise ValidationError(_('同一员工在俩个重叠的时间不能为请假'))

