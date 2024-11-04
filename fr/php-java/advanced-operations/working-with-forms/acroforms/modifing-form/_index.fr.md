---
title: Modification des AcroForms
linktitle: Modification des AcroForms
type: docs
weight: 40
url: /java/modifing-form/
description: Cette section explique comment modifier les formulaires dans votre document PDF avec Aspose.PDF pour PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Définir une police de champ de formulaire personnalisée

Les champs de formulaire dans les fichiers PDF Adobe peuvent être configurés pour utiliser des polices par défaut spécifiques. Aspose.PDF permet aux développeurs d'appliquer n'importe quelle police comme police par défaut d'un champ, qu'il s'agisse de l'une des 14 polices de base ou d'une police personnalisée.  
Pour définir et mettre à jour la police par défaut utilisée pour les champs de formulaire, Aspose.PDF possède la classe DefaultAppearance (Font font, double size, Color color). Cette classe peut être accédée en utilisant com.aspose.pdf.DefaultAppearance. Pour utiliser cet objet, utilisez la méthode setDefaultAppearance(..) de la classe Field.

Le fragment de code suivant vous montre comment définir la police par défaut pour un champ de formulaire PDF.

```php

    // Ouvrir un document
    $document = new Document($inputFile);

    // Obtenir un champ de formulaire particulier du document
    $field = $document->getForm()->get("textbox1");

    // Créer un objet de police
    $fontRepository = new FontRepository();
    $font = $fontRepository->findFont("ComicSansMS");

    $colors = new Color();
    $blackColor = $colors->getBlack();

    // Définir les informations de police pour le champ de formulaire
    $field->setDefaultAppearance(new DefaultAppearance($font, 10, $blackColor));

    // Enregistrer le document mis à jour
    $document->save($outputFile);
    $document->close();        

    $document->close();
```


## Obtenir/Définir FieldLimit

Ce code démontre l'utilisation de la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) pour ouvrir un document, récupérer un champ de formulaire, définir sa longueur maximale, récupérer la longueur maximale avec les méthodes 'setMaxLen' et 'getMaxLen'.

```php

    // Ouvrir un document
    $document = new Document($inputFile);

    // Obtenir un champ de formulaire particulier du document
    $field = $document->getForm()->get("textbox1");
    
    $field->setMaxLen(10);

    // Obtenir la limite maximale du champ en utilisant DOM
    $responseData = "Limite : " . $field->getMaxLen();          

    $document->close();
```

Vous pouvez également obtenir la même valeur en utilisant l'espace de noms Aspose.PDF.Facades avec le code suivant.

```php

    // Ouvrir un document
    $document = new Document($inputFile);

    // Obtenir un champ de formulaire particulier du document
    $field = $document->getForm()->get("textbox1");

    // Obtenir la limite maximale du champ en utilisant DOM
    $responseData = "Limite : " . $field->getMaxLen();          

    $document->close();
```


De même, Aspose.PDF a une méthode qui obtient la limite du champ en utilisant l'approche DOM. Le code ci-dessous montre les étapes.

```php

    // Ouvrir un document
    $document = new Document($inputFile);

    // Obtenir un champ de formulaire particulier du document
    $field = $document->getForm()->get("textbox1");

    // Supprimer le champ
    $field->delete();
    
    $document->close();
```
## Supprimer un Champ de Formulaire Particulier d'un Document PDF

Tous les champs de formulaire sont contenus dans la collection Form de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Cette collection fournit différentes méthodes qui gèrent les champs de formulaire, y compris la méthode de suppression. Si vous souhaitez supprimer un champ particulier, passez le nom du champ en tant que paramètre à la méthode de suppression, puis enregistrez le document PDF mis à jour.

Le code ci-dessous montre comment supprimer un champ nommé d'un document PDF.

```php

    // Ouvrir un document
    $document = new Document($inputFile);

    // Obtenir un champ de formulaire particulier du document
    $field = $document->getForm()->get("textbox1");

    // Supprimer le champ
    $field->delete();
    
    $document->close();
```


## Modifier un Champ de Formulaire dans un Document PDF

La collection Form de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) vous permet de gérer les champs de formulaire dans un document PDF.

Pour modifier un champ de formulaire, obtenez le champ de la collection Form et définissez ses propriétés. Ensuite, enregistrez le document PDF mis à jour.

Le code suivant montre comment modifier un champ de formulaire existant dans un document PDF.

```php

    // Ouvrir un document
    $document = new Document($inputFile);

    // Obtenir un champ de formulaire particulier du document
    $field = $document->getForm()->get("textbox1");

    // Modifier la valeur du champ
    $field->setValue("Valeur Mise à Jour");

    // Définir le champ comme lecture seule
    $field->setReadOnly(true);

    // Enregistrer le document mis à jour
    $document->save($outputFile);        
    $document->close();
```

### Déplacer un Champ de Formulaire vers un Nouvel Emplacement dans un Fichier PDF

Si vous souhaitez déplacer un champ de formulaire vers un nouvel emplacement sur une page PDF, obtenez d'abord l'objet du champ, puis spécifiez une nouvelle valeur pour sa méthode setRect.
 Un objet [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) avec de nouvelles coordonnées est assigné à la méthode setRect(..). Ensuite, enregistrez le PDF mis à jour en utilisant la méthode save de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

L'extrait de code suivant vous montre comment déplacer un champ de formulaire vers un nouvel emplacement.

```php

    // Ouvrir un document
    $document = new Document($inputFile);

    // Obtenir un champ de formulaire particulier du document
    $field = $document->getForm()->get("textbox1");

    // Modifier l'emplacement du champ
    $field->setRect(new Rectangle(300, 400, 600, 500));

    // Enregistrer le document mis à jour
    $document->save($outputFile);        
    $document->close();
```