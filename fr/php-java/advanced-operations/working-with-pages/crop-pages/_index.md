---
title: Rogner les Pages PDF en utilisant PHP
linktitle: Rogner les Pages
type: docs
weight: 80
url: /fr/php-java/crop-pages/
description: Vous pouvez obtenir les propriétés de la page, telles que la largeur, la hauteur, la boîte de fond perdu, de rognage et de découpe en utilisant Aspose.PDF pour PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtenir les Propriétés des Pages

Chaque page dans un fichier PDF a un certain nombre de propriétés, telles que la largeur, la hauteur, la boîte de fond perdu, de rognage et de découpe. Aspose.PDF pour PHP via Java vous permet d'accéder à ces propriétés.

- **Boîte média**: La boîte média est la plus grande boîte de page. Elle correspond à la taille de la page (par exemple A4, A5, Lettre US, etc.) sélectionnée lorsque le document a été imprimé en PostScript ou PDF. En d'autres termes, la boîte média détermine la taille physique du support sur lequel le document PDF est affiché ou imprimé.
- **Boîte de fond perdu**: Si le document a un fond perdu, le PDF aura également une boîte de fond perdu.
 Bleed est la quantité de couleur (ou d'œuvre) qui dépasse le bord d'une page. Il est utilisé pour s'assurer que lorsque le document est imprimé et découpé à la taille ("taillé"), l'encre ira jusqu'au bord de la page. Même si la page est mal taillée - coupée légèrement en dehors des marques de découpe - aucun bord blanc n'apparaîtra sur la page.
- **Trim box**: La boîte de découpe indique la taille finale d'un document après impression et découpe.
- **Art box**: La boîte d'art est la boîte dessinée autour du contenu réel des pages de vos documents. Cette boîte de page est utilisée lors de l'importation de documents PDF dans d'autres applications.
- **Crop box**: La boîte de rognage est la taille "de page" à laquelle votre document PDF est affiché dans Adobe Acrobat. En vue normale, seuls les contenus de la boîte de rognage sont affichés dans Adobe Acrobat. Pour des descriptions détaillées de ces propriétés, lisez la spécification Adobe.Pdf, en particulier 10.10.1 Page Boundaries.
- **Page.Rect**: l'intersection (rectangle communément visible) de la MediaBox et de la DropBox. L'image ci-dessous illustre ces propriétés.  
Pour plus de détails, veuillez visiter [cette page](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

L'extrait ci-dessous montre comment recadrer la page :

```php

    // Ouvrir le document
    $document = new Document($inputFile);      

    $page = $document->getPages()->get_Item(1);

    $responseData = $page->getCropBox() . PHP_EOL;
    $responseData = $responseData . $page->getTrimBox() . PHP_EOL;
    $responseData = $responseData . $page->getArtBox() . PHP_EOL;
    $responseData = $responseData . $page->getBleedBox() . PHP_EOL;
    $responseData = $responseData . $page->getMediaBox() . PHP_EOL;

    // Créer un nouveau rectangle de boîte
    $newBox = new Rectangle(200, 220, 2170, 1520);

    $page->setCropBox($newBox);
    $page->setTrimBox($newBox);
    $page->setArtBox($newBox);
    $page->setBleedBox($newBox);

    // Enregistrer le document de sortie
    $document->save($outputFile);
    $document->close();
```

Dans cet exemple, nous avons utilisé un fichier d'exemple [ici](crop_page.pdf). Initially our page looks like shown on the Figure 1.  
![Figure 1. Cropped Page](crop_page.png)

Après le changement, la page ressemblera à la Figure 2.  
![Figure 2. Cropped Page](crop_page2.png)