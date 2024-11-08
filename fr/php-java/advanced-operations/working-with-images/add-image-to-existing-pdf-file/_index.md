---
title: Ajouter une Image à un Fichier PDF Existant 
linktitle: Ajouter Image
type: docs
weight: 10
url: /fr/php-java/add-image-to-existing-pdf-file/
description: Cette section décrit comment ajouter une image à un fichier PDF existant en utilisant PHP.
lastmod: "2024-06-05"
---

Chaque page PDF contient des propriétés de Ressources et de Contenu. Les ressources peuvent être des images et des formulaires par exemple, tandis que le contenu est représenté par un ensemble d'opérateurs PDF. Chaque opérateur a son nom et ses arguments. Cet exemple utilise des opérateurs pour ajouter une image à un fichier PDF.

Pour ajouter une image à un fichier PDF existant :

- Créez un objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) et ouvrez le document PDF d'entrée.
- Obtenez la page sur laquelle vous souhaitez ajouter une image.
- Ajoutez une nouvelle page au document.
- Définissez la taille de la page à 1190.7 x 841.995.
- Ajoutez une image à la page en utilisant le fichier image spécifié et la boîte de rognage de la page.
- Enregistrez le fichier.

Le code suivant montre comment ajouter l'image dans un document PDF.

```php

    // Ouvrir le document en utilisant le fichier d'entrée spécifié.
    $document = new Document($inputFile);
    
    // Ajouter une nouvelle page au document.
    $page = $document->getPages()->add();
    
    // Définir la taille de la page à 1190.7 x 841.995.
    $page->setPageSize(1190.7, 841.995);
    
    // Ajouter une image à la page en utilisant le fichier image spécifié et la boîte de rognage de la page.
    $page->addImage($imageFileName, $page->getCropBox());
    
    // Enregistrer le document modifié dans le fichier de sortie spécifié.
    $document->save($outputFile);
    
    // Fermer le document.
    $document->close();
```