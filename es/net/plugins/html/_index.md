---
title: Conversor HTML
type: docs
weight: 70
url: /es/net/plugins/html/
description: Cómo convertir archivos PDF de y hacia archivos HTML utilizando el complemento PdfHtml de Aspose.PDF
lastmod: "2024-01-24"
draft: false
---

En este artículo, te mostraremos cómo usar el [complemento PdfHtml](https://products.aspose.org/pdf/net/html-converter/), que puede convertir archivos PDF de y hacia archivos HTML.

## Prerrequisitos

Necesitarás lo siguiente:

* Visual Studio 2019 o posterior
* Aspose.PDF para .NET 21.1 o posterior
* Un archivo PDF de muestra y un archivo HTML de muestra

Puedes descargar la biblioteca Aspose.PDF para .NET desde el sitio web oficial o instalarla usando el Administrador de Paquetes NuGet en Visual Studio.

## Pasos

Los pasos básicos para convertir archivos PDF de y hacia archivos HTML usando el complemento PdfHtml son:

1. Crear un objeto de la clase PdfHtml
2. Crear un objeto de la clase PdfToHtmlOptions o HtmlToPdfOptions, dependiendo de la dirección de la conversión
3. Agregar las fuentes de datos de entrada y salida al objeto de opciones
4.
### Paso 1: Crear un objeto de la clase PdfHtml

La clase PdfHtml es la clase principal que proporciona la funcionalidad de convertir archivos PDF a y desde archivos HTML. Para usarla, necesitas crear una instancia de ella utilizando el constructor predeterminado:

```cs
// Crear una instancia del complemento PdfHtml
var plugin = new PdfHtml();
```

### Paso 2: Crear un objeto de la clase PdfToHtmlOptions o HtmlToPdfOptions, dependiendo de la dirección de la conversión

Las clases PdfToHtmlOptions y HtmlToPdfOptions son clases auxiliares que te permiten especificar varias opciones y parámetros para el proceso de conversión, como el formato de salida, el rango de páginas, la codificación, las fuentes, etc. Para usar estas clases, necesitas crear una instancia de la clase apropiada usando el constructor predeterminado o pasando algunos parámetros. Por ejemplo, para convertir un archivo PDF a un archivo HTML con recursos incrustados, puedes usar el siguiente código:

```cs
```cs
// Crear una nueva instancia de la clase PdfToHtmlOptions
var options = new PdfToHtmlOptions(PdfToHtmlOptions.SaveDataType.FileWithEmbeddedResources);
```

Para convertir un archivo HTML a un archivo PDF con configuraciones predeterminadas, puedes usar el siguiente código:

```cs
// Crear una nueva instancia de la clase HtmlToPdfOptions
var options = new HtmlToPdfOptions();
```

También puedes establecer otras opciones, como el formato de salida, el rango de páginas, la codificación, las fuentes, etc. usando las propiedades de las clases de opciones. Por ejemplo, para convertir un archivo PDF a un archivo HTML con codificación UTF-8 y fuente Arial, puedes usar el siguiente código:

```cs
// Crear una nueva instancia de la clase PdfToHtmlOptions
var options = new PdfToHtmlOptions(PdfToHtmlOptions.SaveDataType.FileWithEmbeddedResources);

// Establecer la codificación a UTF-8
options.Encoding = Encoding.UTF8;

// Establecer la fuente a Arial
options.Font = "Arial";
```

### Paso 3: Agregar las fuentes de datos de entrada y salida al objeto de opciones

Las fuentes de datos de entrada y salida son los archivos PDF o HTML que deseas convertir y guardar.
Las fuentes de datos de entrada y salida son los archivos PDF o HTML que desea convertir y guardar.

```cs
// Especifique las rutas de los archivos de entrada y salida
var inputPath = Path.Combine(@"C:\Samples\", "sample.pdf");
var outputPath = Path.Combine(@"C:\Samples\", "sample.html");

// Agregue las rutas de los archivos de entrada y salida a las opciones
options.AddInput(new FileDataSource(inputPath));
options.AddOutput(new FileDataSource(outputPath));
```

### Paso 4: Ejecute el método Process del objeto PdfHtml

El paso final es ejecutar el método Process del objeto PdfHtml, pasando el objeto de opciones como parámetro. Este método realizará la conversión y devolverá un objeto ResultContainer, que contiene los resultados de la conversión, como el estado, los mensajes, las fuentes de datos de salida, etc. Puede acceder a los resultados utilizando las propiedades y métodos de la clase ResultContainer. Por ejemplo, para obtener el primer resultado de la colección de resultados e imprimirlo en la consola, puede usar el siguiente código:

```cs
// Procese la conversión y obtenga el contenedor de resultados
var resultContainer = plugin.Process(options);

// Obtenga el primer resultado de la colección de resultados
var result = resultContainer.ResultCollection[0];

// Imprima el resultado en la consola
Console.WriteLine(result);
```
El resultado contendrá información como las rutas de los archivos de salida.
