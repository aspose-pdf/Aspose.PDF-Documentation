---
title: Añadir Sellos de Página en PDF
linktitle: Sellos de página en archivo PDF
type: docs
weight: 30
url: /cpp/page-stamps-in-the-pdf-file/
description: Añadir un sello de página a un archivo PDF usando la clase PdfPageStamp con C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Añadir Sello de Página con C++

Un [PdfPageStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pdf_page_stamp) se puede usar cuando necesitas aplicar un sello compuesto que contenga gráficos, texto, tablas. El siguiente ejemplo muestra cómo usar un sello para crear papelería como en Adobe InDesign, Illustrator, Microsoft Word. Supongamos que tenemos algún documento de entrada y queremos aplicar 2 tipos de borde con color azul y ciruela.

```cpp
void AddPageStamp()
{
    String _dataDir("C:\\Samples\\");

    String inputFileName ("sample-4pages.pdf");
    String outputFileName ("AddPageStamp_out.pdf");
    String pageStampFileName ("PageStamp.pdf");
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto bluePageStamp = MakeObject<PdfPageStamp>(_dataDir + pageStampFileName, 1);
    bluePageStamp->set_Height(800);
    bluePageStamp->set_Background(true);

    auto plumPageStamp = MakeObject<PdfPageStamp>(_dataDir + pageStampFileName, 2);
    plumPageStamp->set_Height(800);
    plumPageStamp->set_Background(true);

    for (int i = 1; i < 5; i++)
    {
        if (i % 2 == 0)
            document->get_Pages()->idx_get(i)->AddStamp(bluePageStamp);
        else
            document->get_Pages()->idx_get(i)->AddStamp(plumPageStamp);
    }

    document->Save(_dataDir + outputFileName);
}
```