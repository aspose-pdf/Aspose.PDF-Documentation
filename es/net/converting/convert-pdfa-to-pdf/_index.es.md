---
title: Convertir PDF/A a formato PDF
linktitle: Convertir PDF/A a formato PDF
type: docs
weight: 110
url: /net/convert-pdfa-to-pdf/
lastmod: "2021-11-01"
description: Este tema muestra cómo Aspose.PDF permite convertir un archivo PDF/A a un documento PDF con la biblioteca .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Convertir documento PDF/A a PDF

Convertir un documento PDF/A a PDF significa eliminar la restricción <abbr title="Portable Document Format Archive">PDF/A</abbr> del documento original.
La clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) tiene el método [RemovePdfaCompliance(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/removepdfacompliance) para eliminar la información de cumplimiento de PDF del archivo de entrada/fuente.

```csharp
public static void ConvertPDFAtoPDF()
{
    // Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    Document pdfDocument = new Document(_dataDir + "PDFAToPDF.pdf");
    // Eliminar la información de cumplimiento de PDF/A
    pdfDocument.RemovePdfaCompliance();
    // Guardar el documento actualizado
    pdfDocument.Save(_dataDir + "PDFAToPDF_out.pdf");
}
```
Esta información también se elimina si realiza cambios en el documento (por ejemplo, agregar páginas). En el siguiente ejemplo, el documento de salida pierde la conformidad con PDF/A después de agregar la página.

```csharp
public static void ConvertPDFAtoPDFAdvanced()
{
    // Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    Document pdfDocument = new Document(_dataDir + "PDFAToPDF.pdf");
    // Agregar una nueva página (vacía) elimina la información de conformidad con PDF/A.
    pdfDocument.Pages.Add();
    // Guardar el documento actualizado
    pdfDocument.Save(_dataDir + "PDFAToPDF_out.pdf");
}
```
