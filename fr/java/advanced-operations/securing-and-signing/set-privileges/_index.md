---
title: Crypter et décrypter des fichiers PDF en Java
linktitle: Crypter et décrypter un fichier PDF
type: docs
weight: 70
url: /java/set-privileges-encrypt-and-decrypt-pdf-file/
description: Découvrez comment définir les privilèges PDF, crypter des fichiers, décrypter des PDF protégés et modifier les mots de passe en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Définir les autorisations PDF et gérer le cryptage en Java
Abstract: Cet article explique comment sécuriser les fichiers PDF à l'aide d'Aspose.PDF pour Java. Il couvre le chiffrement des documents avec les mots de passe utilisateur et propriétaire, l'application de restrictions d'autorisation, le déchiffrement des fichiers, la modification des mots de passe et la définition des privilèges avec ou sans méthodes sécurisées pour les exceptions.
---
Aspose.PDF pour Java expose les opérations de sécurité PDF via la façade `PdfFileSecurity`.


## 
Crypter un PDF avec les mots de passe utilisateur et propriétaire


1. 
Créez et liez la façade [PdfFileSecurity] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) au document PDF source.

1. 
Configurez les propriétés [DocumentPrivilege] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) et [KeySize] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/keysize/) requises par l'exemple.

1. 
Enregistrez le document PDF mis à jour via [PdfFileSecurity] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).

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

## Chiffrer un PDF avec un algorithme spécifique



`encryptPdfWithEncryptionAlgorithm` utilise `KeySize.x256` avec `Algorithm.AES` pour appliquer des paramètres de cryptage plus forts.


## 
Décrypter un PDF protégé


1. 
Créez et liez la façade [PdfFileSecurity] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) au document PDF source.

1. 
Décryptez le document protégé avec le mot de passe du propriétaire.
1. Enregistrez le document PDF mis à jour via [PdfFileSecurity] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).


```java
public static void decryptPdfWithOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.decryptFile("owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}
```


L'ensemble d'exemples inclut également `tryDecryptPdfWithoutException`, qui renvoie `false` au lieu d'être lancé en cas d'échec du décryptage.


## 
Changer les mots de passe et réinitialiser la sécurité



La classe `PdfFileSecurityExamples` démontre :


- 
`changeUserAndOwnerPassword` pour remplacer les deux mots de passe.
- `changePasswordAndResetSecurity` pour modifier les mots de passe et réappliquer les privilèges en une seule étape.

- 
`tryChangePasswordWithoutException` pour un flux de changement de mot de passe sans lancement.


## 
Définir les privilèges des documents



Pour restreindre des actions telles que l'impression et la copie :


1. 
Créez et liez la façade [PdfFileSecurity] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) au document PDF source.
1. Définissez les autorisations [DocumentPrivilege] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) requises ou les options de cryptage.

1. 
Définissez les propriétés requises par l'exemple.

1. 
Enregistrez le document PDF mis à jour via [PdfFileSecurity] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).

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
