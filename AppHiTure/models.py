from django.db import models
# Create your models here.


#TABLA VENTA
class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    fecha_venta = models.DateTimeField(auto_now= True)
    total = models.IntegerField()
    id_cli_fk = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    id_venta_producto_fk = models.ForeignKey('Venta_producto', on_delete=models.CASCADE)
    id_comprobante_pago_fk = models.ForeignKey('Comprobante_pago', on_delete=models.CASCADE)
    class Meta:
        db_table = "venta"
    

#TABLA CLIENTE
class Cliente(models.Model):
    #El AUtofield es un autoincremento
    id_cli = models.AutoField(primary_key=True)
    rut_cli = models.CharField(max_length=13)
    nombre_cli = models.CharField(max_length=25)
    apellido_cli = models.CharField(max_length=35)
    mail_cli = models.EmailField()
    direccion_cli = models.CharField(max_length=200)
    telefono_cli = models.CharField(max_length=16)
    usuario_cli = models.CharField(max_length=150)
    password_cli = models.CharField(max_length=128)
#    id_tipo_usuario_fk = models.ForeignKey('Tipo_usuario', on_delete=models.CASCADE)
    class Meta:
        db_table = "cliente"


#TABLA DEL TIPO DE USUARIO <- Si el usuario será trabajador o normal
#SOLO SERVIRÍA SI EL TRABAJADOR OBTIENE DESCUENTO
#class Tipo_usuario(models.Model):
#    id_tipo_usuario = models.AutoField(primary_key=True)
#    tu_nombre = models.CharField(max_length=40)

#TABLA ADMINISTRADOR
#class Administrador(models.Model):
    #El Autofield es un autoincremento
#    id_adm = models.AutoField(primary_key=True)
#    rut_adm = models.CharField(max_length=13)
#    nombre_adm = models.CharField(max_length=25)
#    apellido_adm = models.CharField(max_length=35)
#    mail_adm = models.EmailField()
#    direccion_adm = models.CharField(max_length=200)
#    telefono_adm = models.CharField(max_length=16)
#    id_tipo_usuario_fk = models.ForeignKey('Tipo_usuario', on_delete=models.CASCADE)
#    class Meta:
#        db_table = "administrador"


#TABLA DE PRODUCTO
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=40)
    descripcion = models.TextField()
    precio = models.IntegerField()
    url = models.ImageField(default='not_found')
    stock = models.IntegerField(default=0)
    genero_producto = models.ForeignKey('Genero_producto', on_delete=models.CASCADE,default='')
    class Meta:
        db_table = "producto"
    def __str__(self):
        return "id_producto:"+id_producto+", nombre_producto"+nombre_producto+", descripcion"+descripcion+", precio"+precio+", url"+url


#TABLA DEL GENERO DE LOS PRODUCTOS, donde si el genero es 1, puede ser accion o 2 es rpg <- ejemplo
class Genero_producto(models.Model):
    genero_producto = models.CharField(max_length=100)
    class Meta:
        db_table = "genero_producto"
    def __str__(self):
        return u'{0}'.format(self.genero_producto)


#TABLA INTERSECCIÓN DE VENTA Y PRODUCTO (VENTA_PRODUCTO)
class Venta_producto(models.Model):
    id_venta_producto = models.AutoField(primary_key=True)
    precio_total = models.IntegerField()
    cantidad = models.IntegerField()
    id_venta_fk = models.ForeignKey('Venta', on_delete=models.CASCADE)
    id_producto_fk = models.ForeignKey('Producto', on_delete=models.CASCADE)
    class Meta:
        db_table = "venta_producto"


#TABLA DEL COMPROBANTE DE PAGO
class Comprobante_pago(models.Model):
    id_comrpobante_pago = models.AutoField(primary_key=True)
    id_venta_fk = models.ForeignKey('Venta', on_delete=models.CASCADE)
    id_tipo_pago_fk = models.ForeignKey('Tipo_pago', on_delete=models.CASCADE)
    class Meta:
        db_table = "comprobante_pago"


#TABLA DEL TIPO DE PAGO, donde el id puede ser 1 y efectivo, 2 y tarjeta <- ejemplo
class Tipo_pago(models.Model):
    id_tipo_pago = models.AutoField(primary_key=True)
    tp_nombre = models.CharField(max_length=50)
    class Meta:
        db_table = "tipo_pago"
