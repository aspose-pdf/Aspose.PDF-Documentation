---
title: Supprimer des pages PDF par programmation
linktitle: Supprimer des pages PDF
type: docs
weight: 40
url: /fr/php-java/supprimer-pages/
description: Vous pouvez supprimer des pages de votre fichier PDF en utilisant PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Supprimer une page d'un fichier PDF

1. Appelez la méthode de suppression et spécifiez l'index de la page
1. Appelez la méthode de sauvegarde pour enregistrer le fichier PDF mis à jour
Le code suivant montre comment supprimer une page particulière du fichier PDF en utilisant PHP.

```php

    // Ouvrir le document
    $document = new Document($inputFile);      

    $pages = $document->getPages();

    // Supprimer une page particulière
    $pages->delete(2);

    // Enregistrer le document de sortie
    $document->save($outputFile);
    $document->close();
```