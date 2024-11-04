---
title: Extractor de Texto
type: docs
weight: 140
url: /net/plugins/textextractor/
description: Extrae el contenido de texto del documento PDF.
lastmod: "2024-01-24"
---

¿Tienes un documento PDF del cual necesitas [extraer texto programáticamente](https://products.aspose.org/pdf/net/text-extractor/)? Con Aspose.PDF para .NET, puedes lograr esta tarea fácilmente usando la clase TextExtractor. En este artículo, te guiaremos a través de los pasos básicos para crear una aplicación de extracción de texto en .NET, cubriendo la creación de un objeto TextExtractor, añadiendo una fuente de datos y ejecutando el proceso de extracción de texto.

## Requisitos previos

Necesitarás lo siguiente:

* Visual Studio 2019 o posterior
* Aspose.PDF para .NET 24.1 o posterior
* Un archivo PDF de muestra

Adicionalmente, familiarízate con la clase `TextExtractorOptions` y sus funcionalidades. Puedes encontrar información detallada en la [Referencia API de Aspose.PDF](https://reference.aspose.com/pdf/net/aspose.pdf/TextExtractorOptions/).

Ahora, adentrémonos en el código y exploremos cómo extraer texto de un documento PDF.
Ahora, vamos a adentrarnos en el código y explorar cómo extraer texto de un documento PDF.

## Recorrido por el Código

El siguiente código demuestra las capacidades de extracción de texto. Desglosemos los pasos clave:

### 1. Crear un Objeto TextExtractor

El código comienza creando una nueva instancia de la clase `TextExtractor`. Esta clase proporciona métodos para extraer texto de documentos PDF.

```csharp
using TextExtractor extractor = new();
```

### 2. Agregar una Fuente de Datos

A continuación, se crea un `FileDataSource` para el archivo PDF de entrada. Este es el archivo del que se extraerá el texto.

```csharp
FileDataSource fileSource = new(Path.Combine(@"C:\Samples\", "sample.pdf"));
```

### 3. Crear TextExtractorOptions

Se crea un objeto `TextExtractorOptions` para configurar el proceso de extracción de texto. La fuente de archivo de entrada se agrega a las opciones.

```csharp
TextExtractorOptions textExtractorOptions = new();
textExtractorOptions.AddInput(fileSource);
```

### 4. Ejecutar el Proceso de Extracción de Texto

Luego, se llama al método `Process` en el objeto `TextExtractor`, pasando las opciones configuradas.
El método `Process` se llama entonces en el objeto `TextExtractor`, pasando las opciones configuradas.

```csharp
var resultContainer = extractor.Process(textExtractorOptions);
var results = resultContainer.ResultCollection;
Console.WriteLine(results[0]);
```

Puedes ver el código completo a continuación:

``````cs
using Aspose.Pdf.Plugins;
// ...

// Crear una nueva instancia de TextExtractor.
using TextExtractor extractor = new();

// Crear un FileDataSource para el archivo PDF de entrada.
FileDataSource fileSource = new(Path.Combine(@"C:\Samples\", "sample.pdf"));

// Crear TextExtractorOptions.
TextExtractorOptions textExtractorOptions = new();
textExtractorOptions.AddInput(fileSource);

// Procesar la extracción de texto.
var resultContainer = extractor.Process(textExtractorOptions);
var results = resultContainer.ResultCollection;

// Imprimir el texto extraído.
Console.WriteLine(results[0]);

```

