---
title: Ouvrir un Document PDF
linktitle: Ouvrir
type: docs
weight: 20
url: /php-java/open-pdf-document/
description: Apprenez à ouvrir un fichier PDF avec Aspose.PDF pour PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ouvrir un document PDF existant

Les fichiers PDF ou fichiers au format de document portable sont devenus la norme universelle pour l'échange de documents. Ils sont largement utilisés pour conserver le format d'un document. Cependant, travailler avec des fichiers PDF en utilisant des langages de programmation comme PHP via Java peut être un peu difficile. Cet article présente la bibliothèque Aspose.PDF pour PHP via Java qui vous permet d'ouvrir rapidement et facilement votre PDF.

```php

    $document = new Document($inputFile,"mypassword");
    $responseData = "Le document a été ouvert avec succès. Taille du fichier : " . filesize($inputFile);
```