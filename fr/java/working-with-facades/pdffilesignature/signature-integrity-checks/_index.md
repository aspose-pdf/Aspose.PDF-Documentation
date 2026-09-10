---
title: Vérifications de l'intégrité des signatures
linktitle: Vérifications de l'intégrité des signatures
type: docs
weight: 70
url: /java/signature-integrity-checks/
description: Découvrez comment valider la couverture et l'intégrité des signatures en Java avec la façade PdfFileSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Valider la couverture et l'intégrité de la signature PDF en Java
Abstract: Découvrez comment inspecter l'intégrité des signatures avec Aspose.PDF pour Java. L'ensemble d'exemples Java actuel utilise `verifySignature` pour valider la signature sélectionnée et `coversWholeDocument` pour déterminer si la signature protège l'intégralité du PDF.
---
## Vérifier l'intégrité de la signature



Cet article correspond au même flux de travail de vérification exposé par `PdfFileSignatureExamples.java`.


### 
Étapes


1. 
Liez le PDF signé avec `PdfFileSignature`.

2. 
Sélectionnez un nom de signature dans le document.
3. Appelez `verifySignature` pour valider le contenu de la signature.

4. 
Appelez `coversWholeDocument` pour confirmer la couverture à l'échelle du document.

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
