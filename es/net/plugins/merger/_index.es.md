---
title: Merger
type: docs
weight: 100
url: /net/plugins/merger/
description: Cómo fusionar múltiples archivos PDF en uno usando el complemento Aspose.PDF Merger
lastmod: "2024-01-24"
---

En este artículo, le mostraremos cómo usar el [complemento Merger](https://products.aspose.org/pdf/net/merger/), que puede fusionar múltiples archivos PDF en uno y guardarlo como un nuevo archivo.

## Prerrequisitos

Necesitará lo siguiente:

* Visual Studio 2019 o posterior
* Aspose.PDF para .NET 21.1 o posterior
* Tres archivos PDF de muestra que desea fusionar

Puede descargar la biblioteca Aspose.PDF para .NET desde el sitio web oficial o instalarla utilizando el Administrador de Paquetes NuGet en Visual Studio.

## Pasos

Los pasos básicos para fusionar múltiples archivos PDF en uno usando el complemento Merger son:

1. Crear un objeto de la clase Merger
2. Crear un objeto de la clase MergeOptions y agregar las rutas de los archivos de entrada y salida
3. Ejecutar el método Process del objeto Merger

Veamos cómo implementar estos pasos en código C#.

### Paso 1: Crear un objeto de la clase Merger
### Paso 1: Crear un objeto de la clase Merger

La clase Merger es la clase principal que proporciona la funcionalidad de fusionar múltiples archivos PDF en uno. Para usarla, necesitas crear una instancia de la misma utilizando el constructor predeterminado:

```cs
// Crear una nueva instancia de Merger
var pdfMerger = new Merger();
```

### Paso 2: Crear un objeto de la clase MergeOptions y añadir las rutas de los archivos de entrada y salida

La clase MergeOptions es una clase auxiliar que te permite especificar varias opciones y parámetros para el proceso de fusión, como el rango de páginas, el orden, la seguridad, etc.
La clase MergeOptions es una clase de ayuda que le permite especificar varias opciones y parámetros para el proceso de fusión, como el rango de páginas, el orden, la seguridad, etc.

```cs
// Especificar las rutas de los archivos de entrada y salida
string inputFilePath1 = Path.Combine(@"C:\Samples\", "sample1.pdf");
string inputFilePath2 = Path.Combine(@"C:\Samples\", "sample2.pdf");
string inputFilePath3 = Path.Combine(@"C:\Samples\", "sample3.pdf");
var outputFilePath = "TestMerge.pdf";

// Crear una instancia de la clase MergeOptions
var mergeOptions = new MergeOptions();

// Agregar las rutas de los archivos de entrada y salida a las opciones
mergeOptions.Inputs.Add(new FileDataSource(inputFilePath1));
mergeOptions.Inputs.Add(new FileDataSource(inputFilePath2));
mergeOptions.Inputs.Add(new FileDataSource(inputFilePath3));
mergeOptions.AddOutput(new FileDataSource(outputFilePath));
```

### Paso 3: Ejecutar el método Process del objeto Merger

El paso final es ejecutar el método Process del objeto Merger, pasando el objeto mergeOptions como parámetro.
El paso final es ejecutar el método Process del objeto Merger, pasando el objeto mergeOptions como parámetro.

```cs
// Procesar la fusión y guardar el archivo fusionado
pdfMerger.Process(mergeOptions);

// Imprimir un mensaje de confirmación
Console.WriteLine("Los archivos PDF se han fusionado exitosamente.");
```
