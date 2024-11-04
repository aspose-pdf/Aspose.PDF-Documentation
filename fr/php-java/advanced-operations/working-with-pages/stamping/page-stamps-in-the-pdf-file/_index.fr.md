---
title: Ajouter un Tampon de Page PDF au PDF 
linktitle: Tampons de page dans le fichier PDF
type: docs
weight: 30
url: /php-java/page-stamps-in-the-pdf-file/
description: Ajouter un tampon de page à un fichier PDF en utilisant la classe PdfPageStamp avec PHP.
lastmod: "2024-09-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ajouter un Tampon de Page

Un [PdfPageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfPageStamp) peut être utilisé lorsque vous avez besoin d'appliquer un tampon composite contenant des graphiques, du texte, des tableaux. L'exemple suivant montre comment utiliser un tampon pour créer des éléments de papeterie comme dans l'utilisation d'Adobe InDesign, Illustrator, Microsoft Word. Supposons que nous ayons un document d'entrée et que nous souhaitions appliquer 2 types de bordures avec les couleurs bleu et prune.

```php

    // Ouvrir le document
    $document = new Document($inputFile);        
    $bluePageStamp = new PdfPageStamp($inputPageFile, 1);
    $bluePageStamp->setHeight(800);
    $bluePageStamp->setBackground(true);        

    $plumPageStamp = new PdfPageStamp($inputPageFile, 2);
    $plumPageStamp->setHeight(800);
    $plumPageStamp->setBackground(true);

    for ($i = 1; $i < 5; $i++)
    {
        if ($i % 2 == 0)
            $document->getPages()->get_Item($i).addStamp($bluePageStamp);
        else
            $document->getPages()->get_Item($i).addStamp($plumPageStamp);
    }

    // Sauvegarder le document de sortie
    $document->save($outputFile);
    $document->close();  
```