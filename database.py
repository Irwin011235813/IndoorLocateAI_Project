from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos SQLite (se creará un archivo indoorlocate.db)
DATABASE_URL = "sqlite:///indoorlocate.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Modelo para los puntos de referencia de calibración (las "huellas digitales")
class ReferencePoint(Base):
    __tablename__ = "reference_points"
    id = Column(Integer, primary_key=True, index=True)
    x = Column(Float, index=True)
    y = Column(Float, index=True)
    # Las señales RSSI se almacenarán como un string JSON o en otra tabla relacionada si es necesario, por ahora lo simplificamos aquí
    rssi_data = Column(String) 

# Función para crear las tablas en la base de datos
def init_db():
    Base.metadata.create_all(bind=engine)

# Helper para obtener la sesión de DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
