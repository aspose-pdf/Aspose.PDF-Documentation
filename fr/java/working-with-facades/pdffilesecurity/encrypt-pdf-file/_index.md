---
title: Crypter le fichier PDF
linktitle: Crypter le fichier PDF
type: docs
weight: 30
url: /java/encrypt-pdf-file/
description: Découvrez comment crypter un PDF et configurer les autorisations en Java avec la façade PdfFileSecurity.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cryptez les fichiers PDF et définissez les autorisations des utilisateurs en Java
Abstract: Découvrez comment chiffrer un PDF avec Aspose.PDF pour Java. L'ensemble d'exemples Java couvre le chiffrement basé sur un mot de passe avec des privilèges restreints, le chiffrement axé sur les autorisations et le chiffrement basé sur AES avec une taille de clé de 256 bits.
---
## Crypter le fichier PDF



Utilisez `PdfFileSecurity` lorsque vous devez protéger un PDF avec des mots de passe et des règles de privilèges.


### 
Étapes


1. 
Créez une instance `PdfFileSecurity`.

2. 
Liez le PDF source avec `bindPdf`.
3. Créez un objet `DocumentPrivilege` qui correspond aux actions autorisées.

4. 
Appelez la surcharge `encryptFile` appropriée pour la taille de clé et l'algorithme dont vous avez besoin.

5. 
Enregistrez le fichier sécurisé et fermez l'objet.


### 
Exemples Java

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
