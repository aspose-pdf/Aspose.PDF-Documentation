---
title: Proteger arquivos PDF em Java
linktitle: Criptografar e descriptografar arquivo PDF
type: docs
weight: 70
url: /pt/java/protect-pdf-file/
description: Aprenda como criptografar arquivos PDF, descriptografar documentos protegidos, alterar senhas e verificar a proteção por senha em Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Definir permissões de PDF e gerenciar criptografia em Java
Abstract: Este artigo explica como proteger arquivos PDF em Java usando Aspose.PDF. Ele aborda a aplicação de senhas de usuário e proprietário, a definição de privilégios de documento, a criptografia e descriptografia de arquivos PDF, a alteração de senhas e a verificação de senhas candidatas para documentos criptografados.
---
Aspose.PDF for Java fornece várias APIs para proteger arquivos PDF com senhas e permissões.

## Proteger documentos PDF em Java

Os exemplos em `ProtectDocumentExamples.java` demonstrar como:

1. Aplicar criptografia a um [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) com senhas de usuário e proprietário.
1. Restringir permissões com [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/).
1. Escolha um [CryptoAlgorithm](https://reference.aspose.com/pdf/java/com.aspose.pdf/cryptoalgorithm/) para o protegido [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Descriptografar um protegido [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Alterar senhas existentes no [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Testar senhas candidatas com [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffileinfo/) e [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

## Criptografar um PDF com privilégios restritos

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

## Criptografar um arquivo PDF

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

## Descriptografar um PDF protegido

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

## Alterar senhas

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

## Determine a senha correta a partir de uma lista

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
