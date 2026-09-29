---
title: Descifrar archivo PDF
linktitle: Descifrar archivo PDF
type: docs
weight: 20
url: /es/java/decrypt-pdf-file/
description: Aprenda cómo desencriptar un PDF en Java con la fachada PdfFileSecurity.
lastmod: "2026-09-29"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar restricciones de seguridad del PDF con Java
Abstract: Aprenda cómo desencriptar un PDF con Aspose.PDF for Java. El conjunto de ejemplos de Java incluye desencriptación directa con contraseña de propietario y un flujo de trabajo de desencriptación estilo try que le permite manejar fallos sin generar una excepción.
---
## Descifrar archivo PDF

Utilice este flujo de trabajo cuando tenga la contraseña del propietario y necesite eliminar la seguridad de un PDF.

### Pasos

1. Cree una instancia de `PdfFileSecurity`.
2. Vincule el PDF cifrado con `bindPdf`.
3. Llame `decryptFile` o `tryDecryptFile` con la contraseña de propietario.
4. Guarde la salida si el descifrado tiene éxito.
5. Cierre el objeto de seguridad.

### Ejemplos de Java

```java
public static void decryptPdfWithOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.decryptFile("owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void tryDecryptPdfWithoutException(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    if (fileSecurity.tryDecryptFile("owner_password")) {
        fileSecurity.save(outputFile.toString());
    } else {
        System.out.println("Decryption failed. Check password or document security.");
    }
    fileSecurity.close();
}
```
