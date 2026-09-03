---
title: Cifrar archivo PDF
linktitle: Cifrar archivo PDF
type: docs
weight: 30
url: /es/java/encrypt-pdf-file/
description: Aprenda cómo cifrar un PDF y configurar permisos en Java con la fachada PdfFileSecurity.
lastmod: "2026-09-03"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cifre archivos PDF y defina permisos de usuario en Java
Abstract: Aprenda cómo cifrar un PDF con Aspose.PDF for Java. El conjunto de ejemplos Java cubre el cifrado basado en contraseña con privilegios restringidos, cifrado centrado en permisos y cifrado basado en AES con un tamaño de clave de 256 bits.
---
## Cifrar archivo PDF

Usar `PdfFileSecurity` cuando necesitas proteger un PDF con contraseñas y reglas de privilegios.

### Pasos

1. Crear un `PdfFileSecurity` instancia.
2. Vincular el PDF de origen con `bindPdf`.
3. Construir un `DocumentPrivilege` objeto que coincide con las acciones permitidas.
4. Llama al apropiado `encryptFile` sobrecarga para el tamaño de clave y el algoritmo que necesitas.
5. Guarda el archivo seguro y cierra el objeto.

### Ejemplos de Java

```java
public static void encryptPdfWithUserOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    fileSecurity.encryptFile("user_password", "owner_password", privilege, KeySize.x128);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void encryptPdfWithPermissions(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getAllowAll();
    privilege.setAllowPrint(false);
    privilege.setAllowCopy(false);
    fileSecurity.encryptFile("user_password", "owner_password", privilege, KeySize.x128);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void encryptPdfWithEncryptionAlgorithm(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    fileSecurity.encryptFile("user_password", "owner_password", privilege, KeySize.x256, Algorithm.AES);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}
```
