---
title: Créer un document PDF
linktitle: Créer
type: docs
weight: 10
url: fr/php-java/create-document/
description: Apprenez à créer un fichier PDF dans Aspose.PDF pour PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

L'API **Aspose.PDF pour PHP via Java** permet aux développeurs d'applications d'intégrer des fonctionnalités de traitement de documents PDF dans leurs applications. Elle peut être utilisée pour créer et lire des fichiers PDF sans avoir besoin d'aucun autre logiciel installé sur la machine sous-jacente. Aspose.PDF pour PHP via Java peut être utilisé dans divers types d'applications telles que les applications Desktop, JSP et JSF.

## Comment créer un fichier PDF en utilisant PHP via Java

Pour créer un fichier PDF en utilisant PHP via Java, les étapes suivantes peuvent être utilisées.

1. Instancier un objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)
1. Ajouter une [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) à l'objet document

1. Créez un objet [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment)
1. Ajoutez [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment) à la collection [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) de la page
1. Enregistrez le document PDF résultant

```php

    $document = new Document();    
    $page = $document->getPages()->add();
    $textFragment = new TextFragment("Hello World!");    
    $page->getParagraphs()->add($textFragment);
    $document->save($outputFile);
```