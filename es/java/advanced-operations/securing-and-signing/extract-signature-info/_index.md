---
title: Extraer información de firma de PDF en Java
linktitle: Extraer detalles de la firma
type: docs
weight: 20
url: /es/java/extract-image-and-signature-information/
description: Aprenda cómo extraer los detalles del certificado y de la firma digital de archivos PDF en Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraer detalles de la firma y datos del certificado de PDFs firmados en Java
Abstract: Este artículo explica cómo inspeccionar firmas digitales en documentos PDF usando Aspose.PDF for Java. Aprenda cómo leer los detalles del firmante, verificar una firma, comprobar si una firma cubre todo el documento, extraer el certificado de firma incrustado y eliminar una firma existente.
---
Usar `PdfFileSignature` para inspeccionar y gestionar firmas que ya existen en un documento PDF.

## Leer información de la firma

1. Crear el [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) fachada y enlazar el documento PDF de origen.
1. Acceda al nombre de la firma del documento y configure el flujo de inspección de firmas requerido por el ejemplo.
1. Lea y verifique la información de la firma del [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) fachada.
1. Lea los valores devueltos o continúe con su siguiente paso de procesamiento.

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

## Verificar una firma

1. Crear el [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) fachada y enlazar el documento PDF de origen.
1. Acceda al nombre de la firma del documento y configure el flujo de verificación requerido por el ejemplo.
1. Lea y verifique la información de la firma del [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) fachada.

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

1. Crear el [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) fachada y enlazar el documento PDF de origen.
1. Acceder al nombre de la firma del documento necesario para la extracción del certificado.
1. Escribe la salida extraída o inspecciona los valores devueltos de la [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) fachada.

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
