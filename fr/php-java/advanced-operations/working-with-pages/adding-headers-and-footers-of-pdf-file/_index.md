---
title: Ajouter un en-tête et un pied de page PDF 
linktitle: Ajouter un en-tête et un pied de page PDF
type: docs
weight: 70
url: /fr/php-java/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF pour PHP via Java vous permet d'ajouter des en-têtes et des pieds de page à votre fichier PDF en utilisant la classe TextStamp.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Les tampons PDF sont souvent utilisés dans les contrats, rapports et documents restreints, pour prouver que les documents ont été examinés et marqués comme "lu", "qualifié" ou "confidentiel", etc. Cet article vous montrera comment nous pouvons ajouter des tampons d'image et des tampons de texte aux documents PDF en utilisant **Aspose.PDF pour PHP via Java**.

Si vous lisez les extraits de code ci-dessus ligne par ligne, vous devez constater que la syntaxe et la logique du code sont assez faciles à comprendre.

## Ajouter du texte dans l'en-tête du fichier PDF

Vous pouvez utiliser la classe [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) pour ajouter du texte dans l'en-tête d'un fichier PDF.
 TextStamp classe fournit les propriétés nécessaires pour créer un tampon basé sur du texte comme la taille de la police, le style de la police et la couleur de la police, etc. Afin d'ajouter du texte dans l'en-tête, vous devez créer un objet Document et un objet TextStamp en utilisant les propriétés requises. Après cela, vous pouvez appeler la méthode AddStamp de la Page pour ajouter le texte dans l'en-tête du PDF.

Vous devez définir la propriété TopMargin de manière à ajuster le texte dans la zone d'en-tête de votre PDF. Vous devez également définir HorizontalAlignment sur Center et VerticalAlignment sur Top.

Le code suivant vous montre comment ajouter du texte dans l'en-tête d'un fichier PDF avec PHP.

```php

    // Ouvrir le document
    $document = new Document($inputFile);

    // Créer l'en-tête
    $textStamp = new TextStamp("Texte de l'en-tête");
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    // Définir les propriétés du tampon
    $textStamp->setTopMargin(10);
    $textStamp->setHorizontalAlignment($horizontalAlignment->Center);
    $textStamp->setVerticalAlignment($verticalAlignment->Top);

    $pages = $document->getPages();

    // Ajouter le pied de page sur la première page
    $page = $pages->get_Item(1);
    $page->addStamp($textStamp);
    
    // Enregistrer le document de sortie
    $document->save($outputFile);
    $document->close();
```

## Ajout de texte dans le pied de page d'un fichier PDF

Vous pouvez utiliser la classe TextStamp pour ajouter du texte dans le pied de page d'un fichier PDF. La classe TextStamp fournit les propriétés nécessaires pour créer un tampon basé sur du texte comme la taille de la police, le style de la police et la couleur de la police, etc. Afin d'ajouter du texte dans le pied de page, vous devez créer un objet Document et un objet TextStamp en utilisant les propriétés requises. Après cela, vous pouvez appeler la méthode addStamp de la Page pour ajouter le texte dans le pied de page du PDF.

Le code suivant vous montre comment ajouter du texte dans le pied de page d'un fichier PDF avec PHP.

```php

    // Ouvrir le document
    $document = new Document($inputFile);

    // Créer l'en-tête
    $textStamp = new TextStamp("Header Text");
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    // Définir les propriétés du tampon
    $textStamp->setBottomMargin(10);
    $textStamp->setHorizontalAlignment($horizontalAlignment->Center);
    $textStamp->setVerticalAlignment($verticalAlignment->Bottom);

    $pages = $document->getPages();

    // Ajouter le pied de page sur la 1ère page
    $page = $pages->get_Item(1);
    $page->addStamp($textStamp);
    
    // Enregistrer le document de sortie
    $document->save($outputFile);
    $document->close();
```


## Ajout d'une Image dans l'En-tête du Fichier PDF

Vous pouvez utiliser la classe [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp) pour ajouter une image dans l'en-tête d'un fichier PDF. La classe Image Stamp fournit les propriétés nécessaires pour créer un tampon basé sur une image comme la taille de la police, le style de la police, et la couleur de la police, etc. Pour ajouter une image dans l'en-tête, vous devez créer un objet Document et un objet Image Stamp en utilisant les propriétés requises. Après cela, vous pouvez appeler la méthode [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp) de la Page pour ajouter l'image dans l'en-tête du PDF.

```php

    // Ouvrir le document
    $document = new Document($inputFile);
    
    // Créer le pied de page
    $imageStamp = new ImageStamp($inputImage);
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    // Définir les propriétés du tampon
    $imageStamp->setTopMargin(10);
    $imageStamp->setHorizontalAlignment($horizontalAlignment->Center);
    $imageStamp->setVerticalAlignment($verticalAlignment->Top);

    $pages = $document->getPages();

    // Ajouter le pied de page à la 1ère page
    $page = $pages->get_Item(1);
    $page->addStamp($imageStamp);

    // Enregistrer le document de sortie
    $document->save($outputFile);
    $document->close();
```


Le snippet de code suivant vous montre comment ajouter une image dans l'en-tête d'un fichier PDF avec PHP.

## Ajouter une image dans le pied de page d'un fichier PDF

Vous pouvez utiliser la classe Image Stamp pour ajouter une image dans le pied de page d'un fichier PDF. La classe Image Stamp fournit les propriétés nécessaires pour créer un tampon basé sur une image, comme la taille de la police, le style de la police, et la couleur de la police, etc. Pour ajouter une image dans le pied de page, vous devez créer un objet Document et un objet Image Stamp en utilisant les propriétés requises. Après cela, vous pouvez appeler la méthode AddStamp de la Page pour ajouter l'image dans le pied de page du PDF.

{{% alert color="primary" %}}

Vous devez définir la propriété BottomMargin de manière à ajuster l'image dans la zone de pied de page de votre PDF. Vous devez également définir [HorizontalAlignment](https://reference.aspose.com/pdf/java/com.aspose.pdf/HorizontalAlignment) sur `Center` et [VerticalAlignment](https://reference.aspose.com/pdf/java/com.aspose.pdf/VerticalAlignment) sur `Bottom`.

{{% /alert %}}

Le snippet de code suivant vous montre comment ajouter une image dans le pied de page d'un fichier PDF avec PHP.

```php

    // Ouvrir le document
    $document = new Document($inputFile);
    
    // Créer un pied de page
    $imageStamp = new ImageStamp($inputImage);
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    // Définir les propriétés du tampon
    $imageStamp->setBottomMargin(10);
    $imageStamp->setHorizontalAlignment($horizontalAlignment->Center);
    $imageStamp->setVerticalAlignment($verticalAlignment->Bottom);

    $pages = $document->getPages();

    // Ajouter un pied de page à la 1ère page
    $page = $pages->get_Item(1);
    $page->addStamp($imageStamp);

    // Enregistrer le document de sortie
    $document->save($outputFile);
    $document->close();
```

## Ajouter différents en-têtes dans un fichier PDF

Nous savons que nous pouvons ajouter TextStamp dans la section En-tête/Pied de page du document en utilisant les propriétés TopMargin ou Bottom Margin, mais parfois nous pouvons avoir besoin d'ajouter plusieurs en-têtes/pieds de page dans un seul document PDF. **Aspose.PDF pour PHP via Java** explique comment faire cela.

Afin de répondre à cette exigence, nous créerons des objets [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) individuels (le nombre d'objets dépend du nombre d'en-têtes/pieds de page requis) et les ajouterons au document PDF.
 Nous pouvons également spécifier différentes informations de formatage pour chaque objet de tampon individuel. Dans l'exemple suivant, nous avons créé un objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) et trois objets [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp), puis nous avons utilisé la méthode [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp) de la page pour ajouter le texte dans la section d'en-tête du PDF. Le code suivant vous montre comment ajouter une image dans le pied de page d'un fichier PDF avec Aspose.PDF pour PHP via Java.

```php

    // Ouvrir le document
    $document = new Document($inputFile);

    // Créer trois tampons
    $stamp1 = new TextStamp("En-tête 1");
    $stamp2 = new TextStamp("En-tête 2");
    $stamp3 = new TextStamp("En-tête 3");
    
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();
    $fontStyles = new FontStyles();

    // Définir l'alignement du tampon (placer le tampon en haut de la page, centré horizontalement)
    $stamp1->setVerticalAlignment ($verticalAlignment->Top);
    $stamp1->setHorizontalAlignment($horizontalAlignment->Center);

    // Spécifier le style de police en gras
    $stamp1->getTextState()->setFontStyle($fontStyles->Bold);
    // Définir la couleur du texte comme rouge
    $stamp1->getTextState()->setForegroundColor((new Color())->getRed());
    // Spécifier la taille de la police comme 14
    $stamp1->getTextState()->setFontSize(14);

    // Maintenant, nous devons définir l'alignement vertical du deuxième objet de tampon en haut
    $stamp2->setVerticalAlignment($verticalAlignment->Top);
    // Définir les informations d'alignement horizontal pour le tampon comme centré
    $stamp2->setHorizontalAlignment($horizontalAlignment->Center);
    // Définir le facteur de zoom pour l'objet de tampon
    $stamp2->setZoom(10);

    // Définir le formatage du troisième objet de tampon
    // Spécifier les informations d'alignement vertical pour l'objet de tampon en haut
    $stamp3->setVerticalAlignment($verticalAlignment->Top);
    // Définir les informations d'alignement horizontal pour l'objet de tampon comme centré
    $stamp3->setHorizontalAlignment ($horizontalAlignment->Center);
    // Définir l'angle de rotation pour l'objet de tampon
    $stamp3->setRotateAngle(35);
    // Définir le rose comme couleur de fond pour le tampon
    $stamp3->getTextState()->setBackgroundColor ((new Color())->getPink());  
    // Changer la police pour le tampon en Verdana
    $stamp3->getTextState()->setFont ((new FontRepository())->findFont("Verdana"));

    // Le premier tampon est ajouté sur la première page ;
    $document->getPages()->get_Item(1)->addStamp($stamp1);
    // Le deuxième tampon est ajouté sur la deuxième page ;
    $document->getPages()->get_Item(2)->addStamp($stamp2);
    // Le troisième tampon est ajouté sur la troisième page.
    $document->getPages()->get_Item(3)->addStamp($stamp3);
    
    // Enregistrer le document de sortie
    $document->save($outputFile);
    $document->close();
```