---
title: Ajouter une signature numérique ou signer numériquement un PDF en Java
linktitle: Signer numériquement un PDF
type: docs
weight: 10
url: /java/digitally-sign-pdf-file/
description: Découvrez comment signer et certifier numériquement des documents PDF en Java à l'aide d'Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Signer numériquement des fichiers PDF avec Java
Abstract: Ce guide explique comment signer numériquement des documents PDF à l'aide d'Aspose.PDF pour Java. Il couvre la signature avec un objet de certificat, la signature avec les paramètres de certificat de base et la certification d'un document avec une signature DocMDP pour contrôler les modifications autorisées après la signature.
---
Aspose.PDF pour Java prend en charge plusieurs flux de signature via `PdfFileSignature`.


## 
Signer un PDF avec un objet de certificat


1. 
Créez la façade [PdfFileSignature] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) et liez le document PDF source.

1. 
Créez l'objet de signature [PKCS7] (https://reference.aspose.com/pdf/java/com.aspose.pdf/pkcs7/) et configurez les options de signature.

1. 
Appliquez la signature au document PDF via [PdfFileSignature] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).
1. Enregistrez le document PDF mis à jour.


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
```


Cette approche crée d'abord un objet de signature `PKCS7`, puis l'applique à la page 1.


## 
Signer un PDF avec les paramètres de certificat de base


1. 
Créez la façade [PdfFileSignature] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) et liez le document PDF source.

1. 
Configurez les paramètres de certificat requis par l'exemple de signature.
1. Appliquez la signature au document PDF via [PdfFileSignature] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).

1. 
Enregistrez le document PDF mis à jour.


```java
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

## 
Certifier un PDF avec DocMDP



Utilisez une signature de détection et de prévention des modifications de documents lorsque vous avez besoin de restrictions au niveau de la certification :


1. 
Créez la façade [PdfFileSignature] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) et liez le document PDF source.
1. Créez l'objet [DocMDPSignature] (https://reference.aspose.com/pdf/java/com.aspose.pdf/docmdpsignature/) et configurez les options de signature [DocMDPAccessPermissions] (https://reference.aspose.com/pdf/java/com.aspose.pdf/docmdpaccesspermissions/).

1. 
Appliquez la signature de certification et enregistrez le document PDF mis à jour.

```java
public static void certifyPdfWithMdpSignature(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        DocMDPSignature signature = new DocMDPSignature(
                createPkcs7(certificateFile, "Certified for form filling and signing"),
                DocMDPAccessPermissions.FillingInForms);
        pdfSignature.certify(1, "Certified for form filling and signing", "security@example.com",
                "New York, USA", true, signatureRectangle(), signature);
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```
