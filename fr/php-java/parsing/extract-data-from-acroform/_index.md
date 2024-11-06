---
title:  Extraire des données d'AcroForm 
linktitle:  Extraire des données d'AcroForm
type: docs
weight: 50
url: fr/php-java/extract-data-from-acroform/
description: Les AcroForms existent dans de nombreux documents PDF. Cet article vise à vous aider à comprendre comment extraire des données d'AcroForms en utilisant PHP et Aspose.PDF.
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extraire les champs de formulaire d'un document PDF

Aspose.PDF pour PHP ne vous permet pas seulement de créer et remplir des champs de formulaire, mais facilite également l'extraction des données ou des informations des champs de formulaire à partir de fichiers PDF.

Supposons que nous ne connaissions pas à l'avance les noms des champs de formulaire. Ensuite, nous devrions parcourir chaque page du PDF pour extraire des informations sur tous les AcroForms dans le PDF ainsi que les valeurs des champs de formulaire. Pour accéder au formulaire, nous devons utiliser la méthode [getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--).

```php

    // Créer une nouvelle instance de la classe License et définir le fichier de licence
    $licenceObject = new License();
    $licenceObject->setLicense($license);

    // Définir le chemin vers le répertoire contenant le document PDF
    $dataDir = getcwd() . DIRECTORY_SEPARATOR . "samples";

    // Définir le chemin vers le fichier PDF d'entrée
    $inputFile = $dataDir . DIRECTORY_SEPARATOR . "StudentInfoFormElectronic.pdf";

    // Définir l'en-tête de la réponse pour indiquer que la réponse sera au format JSON
    header('Content-Type: application/json; charset=utf-8');

    // Initialiser la variable de données de réponse
    $responseData = "";

    try {
        // Créer une nouvelle instance de la classe Document et charger le fichier PDF d'entrée
        $document = new Document($inputFile);

        // Obtenir les champs de formulaire du document et les convertir en valeurs PHP
        $fields = java_values($document->getForm()->getFields());

        // Parcourir chaque champ de formulaire et extraire le nom et la valeur du champ
        foreach ($fields as $formField) {
            // Concaténer le nom et la valeur du champ aux données de réponse
            $responseData = $responseData . "(Nom du champ: " . $formField->getPartialName() . " |";
            $responseData = $responseData . " Valeur: " . $formField->getValue() . "),";
        }

        // Fermer le document
        $document->close();
    }
```


Si vous connaissez le nom des champs de formulaire dont vous souhaitez extraire les valeurs, vous pouvez utiliser l'indexeur dans la collection Documents.Form pour récupérer rapidement ces données.

## Extraire des données vers XML à partir d'un fichier PDF

La classe Form permet d'exporter des données vers un fichier XML à partir du fichier PDF en utilisant la méthode ExportXml. Pour exporter des données vers XML, vous devez créer un objet de la classe Form puis appeler la méthode ExportXml en utilisant l'objet FileStream. Enfin, vous pouvez fermer l'objet FileStream et disposer de l'objet Form. L'extrait de code suivant vous montre comment exporter des données vers un fichier XML.

```php

    // Ouvrir le document
    $form = new facades_Form();
    $form->bindPdf($inputFile);

    // Créer un objet FileOutputStream pour écrire le fichier de police.
    $xmlOutputStream = new java("java.io.FileOutputStream", "output.xml");

    // Exporter les données
    $form->exportXml($xmlOutputStream);

    // Fermer le flux de fichier
    $xmlOutputStream->close();

    // Fermer le document
    $form->close();
```

## Exporter des données vers FDF à partir d'un fichier PDF

Pour exporter les données des formulaires PDF vers un fichier XFDF, nous pouvons utiliser la méthode [exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-) dans la classe [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

Veuillez noter qu'il s'agit d'une classe de `com.aspose.pdf.facades`. Malgré le nom similaire, cette classe a un objectif légèrement différent.

Pour exporter des données vers FDF, vous devez créer un objet de la classe `Form` puis appeler la méthode `exportXfdf` en utilisant l'objet `OutputStream`. L'extrait de code suivant vous montre comment exporter des données vers un fichier XFDF.

```php

    // Ouvrir le document
    $form = new facades_Form();
    $form->bindPdf($inputFile);

    // Créer un objet FileOutputStream pour écrire le fichier de police.
    $xmlOutputStream = new java("java.io.FileOutputStream", "output.fdf");

    // Exporter les données
    $form->exportFdf($xmlOutputStream);

    // Fermer le flux de fichier
    $xmlOutputStream->close();

    // Fermer le document
    $form->close();
```

## Exporter des données vers XFDF à partir d'un fichier PDF

Pour exporter les données des formulaires PDF vers un fichier XFDF, nous pouvons utiliser la méthode [exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-) dans la classe [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

Afin d'exporter des données vers XFDF, vous devez créer un objet de la classe `Form` puis appeler la méthode `exportXfdf` en utilisant l'objet `OutputStream`. Le code suivant vous montre comment exporter des données vers un fichier XFDF.

```php

    // Ouvrir le document
    $form = new facades_Form();
    $form->bindPdf($inputFile);

    // Créer un objet FileOutputStream pour écrire le fichier de police.
    $xmlOutputStream = new java("java.io.FileOutputStream", "output.xfdf");

    // Exporter les données
    $form->exportXfdf($xmlOutputStream);

    // Fermer le flux de fichier
    $xmlOutputStream->close();

    // Fermer le document
    $form->close();
```