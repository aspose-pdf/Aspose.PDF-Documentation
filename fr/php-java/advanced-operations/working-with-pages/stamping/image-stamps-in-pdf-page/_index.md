---
title: Ajouter des tampons d'image dans un PDF par programmation 
linktitle: Tampons d'image dans un fichier PDF
type: docs
weight: 10
url: /fr/php-java/image-stamps-in-pdf-page/
description: Ajoutez le tampon d'image dans votre document PDF en utilisant la classe ImageStamp avec la bibliothèque Aspose.PDF pour PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ajouter un tampon d'image dans un fichier PDF

Vous pouvez utiliser la classe [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) pour ajouter une image en tant que tampon dans un document PDF. La classe [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) fournit des méthodes pour spécifier la hauteur, la largeur, l'opacité, etc.

Pour ajouter un tampon d'image :

1. Créez un objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) et un objet ImageStamp en utilisant les propriétés requises.

1. Appelez la méthode [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) de la classe [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) pour ajouter le tampon au PDF.

Le code suivant montre comment ajouter un tampon d'image dans le fichier PDF.

```php

    // Ouvrir le document
    $document = new Document($inputFile);        
    $pages = $document->getPages();
  
    // Créer un tampon d'image
    $imageStamp = new ImageStamp($inputImageFile);
    $imageStamp->setBackground(true);
    $imageStamp->setXIndent(100);
    $imageStamp->setYIndent(100);
    $imageStamp->setHeight(48);
    $imageStamp->setWidth(225);
    $imageStamp->setRotate((new Rotation())->getOn270());
    $imageStamp->setOpacity(0.5);

    // Ajouter le tampon à une page particulière
    $document->getPages()->get_Item(1)->addStamp($imageStamp);

    // Enregistrer le document de sortie
    $document->save($outputFile);
    $document->close()
```

## Contrôler la qualité de l'image lors de l'ajout d'un tampon

La classe [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) vous permet d'ajouter une image en tant que tampon dans un document PDF.
 Il vous permet également de contrôler la qualité de l'image lors de l'ajout d'une image en tant que filigrane dans un fichier PDF. Pour permettre cela, une méthode nommée setQuality(...) a été ajoutée à la classe [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp). Une méthode similaire peut également être trouvée dans la classe [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/Stamp) du package com.aspose.pdf.facades.

L'extrait de code suivant vous montre comment contrôler la qualité de l'image lors de l'ajout d'un tampon dans le fichier PDF.

```php

    // Ouvrir le document
    $document = new Document($inputFile);        
    $pages = $document->getPages();

    // Créer un tampon d'image
    $imageStamp = new ImageStamp($inputImageFile);
    $imageStamp->setQuality(10);

    $document->getPages()->get_Item(1)->addStamp($imageStamp);

    // Enregistrer le document de sortie
    $document->save($outputFile);
    $document->close();        
```

## Tampon d'image comme arrière-plan dans une boîte flottante

L'API Aspose.PDF vous permet d'ajouter un tampon d'image comme arrière-plan dans une boîte flottante. La propriété BackgroundImage de la classe FloatingBox peut être utilisée pour définir l'image de fond pour une boîte flottante comme illustré dans l'exemple de code suivant.

Ce fragment de code démontre le processus de création d'un document PDF et l'ajout d'une FloatingBox. La FloatingBox contient un fragment de texte, une bordure, une image de fond et une couleur de fond. Le document résultant est ensuite enregistré dans un fichier de sortie.

```php

    // Ouvrir le document
    $document = new Document($inputFile);
    $colors = new Color();
    $pages = $document->getPages();

    // Ajouter une page au document PDF
    $page = $pages->add();

    // Créer un objet FloatingBox
    $aBox = new FloatingBox(200, 100);

    // Définir la position gauche pour FloatingBox
    $aBox->setLeft(40);

    // Définir la position haute pour FloatingBox
    $aBox->setTop(80);

    // Définir l'alignement horizontal pour FloatingBox
    $aBox->setHorizontalAlignment((new HorizontalAlignment())->getCenter());

    // Ajouter un fragment de texte à la collection de paragraphes de FloatingBox
    $aBox->getParagraphs()->add(new TextFragment("texte principal"));

    // Définir la bordure pour FloatingBox
    $aBox->setBorder(new BorderInfo(BorderSide::$All, $colors->getRed()));

    // Ajouter une image de fond
    $img = new Image();
    $img->setFile($inputImageFile);
    $aBox->setBackgroundImage($img);

    // Définir la couleur de fond pour FloatingBox
    $aBox->setBackgroundColor($colors->getYellow());

    // Ajouter FloatingBox à la collection de paragraphes de l'objet page
    $page->getParagraphs()->add($aBox);
    
    // Enregistrer le document de sortie
    $document->save($outputFile);
    $document->close();
```