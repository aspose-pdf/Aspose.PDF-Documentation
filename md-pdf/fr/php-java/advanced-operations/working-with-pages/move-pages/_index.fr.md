---
title: Déplacer des Pages PDF 
linktitle: Déplacer des Pages PDF
type: docs
weight: 20
url: /php-java/move-pages/
description: Essayez de déplacer des pages à l'emplacement souhaité ou à la fin d'un fichier PDF en utilisant Aspose.PDF pour PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Déplacement d'une Page d'un Document PDF à un Autre

Ce sujet explique comment déplacer une page d'un document PDF à la fin d'un autre document en utilisant PHP.
Pour déplacer une page, nous devons :

1. Créer un objet de classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) avec le fichier PDF source
1. Créer un objet de classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) avec le fichier PDF de destination
1. Ajouter la page au document de sortie. Enregistrez le fichier de sortie
1. Supprimer la page du document d'entrée. Enregistrez le document d'entrée modifié
1. Fermer les documents
1. Sauvegarder et fermer le document de sortie

Le code suivant vous montre comment déplacer une page.

```php

    // Ouvrir le document
    $document = new Document($inputFile1);
    $dstDocument = new Document($outputFile);
    
    $page = $document->getPages()->get_Item(2);
    $dstDocument->getPages()->add($page);

    // Enregistrer le fichier de sortie
    $dstDocument->save($srcFileName);
    $document->getPages()->delete(2);
    $document->save($dstFileName);
    $document->close();
    $dstDocument->close();
  
    // Enregistrer le document de sortie
    $document->save($outputFile);
    $document->close();
```


## Déplacer un ensemble de pages d'un document PDF à un autre

1. Créez un objet de classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) avec le fichier PDF source.
1. Créez un objet de classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) avec le fichier PDF de destination.
1. Définissez les pages à copier du document d'entrée au document de sortie.
1. Parcourez le tableau :
    1. Obtenez la page à l'index spécifié du document d'entrée.
    1. Ajoutez la page au document de destination.
1. Enregistrez le PDF de sortie en utilisant la méthode Save.
1. Supprimez la page dans le document source en utilisant le tableau.
1. Enregistrez le PDF source en utilisant la méthode Save.

Le fragment de code suivant vous montre comment insérer une page vide à la fin d'un fichier PDF.

```php

    // Ouvrir le document
    $document = new Document($inputFile1);
    $dstDocument = new Document($outputFile);
    
    $pages = [1, 3];
    foreach ($pages as $pageIndex) {
      $page = $document->getPages()->get_Item($pageIndex);
      $dstDocument->getPages()->add(page);
    }
    // Enregistrer les fichiers de sortie
    $dstDocument->save($srcFileName);
    $document->getPages()->delete($pages);

    $document->save(dstFileName);

    $document->close();
    $dstDocument->close();  
```


## Déplacer une page dans un nouvel emplacement dans le document PDF actuel

1. Créez un objet de la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) avec le fichier PDF source.
1. Obtenez la page à partir de la collection [pageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection).
1. Ajoutez la page au nouvel emplacement.
1. Supprimez la page à l'index 2.
1. Enregistrez le PDF de sortie en utilisant la méthode save.

```php

    // Ouvrir le document
    $document = new Document($inputFile);
        
    $pageCollection = $document->getPages();
    
    $page = $pageCollection->get_Item(2);
    $pageCollection->add(page);
    $pageCollection->delete(2);

    // Enregistrer le fichier de sortie
    $document->save($outputFile);
    $document->close();      
```