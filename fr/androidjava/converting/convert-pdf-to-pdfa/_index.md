---
title: Convertir un fichier PDF en PDF/A
linktitle: Convertir un fichier PDF en PDF/A
type: docs
weight: 180
url: fr/androidjava/convert-pdf-file-to-pdfa/
lastmod: "2021-06-05"
description: Ce sujet vous montre comment Aspose.PDF pour Java permet de convertir un fichier PDF en un fichier PDF conforme PDF/A.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF vous permet de convertir un fichier PDF en un fichier PDF conforme PDF/A. Avant de le faire, le fichier doit être validé. Cet article explique comment.

Veuillez noter que nous suivons Adobe Preflight pour valider la conformité PDF/A. Tous les outils sur le marché ont leur propre "représentation" de la conformité PDF/A. Veuillez consulter cet article sur les [outils de validation PDF/A](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results) pour référence. Nous avons choisi les produits Adobe pour vérifier comment Aspose.PDF produit des fichiers PDF car Adobe est au centre de tout ce qui est lié au PDF.

Avant de convertir le PDF en un fichier conforme PDF/A, validez le PDF en utilisant la méthode validate.
 Le résultat de la validation est stocké dans un fichier XML, puis ce résultat est également passé à la méthode de conversion. Vous pouvez également spécifier l'action pour les éléments qui ne peuvent pas être convertis en utilisant l'énumération [ConvertErrorAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction).

{{% alert color="primary" %}}

Essayez en ligne. Vous pouvez vérifier la qualité de la conversion Aspose.PDF et visualiser les résultats en ligne à ce lien [products.aspose.app/pdf/conversion/pdf-to-pdfa1a](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)

{{% /alert %}}

## Conversion de PDF en PDF/A_1b

L'extrait de code suivant montre comment convertir des fichiers PDF en PDF conforme à PDF/A-1b.

```java
public void convertPDFtoPDFa1b() {
        // Ouvrir le document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convertir en document conforme PDF/A
        // Pendant le processus de conversion, la validation est également effectuée
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");
        document.convert(logFileName.toString(), PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

        // Enregistrer le document de sortie
        document.save(pdfaFileName.toString());
    }
```

Pour effectuer uniquement la validation, utilisez la ligne de code suivante :

```java
public void ValidatePDF_A_1B() {
        // Ouvrir le document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Valider le document conforme à PDF/A

        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        if (document.validate(logFileName.toString(), PdfFormat.PDF_A_1B)){
            resultMessage.setText("Le document est valide");
        }
        else {
            resultMessage.setText("Le document n'est pas valide");
        }
    }
```

## Conversion de PDF en PDF/A_3b

```java
    public void convertPDFtoPDFa3b() {
        // Ouvrir le document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convertir en document conforme à PDF/A
        // Pendant le processus de conversion, la validation est également effectuée
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

        // Enregistrer le document de sortie
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


## Conversion de PDF à PDF/A_3a

```java
public void convertPDFtoPDFa3a() {
        // Ouvrir le document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convertir en document conforme au PDF/A
        // Pendant le processus de conversion, la validation est également effectuée
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);

        // Enregistrer le document de sortie
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Conversion de PDF à PDF/A_2a

```java
public void convertPDFtoPDFa2a() {
        // Ouvrir le document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convertir en document conforme au PDF/A
        // Pendant le processus de conversion, la validation est également effectuée
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_2A, ConvertErrorAction.Delete);

        // Enregistrer le document de sortie
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```


## Conversion de PDF en PDF/A_3U

```java
 public void convertPDFtoPDFa3u() {
        // Ouvrir le document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convertir en document conforme PDF/A
        // Pendant le processus de conversion, la validation est également effectuée
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);

        // Enregistrer le document de sortie
        try {
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Créer PDF/A-3 et attacher un fichier XML

Aspose.PDF pour Android via Java offre la fonctionnalité de convertir des fichiers PDF au format PDF/A et prend également en charge la capacité d'ajouter des fichiers en tant que pièce jointe au document PDF.
 Dans le cas où vous avez besoin de joindre des fichiers au format de conformité PDF/A, nous vous recommandons d'utiliser la valeur PDF_A_3A de l'énumération com.aspose.pdf.PdfFormat, le PDF/A_3a est le format qui offre la fonctionnalité de joindre tout format de fichier en tant que pièce jointe à un fichier conforme PDF/A. Cependant, une fois le fichier joint, vous devez le convertir à nouveau au format Pdf-3a, afin de corriger les métadonnées. Veuillez consulter l'extrait de code suivant.

```java
 public void convertPDFtoPDFa3u_attachXML() {
        // Ouvrir le document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convertir en document conforme PDF/A
        // Pendant le processus de conversion, la validation est également effectuée
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");
        File attachment = new File(fileStorage,"sample.xml");

        // Enregistrer le document de sortie
        try {
            // charger le fichier XML
            FileSpecification fileSpecification = new FileSpecification(attachment.toString(), "Fichier xml d'exemple");
            // Ajouter la pièce jointe à la collection de pièces jointes du document
            document.getEmbeddedFiles().add(fileSpecification);
            document.convert(logFileName.toString(), PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);
            document.save(pdfaFileName.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```