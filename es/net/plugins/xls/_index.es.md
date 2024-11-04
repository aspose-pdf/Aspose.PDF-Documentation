---
title: XLS Converter
type: docs
weight: 20
url: /net/plugins/xls/
description: Cómo convertir archivos PDF a hojas de cálculo de Excel utilizando los complementos de Aspose.Pdf
lastmod: "2024-01-24"
---

{{% alert color="primary" %}}

En este artículo, te mostraremos cómo usar el [complemento PdfXls](https://products.aspose.org/pdf/net/xls-converter/), que puede convertir archivos PDF a formato Excel con alta fidelidad y precisión.

{{% /alert %}}

## Prerrequisitos

Necesitarás lo siguiente:

* Visual Studio 2019 o posterior
* Aspose.PDF para .NET 24.1 o posterior
* Un archivo PDF de muestra que quieras convertir a formato Excel

Puedes descargar la biblioteca Aspose.PDF para .NET desde el sitio web oficial o instalarla usando el Administrador de Paquetes NuGet en Visual Studio.

## Pasos

Los pasos básicos para convertir un archivo PDF a formato Excel usando el complemento PdfXls son:

1. Crear un objeto de la clase PdfXls
1. Agregar las fuentes de datos de entrada y salida al objeto PdfToXlsOptions
1. Ejecutar el método Process del objeto PdfXls

Veamos cómo implementar estos pasos en código C#.
Veamos cómo implementar estos pasos en código C#.

### Paso 1: Crear un objeto de la clase PdfXls

La clase PdfXls es la clase principal que proporciona la funcionalidad de convertir PDF a Excel. Para usarla, necesitas crear una instancia de ella usando el constructor predeterminado:

```csharp
// Crear una instancia del plugin PdfXls
var plugin = new PdfXls();
```

### Paso 2: Agregar las fuentes de datos de entrada y salida al objeto PdfToXlsOptions

La clase PdfToXlsOptions es una clase auxiliar que te permite especificar varias opciones y parámetros para el proceso de conversión. Para usarla, necesitas crear una instancia de ella y agregar las fuentes de datos de entrada y salida utilizando los métodos `AddInput` y `AddOutput`. Las fuentes de datos pueden ser rutas de archivos o streams. Por ejemplo, para convertir un archivo PDF llamado `sample.pdf` en la carpeta `C:\Samples` a un archivo Excel llamado `sample.xlsx` en la misma carpeta, puedes usar el siguiente código:

```csharp
// Especificar las rutas de archivo de entrada y salida
var inputPath = Path.Combine(@"C:\Samples\", "sample.pdf");
var outputPath = Path.Combine(@"C:\Samples\", "sample.xlsx");

// Crear una instancia de la clase PdfToXlsOptions
var options = new PdfToXlsOptions();

// Agregar las rutas de archivo de entrada y salida a las opciones
options.AddInput(new FileDataSource(inputPath));
options.AddOutput(new FileDataSource(outputPath));
```
También puedes configurar otras opciones, como el formato de salida, el rango de páginas, el nombre de la hoja de trabajo, etc. utilizando las propiedades de la clase PdfToXlsOptions. Por ejemplo, para convertir el archivo PDF al formato XLSX, insertar una columna en blanco en la primera posición y nombrar la hoja de trabajo como "MySheet", puedes usar el siguiente código:

```csharp
// Establecer el formato de salida a XLSX
options.Format = PdfToXlsOptions.ExcelFormat.XLSX;

// Insertar una columna en blanco en la primera posición
options.InsertBlankColumnAtFirst = true;
```

### Paso 3: Ejecutar el método Process del objeto PdfXls

El paso final es ejecutar el método Process del objeto PdfXls, pasando el objeto PdfToXlsOptions como parámetro.
El paso final es ejecutar el método Process del objeto PdfXls, pasando el objeto PdfToXlsOptions como parámetro.

```csharp
// Procesa la conversión de PDF a Excel usando el plugin y las opciones
var resultContainer = plugin.Process(options);

// Obtiene el primer resultado de la colección de resultados
var result = resultContainer.ResultCollection[0];

// Imprime el resultado
Console.WriteLine(result);
```

El resultado contendrá información como las rutas de los archivos de salida.
