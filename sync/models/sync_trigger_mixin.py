# Copyright 2020 Ivan Yelizariev <https://twitter.com/yelizariev>
# License MIT (https://opensource.org/licenses/MIT).

from odoo import api, fields, models


class SyncTriggerMixin(models.AbstractModel):

    _name = "sync.trigger.mixin"
    _description = "Mixing for trigger models"

    trigger_name = fields.Char(
        "Trigger Name", help="Technical name to be used in task code", required=True
    )


class SyncTriggerMixinModelId(models.AbstractModel):

    _name = "sync.trigger.mixin.model_id"
    _description = "Mixing to fill model_id field"

    @api.model_create_multi
    def create(self, vals_list):
        model_id = self.env.ref("base.model_res_partner").id
        for vals in vals_list:
            vals.setdefault("model_id", model_id)
        return super(SyncTriggerMixinModelId, self).create(vals_list)
