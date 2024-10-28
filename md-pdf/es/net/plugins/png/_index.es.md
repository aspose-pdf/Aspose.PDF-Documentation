---
title: Convertidor de PNG
type: docs
weight: 110
url: /net/plugins/png/
description: Convertir documentos PDF a imágenes PNG con el plugin Aspose.PDF PNG
lastmod: "2024-01-24"
---

Si estás buscando [convertir documentos PDF en imágenes PNG](https://products.aspose.org/pdf/net/png-converter/) utilizando .NET, Aspose.PDF para .NET ofrece una solución robusta. En este artículo, repasaremos los pasos esenciales para crear un objeto, agregar una fuente de datos y ejecutar el método de proceso utilizando la biblioteca Aspose.PDF.

## Requisitos previos

Necesitarás lo siguiente:

* Visual Studio 2019 o posterior
* Aspose.PDF para .NET 24.1 o posterior
* Un archivo PDF de muestra

## Recorrido por el código

El código a continuación demuestra una demostración de conversión de PNG utilizando el plugin Aspose.PDF PNG:

```csharp
using Aspose.Pdf.Plugins;

//....

// Crear una nueva instancia de la clase PngOptions.
var convertorOptions = new PngOptions();

// Agregar las rutas de entrada y salida a las opciones de Png.
convertorOptions.AddInput(new FileDataSource(Path.Combine(@"C:\Samples\", "sample.pdf")));
convertorOptions.AddOutput(new FileDataSource(Path.Combine(@"C:\Samples\", "images")));

// Establecer la resolución de salida a 300 DPI.
convertorOptions.OutputResolution = 300;

// Crear una nueva instancia de la clase Png.
Png converter = new ();

// Procesar la conversión PNG y obtener el contenedor de resultados.
ResultContainer resultContainer = converter.Process(convertorOptions);

// Imprimir el resultado en la consola.
foreach (FileResult operationResult in resultContainer.ResultCollection.Cast<FileResult>())
{
      Console.WriteLine(operationResult.Data.ToString());
}
```
Desglosemos los pasos clave:

1. **Crear un Objeto (PngOptions y Png)**

   El código comienza creando una instancia de la clase `PngOptions` para configurar la conversión a PNG. Además, se crea una instancia de la clase `Png` para el procesamiento posterior.

2. **Agregar Fuente de Datos**

   La ruta del archivo PDF de entrada se agrega a `PngOptions` usando el método `AddInput`. De manera similar, la ruta de salida para las imágenes PNG se agrega usando el método `AddOutput`.

3. **Establecer Resolución de Salida**

   El código establece la resolución de salida a 300 DPI usando la propiedad `OutputResolution` de la clase `PngOptions`.

4. **Ejecutar Método Process**

   La conversión a PNG se inicia llamando al método `Process` en la clase `Png`, pasando el `PngOptions` configurado. El resultado se almacena en el `resultContainer`.

5. **Manejar Resultado**

   El código imprime el resultado en la consola, mostrando la(s) ruta(s) del archivo convertido.
