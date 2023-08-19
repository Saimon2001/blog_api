# Información relevante para trabajar

1. Crear un ambiente virtual con conda.
```bash
conda create -n TGL_fastAPI python=3.9
```
2. Activar el ambiente virtual creado previamente.
```bash
conda activate TGL_fastAPI
```

3. Exportar el ambiente creado a un archivo `yml`. Esto se realiza sola primera vez; luego se actualiza el archivo.
 ```bash
conda env export > requirements.yml
```

4. Actualizar el archivo `requirements.yml` luego de agregar dependencias al ambiente de desarrollo de conda. 
 ```bash
conda env update -f requirements.yml
```

5. Si requiero bajar cambios que se encuentran en un repositorio remoto. Me ubico en la rama en la que quiero bajar los cambios y especifico la rama de la que quiero bajar los cambios; en este caso rama `main`. 
```bash
git pull origin  main
```
También puede hacerse directamente desde el `source control` de visual studio code, en el área de de `branches`. 