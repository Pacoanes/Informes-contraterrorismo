# Proyecto Pipelies 
# Herramienta para crear informes

**La herramienta genera un informe de actividad terrorista según el pais deseado.**

Para poder recolectar los datos partimos de un dataset grande, el GTD (Global Terrorism Database). URL: https://www.kaggle.com/START-UMD/gtd.Fuente original https://www.start.umd.edu/gtd/. Este archivo original pesa más de 100 megas (170mb) por lo que no se puede subir a GitHub. Para poder contar con él, hice una primera limpieza a base de borrar columnas donde su contenido era principalmente "NaN". El resultado de esta primera limpieza es un csv de 28 megas.

Es importante entender que el csv recoge cualquier actividad terrorista. Entedamos como acción terrorista "cualquier actos violento perpetrado por organizaciones no estatales contra la población general con fines políticos". Disponemos de información de cualquier ataque o accion terrorista perpetrado desde 1970 hasta 2017: Grupos terroristas, metodos empleados, ciudad, longitud y latitud, etc. 

Una vez seleccionado el pais deseado La herramienta genera un informe sobre los principales grupos de ese pais, principales metodos de ataque, años con mayor ataque o probabilidad de sufrir un ataque por población. Para enriquecer la herramienta hacemos un web scrapping para tener la población y pib de todos los paises, nos conectamos con la API de New York Times para devolver un articulo sobre el pais elegido y tambien con la API de Google para disponer de una imagen en el informe.
