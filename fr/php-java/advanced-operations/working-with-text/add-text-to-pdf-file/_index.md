---
title: Ajouter du texte au fichier PDF 
linktitle: Ajouter du texte au fichier PDF
type: docs
weight: 10
url: /fr/php-java/add-text-to-pdf-file/
description: Cet article décrit divers aspects du travail avec le texte dans Aspose.PDF. Apprenez comment ajouter du texte au PDF, ajouter des fragments HTML ou utiliser des polices OTF personnalisées.
lastmod: "2024-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Pour ajouter du texte à un fichier PDF existant :

1. Ouvrez le PDF d'entrée en utilisant l'objet Document.
1. Obtenez la page particulière à laquelle vous souhaitez ajouter le texte.
1. Créez un fragment de texte avec le contenu "Aspose.PDF".
1. Définissez la position du fragment de texte sur la page.
1. Définissez les propriétés du texte du fragment de texte.
1. Créez un objet TextBuilder pour la page.
1. Ajoutez le fragment de texte à la page PDF.
4. Enregistrez le document PDF résultant dans le fichier de sortie.

## Ajout de texte

Le code suivant montre comment ajouter du texte dans un fichier PDF existant.

```php

    // Ouvrir le document
    $document = new Document($inputFile);
    
    // obtenir une page particulière
    $page = $document->getPages()->add();
    
    // créer un fragment de texte
    $textFragment = new TextFragment("Aspose.PDF");
    $textFragment->setPosition(new Position(80, 700));

    // définir les propriétés du texte
    $fontRepository = new FontRepository();
    
    $colors = new Color();
    $textFragment->getTextState()->setFont($fontRepository->findFont("Verdana"));
    $textFragment->getTextState()->setFontSize(14);
    $textFragment->getTextState()->setForegroundColor($colors->getBlue());
    $textFragment->getTextState()->setBackgroundColor($colors->getLightGray());

    // créer un objet TextBuilder
    $textBuilder = new TextBuilder($page);
    // ajouter le fragment de texte à la page PDF
    $textBuilder->appendText($textFragment);

    // Enregistrer le document PDF résultant.    
    $document->save($outputFile);
    $document->close();
```