---
title: Extraction de signatures
linktitle: Extraction de signatures
type: docs
weight: 50
url: /java/signature-extraction/
description: Découvrez comment extraire le certificat de signature d'un PDF signé en Java avec PdfFileSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraire un certificat de signature d'un PDF en Java
Abstract: Découvrez comment extraire le certificat associé à une signature PDF à l'aide d'Aspose.PDF pour Java. L'ensemble d'exemples Java actuel inclut l'extraction de certificat vers un flux de sortie, mais il n'inclut pas d'exemple d'extraction d'image de signature distinct.
---
## Extraire le certificat de signature



Utilisez ce workflow lorsque vous devez enregistrer le certificat associé à une signature existante.


### 
Étapes


1. 
Créez une instance `PdfFileSignature` et liez le PDF signé.

2. 
Sélectionnez le nom de la signature à inspecter.
3. Appelez `extractCertificate` pour ouvrir le flux de certificat.

4. 
Copiez les octets du certificat dans un fichier de sortie.

5. 
Fermez les ressources de flux et l'objet façade.


### 
Exemple Java


```java
public static void extractSignatureCertificate(Path inputFile, Path outputFile) throws Exception {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        try (InputStream inputStream = pdfSignature.extractCertificate(signatureName);
             OutputStream outputStream = Files.newOutputStream(outputFile)) {
            inputStream.transferTo(outputStream);
        }
    } finally {
        pdfSignature.close();
    }
}
```


La classe `PdfFileSignatureExamples.java` actuelle n'inclut pas d'exemple Java dédié pour extraire une image de signature rendue.
