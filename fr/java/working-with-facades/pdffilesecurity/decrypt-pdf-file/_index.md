---
title: Décrypter le fichier PDF
linktitle: Décrypter le fichier PDF
type: docs
weight: 20
url: /java/decrypt-pdf-file/
description: Apprenez à décrypter un PDF en Java avec la façade PdfFileSecurity.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Supprimer les restrictions de sécurité PDF avec Java
Abstract: Apprenez à décrypter un PDF avec Aspose.PDF pour Java. L'ensemble d'exemples Java inclut le déchiffrement direct du mot de passe du propriétaire et un workflow de décryptage de type try qui vous permet de gérer les échecs sans déclencher d'exception.
---
## Décrypter le fichier PDF



Utilisez ce flux de travail lorsque vous disposez du mot de passe du propriétaire et que vous devez supprimer la sécurité d'un PDF.


### 
Étapes


1. 
Créez une instance `PdfFileSecurity`.

2. 
Liez le PDF crypté avec `bindPdf`.
3. Appelez `decryptFile` ou `tryDecryptFile` avec le mot de passe du propriétaire.

4. 
Enregistrez la sortie si le décryptage réussit.

5. 
Fermez l'objet de sécurité.


### 
Exemples Java

```java
public static void decryptPdfWithOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.decryptFile("owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void tryDecryptPdfWithoutException(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    if (fileSecurity.tryDecryptFile("owner_password")) {
        fileSecurity.save(outputFile.toString());
    } else {
        System.out.println("Decryption failed. Check password or document security.");
    }
    fileSecurity.close();
}
```
