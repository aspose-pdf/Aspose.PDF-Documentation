---
title: Enregistrer le document PDF par programme
linktitle: Enregistrer le PDF
type: docs
weight: 30
url: /java/save-pdf-document/
description: Découvrez comment enregistrer des documents PDF en Java dans un fichier, dans un flux ou en tant que standard PDF à l'aide d'Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Enregistrement de documents PDF à l'aide de la bibliothèque Aspose.PDF en Java
Abstract: Cet article décrit comment enregistrer des documents PDF en Java à l'aide d'Aspose.PDF. Il couvre l'enregistrement dans un chemin de fichier, l'enregistrement dans un OutputStream et la conversion d'un document avant de l'enregistrer en tant que fichier standard PDF/X.
---
Aspose.PDF pour Java propose plusieurs façons d'enregistrer un document en fonction de la destination cible et des exigences de sortie.


## 
Enregistrer un document PDF en Java



Vous pouvez enregistrer un document :


1. 
Enregistrez le [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) directement dans un fichier sur le disque.

1. 
Enregistrez le [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dans un `OutputStream`.
1. Convertissez le [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) avec [PdfFormatConversionOptions] (https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) et enregistrez-le dans un format standard tel que [PdfFormat] (https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/).


## 
Enregistrer le document dans un fichier


```java
public static void saveDocumentToFile(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    document.save(outputFile.toString());
    document.close();
}
```

## 
Enregistrer le document pour diffuser


```java
public static void saveDocumentToStream(Path inputFile, Path outputFile) throws Exception {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        document.save(stream);
    } finally {
        document.close();
    }
}
```

## 
Enregistrer le document au format PDF/X

```java
public static void saveDocumentAsStandard(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    document.convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
    document.save(outputFile.toString());
    document.close();
}
```
