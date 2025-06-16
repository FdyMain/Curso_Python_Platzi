import os

#Obtener directorio actual
cwd = os.getcwd()
print("Directorio de trabajo actual", cwd)

#Listar los archivos que tengo en la carpeta

txt_files = [f for f in os.listdir('./resources') if f.endswith('.txt')]
print("Archivos txt son:", txt_files)

#renombrar nombre archivo

os.rename('./resources/cuento.txt', 'cuento_rename.txt')
print('Archivo renombrado')

txt_files = [f for f in os.listdir('./resources') if f.endswith('.txt')]
print("Archivos txt son:", txt_files)