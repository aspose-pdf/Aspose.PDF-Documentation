---
title: Generador de ToC
type: docs
weight: 150
url: /es/net/plugins/tocgenerator/
description: Crea tabla de contenidos con Aspose.PDF ToC Generator para .NET 
lastmod: "2024-01-24"
draft: false
---

¿Deseas mejorar tus documentos PDF [añadiendo una Tabla de Contenidos (TOC)](https://products.aspose.org/pdf/net/toc-generator/) de manera dinámica? Aspose.PDF para .NET ofrece una clase poderosa `TocGenerator` que te permite generar TOCs con facilidad. En esta guía, te mostraremos los pasos básicos para crear un TOC en un documento PDF utilizando Aspose.PDF, cubriendo la creación de un objeto `TocGenerator`, añadiendo rutas de entrada/salida, y ejecutando el proceso de generación de TOC.

## Prerrequisitos

Necesitarás lo siguiente:

* Visual Studio 2019 o posterior
* Aspose.PDF para .NET 24.1 o posterior
* Un archivo PDF de muestra

Además, familiarízate con la clase `TocOptions` y sus funcionalidades. Puedes encontrar información detallada en la [Referencia de la API de Aspose.PDF](https://reference.aspose.com/pdf/net/aspose.pdf/TocOptions/).

Ahora, sumérgete en el código y explora cómo generar una Tabla de Contenidos para tu documento PDF.
Ahora, vamos a sumergirnos en el código y explorar cómo generar un Índice de Contenidos para tu documento PDF.

## Recorrido por el Código

Usaremos la clase `TocGeneratorDemo` con un método `Run` para demostrar cómo crear un Índice de Contenidos. Desglosemos los pasos clave:

```csharp
using Aspose.Pdf.Plugins;

namespace AsposePluginsNet8.Documentation
{
    internal static class TocGeneratorDemo
    {
        private const string PathForSamples = @"C:\Samples\";

        // Ejecuta la demostración de generación del Índice de Contenidos.
        internal static void Run()
        {
            // Crea una nueva instancia de la clase TocGenerator.
            TocGenerator generator = new();

            // Crea una nueva instancia de la clase TocOptions.
            TocOptions options = new();
            // Agrega las rutas de entrada y salida a TocOptions.
            options.AddInput(new FileDataSource(Path.Combine(PathForSamples, "sample.pdf")));
            options.AddOutput(new FileDataSource(Path.Combine(PathForSamples, "sample_toc.pdf")));

            // Procesa la generación del Índice de Contenidos y obtén el contenedor de resultado.
            var resultContainer = generator.Process(options);

            // Obtén el resultado del contenedor de resultados.
            var result = resultContainer.ResultCollection[0];

            // Imprime el resultado en la consola.
            Console.WriteLine(result);
        }
    }
}
```
### 1. Crear un Objeto TocGenerator

El código comienza creando una nueva instancia de la clase `TocGenerator`. Esta clase proporciona métodos para generar TOCs para documentos PDF.

```csharp
TocGenerator generator = new();
```

### 2. Crear TocOptions

A continuación, se crea una nueva instancia de la clase `TocOptions` para configurar el proceso de generación del TOC. Se añaden las rutas de los archivos de entrada y salida a las opciones.

```csharp
TocOptions options = new();
options.AddInput(new FileDataSource(Path.Combine(PathForSamples, "sample.pdf")));
options.AddOutput(new FileDataSource(Path.Combine(PathForSamples, "sample_toc.pdf")));
```

### 3. Ejecutar el Proceso de Generación de TOC

Luego, se llama al método `Process` en el objeto `TocGenerator`, pasando las opciones configuradas. El contenedor de resultados mantiene el TOC generado, y se imprime en la consola.

```csharp
var resultContainer = generator.Process(options);
var result = resultContainer.ResultCollection[0];
Console.WriteLine(result);
```
