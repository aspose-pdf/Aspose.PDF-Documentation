---
title: Certification PDF
linktitle: Certification PDF
type: docs
weight: 30
url: /java/pdf-certification/
description: Découvrez comment certifier des documents PDF en Java avec PdfFileSignature et DocMDPSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Certifier les documents PDF avec les autorisations DocMDP en Java
Abstract: Découvrez comment certifier des documents PDF avec Aspose.PDF pour Java. L'exemple Java utilise PdfFileSignature avec DocMDPSignature et DocMDPAccessPermissions pour certifier un document pour le remplissage et la signature de formulaires tout en limitant d'autres types de modifications.
---
## Certifier les documents PDF



Utilisez la certification lorsque le document doit rester fiable tout en permettant une classe définie de modifications après la signature.


### 
Étapes


1. 
Créez une instance `PdfFileSignature` et liez le PDF source.

2. 
Créez un objet de signature `PKCS7` avec le certificat et le mot de passe du certificat.
3. Enveloppez cette signature dans un `DocMDPSignature` avec la valeur `DocMDPAccessPermissions` requise.

4. 
Appelez `certify` avec la page cible, les métadonnées de signature, le rectangle visible et la signature MDP.

5. 
Enregistrez le PDF certifié et fermez l'objet façade.


### 
Exemple Java

```java
public static void certifyPdfWithMdpSignature(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        DocMDPSignature signature = new DocMDPSignature(
                createPkcs7(certificateFile, "Certified for form filling and signing"),
                DocMDPAccessPermissions.FillingInForms);
        pdfSignature.certify(1, "Certified for form filling and signing", "security@example.com", "New York, USA", true, signatureRectangle(), signature);
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```
