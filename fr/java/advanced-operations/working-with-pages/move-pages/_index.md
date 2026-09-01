---
title: Déplacer les pages PDF en Java
linktitle: Déplacement des pages PDF
type: docs
weight: 100
url: /java/move-pages/
description: Découvrez comment déplacer des pages PDF dans un document ou entre des documents en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Déplacer les pages PDF entre les documents en Java
Abstract: Cet article explique comment déplacer des pages dans des PDF à l'aide d'Aspose.PDF pour Java. Il couvre le déplacement d'une seule page ou de plusieurs pages vers un autre document et le repositionnement d'une page à l'intérieur du même PDF.
---
Aspose.PDF pour Java vous permet de déplacer des pages entre des documents ou de repositionner des pages dans le même PDF.


## 
Déplacer une page vers un autre document



Utilisez cet exemple lorsqu'une seule page doit être supprimée du PDF source et enregistrée dans un document distinct.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et créez un document de destination.

1. 
Ajoutez la page cible à la destination et supprimez-la de la source.
1. Enregistrez les deux documents.


```java
public static void movePageFromOneDocumentToAnother(Path inputFile, Path sourceOutputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString());
         Document anotherDocument = new Document()) {
        anotherDocument.getPages().add(document.getPages().get_Item(2));
        document.getPages().delete(2);
        document.save(sourceOutputFile.toString());
        anotherDocument.save(outputFile.toString());
    }
}
```

## 
Déplacer plusieurs pages vers un autre document



Utilisez cet exemple lorsque plusieurs pages doivent être transférées du PDF source vers un nouveau document.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et créez le document de destination.

1. 
Copiez les pages sélectionnées dans le document de destination.
1. Supprimez les pages déplacées de la source et enregistrez les deux fichiers.


```java
public static void moveBunchPagesFromOneDocumentToAnother(Path inputFile, Path sourceOutputFile, Path outputFile) {
    try (Document srcDocument = new Document(inputFile.toString());
         Document dstDocument = new Document()) {
        Integer[] pages = {1, 2};
        for (Integer pageIndex : pages) {
            dstDocument.getPages().add(srcDocument.getPages().get_Item(pageIndex));
        }
        dstDocument.save(outputFile.toString());
        srcDocument.getPages().delete(pages);
        srcDocument.save(sourceOutputFile.toString());
    }
}
```

## 
Déplacer une page dans le même document



Utilisez cet exemple lorsqu'une page doit être repositionnée vers un nouvel emplacement dans le même PDF.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Dupliquez la page cible dans la nouvelle position et supprimez l'entrée de page d'origine.
1. Enregistrez le document réorganisé.

```java
public static void movePageInNewLocationInSameDocument(Path inputFile, Path outputFile) {
    try (Document srcDocument = new Document(inputFile.toString())) {
        srcDocument.getPages().add(srcDocument.getPages().get_Item(2));
        srcDocument.getPages().delete(2);
        srcDocument.save(outputFile.toString());
    }
}
```
