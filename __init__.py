from odoo import models, fields, api

class Mascota(models.Model):
    _name = 'mi_modulo.mascota'
    _description = 'Mascota'

    name = fields.Char(string='Nombre', required=True)
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento')
    peso = fields.Float(string='Peso (kg)')
    altura = fields.Float(string='Altura (cm)')

    # Campo COMPUTADO: se calcula solo
    edad = fields.Integer(
        string='Edad',
        compute='_compute_edad',   # Le dice a Odoo: "llama a este metodo para calcularlo"
    )
    indice_masa = fields.Float(
        string='Indice de Masa',
        compute='_compute_indice_masa',
    )

    @api.depends('fecha_nacimiento')         # Se recalcula cuando cambia fecha_nacimiento
    def _compute_edad(self):
        from datetime import date
        hoy = date.today()
        for mascota in self:                 # SIEMPRE iterar con "for rec in self"
            if mascota.fecha_nacimiento:
                delta = hoy - mascota.fecha_nacimiento
                mascota.edad = delta.days // 365
            else:
                mascota.edad = 0

    @api.depends('peso', 'altura')           # Se recalcula cuando cambia peso O altura
    def _compute_indice_masa(self):
        for mascota in self:
            if mascota.altura > 0:
                mascota.indice_masa = mascota.peso / (mascota.altura / 100)
            else:
                mascota.indice_masa = 0