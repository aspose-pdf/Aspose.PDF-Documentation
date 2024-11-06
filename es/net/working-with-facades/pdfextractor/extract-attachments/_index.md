---
title: Extraer Adjuntos de Archivo PDF
type: docs
weight: 10
url: es/net/extract-attachments/
description: Esta sección explica sobre la extracción de adjuntos de PDF con la clase PdfExtractor.
lastmod: "2021-06-05"
---

Una de las principales categorías bajo las capacidades de extracción del [espacio de nombres Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) es la extracción de adjuntos. Esta categoría proporciona un conjunto de métodos, que no solo ayudan a extraer los archivos adjuntos, sino que también proporciona los métodos que pueden brindarle la información relacionada con los archivos adjuntos, es decir, los métodos [GetAttachmentInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachmentinfo) y [GetAttachName](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachnames) proporcionan información sobre el archivo adjunto y el nombre del archivo adjunto, respectivamente. Para extraer y luego obtener archivos adjuntos utilizamos los métodos [ExtractAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractattachment) y [GetAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachment).

El siguiente fragmento de código le muestra cómo usar los métodos de PdfExtractor:

```csharp
public static void ExtractAttachments()
{
    PdfExtractor pdfExtractor = new PdfExtractor();
    pdfExtractor.BindPdf(_dataDir + "sample-attach.pdf");

    // Extraer archivos adjuntos
    pdfExtractor.ExtractAttachment();

    // Obtener nombres de archivos adjuntos
    if (pdfExtractor.GetAttachNames().Count > 0)
    {
         Console.WriteLine("Extrayendo y almacenando...");
         // Obtener archivos adjuntos extraídos
         pdfExtractor.GetAttachment(_dataDir);
    }
}
```