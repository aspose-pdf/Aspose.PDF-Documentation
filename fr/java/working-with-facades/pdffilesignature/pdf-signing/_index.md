---
title: Signer des documents PDF
linktitle: Signer des documents PDF
type: docs
weight: 10
url: /java/pdf-signing/
description: Apprenez à signer des documents PDF en Java avec la façade PdfFileSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Signer des documents PDF avec des signatures numériques en Java
Abstract: Découvrez comment signer des documents PDF avec Aspose.PDF pour Java. L'ensemble d'exemples Java couvre la signature avec un chemin de certificat et un mot de passe configurés, ainsi que la signature avec un objet de signature PKCS7 explicite qui inclut des métadonnées de signature telles que le motif, les informations de contact, l'emplacement et l'autorité.
---
## Signer des documents PDF



Utilisez `PdfFileSignature` lorsque vous devez appliquer une signature numérique visible à un PDF.


### 
Étapes


1. 
Créez une instance `PdfFileSignature` et liez le PDF source.

2. 
Chargez le certificat soit via `setCertificate`, soit en créant un objet `PKCS7`.
3. Appelez `sign` avec la page cible, les paramètres de visibilité, le rectangle de signature et les données de signature.

4. 
Enregistrez le PDF signé et fermez l'objet façade.


### 
Exemples Java

```java
public static void signPdfWithCertificateObject(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        pdfSignature.sign(1, false, signatureRectangle(), createPkcs7(certificateFile, "Document approval"));
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}

public static void signPdfWithBasicParameters(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        pdfSignature.setCertificate(certificateFile.toString(), CERTIFICATE_PASSWORD);
        pdfSignature.sign(1, "Document approval", "qa@example.com", "New York, USA", false, signatureRectangle());
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```
