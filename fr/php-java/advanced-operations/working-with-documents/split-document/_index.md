---
title: Diviser un PDF par programmation
linktitle: Diviser des fichiers PDF
type: docs
weight: 60
url: fr/php-java/split-document/
description: Ce sujet montre comment diviser les pages PDF en fichiers PDF individuels dans vos applications PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Vous pouvez diviser des fichiers PDF en utilisant Aspose.PDF et obtenir les résultats en ligne à ce lien : [products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter)

{{% /alert %}}

Ce sujet montre comment diviser les pages PDF avec Aspose.PDF pour PHP via Java en fichiers PDF individuels dans vos applications PHP. Pour diviser les pages PDF en fichiers PDF d'une seule page en utilisant PHP, les étapes suivantes peuvent être suivies :

1. Parcourez les pages du document PDF à travers la collection [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection) de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Pour chaque itération, créez un nouvel objet Document et ajoutez l'objet [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) individuel dans le document vide.
2. Enregistrez le nouveau PDF en utilisant la méthode Save.

Le code PHP suivant vous montre comment diviser les pages PDF en fichiers PDF individuels.

```php

    // Ouvrir le document
    $document = new Document($inputFile);
    $pages = $document->getPages();
    $pagesSize = java_values($pages->size());
       
    // Boucle à travers toutes les pages
    for ($pageCount = 1; $pageCount <= $pagesSize; $pageCount++) {
        $page = $pages->get_Item($pageCount);
        $newDocument = new Document();
        $newDocument->getPages()->add($page);
        $newDocument->save($outputFile . "page_" . $pageCount . ".pdf");
        $newDocument->close();
    }
    $document->close();
```