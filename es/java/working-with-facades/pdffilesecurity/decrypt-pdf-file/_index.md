---
title: Descifrar archivo PDF
linktitle: Descifrar archivo PDF
type: docs
weight: 20
url: /es/java/decrypt-pdf-file/
description: Aprenda cómo descifrar un PDF en Java con la fachada PdfFileSecurity.
lastmod: "2026-09-03"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar restricciones de seguridad de PDF con Java
Abstract: Aprenda cómo descifrar un PDF con Aspose.PDF for Java. El conjunto de ejemplos en Java incluye descifrado directo mediante la contraseña del propietario y un flujo de trabajo de descifrado estilo try que le permite manejar fallos sin generar una excepción.
---
## Descifrar archivo PDF

Utilice este flujo de trabajo cuando tenga la contraseña del propietario y necesite eliminar la seguridad de un PDF.

### Pasos

1. Crear un `PdfFileSecurity` instancia.
2. Vincular el PDF cifrado con `bindPdf`.
3. Llamar `decryptFile` o `tryDecryptFile` con la contraseña del propietario.
4. Guarda la salida si el descifrado tiene éxito.
5. Cierra el objeto de seguridad.

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
