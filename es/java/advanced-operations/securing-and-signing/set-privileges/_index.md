---
title: Cifrar y descifrar archivos PDF en Java
linktitle: Cifrar y descifrar archivo PDF
type: docs
weight: 70
url: /es/java/set-privileges-encrypt-and-decrypt-pdf-file/
description: Aprenda cómo establecer privilegios de PDF, cifrar archivos, descifrar PDFs protegidos y cambiar contraseñas en Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Establezca permisos de PDF y administre el cifrado en Java
Abstract: Este artículo explica cómo proteger archivos PDF usando Aspose.PDF for Java. Cubre el cifrado de documentos con contraseñas de usuario y propietario, la aplicación de restricciones de permisos, la descifrado de archivos, el cambio de contraseñas y la configuración de privilegios con o sin métodos a prueba de excepciones.
---
Aspose.PDF for Java expone operaciones de seguridad de PDF a través del `PdfFileSecurity` fachada.

## Cifrar un PDF con contraseñas de usuario y propietario

1. Crear y vincular el [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) fachada al documento PDF de origen.
1. Configura el [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) y [KeySize](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/keysize/) propiedades requeridas por el ejemplo.
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

`encryptPdfWithEncryptionAlgorithm` usa `KeySize.x256` junto con `Algorithm.AES` para aplicar configuraciones de cifrado más fuertes.

## Descifrar un PDF protegido

1. Crear y vincular el [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) fachada al documento PDF de origen.
1. Desencripte el documento protegido con la contraseña del propietario.
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

El conjunto de ejemplos también incluye `tryDecryptPdfWithoutException`, lo que devuelve `false` en lugar de lanzar una excepción cuando falla el descifrado.

## Cambiar contraseñas y restablecer la seguridad

El `PdfFileSecurityExamples` clase demuestra:

- `changeUserAndOwnerPassword` para reemplazar ambas contraseñas.
- `changePasswordAndResetSecurity` para cambiar contraseñas y volver a aplicar privilegios en un solo paso.
- `tryChangePasswordWithoutException` para un flujo de cambio de contraseña que no genera excepciones.

## Establecer privilegios del documento

Para restringir acciones como imprimir y copiar:

1. Crear y vincular el [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) fachada al documento PDF de origen.
1. Establezca lo requerido [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) opciones de permisos o cifrado.
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
