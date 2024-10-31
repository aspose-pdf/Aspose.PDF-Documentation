---
title: Manipuler un document PDF
linktitle: Manipuler un document PDF
type: docs
weight: 30
url: /php-java/manipulate-pdf-document/
description: Cet article contient des informations sur la façon de valider un document PDF selon la norme PDF A, comment travailler avec la table des matières, comment définir une date d'expiration pour le PDF, et comment déterminer la progression de la génération du fichier PDF.
lastmod: "2024-06-05"
---

## Valider un document PDF pour la norme PDF A (A 1A et A 1B)

Pour valider un document PDF pour la compatibilité avec PDF/A-1a ou PDF/A-1b, utilisez la méthode [validate(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#validate-java.lang.String-com.aspose.pdf.PdfFormat-) de la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Cette méthode vous permet de spécifier le nom du fichier dans lequel le résultat doit être enregistré et le type de validation requis à partir de l'énumération [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfFormat) : PDF_A_1A ou PDF_A_1B.

Le format XML de sortie est un format Aspose personnalisé.
 Le XML contient une collection de balises avec le nom Problème ; chaque balise contient les détails d'un problème particulier. L'attribut ObjectID de la balise Problème représente l'ID de l'objet particulier auquel ce problème est lié. L'attribut Clause représente une règle correspondante dans la spécification PDF.

```php

    // Ouvrir le document
    $document = new Document($inputFile);
    
    $pdfFormat =  (new PdfFormat())->PDF_A_1A;
    // Valider le PDF pour PDF/A-1a
    $document->validate($outputFile, $pdfFormat);
    $document->close();
```

## Travailler avec le TOC

### Ajouter un TOC à un PDF existant

Pour ajouter un TOC à un fichier PDF existant, utilisez la classe [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) dans le package com.aspose.pdf. Le package com.aspose.pdf peut à la fois créer de nouveaux fichiers PDF et manipuler des fichiers PDF existants. Pour ajouter un TOC à un PDF existant, utilisez le package com.aspose.pdf.

Ce snippet de code PHP utilise Aspose.PDF pour ajouter une Table des Matières (TOC) à un document PDF existant :

```php
    // Ouvrir le document
    $document = new Document($inputFile);

    // Accéder à la première page du fichier PDF
    $tocPage = $document->getPages()->insert(1);

    // Créer un objet pour représenter l'information du TOC
    $tocInfo = new TocInfo();

    $title = new TextFragment("Table Des Matières");
    $title->getTextState()->setFontSize(20);
    $title->getTextState()->setFontStyle(FontStyles::$Bold);

    // Définir le titre pour le TOC
    $tocInfo->setTitle($title);
    $tocPage->setTocInfo($tocInfo);

    // Créer des objets chaîne qui seront utilisés comme éléments du TOC
    $titles = ["Première page", "Deuxième page", "Troisième page", "Quatrième page"];

    for ($i = 0; $i < 4; $i++) {
        // Créer un objet Heading
        $heading2 = new Heading(1);

        $segment2 = new TextSegment();
        $heading2->setTocPage($tocPage);
        $heading2->getSegments()->add($segment2);

        // Spécifier la page de destination pour l'objet Heading
        $page = $document->getPages()->get_Item($i + 2);
        $heading2->setDestinationPage($page);

        // Page de destination
        $heading2->setTop($page->getRect()->getHeight());

        // Coordonnée de destination
        $segment2->setText($titles[$i]);

        // Ajouter l'en-tête à la page contenant le TOC
        $tocPage->getParagraphs()->add($heading2);
    }
    // Sauvegarder le document mis à jour
    $document->save($outputFile);
    $document->close();
```

### Définir un type de TabLeader différent pour différents niveaux de TOC

Aspose.PDF permet également de définir différents TabLeaderType pour différents niveaux de TOC. Vous devez définir la propriété LineDash de FormatArray avec la valeur appropriée de l'énumération TabLeaderType comme suit.

```php
    // Ouvrir le document
    $document = new Document($inputFile);
    $tocPage = $document->getPages()->add();

    $tocInfo = new TocInfo();

    // définir le LeaderType
    $tocInfo->setLineDash(TabLeaderType->Solid);

    $title = new TextFragment("Table des matières");
    $title->getTextState()->setFontSize(30);
    $tocInfo->setTitle($title);

    // Ajouter la section de liste à la collection de sections du document Pdf
    $tocPage->setTocInfo($tocInfo);

    // Définir le format des quatre niveaux de liste en définissant les marges gauches et
    // les paramètres de format de texte de chaque niveau
    $fontStyles = new FontStyles();
    $tabLeaderTypes = new TabLeaderType();

    $tocInfo->setFormatArrayLength(4);
    $tocInfo->getFormatArray()[0]->getMargin()->setLeft(0);
    $tocInfo->getFormatArray()[0]->getMargin()->setRight(30);
    $tocInfo->getFormatArray()[0]->setLineDash($tabLeaderTypes->getDot());
    $tocInfo->getFormatArray()[0]->getTextState()->setFontStyle($fontStyles->getBold() | $fontStyles->getItalic());
    $tocInfo->getFormatArray()[1]->getMargin()->setLeft(10);
    $tocInfo->getFormatArray()[1]->getMargin()->setRight(30);
    $tocInfo->getFormatArray()[1]->setLineDash($tabLeaderTypes->getNone());
    $tocInfo->getFormatArray()[1]->getTextState()->setFontSize(10);
    $tocInfo->getFormatArray()[2]->getMargin()->setLeft(20);
    $tocInfo->getFormatArray()[2]->getMargin()->setRight(0);
    $tocInfo->getFormatArray()[2]->getTextState()->setFontStyle($fontStyles->getBold());
    $tocInfo->getFormatArray()[3]->setLineDash($tabLeaderTypes->getSolid());
    $tocInfo->getFormatArray()[3]->getMargin()->setLeft(30);
    $tocInfo->getFormatArray()[3]->getMargin()->setRight(30);
    $tocInfo->getFormatArray()[3]->getTextState()->setFontStyle($fontStyles->getBold());

    // Créer une section dans le document Pdf
    $page = $document->getPages()->add();

    // Ajouter quatre titres dans la section
    for ($Level = 1; $Level <= 4; $Level++) {
      $heading2 = new Heading($Level);
      $segment2 = new TextSegment();

      $heading2->getSegments()->add($segment2);
      $heading2->setAutoSequence(true);
      $heading2->setTocPage($tocPage);

      $segment2->setText("Titre Exemple" . $Level);
      $fontRepository = new FontRepository();
      $heading2->getTextState()->setFont($fontRepository->findFont("Arial UnicodeMS"));

      // Ajouter le titre dans la table des matières.
      $heading2->setInList(true);
      $page->getParagraphs()->add($heading2);
    }

    // Sauvegarder le document mis à jour
    $document->save($outputFile);
    $document->close();
```


### Masquer les numéros de page dans la table des matières

Dans le cas où vous ne souhaitez pas afficher les numéros de page, avec les titres dans la table des matières, vous pouvez utiliser la propriété [ShowPageNumbers](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/#setShowPageNumbers-boolean-) de la classe [TOCInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo) comme faux. Veuillez consulter l'extrait de code suivant pour masquer les numéros de page dans la table des matières :

```php
    // Ouvrir le document
    $document = new Document();
    $tocPage = $document->getPages()->add();
    
    // Créer un objet pour représenter les informations de la table des matières
    $tocInfo = new TocInfo();

    $title = new TextFragment("Table des Matières");
    $title->getTextState()->setFontSize(20);
    $title->getTextState()->setFontStyle(FontStyles::$Bold);

    // Définir le titre pour la table des matières
    $tocInfo->setTitle($title);

    // Ajouter la section de liste à la collection de sections du document Pdf
    $tocPage->setTocInfo($tocInfo);

    // Définir le format de la liste à quatre niveaux en définissant les marges de gauche et
    // les paramètres de format de texte de chaque niveau

    $tocInfo->setShowPageNumbers(false);
    $tocInfo->setFormatArrayLength(4);
    $tocInfo->getFormatArray()[0]->getMargin()->setRight(0);
    $tocInfo->getFormatArray()[0]->getTextState()->setFontStyle(FontStyles::$Bold | FontStyles::$Italic);

    $tocInfo->getFormatArray()[1]->getMargin()->setLeft(30);
    $tocInfo->getFormatArray()[1]->getTextState()->setUnderline(true);
    $tocInfo->getFormatArray()[1]->getTextState()->setFontSize(10);

    $tocInfo->getFormatArray()[2]->getTextState()->setFontStyle(FontStyles::$Bold);
    $tocInfo->getFormatArray()[3]->getTextState()->setFontStyle(FontStyles::$Bold);

    $page = $document->getPages()->add();

    // Ajouter quatre titres dans la section
    for ($Level = 1; $Level < 5; $Level++) {
      $heading2 = new Heading($Level);
      $segment2 = new TextSegment();
      $heading2->setTocPage($tocPage);
      $heading2->getSegments()->add($segment2);
      $heading2->setAutoSequence(true);
      $segment2->setText("ceci est le titre du niveau " + $Level);
      $heading2->setInList(true);
      $page->getParagraphs()->add($heading2);
    }
     
    // Enregistrer le document mis à jour
    $document->save($outputFile);
    $document->close();
```


### Personnaliser les numéros de page lors de l'ajout d'une table des matières

Il est courant de personnaliser la numérotation des pages dans la table des matières lors de l'ajout d'une table des matières dans un document PDF. Par exemple, nous pourrions avoir besoin d'ajouter un préfixe avant le numéro de page comme P1, P2, P3, etc. Dans ce cas, Aspose.PDF pour PHP via Java fournit la propriété PageNumbersPrefix de la classe TocInfo qui peut être utilisée pour personnaliser les numéros de page comme le montre l'exemple de code suivant.

```php

    // Ouvrir le document
    $document = new Document($inputFile);

    // Accéder à la première page du fichier PDF
    $tocPage = $document->getPages()->insert(1);

    // Créer un objet pour représenter les informations de la table des matières
    $tocInfo = new TocInfo();

    $title = new TextFragment("Table des matières");
    $title->getTextState()->setFontSize(20);
    $title->getTextState()->setFontStyle(FontStyles::$Bold);

    // Définir le titre pour la table des matières
    $tocInfo->setTitle($title);
    $tocInfo->setPageNumbersPrefix("P");
    $tocPage->setTocInfo($tocInfo);

    // Créer des objets de chaîne qui seront utilisés comme éléments de la table des matières
    $titles = ["Première page", "Deuxième page", "Troisième page", "Quatrième page"];

    for ($i = 0; $i < 4; $i++) {
        // Créer un objet Heading
        $heading2 = new Heading(1);

        $segment2 = new TextSegment();
        $heading2->setTocPage($tocPage);
        $heading2->getSegments()->add($segment2);

        // Spécifier la page de destination pour l'objet heading
        $page = $document->getPages()->get_Item($i + 2);
        $heading2->setDestinationPage($page);

        // Page de destination
        $heading2->setTop($page->getRect()->getHeight());

        // Coordonnée de destination
        $segment2->setText($titles[$i]);

        // Ajouter l'en-tête à la page contenant la table des matières
        $tocPage->getParagraphs()->add($heading2);
    }
    // Enregistrer le document mis à jour
    $document->save($outputFile);
    $document->close();
```


## Ajouter des Couches au Fichier PDF

Les couches peuvent être utilisées dans les documents PDF de nombreuses manières. Vous pourriez avoir un fichier multilingue que vous souhaitez distribuer et vous voulez que le texte de chaque langue apparaisse sur différentes couches, avec le design de fond apparaissant sur une couche distincte. Vous pourriez également créer des documents avec une animation qui apparaît sur une couche séparée. Un exemple pourrait être d'ajouter un accord de licence à votre fichier, et vous ne voulez pas qu'un utilisateur voie le contenu tant qu'il n'a pas accepté les termes de l'accord.

Aspose.PDF pour PHP via Java prend en charge l'ajout de couches aux fichiers PDF.

Pour travailler avec des couches dans des fichiers PDF, utilisez les membres de l'API suivants.

La classe [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) représente une couche et contient les propriétés suivantes :

- **Name** – le nom de la couche.
- **Id** – l'ID de la couche.
- **Contents** – une liste d'opérateurs de couche.

Une fois que les objets [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) ont été définis, ajoutez-les à la collection Layers de l'objet [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
 Le code ci-dessous montre comment ajouter des calques à un document PDF.

```php
    // Ouvrir le document
    $document = new Document($inputFile);
    $page = $document->getPages()->add();
    $arrayList = new java("java.util.ArrayList");
    $page->setLayers($arrayList);

    $layer = new $layer("oc1", "Ligne Rouge");
    $layer->getContents()->add(new operators_SetRGBColorStroke(1, 0, 0));
    $layer->getContents()->add(new operators_MoveTo(500, 700));
    $layer->getContents()->add(new operators_LineTo(400, 700));
    $layer->getContents()->add(new operators_Stroke());    
    $page->getLayers()->add($layer);

    $layer = new $layer("oc2", "Ligne Verte");
    $layer->getContents()->add(new operators_SetRGBColorStroke(0, 1, 0));
    $layer->getContents()->add(new operators_MoveTo(500, 750));
    $layer->getContents()->add(new operators_LineTo(400, 750));
    $layer->getContents()->add(new operators_Stroke());
    $page->getLayers()->add($layer);

    $layer = new $layer("oc3", "Ligne Bleue");
    $layer->getContents()->add(new operators_SetRGBColorStroke(0, 0, 1));
    $layer->getContents()->add(new operators_MoveTo(500, 800));
    $layer->getContents()->add(new operators_LineTo(400, 800));
    $layer->getContents()->add(new operators_Stroke());
    $page->getLayers()->add($layer);
    
    // Enregistrer le document mis à jour
    $document->save($outputFile);
    $document->close();
```

## Définir l'expiration du PDF

La fonctionnalité d'expiration PDF définit la durée de validité d'un fichier PDF. À une date particulière, si quelqu'un essaie d'y accéder, une fenêtre pop-up s'affiche, expliquant que le fichier a expiré et qu'il doit en obtenir un nouveau.

Aspose.PDF vous permet de définir l'expiration lors de la création et de l'édition de fichiers PDF.

L'extrait de code ci-dessous montre comment définir la date d'expiration pour un fichier PDF. Vous devez utiliser JavaScript car les fichiers enregistrés par des composants tiers (par exemple, OwnerGuard) ne peuvent pas être consultés sur d'autres stations de travail sans cet utilitaire.

Le fichier PDF peut être créé en utilisant PDF OwnerGuard avec un fichier existant ayant une date d'expiration. Mais le nouveau fichier ne peut être ouvert que sur une station de travail qui a PDF OwnerGuard installé. Les stations de travail sans PDF OwnerGuard donneront une erreur ExpirationFeatureError. Par exemple, le lecteur PDF ouvre le fichier si OwnerGuard est installé, mais Adobe Acrobat renvoie une erreur.

```php

    // Ouvrir le document
    $document = new Document($inputFile);
       
    $javaScript = new JavascriptAction(
      "var year=2020;" + 
      "var month=4;" + 
      "var today = new Date(); today = new Date(today.getFullYear(), today.getMonth());" +
      "var expiry = new Date(year, month);" +
      "if (today.getTime() > expiry.getTime())" + 
      "app.alert('Le fichier est expiré. Vous avez besoin d'un nouveau.');"
      );
    $document->setOpenAction($javaScript);
    $document->save($outputFile);
    $document->close();
```