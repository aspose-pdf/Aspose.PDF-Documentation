---
title: Extracción de firma
linktitle: Extracción de firma
type: docs
weight: 50
url: /es/java/signature-extraction/
description: Aprenda cómo extraer el certificado de firma de un PDF firmado en Java con PdfFileSignature.
lastmod: "2026-09-03"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraiga un certificado de firma de PDF en Java
Abstract: Aprenda cómo extraer el certificado asociado a una firma PDF usando Aspose.PDF for Java. El conjunto actual de ejemplos en Java incluye la extracción del certificado a un flujo de salida, pero no incluye un ejemplo separado de extracción de la imagen de la firma.
---
## Extraer certificado de firma

Utilice este flujo de trabajo cuando necesite guardar el certificado asociado a una firma existente.

### Pasos

1. Crear un `PdfFileSignature` instancia y enlaza el PDF firmado.
2. Seleccione el nombre de la firma para inspeccionar.
3. Llamar `extractCertificate` para abrir el flujo del certificado.
4. Copie los bytes del certificado a un archivo de salida.
5. Cierre los recursos del flujo y el objeto fachada.

### Ejemplo de Java

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

El actual `PdfFileSignatureExamples.java` La clase no incluye un ejemplo dedicado de Java para extraer una imagen de firma renderizada.
