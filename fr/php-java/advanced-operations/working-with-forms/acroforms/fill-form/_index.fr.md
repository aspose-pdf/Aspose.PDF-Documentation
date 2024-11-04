---
title: Remplir les AcroForms
linktitle: Remplir les AcroForms
type: docs
weight: 20
url: /php-java/fill-form/
description: Cette section explique comment remplir un champ de formulaire dans un document PDF avec Aspose.PDF pour PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Les documents PDF sont merveilleux et vraiment le type de fichier préféré pour créer des formulaires.

Aspose.PDF pour PHP via Java vous permet de remplir un champ de formulaire, d'obtenir le champ de la collection Form de l'objet Document.

Regardons l'exemple suivant pour résoudre cette tâche :

```php

    // Ouvrir le document
    $document = new Document($inputFile);
    $page = $document->getPages()->get_Item(1);
    
    // Obtenir un champ    
    $textBoxField = $document->getForm()->get("textbox1");

    // Modifier la valeur du champ
    $textBoxField->setValue("Valeur à remplir dans le champ");
        
    // Enregistrer le document mis à jour
    $document->save($outputFile);
    $document->close();
```