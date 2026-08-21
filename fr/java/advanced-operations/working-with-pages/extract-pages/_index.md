---
title: Extraire des pages PDF en Java
linktitle: Extraction de pages PDF
type: docs
weight: 80
url: /java/extract-pages/
description: Découvrez comment extraire une ou plusieurs pages PDF dans de nouveaux fichiers en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extrayez des pages PDF dans de nouveaux documents avec Java
Abstract: Cet article explique comment extraire des pages de fichiers PDF à l'aide d'Aspose.PDF pour Java. Il couvre la copie d'une seule page et l'extraction de plusieurs pages dans un document de destination distinct à l'aide de l'indexation de page basée sur 1.
---
Aspose.PDF pour Java vous permet de copier les pages sélectionnées dans un nouveau document de destination.


## 
Extraire une seule page



Utilisez cet exemple lorsque vous devez enregistrer une page du PDF source dans un document distinct.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et créez un document de destination.

1. 
Copiez la page cible dans la collection de pages de destination.
1. Enregistrez le nouveau PDF.


```java
public static void extractPage(Path inputFile, Path outputFile) {
    try (Document srcDocument = new Document(inputFile.toString());
         Document dstDocument = new Document()) {
        dstDocument.getPages().add(srcDocument.getPages().get_Item(2));
        dstDocument.save(outputFile.toString());
    }
}
```

## 
Extraire plusieurs pages



Utilisez cet exemple lorsque vous devez copier plusieurs pages dans un PDF séparé.


1. 
Ouvrez le PDF source [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et créez un document de destination.

1. 
Itérez les index de page sélectionnés et ajoutez-les à la destination.
1. Enregistrez le document de pages extraites.

```java
public static void extractBunchPages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString());
         Document anotherDocument = new Document()) {
        Integer[] pages = {2, 3};
        for (Integer pageIndex : pages) {
            anotherDocument.getPages().add(document.getPages().get_Item(pageIndex));
        }
        anotherDocument.save(outputFile.toString());
    }
}
```
