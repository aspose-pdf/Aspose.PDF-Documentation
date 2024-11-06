---
title: Extrair Anexos de Arquivo PDF
type: docs
weight: 10
url: pt/net/extract-attachments/
description: Esta seção explica sobre a extração de anexos de pdf com a classe PdfExtractor.
lastmod: "2021-06-05"
---

Uma das principais categorias sob as capacidades de extração do [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) é a extração de anexos. Esta categoria fornece um conjunto de métodos, que não apenas ajudam a extrair os anexos, mas também fornecem os métodos que podem dar a você as informações relacionadas ao anexo, ou seja, os métodos [GetAttachmentInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachmentinfo) e [GetAttachName](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachnames) fornecem informações sobre o anexo e o nome do anexo, respectivamente. Para extrair e depois obter anexos, usamos os métodos [ExtractAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractattachment) e [GetAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getattachment).

O trecho de código a seguir mostra como usar os métodos PdfExtractor:

```csharp
public static void ExtractAttachments()
{
    PdfExtractor pdfExtractor = new PdfExtractor();
    pdfExtractor.BindPdf(_dataDir + "sample-attach.pdf");

    // Extrair anexos
    pdfExtractor.ExtractAttachment();

    // Obter nomes dos anexos
    if (pdfExtractor.GetAttachNames().Count > 0)
    {
         Console.WriteLine("Extraindo e armazenando...");
         // Obter anexos extraídos
         pdfExtractor.GetAttachment(_dataDir);
    }
}
```