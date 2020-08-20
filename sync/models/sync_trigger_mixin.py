# Copyright 2020 Ivan Yelizariev <https://twitter.com/yelizariev>
# License MIT (https://opensource.org/licenses/MIT).

from odoo import api, fields, models


class SyncTriggerMixin(models.AbstractModel):

    _name = "sync.trigger.mixin"
    _description = "Mixing for trigger models"
    _rec_name = "trigger_name"
    _default_name = None

    trigger_name = fields.Char(
        "Trigger Name", help="Technical name to be used in task code", required=True
    )
    job_ids = fields.One2many("sync.job", "task_id")
    job_count = fields.Integer(compute="_compute_job_count")

    def _compute_job_count(self):
        for r in self:
            r.job_count = len(r.job_ids)

    @api.model
    def default_get(self, fields):
        vals = super(SyncTriggerMixin, self).default_get(fields)
        if self._fields.get("state"):
            vals["state"] = "code"
        if self._default_name:
            vals["name"] = self._default_name
        return vals

    def name_get(self):
        result = []
        for r in self:
            name = r.trigger_name
            if r.name and r.name != self._default_name:
                name += " " + r.name
            result.append((r.id, name))
        return result


class SyncTriggerMixinModelId(models.AbstractModel):

    _name = "sync.trigger.mixin.model_id"
    _description = "Mixing to fill model_id field"

    @api.model_create_multi
    def create(self, vals_list):
        model_id = self.env.ref("base.model_res_partner").id
        for vals in vals_list:
            vals.setdefault("model_id", model_id)
        return super(SyncTriggerMixinModelId, self).create(vals_list)
