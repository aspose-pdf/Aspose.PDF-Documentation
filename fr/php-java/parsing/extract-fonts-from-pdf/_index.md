---
title: Extraire des polices d'un PDF 
linktitle: Extraire des polices
type: docs
weight: 30
url: fr/php-java/extract-fonts-from-pdf/
description: Comment extraire des polices d'un PDF en utilisant Aspose.PDF pour PHP
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Si vous souhaitez obtenir toutes les polices d'un document PDF, vous pouvez utiliser la méthode [Document.IDocumentFontUtilities.getAllFonts()](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getFontUtilities--) fournie dans la classe Document.
Veuillez consulter l'extrait de code suivant afin d'obtenir toutes les polices d'un document PDF existant :

```php

    // Créer une nouvelle instance de la classe License et définir le fichier de licence.
    $licenceObject = new License();
    $licenceObject->setLicense($license);

    // Définir le chemin vers le répertoire contenant le document PDF et le répertoire de sortie pour les polices extraites.
    $dataDir = getcwd() . DIRECTORY_SEPARATOR . "samples";
    $inputFile = $dataDir . DIRECTORY_SEPARATOR . "sample.pdf";

    // Initialiser la variable de données de réponse.
    $responseData = "";

    try {
        // Charger le document PDF.
        $document = new Document($inputFile);

        // Obtenir toutes les polices utilisées dans le document PDF.
        $fonts = java_values($document->getFontUtilities()->getAllFonts());

        // Itérer sur chaque police et l'enregistrer en tant que fichier de police TrueType.
        foreach ($fonts as $font) {
            // Définir le chemin du fichier de sortie pour le fichier de police.
            $outputFile = $dataDir . DIRECTORY_SEPARATOR . "results" . DIRECTORY_SEPARATOR . $font->getFontName() . ".ttf";

            // Créer un objet FileOutputStream pour écrire le fichier de police.
            $fontStream = new java("java.io.FileOutputStream", $outputFile);

            // Enregistrer la police en tant que fichier de police TrueType.
            $font->save($fontStream);

            // Fermer le flux de la police.
            $fontStream->close();

            // Ajouter le nom de la police aux données de réponse.
            $responseData = $responseData . $font->getFontName() . ", ";
        }

        // Fermer le document PDF.
        $document->close();
    }
```