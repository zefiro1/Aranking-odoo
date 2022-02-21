# -*- coding: utf-8 -*-

from odoo import models, fields, api
import mysql.connector
cnn = mysql.connector.connect(host="localhost", user="jose", passwd="admin", database="arankingbd")
print(cnn)
# prepare a cursor object using cursor() method
cursor = cnn.cursor()

# ejecuta el SQL query usando el metodo execute().
cursor.execute("SELECT VERSION()")

# procesa una unica linea usando el metodo fetchone().
data = cursor.fetchone()
print("Database version : {0}".format(data))
# Prepare SQL query to READ a record into the database.
sql = "SELECT id, champions FROM arankingbd.champions_csv".format(0)

# Execute the SQL command
cursor.execute(sql)

# Fetch all the rows in a list of lists.
results = cursor.fetchall()

# desconecta del servidor
cnn.close()




class aranking1(models.Model):
    _name = 'aranking.aranking1'

    nombre = fields.Char('Nombre')
    rank_id = fields.Many2one('aranking.aranking', 'champion')


class aranking(models.Model):
    _name = 'aranking.aranking'
    nombre = fields.Selection(results)
    rank = fields.Integer()
    role = fields.Selection([('a', 'TOP'), ('b', 'MID'), ('c', 'BOT')])
    champion = fields.Binary()

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


