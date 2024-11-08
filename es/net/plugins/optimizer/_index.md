---
title: Optimizer 
type: docs
weight: 80
url: /es/net/plugins/optimizer/
description: Cómo optimizar y manipular archivos PDF con Aspose.PDF Optimizer
lastmod: "2024-01-24"
---

En este capítulo, exploraremos cómo utilizar [Aspose.PDF Optimizer](https://products.aspose.org/pdf/net/optimizer/) para optimizar, redimensionar y rotar archivos PDF en tus aplicaciones de C#.
Vamos a sumergirnos y aprender cómo realizar estas tareas paso a paso.

## Prerrequisitos

Necesitarás lo siguiente:

* Visual Studio 2019 o posterior
* Aspose.PDF para .NET 24.1 o posterior
* Un archivo PDF de muestra que contenga algunos campos de formulario

## Optimizando archivos PDF

Optimizar un archivo PDF implica reducir su tamaño y mejorar el rendimiento. Los siguientes fragmentos muestran cómo lograr esta tarea. Aquí está cómo puedes optimizar un archivo PDF:

* Crea una nueva fuente de datos de archivo para el archivo PDF de entrada.
* Crea una nueva fuente de datos de archivo para el archivo PDF de salida optimizado.
* Crea una instancia de `OptimizeOptions`.
* Agrega las fuentes de datos de entrada y salida a las opciones de optimización.
* Agrega las fuentes de datos de entrada y salida a las opciones de optimización.
* Crea una instancia de `Optimizer` y procesa la optimización utilizando las opciones de optimización.

```cs
// Crea una nueva fuente de datos de archivo para el archivo PDF de entrada.
var inputDataSource = new FileDataSource(inputPath);

// Crea una nueva fuente de datos de archivo para el archivo PDF de salida optimizado.
var outputDataSource = new FileDataSource("sample_optimized.pdf");

// Crea una nueva instancia de OptimizeOptions.
var options = new OptimizeOptions();

// Agrega las fuentes de datos de entrada y salida a las opciones de optimización.
options.AddInput(inputDataSource);
options.AddOutput(outputDataSource);

// Crea una nueva instancia de Optimizer.
var optimizer = new Optimizer();

// Procesa la optimización utilizando las opciones de optimización.
optimizer.Process(options);
```

## Redimensionando Archivos PDF

Redimensionar un archivo PDF implica cambiar el tamaño de su página. El siguiente código muestra cómo lograr esta tarea. Sigue estos pasos para redimensionar un archivo PDF:

* Crea una nueva fuente de datos de archivo para el archivo PDF de entrada.
* Cree una nueva fuente de datos de archivo para el archivo PDF de entrada.
* Cree una nueva fuente de datos de archivo para el archivo PDF de salida redimensionado.
* Cree una instancia de `ResizeOptions` y establezca el tamaño de página deseado.
* Agregue las fuentes de datos de entrada y salida a las opciones de redimensionamiento.
* Cree una instancia de `Optimizer` y procese el redimensionamiento utilizando las opciones de redimensionamiento.

```cs
// Cree una nueva fuente de datos de archivo para el archivo PDF de entrada.
var inputDataSource = new FileDataSource("sample.pdf");

// Cree una nueva fuente de datos de archivo para el archivo PDF de salida redimensionado.
var outputDataSource = new FileDataSource("sample_resized.pdf");

// Cree una nueva instancia de ResizeOptions y establezca el tamaño de página deseado.
var opt = new ResizeOptions
{
    PageSize = PageSize.PageLetter
};

// Agregue las fuentes de datos de entrada y salida a las opciones de redimensionamiento.
opt.AddInput(inputDataSource);
opt.AddOutput(outputDataSource);

// Cree una nueva instancia de Optimizer.
var optimizer = new Optimizer();

// Procese el redimensionamiento utilizando las opciones de redimensionamiento.
optimizer.Process(opt);
```

## Rotación de páginas PDF
## Rotación de páginas PDF

Rotar páginas PDF te permite cambiar la orientación de las páginas dentro de un documento PDF. Aquí te mostramos cómo puedes rotar páginas PDF:

* Crea una nueva fuente de datos de archivo para el archivo PDF de entrada.
* Crea una nueva fuente de datos de archivo para el archivo PDF de salida.
* Crea una instancia de `RotateOptions` y establece el valor de rotación.
* Añade las fuentes de datos de entrada y salida a las opciones de rotación.
* Crea una instancia de `Optimizer` y procesa la rotación utilizando las opciones de rotación.

```cs
// Crea una nueva fuente de datos de archivo para el archivo PDF de entrada.
var inputDataSource = new FileDataSource(inputPath);

// Crea una nueva fuente de datos de archivo para el archivo PDF de salida optimizado.
var outputDataSource = new FileDataSource("sample_optimized.pdf");

// Crea una nueva instancia de RotateOptions.
var opt = new RotateOptions();

// Añade las fuentes de datos de entrada y salida a las opciones de rotación.
opt.AddInput(inputDataSource);
opt.AddOutput(outputDataSource);

// Establece el valor de rotación
opt.Rotation = Rotation.on180;

// Crea una nueva instancia de Optimizer.
var optimizer = new Optimizer();

// Procesa la optimización utilizando las opciones de rotación.
optimizer.Process(opt)
```
## Conclusión

Has aprendido cómo optimizar, redimensionar y rotar archivos PDF utilizando el Plugin Optimizador de Aspose.PDF en C#. Incorpora estas técnicas en tus aplicaciones para manipular eficientemente documentos PDF según tus necesidades.
