---
title: Vérification des signatures
linktitle: Vérification des signatures
type: docs
weight: 90
url: /java/signature-verification/
description: Découvrez comment vérifier les signatures PDF en Java avec la façade PdfFileSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Vérifier les signatures PDF en Java
Abstract: Découvrez comment vérifier une signature PDF avec Aspose.PDF pour Java. L'exemple Java sélectionne la première signature disponible, valide la signature et vérifie si elle couvre l'intégralité du document.
---
## Vérifier la signature PDF



Utilisez ce flux de travail lorsque vous avez besoin d’une validation rapide sur un PDF signé existant.


### 
Étapes


1. 
Créez une instance `PdfFileSignature` et liez le PDF signé.

2. 
Sélectionnez le nom de la signature que vous souhaitez inspecter.
3. Appelez `verifySignature` pour valider la signature.

4. 
Appelez `coversWholeDocument` pour vérifier la couverture.

5. 
Fermez l'objet façade.


### 
Exemple Java

```java
public static void verifyPdfSignature(Path inputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        System.out.println("Signature '" + signatureName + "' is valid: " + pdfSignature.verifySignature(signatureName));
        System.out.println("Signature covers whole document: " + pdfSignature.coversWholeDocument(signatureName));
    } finally {
        pdfSignature.close();
    }
}
```
