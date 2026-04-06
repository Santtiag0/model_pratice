from odoo import models, fields

class Mascota(models.Model):
    _name = 'mi_modulo.mascota'
    _description = 'Mascota'

    name = fields.Char(string='Nombre de la mascota', required=True)
    tipo = fields.Selection(
    [('perro', 'Perro'), 
    ('gato', 'Gato'), 
    ('otro', 'Otra raza')
    ], string='Tipo de mascota',
    
    otro_tipo = fields.Char(string='Especifique el tipo de raza')
        
    )
    edad = fields.Integer(string='Edad (anos)')
    peso = fields.float(string= 'Peso (kg)')
    dueno_id = fields.Many2one('res.partner', string='Dueño')    
    es_vacunado = fields.Boolean(string='¿Está vacunado?', default=False)
    fecha_de_nacimiento = fields.Date(string='Fecha de nacimiento')
    nota = fields.Text(string='Notas adicionales')

    state = fields.Selection([
        ('borrado','Borrado'),
        ('registrado','Registrado'),
        ('adoptado', 'Adoptado'),
        ], string= 'Estado', default= 'borrado')
    
    def action_registrado(self):
        for rec in self:
            rec.state = 'registrado'

    def action_adoptado(self):
        for rec in self:
            rec.state = 'adoptado'

    def action_borrado(self):
        for rec in self:
            rec.state = 'borrado'    
    