---
title: Proteger archivos PDF en Java
linktitle: Cifrar y descifrar archivos PDF
type: docs
weight: 70
url: /java/protect-pdf-file/
description: Aprenda a cifrar archivos PDF, descifrar documentos protegidos, cambiar contraseñas e inspeccionar la protección con contraseña en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Establezca permisos de PDF y administre el cifrado en Java
Abstract: Este artículo explica cómo proteger archivos PDF en Java usando Aspose.PDF. Cubre la aplicación de contraseñas de usuario y propietario, la configuración de privilegios de documentos, el cifrado y descifrado de archivos PDF, el cambio de contraseñas y la verificación de contraseñas candidatas para documentos cifrados.
---
Aspose.PDF para Java proporciona varias API para proteger archivos PDF con contraseñas y permisos.


## 
Proteger documentos PDF en Java



Los ejemplos en `ProtectDocumentExamples.java` demuestran cómo:


1. 
Aplicar cifrado a un [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) con contraseñas de usuario y propietario.

1. 
Restrinja los permisos con [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/).
1. Elija un [CriptoAlgoritmo](https://reference.aspose.com/pdf/java/com.aspose.pdf/cryptoalgorithm/) para el [Documento] protegido(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Descifre un [Documento] protegido (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cambie las contraseñas existentes en el [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Pruebe las contraseñas candidatas con [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffileinfo/) y [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).


## 
Cifrar un PDF con privilegios restringidos

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

## 
Descifrar un PDF protegido


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

## 
Cambiar contraseñas


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

## 
Determine la contraseña correcta de una lista

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
