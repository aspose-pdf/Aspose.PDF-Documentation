---
title: Ajouter des tampons de texte dans un PDF par programmation
linktitle: Tampons de texte dans un fichier PDF
type: docs
weight: 20
url: /fr/php-java/text-stamps-in-the-pdf-file/
description: Ajouter un tampon de texte à un fichier PDF en utilisant la classe TextStamp avec PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ajouter un tampon de texte avec Java

Aspose.PDF pour PHP via Java fournit la classe [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) pour ajouter un tampon de texte dans un fichier PDF.
 La classe [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) fournit les méthodes nécessaires pour spécifier la taille de la police, le style de la police, la couleur de la police, etc. pour l'objet tampon. Afin d'ajouter un tampon de texte, vous devez d'abord créer un objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) et un objet [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) en utilisant les méthodes requises. Après cela, vous pouvez appeler la méthode [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) de la classe [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) pour ajouter le tampon dans le document PDF.

Le code suivant vous montre comment ajouter un tampon de texte dans le fichier PDF.

```php

    // Ouvrir le document
    $document = new Document($inputFile);        
    $pages = $document->getPages();
    $colors = new Color();
    // créer un tampon de texte
    $textStamp = new TextStamp("Exemple de Tampon");
    // définir si le tampon est en arrière-plan
    $textStamp->setBackground(true);
    // définir l'origine
    $textStamp->setXIndent(100);
    $textStamp->setYIndent(100);
    // faire pivoter le tampon
    $textStamp->setRotate((new Rotation())->On90);    
    // définir les propriétés du texte
    $fontRepository = new FontRepository();
    $fontStyles = new FontStyles();
    $textStamp->getTextState()->setFont($fontRepository->findFont("Arial"));
    $textStamp->getTextState()->setFontSize(14);
    $textStamp->getTextState()->setFontStyle($fontStyles->Bold | $fontStyles->Italic);
    $textStamp->getTextState()->setForegroundColor($colors->getGreen());

    // ajouter le tampon à une page particulière
    $pages->get_Item(1)->addStamp($textStamp);

    // Enregistrer le document de sortie
    $document->save($outputFile);
    $document->close();
```

## Définir l'alignement pour l'objet TextStamp

L'ajout de filigranes aux documents PDF est l'une des fonctionnalités fréquemment demandées et Aspose.PDF pour PHP via Java est entièrement capable d'ajouter des filigranes d'image ainsi que de texte. La classe [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) fournit la fonctionnalité d'ajouter des tampons de texte sur le fichier PDF. Récemment, il y a eu une demande pour prendre en charge la fonctionnalité de spécifier l'alignement du texte lors de l'utilisation de l'objet [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp). Ainsi, pour répondre à cette exigence, nous avons introduit la méthode setTextAlignment(..) dans la classe [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp). En utilisant cette méthode, vous pouvez spécifier l'alignement horizontal du texte.

Les extraits de code suivants montrent un exemple de chargement d'un document PDF existant et d'ajout de [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) dessus.

```php

    // Ouvrir le document
    $document = new Document($inputFile);        
    $pages = $document->getPages();
    $colors = new Color();

    // instancier un objet FormattedText avec une chaîne d'exemple
    $text = new FormattedText("This");

    // ajouter une nouvelle ligne de texte à FormattedText
    $text->addNewLineText("is sample");
    $text->addNewLineText("Center Aligned");
    $text->addNewLineText("TextStamp");
    $text->addNewLineText("Object");
    
    // créer un tampon de texte
    $textStamp = new TextStamp($text);

    // spécifier l'alignement horizontal du tampon de texte comme centré
    $textStamp->setHorizontalAlignment((new HorizontalAlignment)->getCenter());
    // spécifier l'alignement vertical du tampon de texte comme centré
    $textStamp->setVerticalAlignment((new VerticalAlignment())->getCenter);
    // spécifier l'alignement horizontal du texte de TextStamp comme centré
    $textStamp->setTextAlignment((new HorizontalAlignment)->getCenter());
    // définir la marge supérieure pour l'objet tampon
    $textStamp->setTopMargin(20);
    
    // ajouter le tampon à une page particulière
    $pages->get_Item(1)->addStamp($textStamp);

    // Enregistrer le document de sortie
    $document->save($outputFile);
    $document->close();  
```


## Remplir le Texte de Contour comme un Tampon dans un Fichier PDF

Nous avons mis en œuvre le paramétrage du mode de rendu pour les scénarios d'ajout et de modification de texte. Pour rendre le texte en contour, veuillez créer un objet [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState) et définir RenderingMode sur TextRenderingMode.StrokeText et également sélectionner la couleur pour la propriété StrokingColor. Ensuite, liez TextState au tampon à l'aide de la méthode bindTextState().

Le code suivant démontre l'ajout de texte de contour rempli :

```php

   // Créer un objet TextState pour transférer des propriétés avancées
    $ts = new TextState();
        
    // Définir la couleur pour le contour
    $ts->setStrokingColor((new Color())->getGray());

    // Définir le mode de rendu du texte
    $ts->setRenderingMode(TextRenderingMode::$StrokeText);

    // Charger un document PDF d'entrée
    $fileStamp = new PdfFileStamp(new Document($inputFile));

    $stamp = new Stamp();
    $stamp->bindLogo(
        new FormattedText("PAYÉ EN TOTALITÉ",
            (new Color())->getGray(), "Arial",
            facades_EncodingType::$WinAnsi,
            true, 78));

    // Lier TextState
    $stamp->bindTextState($ts);
    
    // Définir l'origine X,Y
    $stamp->setOrigin(100, 100);
    $stamp->setOpacity (5);
    $stamp->setBlendingSpace(BlendingColorSpace::$DeviceRGB);
    $stamp->setRotation (45.0);
    $stamp->setBackground(false);

    // Ajouter le Tampon
    $fileStamp->addStamp($stamp);
    $fileStamp->save($outputFile);
    $fileStamp->close();
```