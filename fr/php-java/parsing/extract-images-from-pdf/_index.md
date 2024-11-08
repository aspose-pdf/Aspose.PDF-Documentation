---
title: Extraire des Images du PDF
linktitle: Extraire des Images
type: docs
weight: 20
url: /fr/php-java/extract-images-from-the-pdf-file/
description: Comment extraire une partie de l'image du PDF en utilisant Aspose.PDF pour PHP
lastmod: "2024-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Chaque page dans le document PDF contient des ressources (images, formulaires et polices). Nous pouvons accéder à ces ressources en appelant la méthode [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--). La classe [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) contient [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) et nous pouvons obtenir la liste des images en appelant la méthode [getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--).

Ainsi, pour extraire une image d'une page, nous devons obtenir une référence à la page, ensuite aux ressources de la page et enfin à la collection d'images. Nous pouvons extraire une image particulière par exemple par index.

L'index de l'image renvoie un objet [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage).
Cet objet fournit une méthode [save](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-) qui peut être utilisée pour enregistrer l'image extraite. Le fragment de code suivant montre comment extraire des images d'un fichier PDF.

```php

    // Charger le document PDF
    $document = new Document($inputFile);

    // Obtenir la première page du document
    $page = $document->getPages()->get_Item(1);

    // Obtenir la collection d'images sur la page
    $xImageCollection = $page->getResources()->getImages();

    // Obtenir la première image de la collection
    $xImage = $xImageCollection->get_Item(1);

    // Créer un nouvel objet FileOutputStream pour enregistrer l'image
    $outputImage = new java("java.io.FileOutputStream", $outputFile);

    // Enregistrer l'image dans le fichier de sortie
    $xImage->save($outputImage);

    // Fermer le fichier image de sortie
    $outputImage->close();
```