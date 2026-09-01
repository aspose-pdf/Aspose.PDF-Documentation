---
title: Signer des documents PDF à partir d'une carte à puce en Java
linktitle: Signature PDF avec carte à puce
type: docs
weight: 30
url: /java/sign-pdf-document-from-smart-card/
description: Consultez l'exemple Java actuel de signature de PDF basée sur un certificat dans Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Couverture de la signature PDF basée sur un certificat dans l'ensemble d'exemples Java actuel
Abstract: Cette page décrit la portée actuelle des exemples de signature disponibles dans l'arborescence des sources de la documentation Java. Le référentiel comprend des exemples de signature PDF basés sur des certificats avec des informations d'identification PFX ou PKCS7, mais il n'inclut pas actuellement d'exemple de magasin de certificats de carte à puce dédié pour Java.
---
Le référentiel Java actuel n'inclut pas d'exemple de signature de carte à puce dédié basé sur la source sous `facades/pdffilesignature`, mais le flux de travail suivant montre le modèle d'API typique pour signer un PDF avec un certificat sélectionné dans un magasin de certificats local.


## 
Signer un document PDF à partir d'une carte à puce


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez une façade [PdfFileSignature] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) et liez le document PDF source.

1. 
Récupérez le certificat local et créez la [ExternalSignature] (https://reference.aspose.com/pdf/java/com.aspose.pdf/externalsignature/) requise.
1. Configurez l'apparence de la signature visuelle et la cible [Rectangle] (https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).

1. 
Appliquez la signature au document PDF via [PdfFileSignature] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).

1. 
Enregistrez le document PDF mis à jour.

1. 
Liez le document chargé à la façade [PdfFileSignature] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) avec `bindPdf(...)`.

1. 
Récupérez le certificat local qui représente les informations d'identification de la carte à puce en appelant `getLocalCertificate()`.
1. Vérifiez si un certificat a été trouvé. Sinon, enregistrez le fichier de sortie inchangé et arrêtez le flux de travail.

1. 
Créez une [ExternalSignature] (https://reference.aspose.com/pdf/java/com.aspose.pdf/externalsignature/) à partir du certificat sélectionné.

1. 
Définissez l'image d'apparence de la signature visuelle avec `setSignatureAppearance(...)`.

1. 
Appelez `sign(...)` avec la page cible, le motif, le contact, l'emplacement, l'indicateur de visibilité, la signature [Rectangle] (https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) et l'objet de signature externe.

1. 
Enregistrez le PDF signé dans le chemin de sortie.

```java
public static void signWithSmartCard(Path inputFile, Path outputFile, Path pngFile) {
    try (Document document = new Document(inputFile.toString());
            PdfFileSignature pdfSignature = new PdfFileSignature()) {
        pdfSignature.bindPdf(document);
        X509Certificate2 selectedCertificate = getLocalCertificate();
        if (selectedCertificate == null) {
            System.out.println("Local certificate was not found.");
            document.save(outputFile.toString());
            return;
        }

        ExternalSignature externalSignature = new ExternalSignature(selectedCertificate, null);
        pdfSignature.setSignatureAppearance(pngFile.toString());
        pdfSignature.sign(1, "Reason", "Contact", "Location", true,
                new java.awt.Rectangle(100, 100, 200, 200), externalSignature);
        pdfSignature.save(outputFile.toString());
    }
}
```
