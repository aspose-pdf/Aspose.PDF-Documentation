---
title: Firmar documentos PDF desde una tarjeta inteligente en Java
linktitle: Firma de PDF con tarjeta inteligente
type: docs
weight: 30
url: /es/java/sign-pdf-document-from-smart-card/
description: Revisar la cobertura actual de ejemplos Java para la firma de PDF basada en certificado en Aspose.PDF.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cobertura de firma de PDF basada en certificado en el conjunto actual de ejemplos Java
Abstract: Esta página describe el alcance actual de los ejemplos de firma disponibles en el árbol de código fuente de la documentación de Java. El repositorio incluye ejemplos de firma de PDF basados en certificado con credenciales PFX o PKCS7, pero actualmente no incluye un ejemplo dedicado de almacén de certificados de tarjeta inteligente para Java.
---
El repositorio actual de Java no incluye un ejemplo dedicado de firma con tarjeta inteligente respaldado por código fuente bajo `facades/pdffilesignature`, pero el siguiente flujo de trabajo muestra el patrón típico de API para firmar un PDF con un certificado seleccionado de un almacén de certificados local.

## Firmar un documento PDF desde una tarjeta inteligente

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree una fachada [`PdfFileSignature`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) y enlace el documento PDF de origen.
1. Recupere el certificado local y cree lo necesario [`ExternalSignature`](https://reference.aspose.com/pdf/java/com.aspose.pdf/externalsignature/).
1. Configure la apariencia visual de la firma y el objetivo [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).
1. Aplique la firma al documento PDF a través de [`PdfFileSignature`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).
1. Guarde el documento PDF actualizado.
1. Vincule el documento cargado a la fachada [`PdfFileSignature`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) con `bindPdf(...)`.
1. Recupere el certificado local que representa la credencial de tarjeta inteligente llamando `getLocalCertificate()`.
1. Compruebe si se encontró un certificado. Si no, guarda el archivo de salida sin cambios y deténgase el flujo de trabajo.
1. Cree un [`ExternalSignature`](https://reference.aspose.com/pdf/java/com.aspose.pdf/externalsignature/) a partir del certificado seleccionado.
1. Establezca la imagen de apariencia de la firma visual con `setSignatureAppearance(...)`.
1. Llame `sign(...)` con la página de destino, razón, contacto, ubicación, bandera de visibilidad, firma [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/), y objeto de firma externo.
1. Guarde el PDF firmado en la ruta de salida.

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
