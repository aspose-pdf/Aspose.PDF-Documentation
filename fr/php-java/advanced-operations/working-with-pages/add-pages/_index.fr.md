---
title: Ajouter des Pages dans un PDF
linktitle: Ajouter des Pages
type: docs
weight: 10
url: /php-java/add-pages/
description: Cet article explique comment insérer (ajouter) une page à l'emplacement souhaité dans un fichier PDF. Apprenez à déplacer, supprimer (effacer) des pages d'un fichier PDF en utilisant PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ajouter ou Insérer une Page dans un Fichier PDF

Aspose.PDF pour PHP via Java vous permet d'insérer une page dans un document PDF à n'importe quel emplacement dans le fichier ainsi que d'ajouter des pages à la fin d'un fichier PDF. Vous devez passer l'emplacement où vous souhaitez insérer la page vierge à la méthode d'insertion. Cette section montre comment ajouter des pages à un PDF avec Aspose.PDF pour PHP via Java.

### Insérer une Page Vierge dans un Fichier PDF à l'Emplacement Souhaité

L'extrait de code suivant montre comment insérer une page vierge dans un fichier PDF :

1. Créez un objet de la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) avec le fichier PDF d'entrée.
1. Ajoutez une page, et insérez-la dans un PDF.

1. Enregistrez le fichier PDF de sortie en utilisant la méthode Save.

Le code suivant vous montre comment insérer une page dans un fichier PDF.

```php

    // Ouvrir le document
    $document = new Document($inputFile);

    // Ajouter une page
    $document->getPages()->add();

    // Insérer une page vide dans un PDF
    $document->getPages()->insert(2);

    // Enregistrer le document de sortie
    $document->save($outputFile);
    $document->close();
```

Dans l'exemple ci-dessus, nous avons ajouté une page vide avec les paramètres par défaut. Si vous devez faire en sorte que la taille de la page soit la même qu'une autre page dans le document, vous devez ajouter quelques lignes de code :

```php

    // Ouvrir le document
    $document = new Document($inputFile);

    // Ajouter une page
    $page1 = $document->getPages()->add();

    // Insérer une page vide dans un PDF
    $page2 = $document->getPages()->insert(2);

    // copier les paramètres de la page depuis la page 1
    $page2->setCropBox($page1->getCropBox());
    $page2->setMediaBox($page1->getMediaBox());
    $page2->setTrimBox($page1->getTrimBox());
    $page2->setArtBox($page1->getArtBox());
    $page2->setBleedBox($page1->getBleedBox());
    
    // Enregistrer le document de sortie
    $document->save($outputFile);
    $document->close();
```


### Ajouter une Page Vide à la Fin d'un Fichier PDF

Parfois, vous souhaitez vous assurer qu'un document se termine par une page vide. Ce sujet explique comment insérer une page vide à la fin du document PDF.

Pour insérer une page vide à la fin d'un fichier PDF :

1. Créez un objet de classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) avec le fichier PDF d'entrée.
2. Ajoutez une page, et insérez-la dans un PDF.
3. Enregistrez le PDF de sortie en utilisant la méthode save.

Le code suivant vous montre comment insérer une page vide à la fin d'un fichier PDF.

```php

    // Ouvrir le document
    $document = new Document($inputFile);

    // Ajouter une page
    $document->getPages()->add();

    // Insérer une page vide dans un PDF
    $document->getPages()->insert(2);

    // Enregistrer le document de sortie
    $document->save($outputFile);
    $document->close();
```