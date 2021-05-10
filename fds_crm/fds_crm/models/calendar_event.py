from odoo import models, fields, api


class CalendarEvent_FDS(models.Model):
    _inherit = "calendar.event"
    fds_attendees_custom = fields.Char(string="OnChange Attendees" ,compute='_compute_fds_attendees_custom')
    #attendees_to_display = fields.Text("Attendees TD")

    def _compute_fds_attendees_custom(self):
        for record in self:
            record.fds_attendees_custom = ', '.join(record.partner_ids.mapped('display_name'))
