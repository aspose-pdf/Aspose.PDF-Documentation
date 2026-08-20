---
title: Cifrar archivo PDF
linktitle: Cifrar archivo PDF
type: docs
weight: 30
url: /java/encrypt-pdf-file/
description: Aprenda a cifrar un PDF y configurar permisos en Java con la fachada PdfFileSecurity.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cifre archivos PDF y defina permisos de usuario en Java
Abstract: Aprenda a cifrar un PDF con Aspose.PDF para Java. El conjunto de ejemplos de Java cubre el cifrado basado en contraseñas con privilegios restringidos, el cifrado centrado en permisos y el cifrado basado en AES con un tamaño de clave de 256 bits.
---
## Cifrar archivo PDF



Utilice `PdfFileSecurity` cuando necesite proteger un PDF con contraseñas y reglas de privilegios.


### 
Pasos


1. 
Cree una instancia `PdfFileSecurity`.

2. 
Vincule el PDF de origen con `bindPdf`.
3. Cree un objeto `DocumentPrivilege` que coincida con las acciones permitidas.

4. 
Llame a la sobrecarga `encryptFile` adecuada para el tamaño de clave y el algoritmo que necesita.

5. 
Guarde el archivo protegido y cierre el objeto.


### 
Ejemplos de Java

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
