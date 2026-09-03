---
title: Descifrar archivo PDF
linktitle: Descifrar archivo PDF
type: docs
weight: 20
url: /java/decrypt-pdf-file/
description: Aprenda a descifrar un PDF en Java con la fachada PdfFileSecurity.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Elimine las restricciones de seguridad de PDF con Java
Abstract: Aprenda a descifrar un PDF con Aspose.PDF para Java. El conjunto de ejemplos de Java incluye descifrado directo de la contraseña del propietario y un flujo de trabajo de descifrado de estilo de prueba que le permite controlar los errores sin generar una excepción.
---
## Descifrar archivo PDF



Utilice este flujo de trabajo cuando tenga la contraseña del propietario y necesite eliminar la seguridad de un PDF.


### 
Pasos


1. Cree una instancia `PdfFileSecurity`.

2. Vincula el PDF cifrado con `bindPdf`.
3. Llame a `decryptFile` o `tryDecryptFile` con la contraseña del propietario.

4. Guarde el resultado si el descifrado se realiza correctamente.

5. Cierre el objeto de seguridad.


### 
Ejemplos de Java

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
