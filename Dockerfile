FROM python:3.10

#INSTALACION DE DBT PARA POSTGRES

RUN pip install --upgrade pip && \
    pip install dbt-postgres


#CREAR CARPETA DE TABAJO

WORKDIR /usr/app

#PUNTO DE ENTRADA BASICO PARA MANTENE EL CONTENEDOR CORRIENDO

ENTRYPOINT ["tail", "-f", "/dev/null"]