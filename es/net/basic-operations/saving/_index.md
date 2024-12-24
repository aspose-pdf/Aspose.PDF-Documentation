---
title: Guardar documento PDF programáticamente
linktitle: Guardar PDF
type: docs
weight: 30
url: /es/net/save-pdf-document/
description: Aprende cómo guardar un archivo PDF en C# Aspose.PDF para la biblioteca .NET PDF. Guarda el documento PDF en el sistema de archivos, en un stream y en aplicaciones web.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

El siguiente fragmento de código también funciona con la nueva interfaz gráfica [Aspose.Drawing](/pdf/es/net/drawing/).

## Guardar documento PDF en el sistema de archivos

Puedes guardar el documento PDF creado o manipulado en el sistema de archivos utilizando el método `Save` de la clase `Document`.
Cuando no proporcionas el tipo de formato (opciones), entonces el documento se guarda en formato Aspose.PDF v.1.7 (*.pdf).

```csharp
public static void SaveDocument()
{
    var originalFileName = Path.Combine(_dataDir, "SimpleResume.pdf");
    var modifiedFileName = Path.Combine(_dataDir, "SimpleResumeModified.pdf");

    var pdfDocument = new Aspose.Pdf.Document(originalFileName);
    // hacer algunas manipulaciones, por ejemplo, añadir una nueva página vacía
    pdfDocument.Pages.Add();
    pdfDocument.Save(modifiedFileName);
}
```
## Guardar documento PDF en un stream

También puede guardar el documento PDF creado o manipulado en un stream utilizando sobrecargas de los métodos `Save`.

```csharp
public static void SaveDocumentStream()
{
    var originalFileName = Path.Combine(_dataDir, "SimpleResume.pdf");
    var modifiedFileName = Path.Combine(_dataDir, "SimpleResumeModified.pdf");

    var pdfDocument = new Aspose.Pdf.Document(originalFileName);
    // hacer algunas manipulaciones, por ejemplo, añadir una nueva página vacía
    pdfDocument.Pages.Add();
    pdfDocument.Save(System.IO.File.OpenWrite(modifiedFileName));
}
```

## Guardar documento PDF en aplicaciones Web

Para guardar documentos en aplicaciones Web, puede utilizar los métodos propuestos anteriormente. Además, la clase `Document` tiene el método `Save` sobrecargado para usar con la clase [HttpResponse](https://docs.microsoft.com/en-us/dotnet/api/system.web.httpresponse?view=netframework-4.8).

```csharp
var originalFileName = Path.Combine(_dataDir, "SimpleResume.pdf");
var pdfDocument = new Aspose.Pdf.Document(originalFileName);
// hacer algunas manipulaciones, por ejemplo, añadir una nueva página vacía
pdfDocument.Pages.Add();
pdfDocument.Save(Response, originalFileName, ContentDisposition.Attachment, new PdfSaveOptions());
```
Para una explicación más detallada, por favor sigue la sección [Showcase](/pdf/es/net/showcases/).

## Guardar formato PDF/A o PDF/X

PDF/A es una versión estandarizada por ISO del Formato de Documento Portátil (PDF) para su uso en el archivo y preservación a largo plazo de documentos electrónicos.
PDF/A difiere de PDF en que prohíbe características no adecuadas para el archivo a largo plazo, como la vinculación de fuentes (en lugar de la incrustación de fuentes) y el cifrado. Los requisitos de ISO para los visores de PDF/A incluyen directrices de gestión de color, soporte de fuentes incrustadas y una interfaz de usuario para leer anotaciones incrustadas.

PDF/X es un subconjunto del estándar ISO PDF. El propósito de PDF/X es facilitar el intercambio de gráficos, por lo tanto, tiene una serie de requisitos relacionados con la impresión que no se aplican a los archivos PDF estándar.

En ambos casos, se utiliza el método `Save` para almacenar los documentos, mientras que los documentos deben ser preparados usando el método `Convert`.

```csharp
public static void SaveDocumentAsPDFx()
{
    var pdfDocument = new Aspose.Pdf.Document("..\\..\\..\\Samples\\SimpleResume.pdf");
    pdfDocument.Pages.Add();
    pdfDocument.Convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
    pdfDocument.Save("..\\..\\..\\Samples\\SimpleResume_X3.pdf");
}
```

