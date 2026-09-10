---
title: Ouvrir un document PDF par programme
linktitle: Ouvrir le PDF
type: docs
weight: 20
url: /java/open-pdf-document/
description: Découvrez comment ouvrir un fichier PDF en Java à l'aide d'Aspose.PDF à partir d'un chemin de fichier, d'un flux ou avec un mot de passe.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ouverture de documents PDF à l'aide de la bibliothèque Aspose.PDF en Java
Abstract: Cet article montre comment ouvrir des documents PDF existants en Java à l'aide d'Aspose.PDF. Il couvre l'ouverture d'un PDF par chemin de fichier, l'ouverture d'un PDF à partir d'un InputStream et l'ouverture d'un document protégé par mot de passe, chaque exemple lisant le nombre de pages du document chargé.
---
Aspose.PDF pour Java prend en charge plusieurs façons de charger un document PDF existant en fonction de l'origine des données source.


## 
Ouvrir un document PDF en Java



Vous pouvez ouvrir un document PDF :


1. 
Ouvrez un [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) directement à partir d'un chemin de fichier.

1. 
Ouvrez un [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) à partir d'un `InputStream`.
1. Ouvrez un [Document] crypté (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) en fournissant le mot de passe.


## 
Ouvrir un document à partir d'un fichier


```java
public static void openDocumentFromFile(Path inputFile) {
    Document document = new Document(inputFile.toString());
    System.out.println("Pages: " + document.getPages().size());
    document.close();
}
```

## 
Ouvrir le document à partir du flux


```java
public static void openDocumentFromStream(Path inputFile) throws Exception {
    try (InputStream stream = Files.newInputStream(inputFile)) {
        Document document = new Document(stream);
        System.out.println("Pages: " + document.getPages().size());
        document.close();
    }
}
```

## 
Ouvrir un document crypté

```java
public static void openDocumentEncrypted(Path inputFile) {
    Document document = new Document(inputFile.toString(), "P@ssw0rd");
    System.out.println("Pages: " + document.getPages().size());
    document.close();
}
```
