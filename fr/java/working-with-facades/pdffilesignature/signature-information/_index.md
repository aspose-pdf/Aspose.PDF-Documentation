---
title: Informations sur la signature
linktitle: Informations sur la signature
type: docs
weight: 60
url: /java/signature-information/
description: Découvrez comment lire les noms de signature et les détails des signataires à partir de PDF signés en Java avec PdfFileSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Lire les détails de la signature des documents PDF en Java
Abstract: Découvrez comment inspecter les métadonnées de signature avec Aspose.PDF pour Java. L'exemple Java lit le premier nom de signature disponible, puis récupère le signataire, la date, le motif et l'emplacement du PDF signé.
---
## Obtenir des informations sur la signature



Utilisez ce flux de travail lorsque vous devez vérifier qui a signé un PDF et quelles métadonnées de signature ont été stockées.


### 
Étapes


1. 
Créez une instance `PdfFileSignature` et liez le PDF signé.

2. 
Lisez la collection de signatures et sélectionnez un nom de signature.
3. Appelez les accesseurs aux informations de signature pour connaître le nom du signataire, la date, la raison et le lieu.

4. 
Fermez l'objet de façade lorsque vous avez terminé.


### 
Exemple Java

```java
public static void getSignatureInformation(Path inputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        System.out.println("Signature Names: " + pdfSignature.getSignNames());
        System.out.println("Signer: " + pdfSignature.getSignerName(signatureName));
        System.out.println("Date: " + pdfSignature.getDateTime(signatureName));
        System.out.println("Reason: " + pdfSignature.getReason(signatureName));
        System.out.println("Location: " + pdfSignature.getLocation(signatureName));
    } finally {
        pdfSignature.close();
    }
}
```
