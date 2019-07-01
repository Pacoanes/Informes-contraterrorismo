# Proyecto Pipelies 
# Herramienta para crear informes
empezamos con un dataset grande de GTD Global Terrorism Database. URL: https://www.kaggle.com/START-UMD/gtd.
Fuente original https://www.start.umd.edu/gtd/. COmo este archivo pesaba más de 100 megas (170mb) hice una primera limpieza a base de borrar columnas sus celdas a NaN y me quede con un csv de 28 megas.

El dataframe aloja informacion de cualquier ataque o accion terrositas desde 1970 hasta 2017. Entedamos como acción terrorista "cualquier actos violento perpetrado por organizaciones no estatales contra la población general con fines políticos".

La herramienta permite seleccionar un pais del mundo para generar un informe sobre los principales grupos, principales metodos de ataque, años con mayor ataque o probabilidad de sufrir un ataque. La herramienta conecta con la api de New York Times para devolver un articulo sobre el pais elegido.
