---
title: Gestion des signatures
linktitle: Gestion des signatures
type: docs
weight: 80
url: /java/signature-management/
description: Découvrez comment supprimer une signature PDF existante en Java avec la façade PdfFileSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Supprimer les signatures PDF en Java
Abstract: Découvrez comment supprimer une signature d'un PDF signé avec Aspose.PDF pour Java. L'ensemble d'exemples Java actuel couvre la suppression d'une signature existante par son nom et l'enregistrement du document mis à jour. Il n'inclut pas d'échantillon distinct pour nettoyer le champ de signature associé.
---
## Supprimer une signature



Utilisez ce flux de travail lorsqu'une signature numérique existante doit être supprimée du document.


### 
Étapes


1. 
Créez une instance `PdfFileSignature` et liez le PDF signé.

2. 
Lisez la collection de signatures et sélectionnez un nom de signature.
3. Appelez `removeSignature` avec ce nom.

4. 
Enregistrez le fichier mis à jour et fermez l'objet façade.


### 
Exemple Java


```java
public static void removeSignature(Path inputFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        pdfSignature.removeSignature(signatureName);
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```


L'ensemble d'exemples Java actuel n'inclut pas de méthode distincte pour supprimer le champ de signature associé après la suppression de la signature.
