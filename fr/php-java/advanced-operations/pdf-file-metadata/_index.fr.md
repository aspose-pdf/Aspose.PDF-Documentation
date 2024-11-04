---
title: Travailler avec les Métadonnées de Fichier PDF 
linktitle: Métadonnées de Fichier PDF
type: docs
weight: 140
url: /php-java/pdf-file-metadata/
description: Cette section explique comment obtenir des informations sur un fichier PDF, comment obtenir des métadonnées XMP à partir d'un fichier PDF, définir des informations de fichier PDF.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtenir des Informations sur le Fichier PDF

Pour obtenir des informations spécifiques à un fichier sur un fichier PDF, récupérez d'abord l'objet 'docInfo' en utilisant la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) [getInfo()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getInfo--). Une fois l'objet 'docInfo' récupéré, vous pouvez obtenir les valeurs des propriétés individuelles.

Le code suivant vous montre comment définir des informations de fichier PDF.

```php

    // Ouvrir le document
    $document = new Document($inputFile);
    
    // Obtenir des informations sur le document
    $docInfo = $document->getInfo();

    // Afficher les informations du document
    $responseData1 = "Auteur : " . $docInfo->getAuthor() . ", ";
    $responseData2 = "Date de création : " . $docInfo->getCreationDate() . ", ";
    $responseData3 = "Mots-clés : " . $docInfo->getKeywords() . ", ";
    $responseData4 = "Date de modification : " . $docInfo->getModDate() . ", ";
    $responseData5 = "Sujet : " . $docInfo->getSubject() . ", ";
    $responseData6 = "Titre : " . $docInfo->getTitle() . "";

    $document->close();
```