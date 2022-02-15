# -*- coding: utf-8 -*-

from odoo import models, fields, api


class aranking1(models.Model):
    _name = 'aranking.aranking1'

    nombre = fields.Char('Nombre')
    rank_id = fields.Many2one('aranking.aranking', 'champion')


class aranking(models.Model):
    _name = 'aranking.aranking'

    rank = fields.Integer()
    role = fields.Selection([('a', 'TOP'), ('b', 'MID'), ('c', 'BOT')])
    champion = fields.Char()
    tier = fields.Selection(
        [('a', 'S+'), ('b', 'S'), ('c', 'A+'), ('d', 'A'), ('e', 'B+'), ('f', 'B'), ('g', 'C+'), ('h', 'C'),
         ('i', 'D+'), ('j', 'D')])
    partidas = fields.Integer()
    win = fields.Integer()
    winrate = fields.Char(compute="_value_pc", store=True, digits=(12, 6))
    description = fields.Text()
    player_id = fields.One2many('aranking.aranking1', 'rank_id', 'nombre')

    @api.depends('win', 'partidas')
    def _value_pc(self):
        if self.partidas > 0:
            self.winrate = str(((float(self.win) / float(self.partidas)) * 100)) + "%"

class aranking(models.Aranking):
    _name='ArankingUserAdmin'
    _description='Ranking Administrators'

class aranking(models.Aranking):
    _name='ArankingUserEveryone'
    _description='Ranking Common Users'