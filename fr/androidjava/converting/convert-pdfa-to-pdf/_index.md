---
title: Convertir PDF/A en PDF
linktitle: Convertir PDF/A en PDF
type: docs
weight: 350
url: /fr/androidjava/convert-pdfa-to-pdf/
lastmod: "2026-07-01"
description: Pour convertir PDF/A en PDF, vous devez supprimer les restrictions du document original. Aspose.PDF for Android via Java vous permet de résoudre ce problème facilement et simplement.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Convertir un document PDF/A en PDF signifie supprimer <abbr title="Portable Document Format Archive
">PDF/A</abbr> restriction du document original. Classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) a la méthode RemovePdfaCompliance(..) pour supprimer
les informations de conformité PDF du fichier d'entrée/source.

```java

    public void convertPDFAtoPDF() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        try {
            // Create Document object
            document = new Document(pdfaDocumentFileName);

            // Remove PDF/A compliance information
            document.removePdfaCompliance();

            // Save output in XML format
            document.save(pdfDocumentFileName);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);

    }
```

Ces informations sont également supprimées si vous apportez des modifications au document (par ex. ajouter des pages). Dans l'exemple suivant, le document de sortie perd la conformité PDF/A après l'ajout de page.

```java
   public void convertPDFAtoPDFAdvanced() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        // Create Document object
        document = new Document(pdfaDocumentFileName);

        // Adding a new (empty) page removes PDF/A compliance information.
        document.getPages().add();

        // Save updated document
        document.save(pdfDocumentFileName);
    }
```




