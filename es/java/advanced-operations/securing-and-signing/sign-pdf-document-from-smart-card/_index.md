---
title: Firmar documentos PDF desde una tarjeta inteligente en Java
linktitle: Firma de PDF con tarjeta inteligente
type: docs
weight: 30
url: /java/sign-pdf-document-from-smart-card/
description: Revise la cobertura de ejemplo de Java actual para la firma de PDF basada en certificados en Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cobertura de firma de PDF basada en certificados en el conjunto de ejemplos de Java actual
Abstract: Esta página describe el alcance actual de los ejemplos de firma disponibles en el árbol de fuentes de documentación de Java. El repositorio incluye ejemplos de firma de PDF basados ​​en certificados con credenciales PFX o PKCS7, pero actualmente no incluye un ejemplo de almacén de certificados de tarjeta inteligente dedicado para Java.
---
El repositorio de Java actual no incluye un ejemplo de firma de tarjeta inteligente respaldada por código fuente dedicado en `facades/pdffilesignature`, pero el siguiente flujo de trabajo muestra el patrón API típico para firmar un PDF con un certificado seleccionado de un almacén de certificados local.


## 
Firmar un documento PDF desde una tarjeta inteligente


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree una fachada [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) y vincule el documento PDF de origen.

1. 
Recupere el certificado local y cree la [Firma externa](https://reference.aspose.com/pdf/java/com.aspose.pdf/externalsignature/) requerida.
1. Configure la apariencia de la firma visual y el objetivo [Rectángulo](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).

1. 
Aplique la firma al documento PDF a través de [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).

1. 
Guarde el documento PDF actualizado.

1. 
Vincule el documento cargado a la fachada [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) con `bindPdf(...)`.

1. 
Recupere el certificado local que representa la credencial de la tarjeta inteligente llamando a `getLocalCertificate()`.
1. Compruebe si se encontró un certificado. De lo contrario, guarde el archivo de salida sin cambios y detenga el flujo de trabajo.

1. 
Cree una [Firma externa](https://reference.aspose.com/pdf/java/com.aspose.pdf/externalsignature/) a partir del certificado seleccionado.

1. 
Establezca la imagen de apariencia de la firma visual con `setSignatureAppearance(...)`.

1. 
Llame a `sign(...)` con la página de destino, el motivo, el contacto, la ubicación, el indicador de visibilidad, la firma [Rectángulo](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) y el objeto de firma externo.

1. 
Guarde el PDF firmado en la ruta de salida.

```java
public static void signWithSmartCard(Path inputFile, Path outputFile, Path pngFile) {
    try (Document document = new Document(inputFile.toString());
            PdfFileSignature pdfSignature = new PdfFileSignature()) {
        pdfSignature.bindPdf(document);
        X509Certificate2 selectedCertificate = getLocalCertificate();
        if (selectedCertificate == null) {
            System.out.println("Local certificate was not found.");
            document.save(outputFile.toString());
            return;
        }

        ExternalSignature externalSignature = new ExternalSignature(selectedCertificate, null);
        pdfSignature.setSignatureAppearance(pngFile.toString());
        pdfSignature.sign(1, "Reason", "Contact", "Location", true,
                new java.awt.Rectangle(100, 100, 200, 200), externalSignature);
        pdfSignature.save(outputFile.toString());
    }
}
```
