---
title: Création d'un PDF conforme PDF/3-A et pièce jointe d'une facture ZUGFeRD en Java
linktitle: Joindre ZUGFeRD au PDF
type: docs
weight: 10
url: /java/attach-zugferd/
description: Découvrez comment joindre une facture XML ZUGFeRD à un PDF et la convertir en PDF/A-3A en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Joindre une facture XML ZUGFeRD à un document PDF avec Java
Abstract: Cet article explique comment créer un document de facture conforme PDF/A-3A à l'aide d'Aspose.PDF pour Java. Il couvre la pièce jointe de la facture XML en tant que fichier intégré, la définition du type MIME et de la relation entre les fichiers associés, la conversion du PDF en PDF/A-3A et l'enregistrement du document final prêt pour ZUGFeRD.
---
Utilisez les API `Document` et `FileSpecification` lorsque vous devez regrouper le XML d'une facture dans un PDF pour les flux de travail de style ZUGFeRD.


## 
Joindre la facture XML ZUGFeRD à un PDF


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez le [FileSpecification] (https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) pour le fichier de facture XML.

1. 
Définissez les métadonnées du fichier intégré, y compris le type MIME et [AFRelationship] (https://reference.aspose.com/pdf/java/com.aspose.pdf/afrelationship/).
1. Ajoutez le [FileSpecification] (https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) à la collection de fichiers incorporés au document.

1. 
Convertissez le document en [PdfFormat] (https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_A_3A`.

1. 
Enregistrez le [Document] PDF mis à jour (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void attachInvoiceZugferdFormat(Path inputFile, Path invoiceFile, Path outputFile) {
        try (Document document = new Document(inputFile.toString())) {
            String description = "Invoice metadata conforming to ZUGFeRD standard";
            FileSpecification fileSpecification = new FileSpecification(invoiceFile.toString(), description);

            fileSpecification.setMIMEType("text/xml");
            fileSpecification.setAFRelationship(AFRelationship.Alternative);

            document.getEmbeddedFiles().add("factur", fileSpecification);

            String outputFileName = outputFile.toString();
            String logPath = outputFileName.replace(".pdf", "_log.xml");
            document.convert(logPath, PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);
            document.save(outputFile.toString());
        }
        System.out.println("ZUGFeRD invoice attached to " + outputFile);
    }
```
