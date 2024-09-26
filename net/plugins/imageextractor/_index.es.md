---
title: Extractor de Imágenes
type: docs
weight: 80
url: /net/plugins/imageextractor/
description: Extracción de imágenes de PDFs simplificada con el plugin ImageExtractor
lastmod: "2024-01-24"
draft: false
---

Si alguna vez has necesitado extraer imágenes de un archivo PDF usando .NET, Aspose.PDF para .NET ofrece una solución poderosa y sencilla. En esta guía, te mostraremos los pasos básicos para crear un objeto, añadir una fuente de datos y ejecutar el método de proceso usando el [Extractor de Imágenes Aspose.PDF](https://products.aspose.org/pdf/net/image-extractor/).

## Prerrequisitos

Necesitarás lo siguiente:

* Visual Studio 2019 o posterior
* Aspose.PDF para .NET 21.1 o posterior
* Un archivo PDF de muestra

Puedes descargar la biblioteca Aspose.PDF para .NET desde el sitio web oficial o instalarla usando el Gestor de Paquetes NuGet en Visual Studio.
Ahora, vamos a sumergirnos en el código y aprender cómo usar el plugin ImageExtractor.

## Pasos

El código proporcionado demuestra el uso del plugin `ImageExtractor` para extraer imágenes de un archivo PDF.
El código proporcionado demuestra el uso del complemento `ImageExtractor` para extraer imágenes de un archivo PDF.

### 1. Crear un Objeto (ImageExtractor)

El primer paso involucra crear una instancia del complemento `ImageExtractor`. Esto se logra utilizando el siguiente código:

```csharp
using var plugin = new ImageExtractor();
```

Aquí, la declaración `using` asegura la eliminación adecuada de los recursos cuando la operación está completa.

### 2. Agregar Fuente de Datos

A continuación, se crea una instancia de la clase `ImageExtractorOptions` para configurar el proceso de extracción de imágenes. La ruta del archivo de entrada se agrega a las opciones utilizando el método `AddInput`:

```csharp
var imageExtractorOptions = new ImageExtractorOptions();
imageExtractorOptions.AddInput(new FileDataSource(Path.Combine(@"C:\Samples\", "sample.pdf")));
```

Asegúrate de reemplazar `"C:\Samples\"` y `"sample.pdf"` con la ruta y el nombre de archivo adecuados de tu archivo PDF.

### 3. Ejecutar Método Process

El paso final es procesar la extracción de imágenes utilizando el complemento y las opciones:

```csharp

El resultado se almacena en el `resultContainer`, que contiene la(s) imagen(es) extraída(s).

### 4. Manejar la(s) Imagen(es) Extraída(s)

Después de ejecutar el proceso, puedes recuperar la(s) imagen(es) extraída(s) del contenedor de resultados. El código a continuación demuestra cómo guardar la primera imagen extraída en una ubicación temporal:

```csharp
var imageExtracted = resultContainer.ResultCollection[0].ToStream();
var someTemporaryPlace = File.OpenWrite("C:\\tmp\\tmp.jpg");
imageExtracted.CopyTo(someTemporaryPlace);
```

Asegúrate de personalizar la ruta de destino y el nombre del archivo según tus preferencias.

Puedes copiar el ejemplo completo a continuación:

```cs
using Aspose.Pdf.Plugins;

namespace AsposePluginsNet8.Documentation;

internal static class ImageExtractorDemo
{
    // <summary>
    // Demuestra el uso del plugin ImageExtractor para extraer imágenes de un archivo PDF.
    // </summary>
    internal static void Run()
    {
        // Crear una instancia del plugin ImageExtractor.
        using var plugin = new ImageExtractor();

        // Crear una instancia de la clase ImageExtractorOptions.
        var imageExtractorOptions = new ImageExtractorOptions();

        // Añadir la ruta del archivo de entrada a las opciones.
        imageExtractorOptions.AddInput(new FileDataSource(Path.Combine(@"C:\Samples\", "sample.pdf")));

        // Procesar la extracción de imágenes usando el plugin y las opciones.
        var resultContainer = plugin.Process(imageExtractorOptions);

        // Obtener la imagen extraída del contenedor de resultados.
        var imageExtracted = resultContainer.ResultCollection[0].ToStream();
        var someTemporaryPlace = File.OpenWrite(Path.Combine(@"C:\Samples\","tmp.jpg"));
        imageExtracted.CopyTo(someTemporaryPlace);
    }
}
```

