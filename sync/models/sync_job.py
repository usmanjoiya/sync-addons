# Copyright 2020 Ivan Yelizariev <https://twitter.com/yelizariev>
# License MIT (https://opensource.org/licenses/MIT).

from odoo import api, fields, models


class SyncJob(models.Model):

    _name = "sync.job"
    _description = "Sync Job"

    trigger_id = fields.Many2one("sync.trigger")
