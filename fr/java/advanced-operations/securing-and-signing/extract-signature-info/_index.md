---
title: Extraire les informations de signature d'un PDF en Java
linktitle: Extraire les détails de la signature
type: docs
weight: 20
url: /java/extract-image-and-signature-information/
description: Découvrez comment extraire les détails d'un certificat et d'une signature numérique à partir de fichiers PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraire les détails de la signature et les données du certificat des PDF signés en Java
Abstract: Cet article explique comment inspecter les signatures numériques dans les documents PDF à l'aide d'Aspose.PDF pour Java. Découvrez comment lire les détails du signataire, vérifier une signature, vérifier si une signature couvre l'intégralité du document, extraire le certificat de signature intégré et supprimer une signature existante.
---
Utilisez `PdfFileSignature` pour inspecter et gérer les signatures qui existent déjà dans un document PDF.


## 
Lire les informations de signature


1. 
Créez la façade [PdfFileSignature] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) et liez le document PDF source.

1. 
Accédez au nom de la signature du document et configurez le flux d'inspection des signatures requis par l'exemple.

1. 
Lisez et vérifiez les informations de signature de la façade [PdfFileSignature] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).
1. Lisez les valeurs renvoyées ou passez à l'étape de traitement suivante.


```java
public static void getSignatureInformation(Path inputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        System.out.println("Signature Names: " + pdfSignature.getSignNames());
        System.out.println("Signer: " + pdfSignature.getSignerName(signatureName));
        System.out.println("Date: " + pdfSignature.getDateTime(signatureName));
        System.out.println("Reason: " + pdfSignature.getReason(signatureName));
        System.out.println("Location: " + pdfSignature.getLocation(signatureName));
    } finally {
        pdfSignature.close();
    }
}
```

## 
Vérifier une signature


1. 
Créez la façade [PdfFileSignature] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) et liez le document PDF source.

1. 
Accédez au nom de la signature du document et configurez le flux de vérification requis par l'exemple.

1. 
Lisez et vérifiez les informations de signature de la façade [PdfFileSignature] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).

```java
public static void verifyPdfSignature(Path inputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        System.out.println("Signature '" + signatureName + "' is valid: "
                + pdfSignature.verifySignature(signatureName));
        System.out.println("Signature covers whole document: "
                + pdfSignature.coversWholeDocument(signatureName));
    } finally {
        pdfSignature.close();
    }
}
```

## Extraire le certificat de signature


1. 
Créez la façade [PdfFileSignature] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) et liez le document PDF source.

1. 
Accédez au nom de signature du document requis pour l’extraction du certificat.

1. 
Écrivez la sortie extraite ou inspectez les valeurs renvoyées par la façade [PdfFileSignature] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).

```java
public static void extractSignatureCertificate(Path inputFile, Path outputFile) throws Exception {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        try (InputStream inputStream = pdfSignature.extractCertificate(signatureName);
             OutputStream outputStream = Files.newOutputStream(outputFile)) {
            inputStream.transferTo(outputStream);
        }
    } finally {
        pdfSignature.close();
    }
}
```
