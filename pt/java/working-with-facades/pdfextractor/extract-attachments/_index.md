---
title: Extrair Anexos de Arquivo PDF
type: docs
weight: 10
url: pt/java/extract-attachments/
description: Esta seção explica sobre extração de anexos de pdf com a classe PdfExtractor.
lastmod: "2021-06-05"
draft: false
---

Uma das principais categorias sob as capacidades de extração de [com.aspose.pdf.facades](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/package-frame) é a extração de anexos.
 Esta categoria fornece um conjunto de métodos, que não só ajudam a extrair os anexos, mas também fornecem os métodos que podem lhe dar informações relacionadas ao anexo, ou seja, os métodos [GetAttachmentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#getAttachmentInfo--) e [GetAttachName](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#getAttachNames--) fornecem informações do anexo e o nome do anexo, respectivamente. Para extrair e depois obter os anexos, usamos os métodos [ExtractAttachment](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#extractAttachment--) e [GetAttachment](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#getAttachment--).

O trecho de código a seguir mostra como usar os métodos PdfExtractor:

```java
  public static void ExtractAttachments() {
        PdfExtractor pdfExtractor = new PdfExtractor();
        pdfExtractor.bindPdf(_dataDir + "sample-attach.pdf");

        // Extrair anexos
        pdfExtractor.extractAttachment();

        // Obter nomes dos anexos
        if (pdfExtractor.getAttachNames().size() > 0) {
            System.out.println("Extraindo e armazenando...");
            // Obter anexos extraídos
            pdfExtractor.getAttachment(_dataDir);
        }
    }
```