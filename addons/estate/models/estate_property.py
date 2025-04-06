from odoo import models, fields, api


class EstateProperty(models.Model):
    _name = "real.estate"
    _description = "estate.estate"

    name = fields.Char(required=True)
    bedrooms = fields.Integer()
    area = fields.Float()
    price = fields.Float()
    total = fields.Float(compute="_compute_total", store=True)
    description = fields.Text()
    furnuishstatus = fields.Selection(
        [
            ("furnished", "Furnished"),
            ("semi-furnished", "Semi-Furnished"),
            ("unfurnished", "Unfurnished"),
        ],
        default="furnished",
    )
    type_id = fields.Many2one("estate.property.type", string="Property Type")
    tag_ids = fields.Many2many("estate.property.tag")

    @api.depends("price")
    def _compute_total(self):
        for record in self:
            record.total = 2 * record.price
