---
title: Convertir des PDF aux formats PDF/A 
linktitle: Convertir des PDF aux formats PDF/A
type: docs
weight: 100
url: fr/java/convert-pdf-to-pdfa/
lastmod: "2021-11-19"
description: Ce sujet vous montre comment Aspose.PDF permet de convertir un fichier PDF en un fichier PDF conforme au PDF/A.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF pour Java** vous permet de convertir un fichier PDF en un fichier PDF conforme au PDF/A. Avant de le faire, le fichier doit être validé. Cet article explique comment.

Veuillez noter que nous suivons Adobe Preflight pour valider la conformité PDF/A. Tous les outils sur le marché ont leur propre "représentation" de la conformité PDF/A. Veuillez consulter cet article sur les [outils de validation PDF/A](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results) pour référence. Nous avons choisi les produits Adobe pour vérifier comment Aspose.PDF produit des fichiers PDF car Adobe est au centre de tout ce qui est lié au PDF.

Avant de convertir le PDF en un fichier conforme au PDF/A, validez le PDF en utilisant la méthode validate.
 Le résultat de la validation est stocké dans un fichier XML et ensuite ce résultat est également passé à la méthode de conversion. Vous pouvez également spécifier l'action pour les éléments qui ne peuvent pas être convertis en utilisant l'énumération [ConvertErrorAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction).

## Conversion de PDF en PDF/A_1b

L'extrait de code suivant montre comment convertir des fichiers PDF en PDF conforme à PDF/A-1b.

```java
// Ouvrir le document
Document document = new Document(DATA_DIR + "PDFToPDFA.pdf");

// Convertir en document conforme PDF/A
// Pendant le processus de conversion, la validation est également effectuée
document.convert(DATA_DIR + "log.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

// Enregistrer le document de sortie
document.save(DATA_DIR + "PDFToPDFA_out.pdf");
document.close();
```

Pour effectuer uniquement la validation, utilisez la ligne de code suivante :

```java
// Ouvrir le document
Document document = new Document(DATA_DIR + "ValidatePDFAStandard.pdf");

// Valider le PDF pour PDF/A-1a
if (document.validate(DATA_DIR + "validation-result-A1A.xml", PdfFormat.PDF_A_1B)) {
    System.out.println("Valide");
} else {
    System.out.println("Non valide");
}
document.close();
```

## Conversion de PDF en PDF/A_3b

À partir de [Aspose.PDF pour Java 9.3.0](https://downloads.aspose.com/pdf/java), l'API prend également en charge la conversion de fichiers PDF au format PDF/A_3b.

```java
// Ouvrir le document
Document document = new Document(DATA_DIR + "PDFToPDFA.pdf");

// Convertir en document conforme PDF/A
// Pendant le processus de conversion, la validation est également effectuée
document.convert(DATA_DIR + "log.xml", PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

// Enregistrer le document de sortie
document.save(DATA_DIR + "PDFToPDFA_out.pdf");
document.close();
```

## Conversion de PDF en PDF/A_3a

À partir de [Aspose.PDF pour Java 10.6.0](https://downloads.aspose.com/pdf/java), l'API prend également en charge la conversion de fichiers PDF au format PDF/A_3a.

```java
// Ouvrir le document
Document document = new Document(DATA_DIR + "PDFToPDFA.pdf");

// Convertir en document conforme PDF/A
// Pendant le processus de conversion, la validation est également effectuée
document.convert("file.log", PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);

// Enregistrer le document de sortie
document.save(DATA_DIR + "PDFToPDFA_out.pdf");
document.close();
```


## Conversion PDF en PDF/A_2a

À partir de la version [Aspose.PDF for Java 10.2.0](https://downloads.aspose.com/pdf/java), l'API offre la fonctionnalité de convertir des fichiers PDF en format PDF/A3.

```java
    public static void ConvertPDFtoPDFa2a() {
        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir + "PDFToPDFA.pdf");

        // Convertir en document conforme PDF/A
        // Pendant le processus de conversion, la validation est également effectuée
        pdfDocument.convert("file.log", PdfFormat.PDF_A_2A, ConvertErrorAction.Delete);

        // Enregistrer le document de sortie
        pdfDocument.save(_dataDir + "PDFToPDFA_out.pdf");
    }
```

## Conversion PDF en PDF/A_3U

À partir de la version Aspose.PDF for Java 17.2.0, l'API offre la fonctionnalité de convertir des fichiers PDF en format PDF/A_3U.

```java
    public static void ConvertPDFtoPDFa3u() {
        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir + "PDFToPDFA.pdf");

        // Convertir en document conforme PDF/A
        // Pendant le processus de conversion, la validation est également effectuée
        pdfDocument.convert("file.log", PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);

        // Enregistrer le document de sortie
        pdfDocument.save(_dataDir + "PDFToPDFA_out.pdf");
    }
```


## Créer un PDF/A-3 et attacher un fichier XML

Aspose.PDF pour Java offre la fonctionnalité de convertir des fichiers PDF au format PDF/A et prend également en charge les capacités d'ajouter des fichiers en tant que pièces jointes à un document PDF. Si vous avez besoin d'attacher des fichiers au format conforme PDF/A, nous vous recommandons d'utiliser la valeur PDF_A_3A de l'énumération com.aspose.pdf.PdfFormat. Le PDF/A_3a est le format qui offre la possibilité d'attacher tout format de fichier en tant que pièce jointe à un fichier conforme PDF/A. Cependant, une fois le fichier attaché, vous devez le convertir à nouveau au format Pdf-3a afin de corriger les métadonnées. Veuillez consulter l'extrait de code suivant.

```java
    public static void ConvertPDFtoPDFa3u_attachXML() {
        Document doc = new Document();
        // ajouter une page au fichier PDF
        doc.getPages().add();
        // charger le fichier XML
        FileSpecification fileSpecification = new FileSpecification(_dataDir + "attachment.xml", "Fichier xml d'exemple");
        // Ajouter la pièce jointe à la collection de pièces jointes du document
        doc.getEmbeddedFiles().add(fileSpecification);
        // effectuer la conversion PDF/A_3a
        doc.convert(_dataDir + "log.xml", PdfFormat.PDF_A_3A/* ou PDF_A_3B */, ConvertErrorAction.Delete);
        // enregistrer le fichier PDF final
        doc.save(_dataDir + "attached_PDFA_3A.pdf");
    }
```


{{% alert color="primary" %}}
**Essayez de convertir PDF en PDF/A en ligne**

Aspose.PDF pour Java vous présente une application en ligne gratuite ["PDF en PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), où vous pouvez essayer d'examiner la fonctionnalité et la qualité avec lesquelles elle fonctionne.

[![Aspose.PDF Conversion PDF en PDF/A avec Application Gratuite](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}