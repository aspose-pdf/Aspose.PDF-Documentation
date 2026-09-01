---
title: Supprimer des pages PDF en Java
linktitle: Suppression de pages PDF
type: docs
weight: 80
url: /java/delete-pages/
description: Découvrez comment supprimer des pages de fichiers PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Supprimer une ou plusieurs pages PDF en Java
Abstract: Cet article explique comment supprimer des pages de fichiers PDF à l'aide d'Aspose.PDF pour Java. Il couvre la suppression d'une seule page et la suppression de plusieurs pages à la fois via l'API de collection de pages.
---
Use the document page collection when you need to remove one or more pages from a PDF.


## 
Delete a single page



Use this example when you need to remove one page by its index.


1. 
Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Delete the target page from the page collection.
1. Enregistrez le document mis à jour.


```java
public static void deletePage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().delete(2);
        document.save(outputFile.toString());
    }
}
```

## 
Supprimer plusieurs pages



Utilisez cet exemple lorsque plusieurs pages doivent être supprimées en une seule opération.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Transmettez les index de pages à supprimer de la collection de pages.
1. Enregistrez le PDF modifié.

```java
public static void deleteBunchPages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().delete(new Integer[]{2, 3, 4});
        document.save(outputFile.toString());
    }
}
```
