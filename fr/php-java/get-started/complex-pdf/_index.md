---
title: Création d'un PDF complexe
linktitle: Création d'un PDF complexe
type: docs
weight: 60
url: fr/php-java/complex-pdf-example/
description: Aspose.PDF pour PHP via Java vous permet de créer des documents plus complexes contenant des images, des fragments de texte et des tableaux dans un seul document.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

L'exemple [Hello, World](/pdf/php-java/hello-world-example/) a montré des étapes simples pour créer un document PDF en utilisant Aspose.PDF. Dans cet article, nous allons examiner la création d'un document plus complexe avec Aspose.PDF pour PHP via Java. À titre d'exemple, nous prendrons un document d'une entreprise fictive qui exploite des services de ferry pour passagers.

Si nous créons un document à partir de zéro, nous devons suivre certaines étapes :

1. Instancier un objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document). Dans cette étape, nous allons créer un document PDF vide avec quelques métadonnées mais sans pages.

1. Ajoutez une [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page) à l'objet document. Ainsi, notre document aura désormais une page.

1. Ajoutez une [Image](https://reference.aspose.com/pdf/java/com.aspose.pdf/image). C'est une opération complexe basée sur des actions de bas niveau avec des opérateurs PDF.
    - Charger l'image depuis le flux
    - Ajouter l'image à la collection d'Images des Ressources de Page
    - Utiliser l'opérateur GSave : cet opérateur enregistre l'état graphique actuel.
    - Créer un objet [Matrix](https://reference.aspose.com/pdf/java/com.aspose.pdf/matrix/).
    - Utiliser l'opérateur ConcatenateMatrix : définit comment l'image doit être placée.
    - Utiliser l'opérateur Do : cet opérateur dessine l'image.
    - Utiliser l'opérateur GRestore : cet opérateur restaure l'état graphique.

1. Créez un [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) pour l'en-tête. Pour l'en-tête, nous utiliserons la police Arial avec une taille de police de 24pt et un alignement centré.

1. Ajouter un en-tête à la page [Paragraphes](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--).
1. Créer un [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) pour la description. Pour la description, nous utiliserons la police Arial avec une taille de police de 24pt et un alignement centré.
1. Ajouter (description) aux paragraphes de la page.
1. Créer un tableau, ajouter des propriétés de tableau.
1. Ajouter (table) aux [Paragraphes](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--).
1. Enregistrer un document "Complex.pdf".

```php

    $document = new Document();
    //Ajouter une page
    $page = $document->getPages()->add();
    // -------------------------------------------------------------
    // Ajouter une image
    $imageFileName = $dataDir . DIRECTORY_SEPARATOR . 'logo.png';
    $page->AddImage($imageFileName, new Rectangle(20, 730, 120, 830));

    // -------------------------------------------------------------
    // Ajouter un en-tête
    $fontRepository = new FontRepository();
    $fontArial = $fontRepository->findFont("Arial");

    $header = new TextFragment("Nouvelles routes de ferry à l'automne 2020");
    $header->getTextState()->setFont($fontArial);
    $header->getTextState()->setFontSize(24);
    $header->setHorizontalAlignment(2);
    $header->setPosition(new Position(130, 720));
    $page->getParagraphs()->add($header);

    // Ajouter une description
    $descriptionText = "Les visiteurs doivent acheter des billets en ligne et les billets sont limités à 5 000 par jour. Le service de ferry fonctionne à demi-capacité et selon un horaire réduit. Attendez-vous à des files d'attente.";
    $description = new TextFragment($descriptionText);
    $description->getTextState()->setFont($fontRepository->findFont("Times New Roman"));
    $description->getTextState()->setFontSize(14);
    $header->setHorizontalAlignment(1);
    $page->getParagraphs()->add($description);

    // Ajouter un tableau
    $table = new Table();
    $table->setColumnWidths("200");

    $colors = new Color();
    $darkSlateGrayColor = $colors->getDarkSlateGray();
    $blackColor = $colors->getBlack();
    $grayColor = $colors->getGray();
    $whiteSmokeColor = $colors->getWhiteSmoke();

    $table->setBorder(new BorderInfo(BorderSide::$Box, 1.0, $darkSlateGrayColor));
    $table->setDefaultCellBorder(new BorderInfo(BorderSide::$Box, 0.5, $blackColor));
    $table->getMargin()->setBottom(10);
    $table->getDefaultCellTextState()->setFont($fontRepository->findFont("Helvetica"));

    $headerRow = $table->getRows()->add();

    $headerRowCell = $headerRow->getCells()->add("Départs Ville");
    $headerRowCell->setBackgroundColor($grayColor);
    $headerRowCell->getDefaultCellTextState()->setForegroundColor($whiteSmokeColor);

    $headerRowCell = $headerRow->getCells()->add("Départs Île");
    $headerRowCell->setBackgroundColor($grayColor);
    $headerRowCell->getDefaultCellTextState()->setForegroundColor($whiteSmokeColor);

    $timenow = new DateTime('06:00');

    for ($i = 0; $i < 10; $i++) {
        $dataRow = $table->getRows()->add();
        $cell = $dataRow->getCells()->add($timenow->format('H:i'));
        $timenow->add(new DateInterval('PT30M'));
        $dataRow->getCells()->add($timenow->format('H:i'));
    }

    $page->getParagraphs()->add($table);

    $document->save($outputFile);
```