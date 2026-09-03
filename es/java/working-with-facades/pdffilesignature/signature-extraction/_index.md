---
title: Extracción de firma
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


### 
Pasos


1. Cree una instancia `PdfFileSignature` y vincule el PDF firmado.

2. Seleccione el nombre de la firma para inspeccionar.
3. Llame a `extractCertificate` para abrir el flujo de certificados.

4. Copie los bytes del certificado a un archivo de salida.

5. Cierre los recursos del flujo y el objeto de fachada.


### 
Ejemplo de Java


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


La clase `PdfFileSignatureExamples.java` actual no incluye un ejemplo de Java dedicado para extraer una imagen de firma renderizada.
