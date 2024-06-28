# Análisis y combinación de datos de caudal de ríos en la Región de Ñuble

## Descripción

Este proceso consiste en la lectura, limpieza, agrupación y análisis de datos de caudal mensual de varios ríos en la Región de Ñuble. Los datos se fueron extraídos de la [Dirección General de Aguas](https://snia.mop.gob.cl/BNAConsultas/reportes) en archivos Excel y fueron procesados para obtener resultados anuales promedio, que luego se guardaron en archivos separados por río. 

## Pasos detallados

### 1. Recepción y lectura de datos

- Se recibieron múltiples archivos Excel (`.xlsx`) que contenían datos de caudal mensual de diferentes ríos y sus subcuencas.
- Cada archivo contenía varias hojas, cada una representando datos de diferentes ubicaciones de un río o subcuenca.

### 2. Agrupación de datos por río

- Se leyeron todas las hojas de cada archivo Excel y se agruparon los datos por el nombre del río principal.
- Los nombres de los ríos se identificaron a partir de las primeras palabras en el nombre de cada hoja.
- Los datos de todas las hojas correspondientes a un mismo río se combinaron en un solo DataFrame.

### 3. Limpieza de datos

- Se seleccionaron y renombraron manualmente las columnas relevantes (`AÑO`, `ENE`, `FEB`, `MAR`, `ABR`, `MAY`, `JUN`, `JUL`, `AGO`, `SEP`, `OCT`, `NOV`, `DIC`).
- Se eliminaron filas y columnas innecesarias, asegurando que solo se mantuvieran los datos relevantes para el análisis.
- Se corrigieron los valores no numéricos en la columna `AÑO` y se convirtieron a enteros.

### 4. Combinación de subcuencas en ríos principales

- Los datos de las subcuencas se combinaron con los ríos principales correspondientes:
  - `Río Niblinto` se combinó con `Río Cato`.
  - `Río Larqui`, `Río Renegado` y `Río Lonquén` se combinaron con `Río Itata`.
  - `Río Sauces` se combinó con `Río Ñuble`.
- Se promediaron los datos de las subcuencas y se agregaron a los ríos principales.

### 5. Cálculo de promedios anuales

- Se calcularon los promedios anuales del caudal mensual para cada río.
- Los resultados se guardaron en archivos separados por río.



