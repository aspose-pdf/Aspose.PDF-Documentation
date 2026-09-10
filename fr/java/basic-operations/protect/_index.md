---
title: Protéger les fichiers PDF en Java
linktitle: Crypter et décrypter un fichier PDF
type: docs
weight: 70
url: /java/protect-pdf-file/
description: Découvrez comment crypter des fichiers PDF, déchiffrer des documents protégés, modifier les mots de passe et inspecter la protection par mot de passe en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Définir les autorisations PDF et gérer le cryptage en Java
Abstract: Cet article explique comment protéger les fichiers PDF en Java à l'aide d'Aspose.PDF. Il couvre l'application des mots de passe utilisateur et propriétaire, la définition des privilèges des documents, le cryptage et le déchiffrement des fichiers PDF, la modification des mots de passe et la vérification des mots de passe des candidats pour les documents cryptés.
---
Aspose.PDF pour Java fournit plusieurs API pour sécuriser les fichiers PDF avec des mots de passe et des autorisations.


## 
Protéger les documents PDF en Java



Les exemples dans `ProtectDocumentExamples.java` montrent comment :


1. 
Appliquez le cryptage à un [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) avec les mots de passe utilisateur et propriétaire.

1. 
Restreindre les autorisations avec [DocumentPrivilege] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/).
1. Choisissez un [CryptoAlgorithm] (https://reference.aspose.com/pdf/java/com.aspose.pdf/cryptoalgorithm/) pour le [Document] protégé (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Décryptez un [Document] protégé (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Modifiez les mots de passe existants sur le [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Testez les mots de passe des candidats avec [PdfFileInfo] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffileinfo/) et [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).


## 
Chiffrer un PDF avec des privilèges restreints

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

## Chiffrer un fichier PDF


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
Décrypter un PDF protégé


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
Changer les mots de passe


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
Déterminez le mot de passe correct dans une liste

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
