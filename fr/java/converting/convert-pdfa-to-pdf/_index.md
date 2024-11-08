---
title: Convertir PDF/A en format PDF 
linktitle: Convertir PDF/A en format PDF
type: docs
weight: 110
url: /fr/java/convert-pdfa-to-pdf/
lastmod: "2021-11-19"
description: Ce sujet vous montre comment Aspose.PDF permet de convertir un fichier PDF/A en document PDF avec la bibliothèque Java. 
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Convertir un document PDF/A en PDF

Convertir un document PDF/A en PDF signifie supprimer les restrictions <abbr title="Portable Document Format Archive">PDF/A</abbr> du document original. La classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) possède la méthode RemovePdfaCompliance(..) pour supprimer
les informations de conformité PDF du fichier d'entrée/source.

```java
public static void runPDFA_to_PDF() {
    String pdfaDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF.pdf").toString();
    String documentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF_out.pdf").toString();

    // Créer un objet Document
    Document document = new Document(pdfaDocumentFileName);

    // Supprimer les informations de conformité PDF/A
    document.removePdfaCompliance();

    // Enregistrer la sortie au format XML
    document.save(documentFileName);
    document.close();
}
```


Cette information est également supprimée si vous apportez des modifications au document (par exemple, ajoutez des pages). Dans l'exemple suivant, le document de sortie perd la conformité PDF/A après l'ajout de la page.

```java
public static void runPDFAtoPDFAdvanced() {
    String pdfaDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF.pdf").toString();
    String documentFileName = Paths.get(DATA_DIR.toString(), "PDFAToPDF_out.pdf").toString();

    // Créer un objet Document
    Document document = new Document(pdfaDocumentFileName);

    // L'ajout d'une nouvelle page (vide) supprime les informations de conformité PDF/A.
    document.getPages().add();

    // Enregistrer le document mis à jour
    document.save(documentFileName);
    document.close();
}
```