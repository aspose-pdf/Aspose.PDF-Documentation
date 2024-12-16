---
title: JPEG Converter
type: docs
weight: 90
url: /es/net/plugins/jpeg/
description: Cómo convertir páginas PDF en imágenes JPEG usando Aspose.PDF JPEG Converter
lastmod: "2024-01-24"
draft: false
---

En este artículo, te mostraremos cómo usar el [JPEG Converter](https://products.aspose.org/pdf/net/jpeg-converter/), que puede convertir páginas PDF en imágenes JPEG y guardarlas como archivos separados.

## Prerrequisitos

Necesitarás lo siguiente:

* Visual Studio 2019 o posterior
* Aspose.PDF para .NET 24.1 o posterior
* Un archivo PDF de muestra que contenga algunas páginas

Puedes descargar la biblioteca Aspose.PDF para .NET desde el sitio web oficial o instalarla usando el Administrador de Paquetes NuGet en Visual Studio.

## Pasos

Los pasos básicos para convertir páginas PDF en imágenes JPEG usando el JPEG Converter son:

1. Crear un objeto de la clase Jpeg
1. Crear un objeto de la clase JpegOptions y añadir las rutas de los archivos de entrada y salida
1. Ejecutar el método Process del objeto Jpeg y obtener el contenedor de resultados
1.
1.

Veamos cómo implementar estos pasos en código C#.

### Paso 1: Crear un objeto de la clase Jpeg

La clase Jpeg es la clase principal que proporciona la funcionalidad de convertir páginas PDF en imágenes JPEG. Para usarla, necesitas crear una instancia de ella usando el constructor predeterminado:

```cs
// Crear una nueva instancia de Jpeg
var converter = new Jpeg();
```

### Paso 2: Crear un objeto de la clase JpegOptions y añadir las rutas de los archivos de entrada y salida

La clase JpegOptions es una clase auxiliar que te permite especificar varias opciones y parámetros para el proceso de conversión, como la resolución de salida, el rango de páginas, la calidad de la imagen, etc.
La clase JpegOptions es una clase auxiliar que te permite especificar varias opciones y parámetros para el proceso de conversión, como la resolución de salida, el rango de páginas, la calidad de la imagen, etc.

```cs
// Especifica las rutas de los archivos de entrada y salida
var inputPath = Path.Combine(@"C:\Samples\", "sample.pdf");
var outputPath = Path.Combine(@"C:\Samples\", "images");

// Crea una instancia de la clase JpegOptions
var converterOptions = new JpegOptions();

// Agrega las rutas de los archivos de entrada y salida a las opciones
converterOptions.AddInput(new FileDataSource(inputPath));
converterOptions.AddOutput(new FileDataSource(outputPath));
```

También puedes establecer otras opciones, como la resolución de salida, el rango de páginas, la calidad de la imagen, etc. utilizando las propiedades de la clase JpegOptions. Por ejemplo, para convertir solo la primera página del archivo PDF a una imagen JPEG con una resolución de 300 dpi, puedes usar el siguiente código:

```cs
// Establece la resolución de salida a 300 dpi
converterOptions.OutputResolution = 300;

// Establece el rango de páginas a la primera página
converterOptions.PageRange = new PageRange(1);
```
### Paso 3: Ejecutar el método Process del objeto Jpeg y obtener el contenedor de resultados

El paso final es ejecutar el método Process del objeto Jpeg, pasando el objeto converterOptions como parámetro. Este método realizará la conversión y devolverá un objeto ResultContainer, que contiene los resultados de la conversión, como el estado, los mensajes, las rutas de los archivos de salida, etc. Puedes acceder a los resultados utilizando las propiedades y métodos de la clase ResultContainer. Por ejemplo, para obtener el contenedor de resultados e imprimir el estado de la conversión, puedes usar el siguiente código:

```cs
// Procesar la conversión y obtener el contenedor de resultados
ResultContainer resultContainer = converter.Process(converterOptions);

// Imprimir el estado de la conversión
Console.WriteLine(resultContainer.Status);
```

El estado de la conversión puede ser Éxito o Fallo, dependiendo de si la conversión se completó con éxito o no.

### Paso 4: Imprimir las rutas de las imágenes JPEG convertidas

El contenedor de resultados contiene una colección de resultados, uno para cada ruta de archivo de salida.
El contenedor de resultados contiene una colección de resultados, uno para cada ruta de archivo de salida.

```cs
// Imprime las rutas de las imágenes JPEG convertidas
foreach (FileResult operationResult in resultContainer.ResultCollection.Cast<FileResult>())
{
  Console.WriteLine(operationResult.Data.ToString());
}
```

Las rutas de los archivos de salida tendrán el formato de {outputPath}{pageNumber}.jpg, donde {outputPath} es el directorio de salida y {pageNumber} es el número de página del archivo PDF. Por ejemplo, si el directorio de salida es C:\Samples\images y el archivo PDF tiene tres páginas, las rutas de los archivos de salida serán:

```text
C:\Samples\images\1.jpg
C:\Samples\images\2.jpg
C:\Samples\images\3.jpg
```
