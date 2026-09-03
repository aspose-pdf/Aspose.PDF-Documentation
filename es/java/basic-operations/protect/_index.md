---
title: Proteger archivos PDF en Java
linktitle: Cifrar y descifrar archivo PDF
type: docs
weight: 70
url: /es/java/protect-pdf-file/
description: Aprende a cifrar archivos PDF, descifrar documentos protegidos, cambiar contraseñas y examinar la protección con contraseña en Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Establecer permisos de PDF y gestionar el cifrado en Java
Abstract: Este artículo explica cómo proteger archivos PDF en Java usando Aspose.PDF. Cubre la aplicación de contraseñas de usuario y propietario, la configuración de privilegios del documento, el cifrado y descifrado de archivos PDF, el cambio de contraseñas y la verificación de contraseñas candidatas para documentos cifrados.
---
Aspose.PDF for Java proporciona varias API para asegurar archivos PDF con contraseñas y permisos.

## Proteger documentos PDF en Java

Los ejemplos en `ProtectDocumentExamples.java` demostrar cómo:

1. Aplicar cifrado a un [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) con contraseñas de usuario y propietario.
1. Restringir permisos con [Privilegio de documento](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/).
1. Elige un [AlgoritmoCripto](https://reference.aspose.com/pdf/java/com.aspose.pdf/cryptoalgorithm/) para los protegidos [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Desencriptar un protegido [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cambiar contraseñas existentes en el [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Probar contraseñas candidatas con [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffileinfo/) y [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

## Cifrar un PDF con privilegios restringidos

```java
public static void encryptPassword(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    try {
        DocumentPrivilege documentPrivilege = DocumentPrivilege.getForbidAll();
        documentPrivilege.setAllowScreenReaders(true);

        document.encrypt(
                USER_PASSWORD,
                OWNER_PASSWORD,
                documentPrivilege,
                CryptoAlgorithm.AESx128,
                false);
        document.save(outputFile.toString());
    } finally {
        document.close();
    }
}
```

## Cifrar un archivo PDF

```java
public static void encryptPdfFile(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    try {
        document.encrypt(
                USER_PASSWORD,
                OWNER_PASSWORD,
                DocumentPrivilege.getAllowAll(),
                CryptoAlgorithm.RC4x128,
                false);
        document.save(outputFile.toString());
    } finally {
        document.close();
    }
}
```

## Descifrar un PDF protegido

```java
public static void decryptPdfFile(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString(), USER_PASSWORD);
    try {
        document.decrypt();
        document.save(outputFile.toString());
    } finally {
        document.close();
    }
}
```

## Cambiar contraseñas

```java
public static void changePassword(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString(), OWNER_PASSWORD);
    try {
        document.changePasswords(OWNER_PASSWORD, "newuser", "newowner");
        document.save(outputFile.toString());
    } finally {
        document.close();
    }
}
```

## Determine la contraseña correcta de una lista

```java
public static void determineCorrectPasswordFromList(Path inputFile) {
    try (PdfFileInfo info = new PdfFileInfo(inputFile.toString())) {
        System.out.println("File is password protected: " + info.isEncrypted());
    }
    String[] passwords = {"test", "test1", "test2", "test3", USER_PASSWORD};
    for (String password : passwords) {
        try {
            Document document = new Document(inputFile.toString(), password);
            try {
                int pageCount = document.getPages().size();
                if (pageCount > 0) {
                    System.out.println("Password '" + password + "' is correct. Pages: " + pageCount);
                }
            } finally {
                document.close();
            }
        } catch (InvalidPasswordException ex) {
            System.out.println("Wrong password: " + password);
        }
    }
}
```
