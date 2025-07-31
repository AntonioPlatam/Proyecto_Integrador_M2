from sqlalchemy import(
    create_engine,Column,Integer,String,Date,func,DateTime,Numeric,
    ForeignKey
)
from sqlalchemy.orm import declarative_base, relationship
from db_conector import Base, engine

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    dni = Column(String(20), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    contrasena = Column(String(255), nullable=False)
    fecha_registro = Column(DateTime, nullable=False, server_default=func.now())

    def __repr__(self):
        return f"<usuarios(id={self.id}, nombre={self.nombre}, email={self.email})>"
    
class Categorias(Base):
    __tablename__ = 'categorias'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False, unique=True)
    descripcion = Column(String(255), nullable=True)

    def __repr__(self):
        return f"<categorias(id={self.id}, nombre={self.nombre}, descripcion={self.descripcion})>"
    
class Productos(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)
    descripcion = Column(String(255), nullable=True)
    precio = Column(Numeric(10, 2), nullable=False)
    stock = Column(Integer, nullable=False)
    categoria_id = Column(Integer, ForeignKey('categorias.id'), nullable=False)

    categoria = relationship("categorias", back_populates="productos")

    def __repr__(self):
        return f"<productos(id={self.id}, nombre={self.nombre}, precio={self.precio},stock={self.stock},categoria_id={self.categoria_id})>"
    
class Ordenes(Base):
    __tablename__ = 'ordenes'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    fechas_orden = Column(DateTime, nullable=False, server_default=func.now())
    total = Column(Numeric(10, 2), nullable=False)
    estado = Column(String(50), nullable=False, default='pendiente')

    usuario = relationship("usuarios", back_populates="ordenes")

    def __repr__(self):
        return f"<ordenes(id={self.id}, usuario_id={self.usuario_id}, fechas_orden={self.fechas_orden}, total={self.total}, estado={self.estado})>"
    
class DetalleOrdenes(Base):
    __tablename__ = 'detalle_ordenes'
    id = Column(Integer, primary_key=True)
    orden_id = Column(Integer, ForeignKey('ordenes.id'), nullable=False)
    producto_id = Column(Integer, ForeignKey('productos.id'), nullable=False)
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Numeric(10, 2), nullable=False)

    orden = relationship("ordenes", back_populates="detalle_ordenes")
    producto = relationship("productos", back_populates="detalle_ordenes")

    def __repr__(self):
        return f"<detalle_ordenes(id={self.id}, orden_id={self.orden_id}, producto_id={self.producto_id}, cantidad={self.cantidad}, precio_unitario={self.precio_unitario})>"

class DireccionesEnvio(Base):
    __tablename__ = 'direcciones_envio'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    calle = Column(String(255), nullable=False)
    ciudad = Column(String(100), nullable=False)
    departamento = Column(String(100), nullable=False)
    provincia = Column(String(100), nullable=False)
    distrito = Column(String(100), nullable=False)
    estado = Column(String(100), nullable=False)
    codigo_postal = Column(String(20), nullable=False)
    pais = Column(String(100), nullable=False)


    usuario = relationship("usuarios", back_populates="direcciones_envio")

    def __repr__(self):
        return f"<direcciones_envio(id={self.id}, usuario_id={self.usuario_id}, calle={self.calle}, ciudad={self.ciudad}, departamento={self.departamento},provincia={self.provincia} , distrito={self.distrito}, estado={self.estado}, codigo_postal={self.codigo_postal}, pais={self.pais})>"
    
class carrito(Base):
    __tablename__ = 'carrito'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    producto_id = Column(Integer, ForeignKey('productos.id'), nullable=False)
    cantidad = Column(Integer, nullable=False)
    fecha_agregado = Column(DateTime, nullable=False, server_default=func.now())

    usuario = relationship("usuarios", back_populates="carrito")
    producto = relationship("productos", back_populates="carrito")

    def __repr__(self):
        return f"<carrito(id={self.id}, usuario_id={self.usuario_id}, producto_id={self.producto_id}, cantidad={self.cantidad}, fecha_agregado={self.fecha_agregado})>"
    
class MetodosPago(Base):
    __tablename__ = 'metodos_pago'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(255), nullable=True)

    def __repr__(self):
        return f"<metodos_pago(id={self.id}, nombre={self.nombre}, descripcion={self.descripcion})>"
    
class OrdenesMetodosPago(Base):
    __tablename__ = 'ordenes_metodos_pago'
    id = Column(Integer, primary_key=True)
    orden_id = Column(Integer, ForeignKey('ordenes.id'), nullable=False)
    metodo_pago_id = Column(Integer, ForeignKey('metodos_pago.id'), nullable=False)
    monto_pago = Column(Numeric(10, 2), nullable=False)

    orden = relationship("ordenes", back_populates="ordenes_metodos_pago")
    metodo_pago = relationship("metodos_pago", back_populates="ordenes_metodos_pago")

    def __repr__(self):
        return f"<ordenes_metodos_pago(id={self.id}, orden_id={self.orden_id}, metodo_pago_id={self.metodo_pago_id}, monto_pago={self.monto_pago})>"
    
class ResenasProductos(Base):
    __tablename__ = 'resenas_productos'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    producto_id = Column(Integer, ForeignKey('productos.id'), nullable=False)
    calificacion = Column(Integer, nullable=False)
    comentario = Column(String(255), nullable=True)
    fecha_creacion = Column(DateTime, nullable=False, server_default=func.now())

    producto = relationship("productos", back_populates="resenas_productos")
    usuario = relationship("usuarios", back_populates="resenas_productos")

    def __repr__(self):
        return f"<resenas_productos(id={self.id}, producto_id={self.producto_id}, usuario_id={self.usuario_id}, calificacion={self.calificacion}, comentario={self.comentario})>"
    
class HistorialPagos(Base):
    __tablename__ = 'historial_pagos'
    id = Column(Integer, primary_key=True)
    orden_id = Column(Integer, ForeignKey('ordenes.id'), nullable=False)
    metodo_pago_id = Column(Integer, ForeignKey('metodos_pago.id'), nullable=False)
    monto = Column(Numeric(10, 2), nullable=False)
    fecha_pago = Column(DateTime, nullable=False, server_default=func.now())
    estado_pago = Column(String(50), nullable=False, default='Procesando')

    usuario = relationship("usuarios", back_populates="historial_pagos")
    metodo_pago = relationship("metodos_pago", back_populates="historial_pagos")

    def __repr__(self):
        return f"<historial_pagos(id={self.id}, orden_id={self.orden_id}, metodo_pago_id={self.metodo_pago_id}, monto={self.monto}, fecha_pago={self.fecha_pago}, estado_pago={self.estado_pago})>"