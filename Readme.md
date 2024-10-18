# HIDROCARBUROS EN ESTACIONES DE SERVICIO DISTRIBUCION VENTAS EN CLIENTE FINAL

## DATA SCIENCE

---

Aplicando **_PYTHON_** y sus respectivas librerías vamos a realizar los análisis exploratorio a la base de datos de ventas de las estaciones de servicio de combustible del sistema de liquidos **MOL**, ya que este contiene el detalle de distribución al cliente final.

La tabla ventas en **_MSSQL_** se compone de :

```sql
[Pk_IdVenta],[Id_Venta_Estacion],[IdEstacion],[Fecha_Inicial],[Fecha_Final],[Posicion],[Manguera],[Precio_Unitario],[Cantidad]   ,[ValorTotal],[Producto],[TipoTransaccion],[Documento_Vendedor],[Trama],[Documento_Tercero],[Sincronizado],[Id_Corte]
```

---

> Que tipo de analisis puedo aplicar, tener encuenta el campo fecha tiene hora porque se debe calcular el tiempo que dura el llenado de un vehiculo.

---

# Preguntas del negocio.

## 1. Análisis Descriptivo:

- **Estadísticas básicas:** Medias, medianas, varianzas de Precio_Unitario, Cantidad, ValorTotal.

- **Distribuciones:** Histogramas o gráficos de densidad de variables numéricas como Precio_Unitario, Cantidad, ValorTotal.

- **Gráficos de barras:** para variables categóricas como Tipo Transaccion, Producto

## 2. Análisis de Tiempos de Llenado:

- **Duración del llenado:** La diferencia entre Fecha_Inicial y Fecha_Final te permitirá calcular el tiempo que tarda en llenarse un vehículo. Este dato es clave para análisis operativos.

```python
df['Duracion_Llenado'] = df['Fecha_Final'] - df['Fecha_Inicial']
```

- **Promedio del tiempo de llenado:** Cálculo del tiempo promedio por vehículo para identificar si hay patrones de congestión.

- **Distribución del tiempo de llenado:** Graficar histogramas para ver la distribución de tiempos de llenado, detectando outliers o llenados más lentos de lo usual.

## 3. Análisis Temporal:

- **Tendencias de ventas por día, semana, mes:** Analizar cómo cambian las ventas a lo largo del tiempo, agregando las ventas por Fecha_Inicial.

- **Horas pico:** Analizar en qué horas del día se realizan más ventas (Fecha_Inicial), lo que puede ayudar a entender la demanda.

## 4. Análisis por Estación y Posición:

- **Rendimiento por estación y posición:** Comparar el volumen de ventas y el valor total entre diferentes estaciones (IdEstacion) o posiciones de manguera (Posicion, Manguera).

- **Análisis por producto:** ¿Qué tipo de producto se vende más en qué estaciones y momentos?

## 5. Análisis de Transacciones:

- **Tipo de Transacción:** Identificar si hay diferencias en el volumen de ventas entre los diferentes TipoTransaccion (por ejemplo, efectivo vs tarjeta).

- **Frecuencia de ventas por cliente:** Si Documento_Tercero es único para cada cliente, se puede analizar la recurrencia de compras de cada cliente.

## 6. Sincronización y Corte:

- **Transacciones no sincronizadas:** Evaluar cuántas transacciones están marcadas como no sincronizadas (Sincronizado), ya que esto puede ser útil para evaluar posibles problemas operativos.

- **Análisis por cortes de ventas:** Agrupar los datos por Id_Corte para analizar el volumen de ventas por cada cierre de turno o corte.

---

> Estos análisis te darán una visión completa del comportamiento de las ventas, permitiéndote optimizar tanto las operaciones de la estación como la experiencia del cliente.

> ##### Analisis adicionales
>
> 1.  Cálculo de Duración del Llenado y Análisis de Distribución
> 2.  Análisis Temporal: Ventas por Día, Semana y Mes
> 3.  Desempeño por Estación, Manguera y Producto
> 4.  Análisis de Transacciones No Sincronizadas

<!-- Github Markdowns -->

- [x] Preguntas del negocio
- [ ] Extraer datos
- [ ] Sincronizar GitHub
- [ ] Documentar

@cio_primax_cu :+1: :smiley:

Pasos pa desarrollar proyectos de software

1.  **Reconocer el problema o necesidad**: Identificar el problema o necesidades
2.  **Definir el alcance del proyecto**: Establecer los objetivos y metas
3.  **Crear un plan de acción**: Desarrollar un plan de acción para resolver
4.  Herramientas de diagrama DB entidad relacion:

[dbdiagram.io](https://dbdiagram.io/ "DB")
[draw.io](https://draw.io/ "Draw.io")
[postgres.new](https://postgres.new/)
[excalidraw](https://excalidraw.com/)
DBeaver Enterprise
Heidisql
[sqlfiddle](https://sqlfiddle.com/ "SQLFiddle")
[mySql Workbench]

---

- [ ] Preguntas del negocio
- [ ] Extraer datos
- [ ] Sincronizar GitHub
- [ ] Documentar

# Diseñar sistema escoger tecnologías

1.  **Diseñar la base de datos**: Diseñar la base de datos
2.  **Crear la base de datos**: Crear la base de datos
3.  **Crear la aplicación**: Crear la aplicación

- Herramientas frontend
- Herramientas backend
- Diagramas **eraser.io**
- [dbdiagram.io](https://dbdiagram.io/ "DB")
- [draw.io](https://draw.io/ "Draw.io")
- Diseño interfaz grafica
- [Figma](https://www.figma.com/ "Figma")
- [Adobe XD](https://www.adobe.com/es/products/xd.html "Adobe XD")
- [Sketch](https://www.sketch.com/ "Sketch")
- [InVision](https://www.invisionapp.com/ "InVision")

4. **Creación entorno desarrollo**
* Github
* Docker
* Kubernetes (https://blazor.radzen.com/)
* Visual Studio Code + Diagrama DB + Diagramas de flujo
* [Postman](https://www.postman.com/ "Postman")

5. **Creación entorno producción**
* IIS PaaS

6. **Feedback** reunion con cliente final, modificaciones 
6. **Creación entorno de pruebas**



4.  **Implementar la aplicación**: Implementar la aplicación
5.  **Probar la aplicación**: Probar la aplicación
6.  **Desplegar la aplicación**: Desplegar la aplicación
7.  **Mantener la aplicación**: Mantener la aplicación
