---
title: Cifrar y descifrar archivos PDF en Java
linktitle: Cifrar y descifrar archivo PDF
type: docs
weight: 70
url: /es/java/set-privileges-encrypt-and-decrypt-pdf-file/
description: Aprenda cómo establecer privilegios PDF, cifrar archivos, descifrar PDFs protegidos y cambiar contraseñas en Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Establezca permisos PDF y administre el cifrado en Java
Abstract: Este artículo explica cómo asegurar archivos PDF usando Aspose.PDF for Java. Cubre la encriptación de documentos con contraseñas de usuario y propietario, la aplicación de restricciones de permisos, el descifrado de archivos, el cambio de contraseñas y la configuración de privilegios con o sin métodos seguros contra excepciones.
---
Aspose.PDF for Java expone operaciones de seguridad de PDF a través de la fachada `PdfFileSecurity`.

## Cifrar un PDF con contraseñas de usuario y propietario

1. Cree y enlace la fachada [`PdfFileSecurity`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) al documento PDF original.
1. Configure las propiedades [`DocumentPrivilege`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) y [`KeySize`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/keysize/) requeridas por el ejemplo.
1. Guarde el documento PDF actualizado a través de [`PdfFileSecurity`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).

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

`encryptPdfWithEncryptionAlgorithm` usos `KeySize.x256` junto con `Algorithm.AES` para aplicar configuraciones de cifrado más fuertes.

## Descifrar un PDF protegido

1. Cree y enlace la fachada [`PdfFileSecurity`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) al documento PDF original.
1. Descifre el documento protegido con la contraseña de propietario.
1. Guarde el documento PDF actualizado a través de [`PdfFileSecurity`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).

```java
public static void decryptPdfWithOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.decryptFile("owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}
```

El conjunto de ejemplos también incluye `tryDecryptPdfWithoutException`, lo que devuelve `false` en lugar de lanzar una excepción cuando falla la descifrado.

## Cambiar contraseñas y restablecer la seguridad

El `PdfFileSecurityExamples` clase demuestra:

- `changeUserAndOwnerPassword` para reemplazar ambas contraseñas.
- `changePasswordAndResetSecurity` para cambiar contraseñas y volver a aplicar privilegios en un solo paso.
- `tryChangePasswordWithoutException` para un flujo de cambio de contraseña que no lanza excepciones.

## Establecer privilegios de documento

Para restringir acciones como imprimir y copiar:

1. Cree y enlace la fachada [`PdfFileSecurity`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) al documento PDF original.
1. Establezca lo requerido [`DocumentPrivilege`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) opciones de permisos o cifrado.
1. Establezca las propiedades requeridas por el ejemplo.
1. Guarde el documento PDF actualizado a través de [`PdfFileSecurity`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).

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
