---
title: Modifier la Taille des Pages PDF Programmatiquement
linktitle: Changer la Taille des Pages PDF
type: docs
weight: 50
url: /php-java/change-page-size/
description: Modifier la taille des pages de votre fichier PDF en utilisant PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Modifier la Taille des Pages PDF

Aspose.PDF pour PHP via Java vous permet de changer la taille des pages PDF avec quelques lignes de code simples dans vos applications Java. Ce sujet explique comment mettre à jour/modifier les dimensions (taille) des pages d'un fichier PDF existant.

La classe [Page](https://reference.aspose.com/pdf//java/com.aspose.pdf/page) contient la méthode SetPageSize(...) qui vous permet de définir la taille de la page. Le fragment de code ci-dessous met à jour les dimensions des pages en quelques étapes faciles :

1. Charger le fichier PDF source.
1. Obtenir les pages dans l'objet [pageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection).
1. Obtenir une page donnée.
1. Appeler la méthode setPageSize(..) pour mettre à jour ses dimensions.

1. Appelez la méthode save(..) de la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) pour générer le fichier PDF avec les dimensions de page mises à jour.

Le code suivant montre comment changer les dimensions de la page PDF à la taille A4.

```php

    // Ouvrir le document
    $document = new Document($inputFile);
      
    // Obtenir la collection de pages
    $pageCollection = $document->getPages();

    // Obtenir une page particulière
    $page = $pageCollection->get_Item(1);

    // Définir la taille de la page comme A4 (11.7 x 8.3 in) et dans Aspose.Pdf, 1 pouce = 72 points
    // Donc les dimensions A4 en points seront (842.4, 597.6)
    $page.setPageSize(597.6, 842.4);

    // Sauvegarder le document de sortie
    $document->save($outputFile);
    $document->close();
```

## Obtenir la taille de la page PDF

Vous pouvez lire la taille de la page PDF d'un fichier PDF existant en utilisant Aspose.PDF pour PHP via Java. L'exemple de code suivant montre comment lire les dimensions de la page PDF en utilisant PHP.

```php

    // Ouvrir le document
    $document = new Document($inputFile);
      
    // Ajouter une page blanche au document pdf
    $page = $document->getPages()->size() > 0 
        ? $document->getPages()->get_Item(1) 
        : $document->getPages()->add();
    
    // Obtenir les informations de hauteur et de largeur de la page
    $responseData = $page->getPageRect(true)->getWidth() . ":" . $page->getPageRect(true)->getHeight();
    
    // Faire pivoter la page à un angle de 90 degrés
    $rotation = new Rotation();
    $page->setRotate($rotation->getOn90());

    // Obtenir les informations de hauteur et de largeur de la page
    $responseData = $responseData . $page->getPageRect(true)->getWidth() . ":" . $page->getPageRect(true)->getHeight();
    
    // Sauvegarder le document de sortie
    $document->save($outputFile);
    $document->close();
```