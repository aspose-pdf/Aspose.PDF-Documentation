---
title: Extraiga información de firma de PDF en Java
linktitle: Extraer detalles de la firma
type: docs
weight: 20
url: /java/extract-image-and-signature-information/
description: Aprenda a extraer detalles de certificados y firmas digitales de archivos PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraiga detalles de firma y datos de certificados de archivos PDF firmados en Java
Abstract: Este artículo explica cómo inspeccionar firmas digitales en documentos PDF usando Aspose.PDF para Java. Aprenda a leer los detalles del firmante, verificar una firma, verificar si una firma cubre todo el documento, extraer el certificado de firma incorporado y eliminar una firma existente.
---
Utilice `PdfFileSignature` para inspeccionar y administrar firmas que ya existen en un documento PDF.


## 
Leer información de firma


1. Cree la fachada [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) y vincule el documento PDF de origen.

1. Acceda al nombre de la firma del documento y configure el flujo de inspección de firma requerido por el ejemplo.

1. Lea y verifique la información de la firma de la fachada [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).
1. Lea los valores devueltos o continúe con el siguiente paso de procesamiento.


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
Verificar una firma


1. Cree la fachada [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) y vincule el documento PDF de origen.

1. Acceda al nombre de la firma del documento y configure el flujo de verificación requerido por el ejemplo.

1. Lea y verifique la información de la firma de la fachada [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).

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

## Extraer el certificado de firma


1. Cree la fachada [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) y vincule el documento PDF de origen.

1. Acceda al nombre de la firma del documento requerido para la extracción del certificado.

1. Escriba el resultado extraído o inspeccione los valores devueltos desde la fachada [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).

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
