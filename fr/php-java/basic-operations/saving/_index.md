---
title: Enregistrer le document PDF 
linktitle: Enregistrer
type: docs
weight: 30
url: fr/php-java/save-pdf-document/
description: Apprenez à enregistrer un fichier PDF avec la bibliothèque Aspose.PDF pour PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Enregistrer le document PDF sur le système de fichiers

Vous pouvez enregistrer le document PDF créé ou manipulé sur le système de fichiers en utilisant la méthode save de la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

```php

    $document = new Document($inputFile);        
    $document->save($outputFile);
```