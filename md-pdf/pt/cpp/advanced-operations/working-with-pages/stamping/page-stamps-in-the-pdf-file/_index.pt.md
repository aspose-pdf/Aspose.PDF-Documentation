---
title: Adicionar Carimbos de Página em PDF
linktitle: Carimbos de página em arquivo PDF
type: docs
weight: 30
url: /cpp/page-stamps-in-the-pdf-file/
description: Adicione um carimbo de página a um arquivo PDF usando a classe PdfPageStamp com C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Adicionar Carimbo de Página com C++

Um [PdfPageStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pdf_page_stamp) pode ser usado quando você precisa aplicar um carimbo composto contendo gráficos, texto, tabelas. O exemplo a seguir mostra como usar um carimbo para criar papelaria como no uso do Adobe InDesign, Illustrator, Microsoft Word. Suponha que temos algum documento de entrada e queremos aplicar 2 tipos de borda com cores azul e ameixa.

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