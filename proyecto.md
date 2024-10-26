# ANÁLISIS DE TENDENCIAS DE VENTAS DE HIDROCARBUROS AL CLIENTE FINAL EN ESTACIONES DE SERVICIO (EDS)
---
## Introducción 
Teniendo en cuenta que en la actualidad estamos en un entorno empresarial cada vez más competitivo, la capacidad de tomar decisiones informadas es crucial para el éxito de cualquier organización. 

Las estaciones de servicio representan un factor fundamental en la cadena de suministro de combustibles, y su rendimiento puede verse afectado por múltiples factores, como la ubicación, la competencia, tendencias del mercado y cambios en la demanda.
Por lo anterior, se hace necesario un análisis exhaustivo de los datos de ventas a través de diferentes variables como lo son: el tiempo de llenado, tiempo promedio de espera por vehículo y horas de mayor tráfico entre otros,  ya que de esta manera se podría no solo evaluar el desempeño histórico, sino también predecir tendencias futuras, permitiendo a la organización tomar decisiones basadas en hechos.

Dicho análisis incluirá la recopilación y revisión de datos históricos de ventas, lo que permitirá identificar patrones y comportamientos de compra. Al observar las variaciones en las ventas a lo largo del tiempo, se puede determinar qué factores como los precios y condiciones económicas influyen en el comportamiento de ventas en las estaciones de servicio. Lo anterior no solo permitirá anticipar cambios en la demanda de combustible, sino que también ayudará a la empresa a optimizar la asignación de recursos y diseñar estrategias de marketing más efectivas basándose en datos concretos y no en suposiciones.

## ASIS  

El análisis de la situación en la empresa revela un uso intensivo de cuadros de Excel como herramienta principal para gestionar y consolidar datos. Aunque Excel puede ser útil para el manejo de datos en pequeños equipos, su uso excesivo en proyectos complejos presenta varios problemas, especialmente en términos de automatización y consolidación. Aquí está el análisis de la situación actual:

Problemas con el uso de Excel en la gestión de proyectos:
Falta de automatización:

El uso de múltiples hojas de cálculo de Excel hace que el proceso de ingreso, validación y actualización de datos sea manual.
Cualquier cambio en una fuente de datos requiere modificaciones manuales en varios archivos, lo que aumenta la probabilidad de errores humanos.
Es difícil implementar fórmulas y macros que funcionen eficientemente a gran escala o de manera continua para realizar actualizaciones automáticas.
Datos fragmentados y no consolidados:

Los datos de diferentes áreas o departamentos pueden estar en archivos separados, sin una fuente única de verdad, lo que lleva a inconsistencias y duplicidades.
La consolidación manual de datos en informes es lenta y propensa a errores, y puede dar lugar a la pérdida de información clave en el proceso.
Limitaciones en análisis dinámicos y escalabilidad:

Los cuadros de Excel no son dinámicos; cualquier cambio o actualización requiere manipulación manual, lo que ralentiza el análisis.
A medida que crecen los volúmenes de datos, Excel se vuelve ineficiente, con problemas de rendimiento y capacidad de manejo de grandes conjuntos de datos.
Falta de trazabilidad y control:

El control de versiones de los archivos de Excel es difícil, lo que provoca problemas para rastrear quién realizó cambios y cuándo.
Es complicado implementar reglas de negocio que mantengan integridad en los datos y aseguren que todos los usuarios trabajen con información actualizada.
Colaboración ineficaz:

La colaboración entre departamentos se ve obstaculizada por el uso de archivos estáticos y distribuidos. La falta de un sistema centralizado impide una comunicación fluida y una toma de decisiones rápida y basada en datos en tiempo real.
Consecuencias operativas:
Decisiones retardadas debido a la lentitud en la recolección y análisis de datos.
Baja eficiencia en el uso del tiempo y recursos, al tener que realizar tareas manuales repetitivas.
Falta de agilidad para adaptarse a cambios rápidos en el entorno empresarial, ya que cualquier modificación en los datos requiere tiempo considerable.

## TO BE: Transformación con Python y Ciencia de Datos

Automatización del Ingreso y Procesamiento de Datos:

Se eliminarán los procesos manuales de ingreso de datos en Excel y serán reemplazados por scripts en Python que se conecten directamente a las fuentes de datos (bases de datos SQL, API, archivos CSV, etc.).
Se implementarán herramientas automatizados para la extracción, transformación y carga de datos (ETL), utilizando herramientas como pandas y pyodbc para gestionar la conexión entre diferentes fuentes de datos y procesar la información.
Python permitirá la validación automática de los datos, verificando su integridad y consistencia antes de almacenarlos en una base de datos central.
Consolidación Dinámica de los Datos:

Los datos serán almacenados en una base de datos centralizada (como Sqlite, PostgreSQL, MySQL o una base de datos en la nube) en lugar de estar distribuidos en múltiples archivos de Excel.
Python será utilizado para automatizar la consolidación de datos desde distintas áreas o departamentos, asegurando que se unifiquen en un formato estándar que permita su análisis fácil y rápido.
El uso de tablas de resumen y la creación de vistas en tiempo real permitirá que los datos estén siempre actualizados, sin necesidad de intervención manual.
Análisis de Datos Automatizado:

Los análisis que antes se realizaban manualmente en Excel se automatizarán usando notebooks de Jupyter y bibliotecas como NumPy, pandas y scikit-learn para realizar análisis estadísticos, detectar patrones y crear modelos predictivos basados en los datos consolidados.
Los informes manuales serán reemplazados por dashboards interactivos en herramientas como Plotly, que estarán conectados a las bases de datos actualizadas, mostrando métricas clave en tiempo real.
Modelos Predictivos y Machine Learning:

Python permitirá el uso de técnicas de machine learning para crear modelos predictivos que ayuden a la empresa a tomar decisiones estratégicas basadas en datos. Por ejemplo:
Previsión de ventas: Modelos predictivos para estimar la demanda futura de productos.
Análisis de comportamiento de clientes: Segmentación automática de clientes basados en patrones de compra.
Optimización de operaciones: Identificación de cuellos de botella o ineficiencias en los procesos de ventas o distribución.
Visualización Dinámica de Datos:

En lugar de gráficos estáticos en Excel, Python y herramientas de visualización como Matplotlib, Seaborn o Plotly Dash generarán gráficos y paneles interactivos que permitirán explorar los datos desde múltiples perspectivas y realizar análisis de manera dinámica.
Las herramientas de Business Intelligence (BI) estarán conectadas a los datos en tiempo real, permitiendo a los usuarios generar sus propios informes sin depender de un analista de datos.
Automatización de Reportes y KPIs:

Se creará un sistema automatizado de generación de reportes periódicos que se envían a los responsables de cada área, proporcionando una vista clara de los KPIs sin intervención manual.
Python puede integrarse con plataformas de comunicación (como correo electrónico o aplicaciones de mensajería) para enviar alertas automáticas cuando se detecten anomalías o cuando se alcancen ciertos umbrales.

---

# Objetivos del proyecto

## Objetivo general 

Realizar un análisis a las ventas en las estaciones de servicio de combustible del sistema de líquidos _(db)_ **MASTER** con el fin de identificar patrones y obtener información clave. Permitiendo formular recomendaciones estratégicas y de mejora para la organización.

## Objetivos Específicos

* Identificar promedios y distribución de tiempos de llenado de vehículos que permita contribuir a los análisis operativos (Aplicar estadística descriptiva).
* Evaluar las tendencias de ventas en distintos periodos de tiempo para identificar patrones estacionales y períodos de mayor demanda.
* Realizar un análisis de rendimiento en los puntos de venta para comprender patrones de ventas, comportamiento de transacciones con el fin de optimizar la distribución de recursos y mejorar la experiencia del cliente.
* **Evaluar** desempeño de ventas para obtener información detallada del volumen de ventas asociado a un periodo de tiempo.

---

# Delimitación del proyecto
## Alcance del Proyecto:

### Áreas Involucradas:

El proyecto abarcará los departamentos de ventas, operaciones y mantenimiento, ya que son las principales áreas que actualmente gestionan y consolidan datos a través de múltiples hojas de Excel.

## Fuentes de Datos:
- Base de datos en MSQL de nombre MASTER (Master On Line)
La tabla ventas en **_MSSQL_** se compone de :

```sql
 SELECT [Pk_IdVenta], [IdVentaEstacion], [IdEstacion], [FechaIni], 
            [FechaFin], [Posicion], [Manguera], [PPU], [Cantidad], [ValorTotal], 
            [Producto], [TipoTransaccion], [DocumentoVendedor] 
            FROM [MASTER].[dbo].[vista_ventas];
```
- Tablas maestras de productos y estaciones de servicio
```Python
Entrega de variables maestras de productos y estaciones de servicio (.ENV):
PROD_ACPM=102,ACPM
PROD_CORRIENTE=101,CORRIENTE
PROD_EXTRA=103,EXTRA
PROD_MAXPRO=104,MAXPRO
EDS_1=ZEUS,4.772104,-74.0416697
EDS_2=HERA,6.257590259,-75.61103107
EDS_3=POSEIDON,3.399043723,-76.57649259
EDS_4=JUPITER,4.451921427,-75.252591
EDS_5=ERIS,5.518472615,-73.37801856
EDS_6=PERSEFONE,7.155833544,-73.11156997 
```

[![Heds-Pretiction.png](https://i.postimg.cc/x1JfLY0C/Heds-Pretiction.png)](https://postimg.cc/CR0pV3nT)

## Marco Temporal
El proyecto se centrará en el análisis de datos históricos de ventas, desde febrero 2024  hasta Octubre 14 2024

## Limitaciones del Proyecto:
- La base de datos actual no incluye información de transacciones de pagos electrónicos.
- La información se limita a 6  estaciones de servicio de combustible liquido.
- La base de datos no incluye información de los vehículos que se llenan de combustible.
---

## Metodología
En este proyecto, se seguirá un enfoque estructurado para el análisis y visualización de los datos, aplicando diversas técnicas y herramientas que permiten obtener resultados precisos y comprensibles. A continuación, se detallan los pasos a seguir:

### Recolección y limpieza de datos:

Para garantizar la calidad y consistencia de los datos utilizados, se llevarán a cabo las siguientes actividades:

Se aplicarán técnicas de limpieza de datos, tales como la eliminación de inconsistencias, duplicados y la gestión de valores faltantes. Los datos serán recolectados e integrados desde múltiples fuentes, utilizando la biblioteca Pandas en Python para facilitar el manejo y procesamiento eficiente de la información.

### Análisis exploratorio de datos (EDA):
Durante esta fase, se realizan diversas técnicas de análisis descriptivo para obtener una mejor comprensión de los datos y sus características operativas. Las preguntas de negocio que guían este análisis son las siguientes:

### Análisis Descriptivo:

Estadísticas básicas como medias, medianas y varianzas de variables como Precio_Unitario, Cantidad, y ValorTotal.
Distribuciones de variables numéricas mediante histogramas o gráficos de densidad, y gráficos de barras para variables categóricas como Tipo Transacción y Producto.


### Análisis de Tiempos de Llenado:

Duración del llenado: Se calculará la diferencia entre Fecha_Inicial y Fecha_Final para obtener el tiempo que tarda en llenarse un vehículo, lo cual es clave para el análisis operativo.
Promedio del tiempo de llenado por vehículo para identificar patrones de congestión.

### Análisis Temporal:

**Tendencias de ventas**: Análisis de ventas diarias, semanales y mensuales para observar cambios a lo largo del tiempo.

**Horas pico**: Identificación de las horas del día con mayor volumen de ventas basadas en Fecha_Inicial.

**Análisis por producto**: Evaluación de qué productos se venden más en cada estación y momento.

Este análisis exploratorio proporcionará una base sólida para la identificación de patrones, relaciones significativas, y cualquier comportamiento inusual en los datos.

### Modelos predictivos y técnicas de machine learning:

En esta fase, se implementarán modelos y técnicas de aprendizaje automático para extraer patrones y realizar predicciones:

Se utilizará regresión lineal simple para realizar predicciones sobre el precio publico [PPU] y [CANTIDAD] de producto suministrado, ajustando el modelo a las características de los datos.

### Visualización:


Finalmente, se crearán visualizaciones interactivas para facilitar la interpretación de los resultados obtenidos:

Se desarrollarán dashboards interactivos en Python, que mostrarán tanto los patrones identificados como las predicciones realizadas sobre los datos de ventas.
Se incluirán gráficos geográficos para representar de manera visual ubicacion de la red de estaciones de servicio.

---

## Análisis de resultados
El análisis de resultados del proyecto de automatización de datos con Python y ciencia de datos será fundamental para medir el éxito del proyecto y determinar si los objetivos propuestos se han cumplido. Aquí se presenta un análisis basado en diferentes métricas que permitirán evaluar los resultados obtenidos una vez implementado el sistema.

### 1. Medición de la Eficiencia Operativa
#### **Reducción de tiempo en la consolidación de datos**:

* Comparación entre el tiempo que antes tomaba consolidar los datos manualmente en Excel versus el tiempo que ahora toma hacerlo con el sistema automatizado en Python.
* #### **Resultado esperado**:
   Una reducción significativa del tiempo invertido, por ejemplo, de varios días a solo unas horas o minutos.

#### **Ahorro en costos operativos**:

* Evaluación de los costos asociados a la carga manual de trabajo antes de la automatización (salarios, horas extras, errores) frente a los costos actuales, que deberían haber disminuido con la automatización de procesos.

* #### **Resultado esperado**:
  Reducción de costos al eliminar tareas manuales y minimizar errores que impacten negativamente en la operación.

### 2. Calidad y Consistencia de los Datos
##### **Reducción de errores en los datos**:

* Comparación de la cantidad de errores detectados antes (errores de duplicación, inconsistencia, datos faltantes) y después de la implementación del sistema automatizado.

* #### **Resultado esperado**:
  Disminución en la tasa de errores en los datos consolidados, lo que indica una mejora en la calidad de la información.
#### **Integridad de los datos**:

* Medir la integridad de los datos automatizados mediante pruebas que evalúen si todas las fuentes de datos están correctamente conectadas y los datos completos.
* #### **Resultado esperado**:
  Datos integrados correctamente, sin pérdida de información en el proceso de consolidación.
### 3. Impacto en la Toma de Decisiones
#### **Velocidad en la toma de decisiones**:

* Evaluar cuánto tiempo se ha reducido en la generación de informes y la disponibilidad de los datos para la toma de decisiones. Esto se puede medir en comparación con el sistema anterior.
* ##### **Resultado esperado**:
  Toma de decisiones más rápida gracias a la disponibilidad de información en tiempo real, a través de dashboards dinámicos.
#### **Precisión en la planificación estratégica**:

* Comparar la precisión de las decisiones antes y después del proyecto, utilizando métricas como la exactitud de las previsiones de ventas o inventarios generados por los modelos predictivos implementados.
* #### **Resultado esperado**:
  Aumento en la precisión de las decisiones estratégicas, con previsiones más ajustadas y basadas en datos históricos y patrones.
### 4. Rendimiento de los Modelos Predictivos
* #### Evaluación de los modelos predictivos:
  * Se analizarán los resultados de los modelos de machine learning, como la precisión y la tasa de error de las predicciones en ventas.
  * #### **Resultado esperado**:
  Los modelos predictivos alcanzan niveles altos de precisión (>80%) y son útiles para apoyar la planificación y decisiones futuras.
* #### Valor generado por los modelos predictivos:

  * Análisis del impacto de los modelos predictivos en áreas clave, como la optimización de inventarios o el aumento de la eficiencia operativa.
  * #### **Resultado esperado**:
  Uso efectivo de los modelos para prever la demanda y optimizar recursos, generando ahorro o incremento en las ventas.

### 5. Usabilidad y Adopción del Nuevo Sistema
* #### Satisfacción del usuario:

  * Encuestas o entrevistas con los empleados que utilizan el nuevo sistema para medir su nivel de satisfacción en términos de facilidad de uso, eficiencia y si sienten que mejora su trabajo diario.
  * #### **Resultado esperado**:
  Alta satisfacción de los usuarios, con la adopción completa del sistema en sus flujos de trabajo.
*  #### Adopción del sistema:


  * Medición del porcentaje de empleados que utilizan el nuevo sistema de manera constante frente a aquellos que siguen recurriendo a Excel u otros métodos tradicionales.
  * #### **Resultado esperado**:
* Adopción total o mayoritaria del sistema automatizado, con una dependencia mínima o nula de Excel.
### 6. Visualización y Accesibilidad de Datos
* #### Acceso a información en tiempo real:

  * Verificar si los dashboards y paneles de control permiten a los usuarios acceder a los datos en tiempo real y de manera eficiente.
  * #### **Resultado esperado**:
  Los dashboards interactivos están operativos y son utilizados regularmente por los usuarios clave para la toma de decisiones.
* #### Mejora en la interpretación de datos:

Evaluar si la visualización de datos ha mejorado la interpretación de los mismos por parte de los responsables de tomar decisiones. Esto puede incluir la facilidad para identificar tendencias, problemas o oportunidades.
Resultado esperado: Los usuarios perciben mejoras significativas en la claridad y utilidad de los datos presentados, facilitando el análisis de las operaciones de la empresa.

### 7. Impacto General en la Empresa
* #### Incremento en la eficiencia global:

  * Evaluar el impacto general en la eficiencia de la empresa, en términos de tiempo y recursos que se han liberado para actividades de mayor valor agregado, como análisis estratégico o mejoras operacionales.
  * #### **Resultado esperado**:
  La empresa opera con mayor agilidad y puede responder más rápido a cambios en el entorno gracias al sistema de automatización implementado.

---

## Cronograma General:
* Fase 1 (2 dias): Evaluación inicial y limpieza de datos.
* Fase 2 (3 dias): Desarrollo de scripts de automatización (ETL) para la consolidación de datos.
* Fase 3 (5 dias): Implementación de modelos predictivos y generación de informes automáticos.
* Fase 4 (5 dias): Pruebas, ajustes y capacitación usuarios.

---

## Recursos Involucrados:
Equipo de Desarrollo:
Científico de datos (2).
Desarrollador Python (1).
Analista de negocios (1).

## Herramientas y Tecnologías Clave:
* **Python**: Lenguaje base para la automatización y análisis de datos.
* **Python-dotenv**: se utiliza para cargar variables de entorno desde un archivo .env a las variables de entorno de Python.
* **logging**: para registrar eventos y errores en un archivo de texto.
* **os**: interactuar con el sistema operativo.
* **pandas, NumPy**: Para la manipulación de datos.
* **pyodbc**: Para la conexión con bases de datos.
* **sqlite3**: Base de datos ligera basada en disco
* **scikit-learn**: Para modelos de machine learning.
* **Plotly**: Para la visualización de datos.
* **Dash**: Para la creación de dashboards interactivos.
* **Mapbox**: Location intelligence for business - plataforma de código abierto de mapeo

---
# Conclusiones Esperadas del Proyecto:

### 1. Automatización Eficiente de Procesos:

  * Se logrará una automatización completa en los procesos de consolidación, análisis y reporte de datos, eliminando la necesidad de manipulación manual de hojas de cálculo en Excel.
  * El uso de Python reducirá significativamente los tiempos de procesamiento de datos, permitiendo a la empresa reaccionar más rápidamente a cambios en su entorno operativo.
### 2. Mejora en la Calidad y Consistencia de los Datos:

Al centralizar los datos en una base de datos única y automatizar el proceso de validación de los mismos, se reducirá la duplicidad, errores humanos y falta de consistencia en los reportes.
La información será más fiable y precisa, lo que mejorará la toma de decisiones estratégicas basadas en datos.
### 3. Toma de Decisiones Basada en Datos en Tiempo Real:

El sistema automatizado proporcionará acceso a datos en tiempo real, permitiendo que los directivos y responsables de áreas clave puedan tomar decisiones más ágiles y fundamentadas.
Los dashboards interactivos facilitarán la visualización clara de KPIs y métricas clave, ayudando a identificar problemas o tendencias de forma oportuna.
### 4. Reducción de Costos Operativos y Mejora en la Productividad:

Al reducir el tiempo invertido en tareas manuales como la actualización y consolidación de datos, el equipo de trabajo podrá enfocarse en tareas de mayor valor agregado, mejorando la productividad general.
Se espera una reducción de costos operativos asociados a errores en la consolidación de datos o retrasos en la generación de informes.
### 5. Capacitación y Empoderamiento del Personal:

Aunque se requerirá una fase inicial de capacitación, el personal clave tendrá las herramientas necesarias para interactuar con los nuevos sistemas automatizados, lo que generará mayor empoderamiento y una mayor comprensión del valor de los datos dentro de la empresa.
### 6. Escalabilidad y Preparación para el Crecimiento:

La solución implementada será escalable, permitiendo que se amplíe a otras áreas de la empresa más allá de ventas e inventarios en futuras fases.
La empresa estará mejor preparada para manejar grandes volúmenes de datos a medida que crezca, sin comprometer la eficiencia o calidad de la información.
### 7. Capacidad para Desarrollar Modelos Predictivos:

El proyecto incluirá la creación de modelos predictivos que permitan anticipar tendencias futuras, como previsión de ventas o demanda de inventarios, lo que aportará un enfoque proactivo en la planificación y optimización de recursos.
### 8. Mejoras en la Colaboración Interdepartamental:

Al centralizar los datos en una base única y eliminar las versiones dispersas en Excel, los diferentes departamentos de la empresa podrán trabajar con una fuente única de verdad, mejorando la colaboración y evitando la duplicación de esfuerzos.
### 9. Reducción de Riesgos:

La implementación de controles automáticos y la eliminación de procesos manuales reducirán el riesgo de errores humanos y de pérdida de información crítica, lo que disminuirá la posibilidad de decisiones erróneas basadas en datos incorrectos.
### 10. Mejora en la Competitividad de la Empresa:

El uso de ciencia de datos permitirá a la empresa obtener ventajas competitivas al mejorar su capacidad de análisis, anticipar tendencias del mercado y optimizar sus procesos internos, lo que la hará más ágil y eficiente en comparación con sus competidores.

---
## Referencias
* **Python Tutorial**. Guido van Rossum and the Python development team September 02, 2018
* **Machine Learning y Scikit-Learn** - Sebastian Raschka - Yuxi Liu - Ed Marcombo 2023
* **Machine Learning y Deep Learning** - Jesús Bobadilla - Ed Ra-Ma - 2021
* **Estadistica práctica para ciencia de datos con R y Python** - Peter Bruce, Andrew Bruce y Peter Gedeck - Marcombo 2022
* https://plotly.com/
* https://dash.plotly.com/
* https://www.mapbox.com/

## 🎉 Equipo Estrella - Data Science 🎉
* Angélica Vargas - Ing Electronica - 🌟 Data Wizard – Siempre despejando el camino y poniendo magia en cada modelo.
* Andrés Castro - Analista de Datos - 📊 Maestro en encontrar patrones, con ojos de halcón para detectar insights entre líneas de datos.
* Cristian Ramirez - Analista de Datos - 📈 Cuenta historias en gráficos, ¡porque un buen gráfico vale más que mil palabras!
* Cristian Camilo Chávez - 5Sem/Ing Software - Analista de Datos - 🚀 DevOps de Datos – Impulsa nuestros datos hacia las estrellas, asegurándose de que todo esté en su lugar y seguro.


