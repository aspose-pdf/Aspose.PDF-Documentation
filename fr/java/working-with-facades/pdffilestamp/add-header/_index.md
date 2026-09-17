---
title: Ajouter un en-tête au PDF
linktitle: Ajouter un en-tête au PDF
type: docs
weight: 20
url: /java/add-header/
description: Découvrez comment ajouter des en-têtes de texte et d'image aux pages PDF en Java avec la façade PdfFileStamp.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter des en-têtes de texte et d'image au PDF en Java
Abstract: Découvrez comment ajouter du contenu d'en-tête aux documents PDF avec Aspose.PDF pour Java à l'aide de la façade PdfFileStamp. Les exemples Java couvrent les en-têtes de texte brut, les en-têtes d'image chargés à partir d'un flux et les en-têtes stylisés avec des valeurs de marge explicites.
---
## Ajouter un en-tête au PDF



Utilisez `PdfFileStamp` lorsque vous avez besoin d'un contenu d'en-tête répété sur chaque page.


### 
Étapes


1. 
Créez une instance `PdfFileStamp` et liez le PDF source.

2. 
Créez le contenu de l'en-tête sous la forme `FormattedText` ou chargez-le à partir d'un flux d'images.
3. Appelez la surcharge `addHeader` appropriée.

4. 
Enregistrez la sortie et fermez l’objet façade.


### 
Exemples Java

```java
public static void addTextHeader(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText("Sample Header");
        pdfStamper.addHeader(text, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addImageHeader(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try (InputStream imageStream = Files.newInputStream(imageFile)) {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addHeader(imageStream, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addHeaderWithMargins(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText(
                "Sample Header",
                Color.BLUE,
                FontStyle.Helvetica,
                EncodingType.Winansi,
                true,
                12.0f);
        pdfStamper.addHeader(text, 20, 20, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
