import random
class persona:
    def __init__(self,cedula,edad, vestuario, ojos, cabello,colorpiel, genero,formacara, emocion, provincia):
        self.cedula=cedula
        self.edad=edad
        self.vestuario=vestuario
        self.ojos=ojos
        self.cabello=cabello
        self.colorpiel=colorpiel
        self.genero=genero
        self.formacara=formacara
        self.emocion=emocion
        self.provincia=provincia
    def get_cedula(self):
        return self.cedula
    def get_edad(self):
        return self.edad
    def get_vestuario(self):
        return self.vestuario
    def get_ojos(self):
        return self.ojos
    def get_cabello(self):
        return self.cabello
    def get_colorpiel(self):
        return self.colorpiel
    def get_genero(self):
        return self.genero
    def get_formacara(self):
        return self.formacara
    def get_emocion(self):
        return self.emocion
    def get_provincia(self):
        return self.provincia

    def set_cedula(self,cedula):
        self.cedula=cedula
    def set_edad(self,edad):
        self.edad=edad
    def set_vestuario(self,vestuario):
        self.vestuario=vestuario
    def set_ojos(self,ojos):
        self.ojos=ojos
    def set_cabello(self,cabello):
        self.cabello=cabello
    def set_colorpiel(self,colorpiel):
        self.colorpiel=colorpiel
    def set_genero(self,genero):
        self.genero=genero
    def set_formacara(self,formacara):
        self.formacara=formacara
    def set_emocion(self,emocion):
        self.emocion=emocion
    def set_provincia(self,provincia):
        self.provincia=provincia

class ojos:
    def __init__(self,idojos,forma,color):
        self.idojos=idojos
        self.forma=forma
        self.color=color
    def get_idojos(self):
        return self.idojos
    def get_forma(self):
        return self.forma 
    def get_color(self):
        return self.color

    def set_idojos(self,idojos):
        self.idojos=idojos
    def set_forma(self,forma):
        self.forma=forma
    def set_color(self,color):
        self.color=color
class formaojos:
    def __init__(self,idformaO,nombre):
        self.idformaO=idformaO
        self.nombre=nombre
    def get_idformaO(self):
        return self.idformaO
    def get_nombre(self):
        return self.nombre

    def set_idformaO(self,idformaO):
        self.idformaO=idformaO
    def set_nombre(self,nombre):
        self.nombre=nombre
class colorojos:
    def __init__(self,idcolorO,nombre):
        self.idcolorO=idcolorO
        self.nombre=nombre
    def get_idcolorO(self):
        return self.idcolorO
    def get_nombre(self):
        return self.nombre

    def set_idcolorO(self,idcolorO):
        self.idcolorO=idcolorO
    def set_nombre(self,nombre):
        self.nombre=nombre

class emocion:
    def __init__(self,idemocion,nombre):
        self.idemocion=idemocion
        self.nombre=nombre
    def get_idemocion(self):
        return self.idemocion
    def get_nombre(self):
        return self.nombre
    
    def set_idemocion(self,idemocion):
        self.idemocion=idemocion
    def set_nombre(self,nombre):
        self.nombre=nombre
    
class genero:
    def __init__(self, idgenero, nombre):
        self.idgenero=idgenero
        self.nombre=nombre
    def get_idgenero(self):
        return self.idgenero
    def get_nombre(self):
        return self.nombre
    
    def set_idgenero(self,idgenero):
        self.idgenero=idgenero
    def set_nombre(self,nombre):
        self.nombre=nombre
class provincia:
    def __init__(self,idprovincia,nombre):
        self.idprovincia=idprovincia
        self.nombre=nombre
    def get_idprovincia(self):
        return self.idprovincia
    def get_nombre(self):
        return self.nombre
    
    def set_idprovincia(self,idprovincia):
        self.idprovincia=idprovincia
    def set_nombre(self,nombre):
        self.nombre=nombre

class cabello:
    def __init__(self,idcabello, color,densidad,textura):
        self.idcabello=idcabello
        self.color=color
        self.densidad=densidad
        self.textura
    def get_idcabello(self):
        return self.idcabello
    def get_color(self):
        return self.color
    def get_densidad(self):
        return self.densidad
    def get_textura(self):
        return self.textura
    
    def set_idcabello(self,idcabello):
        self.idcabello=idcabello
    def set_color(self,color):
        self.color=color
    def set_densidad(self,densidad):
        self.densidad=densidad
    def set_textura(self, textura):
        self.textura=textura
class texturacabello:
    def __init__(self,idtexturacabello, nombre):
        self.idtexturacabello=idtexturacabello
        self.nombre=nombre
    def get_idtexturacabello(self):
        return self.idtexturacabello
    def get_nombre(self):
        return self.nombre
    
    def set_idtexturacabello(self,idtexturacabello):
        self.idtexturacabello=idtexturacabello
    def set_nombre(self,nombre):
        self.nonbre=nombre
class densidadcabello:
    def __init__(self,iddencidadcabello,nombre):
        self.iddensidadcabello=iddencidadcabello
        self.nombre=nombre
    def get_iddencidadcabello(self):
        return self.iddensidadcabello
    def get_nombre(self):
        return self.nombre
    
    def set_iddencidadcabello(self,iddencidadcabello):
        self.iddensidadcabello=iddencidadcabello
    def set_nombre(self,nombre):
        self.nombre=nombre
class colorcabello:
    def __init__(self, idcolorcabello,nombre):
        self.idcolorcabello=idcolorcabello
        self.nombre=nombre
    def get_idcolorcabello(self):
        return self.idcolorcabello
    def get_nombre(self):
        return self.nombre
    
    def set_idcolorcabello(self, idcolorcabello):
        self.idcolorcabello=idcolorcabello
    def set_nombre(self, nombre):
        self.nombre=nombre
class formacara:
    def __init__(self,idformacara, nombre):
        self.idformacara=idformacara
        self.nombre
    def get_idformacara(self):
        return self.idformacara
    def get_nombre(self):
        return self.nombre
    
    def set_idformacara(self, idformacara):
        self.idformacara=idformacara
    def set_nombre(self, nombre):
        self.nombre=nombre
class colorpiel:
    def __init__(self, idcolorpiel, nombre):
        self.idcolorpiel=idcolorpiel
        self.nombre=nombre
    def get_idcolorpiel(self):
        return self.idcolorpiel
    def get_nombre(self):
        return self.nombre
    
    def set_idcolorpiel(self,idcolorpiel):
        self.idcolorpiel=idcolorpiel
    def set_nombre(self, nombre):
        self.nombre=nombre
class vestuario:
    def __init__(self,idvestuario,listaropa,calzado,listaaccesorios):
        self.idvestuario=idvestuario
        self.listaropa=listaropa
        self.listaaccesorios=listaaccesorios
    def get_idvestuario(self):
        return self.idvestuario
    def get_listaropa(self):
        return self.listaropa
    def get_calzado(self):
        return self.calzado
    def get_listaaccesorios(self):
        return self.listaaccesorios
    
    def set_idvestuario(self, idvestuario):
        self.idvestuario=idvestuario
    def set_listaropa(self,listaropa):
        self.listaropa=listaropa
    def set_calzado(self,calzado):
        self.calzado=calzado
    def set_listaacesorios(self, listaaccesorios):
        self.listaaccesorios