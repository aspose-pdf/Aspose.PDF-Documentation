---
title: Faire pivoter les pages PDF par programmation
linktitle: Faire pivoter les pages PDF
type: docs
weight: 60
url: /fr/php-java/rotate-pages/
description: Changer l'orientation des pages et ajuster le contenu de la page à la nouvelle orientation de la page en utilisant Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Changer l'orientation de la page

Cet article décrit comment mettre à jour ou changer l'orientation des pages dans un fichier PDF existant.

Aspose.PDF pour PHP via Java a la fonctionnalité de changer l'orientation de la page de paysage à portrait et vice versa.

1. Ouvrez le document en utilisant le fichier d'entrée spécifié.
1. Obtenez toutes les pages du document.
1. Parcourez chaque page et définissez la rotation à 90 degrés.
1. Enregistrez le document modifié dans le fichier de sortie spécifié.
1. Fermez le document.

```php

    // Ouvrir le document
    $document = new Document($inputFile);                
    $pages = $document->getPages();
    $pagesSize = java_values($pages->size());
       
    // Parcourir toutes les pages
    for ($pageCount = 1; $pageCount <= $pagesSize; $pageCount++) {
        $page = $pages->get_Item($pageCount);
       
        $page->setRotate((new Rotation())->On90);
    }

    // Enregistrer le document de sortie
    $document->save($outputFile);
    $document->close();
```