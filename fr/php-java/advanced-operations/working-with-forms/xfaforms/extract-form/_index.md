---
title: Extraire le formulaire XFA
linktitle: Extraire le formulaire XFA
type: docs
weight: 30
url: /fr/php-java/extract-form/
description: Cette section explique comment extraire des formulaires de votre document PDF avec Aspose.PDF pour PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtenir la valeur d'un champ de formulaire du document PDF

La méthode [getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) du champ de formulaire vous permet d'obtenir la valeur d'un champ particulier.

Pour obtenir la valeur, récupérez le champ de formulaire à partir de la collection de formulaires de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Cet exemple sélectionne un [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) et récupère sa valeur en utilisant la méthode [getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--).

```php

    // Charger le formulaire XFA
    $document = new Document($inputFile);
    
    // Obtenir les noms des champs du formulaire XFA
    $names = $document->getForm()->getXFA()->getFieldNames();
        
    // Obtenir les valeurs des champs
    $document->getForm()->getXFA()->get_Item($names[0]);
    $document->getForm()->getXFA()->get_Item($names[1]);
    
    // Enregistrer le PDF modifié    
    $document->close();
```