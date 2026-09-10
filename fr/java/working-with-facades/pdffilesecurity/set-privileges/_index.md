---
title: Définir des privilèges sur un fichier PDF existant
linktitle: Définir des privilèges sur un fichier PDF existant
type: docs
weight: 40
url: /java/set-privileges/
description: Découvrez comment définir les privilèges PDF en Java avec la façade PdfFileSecurity.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gérer les autorisations PDF et les contrôles d'accès en Java
Abstract: Découvrez comment contrôler les autorisations PDF avec Aspose.PDF pour Java. L'ensemble d'exemples Java couvre l'application de privilèges sans mots de passe, l'application de privilèges avec des mots de passe utilisateur et propriétaire, ainsi qu'un workflow de mise à jour des privilèges de style essai qui renvoie un indicateur de réussite.
---
## Définir des privilèges sur un fichier PDF existant



Utilisez ce flux de travail lorsque vous devez modifier ce que les utilisateurs peuvent faire avec un PDF existant.


### 
Étapes


1. 
Créez une instance `PdfFileSecurity`.

2. 
Liez le PDF source avec `bindPdf`.
3. Créez un objet `DocumentPrivilege` et configurez les actions autorisées.

4. 
Appelez la surcharge `setPrivilege` ou `trySetPrivilege` appropriée.

5. 
Enregistrez le résultat si la mise à jour réussit, puis fermez l'objet.


### 
Exemples Java

```java
public static void setPdfPrivilegesWithoutPasswords(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    fileSecurity.setPrivilege(privilege);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

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

public static void trySetPdfPrivilegesWithoutException(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    if (fileSecurity.trySetPrivilege("user_password", "owner_password", privilege)) {
        fileSecurity.save(outputFile.toString());
    } else {
        System.out.println("Setting privileges failed. Check passwords or document state.");
    }
    fileSecurity.close();
}
```
