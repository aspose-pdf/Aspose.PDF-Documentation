---
title: Extraire des Données AcroForms
linktitle: Extraire des Données AcroForms
type: docs
weight: 30
url: /php-java/extract-form/
description: Cette section explique comment extraire des formulaires de votre document PDF avec Aspose.PDF pour PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtenir la Valeur d'un Champ Individuel du Document PDF

La méthode [getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) du champ de formulaire vous permet d'obtenir la valeur d'un champ particulier.

Pour obtenir la valeur, récupérez le champ de formulaire à partir de la collection de formulaires de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Cet exemple sélectionne un [textBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) et récupère sa valeur à l'aide de la méthode [getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--).

```php

    // Ouvrir un document
    $document = new Document($inputFile);

    // Obtenir un champ
    $textBoxField = $document->getForm()->get("textbox1");

    // Obtenir le nom du champ
    $responseData = "PartialName: " . $textBoxField->getPartialName();

    // Obtenir la valeur du champ
    $responseData = $responseData . " Value: " . $textBoxField->getValue();
    $document->close();
```