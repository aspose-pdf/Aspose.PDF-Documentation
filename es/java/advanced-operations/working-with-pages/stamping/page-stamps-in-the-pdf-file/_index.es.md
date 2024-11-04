---
title: Agregar Sello de Página a PDF
linktitle: Sellos de página en archivo PDF
type: docs
weight: 30
url: /java/page-stamps-in-the-pdf-file/
description: Agregar un sello de página a un archivo PDF usando la clase PdfPageStamp con Java.
lastmod: "2021-09-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Agregar Sello de Página con Java

Un [PdfPageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfPageStamp) se puede usar cuando necesitas aplicar un sello compuesto que contenga gráficos, texto, tablas. El siguiente ejemplo muestra cómo usar un sello para crear papelería como en el uso de Adobe InDesign, Illustrator, Microsoft Word. Supongamos que tenemos algún documento de entrada y queremos aplicar 2 tipos de borde con color azul y ciruela.

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