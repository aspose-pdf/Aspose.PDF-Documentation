---
title: Remplir les AcroForms
linktitle: Remplir les AcroForms
type: docs
weight: 20
url: fr/php-java/fill-form/
description: Cette section explique comment remplir un champ de formulaire dans un document PDF avec Aspose.PDF pour PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Les documents PDF sont merveilleux, et vraiment le type de fichier préféré, pour créer des formulaires.

Aspose.PDF pour PHP via Java vous permet de remplir un champ de formulaire, d'obtenir le champ de la collection Form de l'objet Document.

Regardons l'exemple suivant pour résoudre cette tâche :

```php

    // Charger le formulaire XFA
    $document = new Document($inputFile);
    
    // Obtenir les noms des champs du formulaire XFA
    $names = $document->getForm()->getXFA()->getFieldNames();
        
    // Définir les valeurs des champs        
    $document->getForm()->getXFA()->set_Item($names[0],"Field 0");
    $document->getForm()->getXFA()->set_Item($names[1],"Field 1");
        
    // Enregistrer le document mis à jour
    $document->save($outputFile);
    
    // Enregistrer le PDF modifié    
    $document->close();
```