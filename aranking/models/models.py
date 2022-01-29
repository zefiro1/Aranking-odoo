# -*- coding: utf-8 -*-

from odoo import models, fields, api


class aranking(models.Model):
    _name = 'aranking.aranking'

    rank = fields.Integer()
    role = fields.Selection([('a', 'TOP'), ('b','MID'), ('c','BOT')])
    champion = fields.Char()
    tier = fields.Selection([('a', 'S+'), ('b','S'), ('c','A+'),('d', 'A'), ('e','B+'), ('f','B'),('g', 'C+'), ('h','C'), ('i','D+'),('j', 'D')])
    partidas = fields.Integer()
    win = fields.Integer()
    winrate = fields.Char(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('win','partidas')
    def _value_pc(self):

        self.winrate = str((float(self.win) / float(self.partidas)) * 100)+"%"

