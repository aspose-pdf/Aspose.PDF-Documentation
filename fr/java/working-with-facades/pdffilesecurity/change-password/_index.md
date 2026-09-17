---
title: Changer le mot de passe du fichier PDF
linktitle: Changer le mot de passe du fichier PDF
type: docs
weight: 10
url: /java/change-password/
description: Découvrez comment modifier les mots de passe PDF en Java avec la façade PdfFileSecurity.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mettre à jour les mots de passe utilisateur et propriétaire PDF en Java
Abstract: Découvrez comment modifier les mots de passe PDF avec Aspose.PDF pour Java. L'ensemble d'exemples Java couvre la modification directe des mots de passe utilisateur et propriétaire, la modification des mots de passe tout en réinitialisant les paramètres de sécurité, ainsi qu'un workflow de modification de mot de passe de style essai qui renvoie un indicateur de réussite.
---
## Changer le mot de passe du fichier PDF



Utilisez `PdfFileSecurity` lorsque vous devez alterner les informations d'identification sur un PDF déjà sécurisé.


### 
Étapes


1. 
Créez une instance `PdfFileSecurity`.

2. 
Liez le PDF sécurisé avec `bindPdf`.
3. Appelez la surcharge `changePassword` appropriée, selon que vous souhaitez également réinitialiser les privilèges et la taille de la clé.

4. 
Enregistrez le fichier mis à jour et fermez l'objet de sécurité.


### 
Exemples Java

```java
public static void changeUserAndOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.changePassword("owner_password", "new_user_password", "new_owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void changePasswordAndResetSecurity(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    fileSecurity.changePassword("owner_password", "new_user_password", "new_owner_password", privilege, KeySize.x128);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void tryChangePasswordWithoutException(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    if (fileSecurity.tryChangePassword("owner_password", "new_user_password", "new_owner_password")) {
        fileSecurity.save(outputFile.toString());
    } else {
        System.out.println("Password change failed. Check owner password or document security.");
    }
    fileSecurity.close();
}
```
