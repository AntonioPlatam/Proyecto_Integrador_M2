from db_conector import get_db_engine,Base
import modelos

def main():
    # Crea el motor de la base de datos
    engine = get_db_engine()

    # Crea todas las tablas definidas en los modelos
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print(f"Error al crear las tablas: {e}")
        raise

if __name__ == "__main__":
    main()
    print("Tablas creadas exitosamente.")


    