---
title: Proteja arquivos PDF em Java
linktitle: Criptografar e descriptografar arquivo PDF
type: docs
weight: 70
url: /java/protect-pdf-file/
description: Aprenda como criptografar arquivos PDF, descriptografar documentos protegidos, alterar senhas e inspecionar a proteção por senha em Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Defina permissões de PDF e gerencie criptografia em Java
Abstract: Este artigo explica como proteger arquivos PDF em Java usando Aspose.PDF. Abrange a aplicação de senhas de usuário e proprietário, definição de privilégios de documentos, criptografia e descriptografia de arquivos PDF, alteração de senhas e verificação de senhas candidatas para documentos criptografados.
---
Aspose.PDF for Java fornece várias APIs para proteger arquivos PDF com senhas e permissões.

## Proteja documentos PDF em Java

Os exemplos em `ProtectDocumentExamples.java` demonstram como:

1. Aplique criptografia a um [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) com senhas de usuário e proprietário.
1. Restrinja as permissões com [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/).
1. Escolha um [CryptoAlgorithm](https://reference.aspose.com/pdf/java/com.aspose.pdf/cryptoalgorithm/) para o [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) protegido.
1. Descriptografe um [documento] protegido (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Altere as senhas existentes no [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Teste as senhas dos candidatos com [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffileinfo/) e [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

## Criptografe um PDF com privilégios restritos

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

## Determine a senha correta em uma lista

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
