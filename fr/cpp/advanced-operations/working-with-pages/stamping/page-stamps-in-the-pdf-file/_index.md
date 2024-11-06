---
title: Ajouter des tampons de page PDF dans le PDF
linktitle: Tampons de page dans le fichier PDF
type: docs
weight: 30
url: fr/cpp/page-stamps-in-the-pdf-file/
description: Ajouter un tampon de page à un fichier PDF en utilisant la classe PdfPageStamp avec C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ajouter un tampon de page avec C++

Un [PdfPageStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pdf_page_stamp) peut être utilisé lorsque vous avez besoin d'appliquer un tampon composite contenant des graphiques, du texte, des tableaux. L'exemple suivant montre comment utiliser un tampon pour créer de la papeterie comme dans l'utilisation d'Adobe InDesign, Illustrator, Microsoft Word. Supposons que nous ayons un document d'entrée et que nous voulions appliquer 2 types de bordure avec des couleurs bleu et prune.

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