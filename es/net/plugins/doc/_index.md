---
title: DOC Converter
type: docs
weight: 10
url: /es/net/plugins/doc/
description: Convertir PDF a Word de manera simple con el plugin PdfDoc
lastmod: "2024-01-24"
---

Este artículo te guía sobre cómo usar el [Convertidor de DOC Aspose.Pdf para .NET](https://products.aspose.org/pdf/net/doc-converter/) para convertir un documento PDF al formato Microsoft Word (.doc / .docx).

## Prerrequisitos

Necesitarás lo siguiente:

* Visual Studio 2019 o posterior
* Aspose.PDF para .NET 24.1 o posterior
* Un archivo PDF de muestra que contenga algunos campos de formulario

Puedes descargar la biblioteca Aspose.PDF para .NET desde el sitio web oficial o instalarla utilizando el Gestor de Paquetes NuGet en Visual Studio.

## Pasos

### 1. Configuración de tu conversión (captura de pantalla de la clase FileDataSource)

El proceso de conversión involucra tres pasos principales: definir los archivos de entrada y salida, crear un objeto `PdfDoc` y especificar las opciones de conversión.

#### 1.1. Definición de fuentes de datos

* **Archivo de entrada:** Utilizaremos la clase `FileDataSource` para especificar la ubicación del archivo PDF que quieres convertir.
* **Archivo de Entrada:** Usaremos la clase `FileDataSource` para especificar la ubicación del archivo PDF que deseas convertir.
  
```csharp
  FileDataSource inputDataSource = new(Path.Combine(@"C:\Samples\", "sample.pdf"));
```

  * Reemplaza `"C:\Samples\sample.pdf"` con la ruta actual a tu archivo PDF.

* **Archivo de Salida:** De manera similar, usa otro objeto `FileDataSource` para definir la ubicación y el nombre del archivo para el documento de Word resultante.

```csharp
  FileDataSource outputDataSource = new(Path.Combine(@"C:\Samples\", "sample.docx"));
```

* Reemplaza `"C:\Samples\sample.docx"` con la ruta y nombre de archivo de salida deseados.

### 2. Creando el Objeto del Plugin PdfDoc (captura de pantalla de la clase PdfDoc)

A continuación, creamos una instancia de la clase `PdfDoc` para realizar la conversión.

```csharp
  var plugin = new PdfDoc();
```

Este objeto sirve como el motor para el proceso de conversión.

### 3. Configurando Opciones de Conversión

La clase `PdfToDocOptions` te permite ajustar el proceso de conversión.
La clase `PdfToDocOptions` te permite ajustar el proceso de conversión.

* **Guardar Formato:** Especifica el formato de salida deseado para el documento Word. En este caso, utilizamos `SaveFormat.DocX` para generar un documento compatible con Microsoft Word 2007 o posterior (.docx).

* **Modo de Conversión:** Define cómo el complemento interpreta la estructura del PDF durante la conversión. Usaremos `ConversionMode.EnhancedFlow` para optimizar el documento Word resultante en cuanto a diseño y formato.

Aquí tienes el fragmento de código para configurar las opciones:

```csharp
  PdfToDocOptions options = new()
  {
      SaveFormat = SaveFormat.DocX,
      ConversionMode = ConversionMode.EnhancedFlow
  };
```

**Añadiendo Entrada y Salida:**

Finalmente, asociamos las fuentes de datos definidas anteriormente con las opciones de conversión usando los métodos `AddInput` y `AddOutput`:

```csharp
  options.AddInput(inputDataSource);
  options.AddOutput(outputDataSource);
```

Esto conecta el PDF de entrada y el documento Word de salida deseado al proceso de conversión.

### 4.
### 4.

Con todo configurado, iniciemos la conversión llamando al método `Process` del complemento `PdfDoc` y pasando las opciones configuradas:

```csharp
  var resultContainer = plugin.Process(options);
```

Este método ejecuta la conversión y devuelve un objeto `ResultContainer` que contiene detalles sobre el proceso.

**Recuperación de Resultados:**

Aunque no es esencial para la conversión básica, puedes acceder a los resultados a través de la propiedad `ResultCollection` del objeto `ResultContainer`. Esto puede ser útil para depuración o seguimiento de detalles específicos de la conversión.

```csharp
  var result = resultContainer.ResultCollection[0];

  // Imprimir el resultado (opcional para fines de demostración)
  Console.WriteLine(result);
```

Con este paso final, tu documento PDF será convertido al formato de Word especificado y guardado en la ubicación de salida definida.

