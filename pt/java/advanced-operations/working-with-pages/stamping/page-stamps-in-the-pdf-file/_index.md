---
title: Adicionar Carimbo de Página ao PDF 
linktitle: Carimbos de página em arquivo PDF
type: docs
weight: 30
url: pt/java/page-stamps-in-the-pdf-file/
description: Adicione um carimbo de página a um arquivo PDF usando a classe PdfPageStamp com Java.
lastmod: "2021-09-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Adicionar Carimbo de Página com Java

Um [PdfPageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfPageStamp) pode ser usado quando você precisa aplicar um carimbo composto contendo gráficos, texto, tabelas. O exemplo a seguir mostra como usar um carimbo para criar papelaria como no uso do Adobe InDesign, Illustrator, Microsoft Word. Suponha que temos algum documento de entrada e queremos aplicar 2 tipos de borda com cor azul e ameixa.

```java
public static void AddPageStamp()
{
    String inputFileName = "sample-4pages.pdf";
    String outputFileName = "AddPageStamp_out.pdf";
    String pageStampFileName = "PageStamp.pdf";
    Document document = new Document(_dataDir + inputFileName);

    PdfPageStamp bluePageStamp = new PdfPageStamp(_dataDir + pageStampFileName, 1);
    bluePageStamp.setHeight(800);
    bluePageStamp.setBackground(true);

    PdfPageStamp plumPageStamp = new PdfPageStamp(_dataDir + pageStampFileName, 2);
    plumPageStamp.setHeight(800);
    plumPageStamp.setBackground(true);

    for (int i = 1; i < 5; i++)
    {
        if (i % 2 == 0)
            document.getPages().get_Item(i).addStamp(bluePageStamp);
        else
            document.getPages().get_Item(i).addStamp(plumPageStamp);
    }

    document.save(_dataDir + outputFileName);
}
```