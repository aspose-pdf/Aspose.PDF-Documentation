---
title: Convertir PDF a HTML en .NET 
linktitle: Convertir PDF a formato HTML
type: docs
weight: 50
url: es/net/convert-pdf-to-html/
lastmod: "2021-11-01"
description: Este tema te muestra cómo convertir un archivo PDF a formato HTML con la biblioteca Aspose.PDF C#.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Visión general

Este artículo explica cómo **convertir PDF a HTML usando C#**. Cubre estos temas.

_Formato_: **HTML**
- [C# PDF a HTML](#csharp-pdf-to-html)
- [C# Convertir PDF a HTML](#csharp-pdf-to-html)
- [C# Cómo convertir un archivo PDF a HTML](#csharp-pdf-to-html)

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Convertir PDF a HTML

**Aspose.PDF para .NET** proporciona muchas características para convertir varios formatos de archivo en documentos PDF y convertir archivos PDF en varios formatos de salida.
**Aspose.PDF para .NET** proporciona muchas características para convertir varios formatos de archivo en documentos PDF y convertir archivos PDF en varios formatos de salida.

**Aspose.PDF para .NET** admite las características para convertir un archivo PDF en HTML. Las principales tareas que puede realizar con la biblioteca Aspose.PDF se enumeran:

- convertir PDF a HTML;
- dividir la salida en HTML de varias páginas;
- especificar carpeta para almacenar archivos SVG;
- comprimir imágenes SVG durante la conversión;
- especificar la carpeta de imágenes;
- crear archivos posteriores solo con contenido del cuerpo;
- renderizado de texto transparente;
- renderizado de capas de documentos PDF.

{{% alert color="success" %}}
**Prueba a convertir PDF a HTML en línea**

Aspose.PDF para .NET te presenta la aplicación gratuita en línea ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), donde puedes probar a investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión de PDF a HTML con Aplicación Gratuita](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

Aspose.PDF para .NET proporciona un código de dos líneas para transformar un archivo PDF fuente a HTML.
Aspose.PDF para .NET proporciona un código de dos líneas para transformar un archivo PDF fuente a HTML.

<a name="csharp-pdf-to-html"><strong>Pasos: Convertir PDF a HTML en C#</strong></a>

1. Crear una instancia del objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) con el documento PDF fuente.
2. Guardarlo en formato **SaveFormat.Html** llamando al método **Document.Save()**.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Abrir el documento PDF fuente
Document pdfDocument = new Document(dataDir + "PDFToHTML.pdf");

// Guardar el archivo en formato de documento MS
pdfDocument.Save(dataDir + "output_out.html", SaveFormat.Html);
```

### Dividir salida en HTML de varias páginas

Al convertir un archivo PDF grande con varias páginas a formato HTML, la salida aparece como una sola página HTML.
Al convertir un archivo PDF grande con varias páginas al formato HTML, la salida aparece como una única página HTML.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Abrir el documento PDF fuente
Document pdfDocument = new Document(dataDir + "PDFToHTML.pdf");

// Instanciar el objeto de opciones de guardado HTML
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();

// Especificar dividir la salida en múltiples páginas
htmlOptions.SplitIntoPages = true;

// Guardar el documento
pdfDocument.Save(@"MultiPageHTML_out.html", htmlOptions);
```

### Especificar Carpeta para Almacenar Archivos SVG

Durante la conversión de PDF a HTML, es posible especificar la carpeta en la que se deben guardar las imágenes SVG.
Durante la conversión de PDF a HTML, es posible especificar la carpeta en la que se deben guardar las imágenes SVG.

```csharp
// Cargar el archivo PDF
Document doc = new Document(dataDir + "PDFToHTML.pdf");

// Instanciar las opciones de guardado de HTML
HtmlSaveOptions newOptions = new HtmlSaveOptions();

// Especificar la carpeta donde se guardan las imágenes SVG durante la conversión de PDF a HTML
newOptions.SpecialFolderForSvgImages = dataDir;

// Guardar el archivo de salida
doc.Save(dataDir + "SaveSVGFiles_out.html", newOptions);
```

### Comprimir imágenes SVG durante la conversión

Para comprimir imágenes SVG durante la conversión de PDF a HTML, por favor intente usar el siguiente código:

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Crear HtmlSaveOption con la característica probada
HtmlSaveOptions newOptions = new HtmlSaveOptions();

// Comprimir las imágenes SVG si las hay
newOptions.CompressSvgGraphicsIfAny = true;
```

### Especificar la carpeta de imágenes

También podemos especificar la carpeta en la que se guardarán las imágenes durante la conversión de PDF a HTML:
También podemos especificar la carpeta donde se guardarán las imágenes durante la conversión de PDF a HTML:

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Crear HtmlSaveOption con la característica probada
HtmlSaveOptions newOptions = new HtmlSaveOptions();

// Especificar la carpeta separada para guardar imágenes
newOptions.SpecialFolderForAllImages = dataDir;
```

### Crear Archivos Subsecuentes Solo con Contenidos del Cuerpo

Recientemente, nos pidieron introducir una característica donde los archivos PDF se convierten a HTML y el usuario puede obtener solo los contenidos de la etiqueta `<body>` para cada página. Esto produciría un archivo con CSS, detalles de `<html>`, `<head>` y todas las páginas en otros archivos solo con contenidos de `<body>`.

Para cumplir con este requisito, se introdujo una nueva propiedad, HtmlMarkupGenerationMode, en la clase HtmlSaveOptions.

Con el siguiente fragmento de código simple, puedes dividir el HTML de salida en páginas.
Con el siguiente fragmento de código simple, puedes dividir la salida HTML en páginas.

```csharp
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Document doc = new Document(dataDir + "PDFToHTML.pdf");
           
HtmlSaveOptions options = new HtmlSaveOptions();
// Esta es la configuración probada
options.HtmlMarkupGenerationMode = HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent;
options.SplitIntoPages = true;

doc.Save(dataDir + "CreateSubsequentFiles_out.html", options);
```

### Renderizado de texto transparente

En caso de que el archivo PDF de entrada contenga textos transparentes sombreados por imágenes en primer plano, entonces podría haber problemas de renderizado de texto. Por lo tanto, para abordar tales escenarios, se pueden utilizar las propiedades SaveShadowedTextsAsTransparentTexts y SaveTransparentTexts.

```csharp
// Para ejemplos completos y archivos de datos, por favor ve a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Document doc = new Document(dataDir + "PDFToHTML.pdf");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.SaveShadowedTextsAsTransparentTexts = true;
htmlOptions.SaveTransparentTexts = true;
doc.Save(dataDir + "TransparentTextRendering_out.html", htmlOptions);
```
### Renderización de capas de documentos PDF

Podemos renderizar las capas de documentos PDF en un elemento de tipo de capa separado durante la conversión de PDF a HTML:

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Document doc = new Document(dataDir + "PDFToHTML.pdf");
// Instanciar objeto de opciones de guardado HTML
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();

// Especificar para renderizar las capas del documento PDF por separado en HTML de salida
htmlOptions.ConvertMarkedContentToLayers = true;

// Guardar el documento
doc.Save(dataDir + "LayersRendering_out.html", htmlOptions);
```

## Vea también

Este artículo también cubre estos temas. Los códigos son los mismos que arriba.

_Formato_: **HTML**
- [Código C# PDF a HTML](#csharp-pdf-to-html)
- [API C# PDF a HTML](#csharp-pdf-to-html)
- [C# PDF a HTML Programáticamente](#csharp-pdf-to-html)
- [Biblioteca C# PDF a HTML](#csharp-pdf-to-html)
- [C# Guardar PDF como HTML](#csharp-pdf-to-html)
- [C# Guardar PDF como HTML](#csharp-pdf-to-html)
- [C# Generar HTML desde PDF](#csharp-pdf-to-html)
- [C# Crear HTML desde PDF](#csharp-pdf-to-html)
- [C# Convertidor de PDF a HTML](#csharp-pdf-to-html)
