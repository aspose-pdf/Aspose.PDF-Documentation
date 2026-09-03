---
title: Cifrar y descifrar archivos PDF en Java
linktitle: Cifrar y descifrar archivos PDF
type: docs
weight: 70
url: /java/set-privileges-encrypt-and-decrypt-pdf-file/
description: Aprenda a configurar privilegios de PDF, cifrar archivos, descifrar archivos PDF protegidos y cambiar contraseñas en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Establezca permisos de PDF y administre el cifrado en Java
Abstract: Este artículo explica cómo proteger archivos PDF usando Aspose.PDF para Java. Cubre el cifrado de documentos con contraseñas de usuario y propietario, la aplicación de restricciones de permisos, el descifrado de archivos, el cambio de contraseñas y la configuración de privilegios con o sin métodos seguros para excepciones.
---
Aspose.PDF para Java expone las operaciones de seguridad de PDF a través de la fachada `PdfFileSecurity`.


## 
Cifrar un PDF con contraseñas de usuario y propietario


1. Cree y vincule la fachada [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) al documento PDF de origen.

1. Configure las propiedades [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) y [KeySize](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/keysize/) requeridas por el ejemplo.

1. Guarde el documento PDF actualizado a través de [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).

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
```

## Cifrar un PDF con un algoritmo específico



`encryptPdfWithEncryptionAlgorithm` usa `KeySize.x256` junto con `Algorithm.AES` para aplicar configuraciones de cifrado más seguras.


## 
Descifrar un PDF protegido


1. Cree y vincule la fachada [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) al documento PDF de origen.

1. Descifre el documento protegido con la contraseña del propietario.
1. Guarde el documento PDF actualizado a través de [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).


```java
public static void decryptPdfWithOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.decryptFile("owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}
```


El conjunto de ejemplo también incluye `tryDecryptPdfWithoutException`, que devuelve `false` en lugar de arrojarlo cuando falla el descifrado.


## 
Cambiar contraseñas y restablecer la seguridad



La clase `PdfFileSecurityExamples` demuestra:


- `changeUserAndOwnerPassword` para reemplazar ambas contraseñas.
- `changePasswordAndResetSecurity` para cambiar contraseñas y volver a aplicar privilegios en un solo paso.

- `tryChangePasswordWithoutException` para un flujo de cambio de contraseña sin retorno.


## 
Establecer privilegios de documentos



Para restringir acciones como imprimir y copiar:


1. Cree y vincule la fachada [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) al documento PDF de origen.
1. Establezca los permisos [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) requeridos o las opciones de cifrado.

1. Establezca las propiedades requeridas por el ejemplo.

1. Guarde el documento PDF actualizado a través de [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).

```java
public static void setPdfPrivilegesWithPasswords(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    privilege.setAllowCopy(false);
    fileSecurity.setPrivilege("user_password", "owner_password", privilege);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}
```
