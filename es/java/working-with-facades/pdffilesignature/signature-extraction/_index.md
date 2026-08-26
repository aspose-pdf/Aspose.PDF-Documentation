---
title: Signature Extraction
linktitle: Extracción de firma
type: docs
weight: 50
url: /java/signature-extraction/
description: Aprenda a extraer el certificado de firma de un PDF firmado en Java con PdfFileSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraiga un certificado de firma de un PDF en Java
Abstract: Aprenda cómo extraer el certificado asociado con una firma PDF usando Aspose.PDF para Java. El conjunto de ejemplos de Java actual incluye la extracción de certificados en un flujo de salida, pero no incluye una muestra de extracción de imágenes de firma separada.
---
## Extraer certificado de firma

Utilice este flujo de trabajo cuando necesite guardar el certificado asociado con una firma existente.

### Steps

1. Create a `PdfFileSignature` instance and bind the signed PDF.
2. Select the signature name to inspect.
3. Call `extractCertificate` to open the certificate stream.
4. Copy the certificate bytes to an output file.
5. Close the stream resources and the facade object.

### Java example

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

The current `PdfFileSignatureExamples.java` class does not include a dedicated Java sample for extracting a rendered signature image.
