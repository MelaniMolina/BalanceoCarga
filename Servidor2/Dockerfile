#Utiliza una imagen de pyrthon
FROM python:latest
#Establecer el directorio de trabajo dentro del contenedor
WORKDIR /Servidor2
#Copiar todos los archivos desde la carpeta del host al contendor(Primero el host y luego del contendor)
COPY servidor2.py . 
#Instalar las dependencias requeridas 
RUN pip install flask
#Exponer puerto del contenedr
#EXPOSE 5000
#Comando para ejecutar mi aplicion
CMD ["python","servidor2.py"]
