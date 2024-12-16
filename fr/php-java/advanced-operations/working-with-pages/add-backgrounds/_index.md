---
title: Ajouter un arrière-plan au PDF 
linktitle: Ajouter des arrière-plans
type: docs
weight: 110
url: /fr/php-java/add-backgrounds/
descriptions: Ajoutez une image d'arrière-plan à votre fichier PDF en utilisant PHP. Utilisez l'objet BackgroundArtifact.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Les images d'arrière-plan peuvent être utilisées pour ajouter un filigrane ou un autre design subtil aux documents. Dans Aspose.PDF pour PHP via Java, chaque document PDF est une collection de pages et chaque page contient une collection d'artefacts. La classe [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/BackgroundArtifact) peut être utilisée pour ajouter une image d'arrière-plan à un objet page.

Le code suivant montre comment ajouter une image d'arrière-plan aux pages PDF en utilisant l'objet BackgroundArtifact avec PHP.

```php

    // Ouvrir le document
    $document = new Document($inputFile);

    // Ajouter une nouvelle page à l'objet document
    $page = $document->getPages()->add();

    // Créer un objet BackgroundArtifact
    $background = new BackgroundArtifact();

    // Spécifier l'image pour l'objet backgroundArtifact
    $fileInputStream = new java("java.io.FileInputStream", "image.jpg");
    $background->setBackgroundImage($fileInputStream);

    // Ajouter backgroundArtifact à la collection d'artefacts de la page
    $page->getArtifacts()->add($background);

    // Enregistrer le fichier PDF mis à jour
    $document->save($outputFile);
    $document->close();
```