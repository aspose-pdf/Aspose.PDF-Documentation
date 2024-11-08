---
title: Convertir PDF/A en PDF 
linktitle: Convertir PDF/A en PDF
type: docs
weight: 350
url: /fr/androidjava/convert-pdfa-to-pdf/
lastmod: "2021-06-05"
description: Pour convertir PDF/A en PDF, vous devez supprimer les restrictions du document original. Aspose.PDF pour Android via Java vous permet de résoudre ce problème facilement et simplement.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Convertir un document PDF/A en PDF signifie supprimer la restriction <abbr title="Portable Document Format Archive
">PDF/A</abbr> du document original. La classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) a la méthode RemovePdfaCompliance(..) pour supprimer
les informations de conformité PDF du fichier d'entrée/source.

```java

    public void convertPDFAtoPDF() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        try {
            // Créer un objet Document
            document = new Document(pdfaDocumentFileName);

            // Supprimer les informations de conformité PDF/A
            document.removePdfaCompliance();

            // Enregistrer la sortie au format XML
            document.save(pdfDocumentFileName);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);

    }
```


Cette information est également supprimée si vous apportez des modifications au document (par exemple, ajouter des pages). Dans l'exemple suivant, le document de sortie perd la conformité PDF/A après l'ajout de la page.

```java
   public void convertPDFAtoPDFAdvanced() {
        String pdfaDocumentFileName = new File(fileStorage, "Conversion/sample-pdfa.pdf").toString();
        String pdfDocumentFileName = new File(fileStorage, "Conversion/sample-out.pdf").toString();

        // Créer un objet Document
        document = new Document(pdfaDocumentFileName);

        // L'ajout d'une nouvelle page (vide) supprime les informations de conformité PDF/A.
        document.getPages().add();

        // Enregistrer le document mis à jour
        document.save(pdfDocumentFileName);
    }
```