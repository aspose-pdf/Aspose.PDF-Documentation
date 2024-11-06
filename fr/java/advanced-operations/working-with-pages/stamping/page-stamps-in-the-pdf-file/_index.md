---
title: Ajouter un tampon de page PDF au PDF
linktitle: Tampons de page dans le fichier PDF
type: docs
weight: 30
url: fr/java/page-stamps-in-the-pdf-file/
description: Ajouter un tampon de page à un fichier PDF en utilisant la classe PdfPageStamp avec Java.
lastmod: "2021-09-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ajouter un tampon de page avec Java

Un [PdfPageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfPageStamp) peut être utilisé lorsque vous avez besoin d'appliquer un tampon composite contenant des graphiques, du texte, des tableaux. L'exemple suivant montre comment utiliser un tampon pour créer de la papeterie comme avec Adobe InDesign, Illustrator, Microsoft Word. Supposons que nous ayons un document d'entrée et que nous souhaitons appliquer 2 types de bordure avec des couleurs bleue et prune.

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