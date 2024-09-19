---
title: Convertir PDF a EPUB, LaTeX, Texto, XPS en C#
linktitle: Convertir PDF a otros formatos
type: docs
weight: 90
url: /net/convert-pdf-to-other-files/
lastmod: "2021-11-01"
keywords: convertir, PDF, EPUB, LaTeX, Texto, XPS, C#
description: Este tema te muestra cómo convertir un archivo PDF a otros formatos de archivo como EPUB, LaTeX, Texto, XPS, etc. usando C# o .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Convertir PDF a EPUB

{{% alert color="success" %}}
**Intenta convertir PDF a EPUB en línea**

Aspose.PDF para .NET te presenta la aplicación gratuita en línea ["PDF a EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), donde puedes probar a investigar la funcionalidad y la calidad con la que funciona.

[![Conversión de Aspose.PDF de PDF a EPUB con aplicación gratuita](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Publicación Electrónica">EPUB</abbr>** es un estándar de libro electrónico libre y abierto del Foro Internacional de Publicación Digital (IDPF).
**<abbr title="Publicación Electrónica">EPUB</abbr>** es un estándar de libro electrónico gratuito y abierto del Foro Internacional de Publicación Digital (IDPF).
EPUB está diseñado para contenido reajustable, lo que significa que un lector de EPUB puede optimizar el texto para un dispositivo de visualización particular. EPUB también admite contenido de diseño fijo. El formato está destinado como un formato único que los editores y las casas de conversión pueden usar internamente, así como para distribución y venta. Supera el estándar Open eBook.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

Aspose.PDF para .NET también admite la función de convertir documentos PDF a formato EPUB. Aspose.PDF para .NET tiene una clase llamada EpubSaveOptions que se puede usar como segundo argumento en el método [`Document.Save(..)`](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index), para generar un archivo EPUB.
Por favor, intente usar el siguiente fragmento de código para cumplir con este requisito con C#.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Cargar documento PDF
Document pdfDocument = new Document(dataDir + "PDFToEPUB.pdf");
// Instanciar opciones de guardado Epub
EpubSaveOptions options = new EpubSaveOptions();
// Especificar el diseño para los contenidos
options.ContentRecognitionMode = EpubSaveOptions.RecognitionMode.Flow;
// Guardar el documento ePUB
pdfDocument.Save(dataDir + "PDFToEPUB_out.epub", options);
```
## Convertir PDF a LaTeX/TeX

**Aspose.PDF para .NET** admite la conversión de PDF a LaTeX/TeX.
El formato de archivo LaTeX es un formato de archivo de texto con un marcado especial y se utiliza en el sistema de preparación de documentos basado en TeX para la composición tipográfica de alta calidad.

{{% alert color="success" %}}
**Prueba a convertir PDF a LaTeX/TeX en línea**

Aspose.PDF para .NET te presenta la aplicación gratuita en línea ["PDF a LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), donde puedes probar a investigar la funcionalidad y calidad con la que funciona.

[![Conversión de Aspose.PDF de PDF a LaTeX/TeX con Aplicación Gratuita](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

Para convertir archivos PDF a TeX, Aspose.PDF tiene la clase [LaTeXSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/latexsaveoptions) que proporciona la propiedad OutDirectoryPath para guardar imágenes temporales durante el proceso de conversión.

El siguiente fragmento de código muestra el proceso de conversión de archivos PDF al formato TEX con C#.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Crear objeto Document
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "PDFToTeX.pdf");

// Instanciar opción de guardado LaTex          
LaTeXSaveOptions saveOptions = new LaTeXSaveOptions();

// Especificar el directorio de salida
string pathToOutputDirectory = dataDir;

// Establecer la ruta del directorio de salida para el objeto de opción de guardado
saveOptions.OutDirectoryPath = pathToOutputDirectory;

// Guardar archivo PDF en formato LaTex
doc.Save(dataDir + "PDFToTeX_out.tex", saveOptions);
```
## Convertir PDF a Texto

**Aspose.PDF para .NET** soporta la conversión de todo el documento PDF y de una sola página a un archivo de texto.

### Convertir todo el documento PDF a archivo de texto

Puedes convertir un documento PDF a archivo TXT utilizando el método [Visit](https://reference.aspose.com/pdf/net/aspose.pdf.text/textabsorber/methods/visit/index) de la clase [TextAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textabsorber).

El siguiente fragmento de código explica cómo extraer los textos de todas las páginas.

```csharp
public static void ConvertPDFDocToTXT()
{
    // Abrir documento
    Document pdfDocument = new Document(_dataDir + "demo.pdf");
    TextAbsorber ta = new TextAbsorber();
    ta.Visit(pdfDocument);
    // Guardar el texto extraído en archivo de texto
    File.WriteAllText(_dataDir + "input_Text_Extracted_out.txt",ta.Text);
}
```

{{% alert color="success" %}}
**Intenta convertir PDF a Texto en línea**

Aspose.PDF para .NET te presenta la aplicación gratuita en línea ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt), donde puedes probar a investigar la funcionalidad y calidad con la que funciona.
Aspose.PDF para .NET te presenta la aplicación gratuita en línea ["PDF a Texto"](https://products.aspose.app/pdf/conversion/pdf-to-txt), donde puedes probar a investigar la funcionalidad y calidad con la que funciona.

[![Aspose.PDF Conversión de PDF a Texto con Aplicación Gratuita](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)

### Convertir página PDF a archivo de texto

Puedes convertir un documento PDF a un archivo TXT con Aspose.PDF para .NET. Debes usar el método `Visit` de la clase `TextAbsorber` para resolver esta tarea.

El siguiente fragmento de código explica cómo extraer los textos de las páginas específicas.

```csharp
public static void ConvertPDFPagestoTXT()
{
    Document pdfDocument = new Document(System.IO.Path.Combine(_dataDir, "demo.pdf"));
    TextAbsorber ta = new TextAbsorber();
    var pages = new [] {1, 3, 4};
    foreach (var page in pages)
    {
        ta.Visit(pdfDocument.Pages[page]);
    }
   
    // Guardar el texto extraído en archivo de texto
    File.WriteAllText(System.IO.Path.Combine(_dataDir, "input_Text_Extracted_out.txt"), ta.Text);
}
```
## Convertir PDF a XPS

**Aspose.PDF para .NET** ofrece la posibilidad de convertir archivos PDF al formato <abbr title="Especificación de Papel XML">XPS</abbr>. Intentemos utilizar el fragmento de código presentado para convertir archivos PDF a formato XPS con C#.

{{% alert color="success" %}}
**Intenta convertir PDF a XPS en línea**

Aspose.PDF para .NET te presenta la aplicación gratuita en línea ["PDF a XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), donde puedes probar a investigar la funcionalidad y calidad con la que trabaja.

[![Aspose.PDF Conversión PDF a XPS con Aplicación Gratuita](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

El tipo de archivo XPS está principalmente asociado con la Especificación de Papel XML de Microsoft Corporation. La Especificación de Papel XML (XPS), anteriormente conocida como Metro y que incluye el concepto de marketing de Ruta de Impresión de Nueva Generación (NGPP), es la iniciativa de Microsoft para integrar la creación y visualización de documentos en el sistema operativo Windows.

Para convertir archivos PDF a XPS, Aspose.PDF tiene la clase [XpsSaveOptions](https://reference.aspose.com/net/pdf/aspose.pdf/xpssaveoptions) que se utiliza como el segundo argumento en el método [Document.Save(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) para generar el archivo XPS.
Para convertir archivos PDF a XPS, Aspose.PDF tiene la clase [XpsSaveOptions](https://reference.aspose.com/net/pdf/aspose.pdf/xpssaveoptions) que se utiliza como segundo argumento en el método [Document.Save(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) para generar el archivo XPS.

El siguiente fragmento de código muestra el proceso de conversión de un archivo PDF a formato XPS.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Cargar documento PDF
Document pdfDocument = new Document(dataDir + "input.pdf");

// Instanciar opciones de guardado XPS
Aspose.Pdf.XpsSaveOptions saveOptions = new Aspose.Pdf.XpsSaveOptions();
// Guardar el documento XPS
pdfDocument.Save("PDFToXPS_out.xps", saveOptions)
```
