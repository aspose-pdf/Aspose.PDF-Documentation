---
title: Vérifier la Signature dans le Fichier PDF
type: docs
weight: 30
url: fr/java/verify-signature-in-pdf/
description: Cette section explique comment travailler avec la signature dans un fichier PDF en utilisant la classe PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Vérifier Si le Fichier PDF Est Signé avec une Signature

Pour vérifier si un fichier PDF est signé en utilisant la méthode VerifySigned de la classe [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature). Cette méthode nécessite le nom de la signature et retourne vrai si le PDF est signé avec ce nom de signature. Il est également possible de vérifier qu'un [PDF est signé](/pdf/java/working-with-signature-in-a-pdf-file/), sans vérifier avec quelle signature il est signé.

### Vérification qu'un PDF Est Signé avec une Signature Donnée

Le code suivant montre comment vérifier si un PDF est signé avec une signature donnée.

```java
    public static void IsPdfSigned() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        if (pdfSign.containsSignature())
            System.out.println("Document Signed");

        pdfSign.close();
    }
```


### Vérification qu'un PDF est signé

Pour déterminer si un fichier est signé, sans fournir le nom de la signature, utilisez le code suivant.

```java
    public static void IsPdfSignedWithGivenSignature() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        if (pdfSign.verifySigned("Signature1")) {
            System.out.println("PDF Signé");
        }
    }
```

## Vérifier si la signature est valide

La méthode [VerifySignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#verifySignature-java.lang.String-) de la classe [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) vous permet de valider une signature particulière. Cette méthode nécessite le nom de la signature en entrée et retourne vrai si la signature est valide. Le snippet de code suivant vous montre comment valider une signature.

```java
    public static void IsPdfSignatureValid() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        if (pdfSign.verifySignature("Signature1")) {
            System.out.println("Signature Vérifiée");
        }
    }
```