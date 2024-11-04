---
title: Verificar Firma en Archivo PDF
type: docs
weight: 30
url: /java/verify-signature-in-pdf/
description: Esta sección explica cómo trabajar con la Firma en un Archivo PDF usando la clase PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Verificar Si el Archivo PDF Está Firmado Usando una Firma

Para verificar si un archivo PDF está firmado usando el método VerifySigned de la clase [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature). Este método requiere el nombre de la firma y devuelve true si el PDF está firmado usando ese nombre de firma. También es posible verificar que un [PDF está firmado](/pdf/java/working-with-signature-in-a-pdf-file/), sin verificar con qué firma está firmado.

### Verificar que un PDF Está Firmado con una Firma Dada

El siguiente fragmento de código muestra cómo verificar si un PDF está firmado usando una firma dada.

```java
    public static void IsPdfSigned() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        if (pdfSign.containsSignature())
            System.out.println("Documento Firmado");

        pdfSign.close();
    }
```


### Verificando que un PDF está firmado

Para determinar si un archivo está firmado, sin proporcionar el nombre de la firma, use el siguiente código.

```java
    public static void IsPdfSignedWithGivenSignature() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        if (pdfSign.verifySigned("Signature1")) {
            System.out.println("PDF Firmado");
        }
    }
```

## Verificar si la Firma es Válida

El método [VerifySignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#verifySignature-java.lang.String-) de la clase [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) le permite validar una firma en particular. Este método requiere el nombre de la firma como entrada y devuelve true si la firma es válida. El siguiente fragmento de código muestra cómo validar una firma.

```java
    public static void IsPdfSignatureValid() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        if (pdfSign.verifySignature("Signature1")) {
            System.out.println("Firma Verificada");
        }
    }
```