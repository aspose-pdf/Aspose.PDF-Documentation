---
title: Splitter
type: docs
weight: 120
url: es/net/plugins/splitter/
description: Divide un documento PDF en páginas separadas
lastmod: "2024-01-24"
draft: false
---

¿Tienes un documento PDF grande que te gustaría dividir en archivos más pequeños y manejables? Con [Aspose.PDF Splitter para .NET](https://products.aspose.org/pdf/net/splitter/), puedes lograr fácilmente esta tarea. En este artículo, exploraremos el proceso de dividir un documento PDF en múltiples archivos utilizando el plugin Aspose.PDF. Sumergámonos en el código y sigamos los pasos.

## Prerrequisitos

Necesitarás lo siguiente:

* Visual Studio 2019 o posterior
* Aspose.PDF para .NET 24.1 o posterior
* Un archivo PDF de muestra

Además, familiarízate con la clase `SplitOptions` y sus propiedades. Puedes encontrar información detallada sobre esta clase en la [Referencia API](https://reference.aspose.com/pdf/net/aspose.pdf/SplitOptions/). Ten en cuenta que cada `FileDataSource` de salida representa una sola página en los archivos PDF divididos.

Ahora, exploremos el código proporcionado y entendamos cómo dividir un documento PDF.
Ahora, exploremos el código proporcionado y comprendamos cómo dividir un documento PDF.

## Descripción del Código

El código a continuación demuestra una demostración de división de PDF usando Aspose.PDF.Plugins:

```csharp
using Aspose.Pdf.Plugins;
// ...........

// Establecer la ruta de entrada del documento PDF a dividir.
using var inputStream = File.OpenRead(Path.Combine(@"C:\Samples\", "sample.pdf"));

// Crear una nueva instancia de Splitter.
var splitter = new Splitter();

// Crear opciones para dividir el documento.
var options = new SplitOptions();

// Agregar fuentes de entrada y salida a las opciones.
options.AddInput(new StreamDataSource(inputStream));

var document = new Aspose.Pdf.Document(inputStream);

for (int i = 1; i <= document.Pages.Count; i++)
{
   var pageNum = string.Format("{0,3}", i.ToString("D3"));
   options.AddOutput(new FileDataSource(Path.Combine(@"C:\Samples\", $"splitter_{pageNum}.pdf")));
}

// Procesar las opciones para dividir el documento.
var result = splitter.Process(options);
Console.WriteLine(result);
```

Desglosemos los pasos clave:
Vamos a desglosar los pasos clave:

1. **Establecer el PDF de Entrada**

   El código comienza especificando la ruta del documento PDF de entrada que será dividido. Esto se realiza utilizando el método `File.OpenRead`.

2. **Crear un Objeto (Divisor y Opciones de División)**

   El código crea una instancia de la clase `Splitter` para manejar el proceso de división. Además, se crea una instancia de la clase `SplitOptions` para configurar la operación de división.

3. **Agregar Fuente de Datos (Entrada y Salida)**

   El documento PDF de entrada se agrega a `SplitOptions` como una fuente de datos de entrada utilizando el método `AddInput`. Para cada página en el documento, se agrega una ruta de archivo de salida como una fuente de datos de salida utilizando el método `AddOutput`.

4. **Ejecutar Método de Proceso**

   El proceso de división se inicia llamando al método `Process` en la clase `Splitter`, pasando las `SplitOptions` configuradas. El resultado de la operación se almacena en la variable `result`.

5. **Manejar Resultado**

   El código imprime el resultado en la consola, proporcionando información sobre el proceso de división.
El código imprime el resultado en la consola, proporcionando información sobre el proceso de división.
