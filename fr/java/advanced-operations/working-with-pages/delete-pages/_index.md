---
title: Supprimer des pages PDF en Java
linktitle: Suppression de pages PDF
type: docs
weight: 80
url: /fr/java/delete-pages/
description: Découvrez comment supprimer des pages de fichiers PDF en Java.
lastmod: "2026-09-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Supprimer une ou plusieurs pages PDF en Java
Abstract: Cet article explique comment supprimer des pages de fichiers PDF à l'aide d'Aspose.PDF for Java. Il couvre la suppression d'une seule page et la suppression de plusieurs pages à la fois via l'API de collection de pages.
---
Utilisez la collection de pages du document pour supprimer une ou plusieurs pages d’un PDF.

## Supprimer une seule page

Utilisez cet exemple pour supprimer une page en indiquant son index.

1. Ouvrez le PDF source dans un objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Supprimez la page cible de la collection de pages.
1. Enregistrez le document mis à jour.

```java
public static void deletePage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().delete(2);
        document.save(outputFile.toString());
    }
}
```

## Supprimer plusieurs pages

Utilisez cet exemple lorsque plusieurs pages doivent être supprimées en une seule opération.

1. Ouvrez le PDF source [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Transmettez les index de pages à supprimer de la collection de pages.
1. Enregistrez le PDF modifié.

```java
public static void deleteBunchPages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().delete(new Integer[]{2, 3, 4});
        document.save(outputFile.toString());
    }
}
```
