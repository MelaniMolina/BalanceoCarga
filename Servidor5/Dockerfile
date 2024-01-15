#Utiliza una imagen de pyrthon
FROM python:latest
#Establecer el directorio de trabajo dentro del contenedor
WORKDIR /Servidor5
#Copiar todos los archivos desde la carpeta del host al contendor(Primero el host y luego del contendor)
COPY servidor5.py . 
#Instalar las dependencias requeridas 
RUN pip install flask
#Exponer puerto del contenedr
#EXPOSE 5000
#Comando para ejecutar mi aplicion
CMD ["python","servidor5.py"]
