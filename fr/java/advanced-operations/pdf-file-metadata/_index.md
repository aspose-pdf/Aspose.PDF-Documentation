---
title: Travailler avec les métadonnées de fichiers PDF en Java
linktitle: Métadonnées du fichier PDF
type: docs
weight: 200
url: /java/pdf-file-metadata/
description: Découvrez comment extraire, mettre à jour et gérer les métadonnées de fichiers PDF, les informations sur les documents et les propriétés XMP en Java à l'aide d'Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Obtenez et définissez les informations du document PDF et les métadonnées XMP en Java
Abstract: Cet article explique comment utiliser les métadonnées PDF à l'aide d'Aspose.PDF pour Java. Apprenez à lire les informations d'un document telles que l'auteur, le titre et les mots-clés, à mettre à jour les propriétés du fichier, à inspecter la version et les privilèges du PDF, à définir les champs de métadonnées XMP et à enregistrer les métadonnées via les API DOM et de façade.
---
Aspose.PDF pour Java propose deux manières principales de travailler avec les métadonnées :


- 
L'API DOM via `Document`, `DocumentInfo` et `document.getMetadata()`.

- 
L'API de façade via `PdfFileInfo`.


## 
Obtenir des informations sur le fichier PDF



Utilisez cet exemple lorsque vous devez lire des champs d'informations standard sur un document tels que l'auteur, le titre, le sujet ou les mots-clés.

1. Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Accédez à l'objet [DocumentInfo] (https://reference.aspose.com/pdf/java/com.aspose.pdf/documentinfo/).

1. 
Lisez les champs de métadonnées requis et affichez leurs valeurs.


```java
public static void getPdfFileInformation(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocumentInfo docInfo = document.getInfo();

        System.out.println("Author: " + docInfo.getAuthor());
        System.out.println("Creation Date: " + docInfo.getCreationDate());
        System.out.println("Keywords: " + docInfo.getKeywords());
        System.out.println("Modify Date: " + docInfo.getModDate());
        System.out.println("Subject: " + docInfo.getSubject());
        System.out.println("Title: " + docInfo.getTitle());
    }
}
```

## 
Définir des métadonnées avec un préfixe d'espace de noms



Utilisez cet exemple lorsque vous devez ajouter ou mettre à jour une propriété XMP à l'aide d'un préfixe d'espace de noms enregistré.

1. Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Enregistrez l'espace de noms XMP requis et ajoutez l'élément de métadonnées.

1. 
Enregistrez le document mis à jour.


```java
public static void setPrefixMetadata(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getMetadata().registerNamespaceUri("xmp", "http://ns.adobe.com/xap/1.0/");
        document.getMetadata().addItem("xmp:ModifyDate", OffsetDateTime.now().toString());
        document.save(outputFile.toString());
    }
    System.out.println("Prefix metadata saved to " + outputFile);
}
```

## 
Mettre à jour les champs d'informations sur le document



Utilisez cet exemple lorsque vous souhaitez écrire des propriétés de fichier PDF standard telles que l'auteur, le titre, le producteur ou la date de création.

1. Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Accédez à [DocumentInfo] (https://reference.aspose.com/pdf/java/com.aspose.pdf/documentinfo/) et attribuez de nouvelles valeurs de métadonnées.

1. 
Enregistrez le document avec les informations de fichier mises à jour.


```java
public static void setFileInformation(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocumentInfo docInfo = document.getInfo();
        Date now = new Date();

        docInfo.setAuthor("Aspose");
        docInfo.setCreationDate(now);
        docInfo.setKeywords("Aspose.Pdf, DOM, API");
        docInfo.setModDate(now);
        docInfo.setSubject("PDF Information");
        docInfo.setTitle("Setting PDF Document Information");
        docInfo.setProducer("Custom producer");
        docInfo.setCreator("Custom creator");

        document.save(outputFile.toString());
    }
    System.out.println("File information saved to " + outputFile);
}
```

## 
Définir les propriétés des métadonnées XMP



Utilisez cet exemple lorsque vous devez stocker des entrées XMP supplémentaires, y compris des valeurs de métadonnées personnalisées.

1. Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Ajoutez les éléments de métadonnées XMP requis via `document.getMetadata()`.

1. 
Enregistrez le fichier de sortie.

```java
public static void setXmpMetadata(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getMetadata().addItem("xmp:CreateDate", OffsetDateTime.now().toString());
        document.getMetadata().addItem("xmp:Nickname", "Nickname");
        document.getMetadata().addItem("xmp:CustomProperty", "Custom Value");
        document.save(outputFile.toString());
    }
    System.out.println("XMP metadata saved to " + outputFile);
}
```
