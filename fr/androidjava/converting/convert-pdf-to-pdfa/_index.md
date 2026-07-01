---
title: Convertir le fichier PDF en PDF/A
linktitle: Convertir le fichier PDF en PDF/A
type: docs
weight: 180
url: /fr/androidjava/convert-pdf-file-to-pdfa/
lastmod: "2026-07-01"
description: Ce sujet vous montre comment Aspose.PDF for Java permet de convertir un fichier PDF en un fichier PDF/A conforme.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF vous permet de convertir un fichier PDF en un fichier PDF conforme à PDF/A. Avant de le faire, le fichier doit être validé. Cet article explique comment.

Veuillez noter que nous suivons Adobe Preflight pour valider la conformité PDF/A. Tous les outils du marché ont leur propre "représentation" de la conformité PDF/A. Veuillez consulter cet article sur [outils de validation PDF/A](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results) à titre de référence. Nous avons choisi les produits Adobe pour vérifier comment Aspose.PDF génère des fichiers PDF car Adobe est au cœur de tout ce qui est lié au PDF.

Avant de convertir le PDF en fichier conforme PDF/A, validez le PDF en utilisant la méthode validate. Le résultat de la validation est stocké dans un fichier XML, puis ce résultat est également transmis à la méthode convert. Vous pouvez également spécifier l'action pour les éléments qui ne peuvent pas être convertis en utilisant la [ConvertErrorAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction) énumération.

{{% alert color="primary" %}}

Essayez en ligne. Vous pouvez vérifier la qualité de la conversion Aspose.PDF et voir les résultats en ligne à ce lien [products.aspose.app/pdf/conversion/pdf-to-pdfa1a](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)

{{% /alert %}}

## Conversion PDF vers PDF/A_1b

L'extrait de code suivant montre comment convertir des fichiers PDF en PDF conforme à la norme PDF/A-1b.

```java
public void convertPDFtoPDFa1b() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");
        document.convert(logFileName.toString(), PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

        // Save output document
        document.save(pdfaFileName.toString());
    }
```

Pour effectuer uniquement la validation, utilisez la ligne de code suivante :

```java
public void ValidatePDF_A_1B() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Validate to PDF/A compliant document

        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        if (document.validate(logFileName.toString(), PdfFormat.PDF_A_1B)){
            resultMessage.setText("Document is valid");
        }
        else {
            resultMessage.setText("Document is not valid");
        }
    }
```

## Conversion de PDF en PDF/A_3b

```java
    public void convertPDFtoPDFa3b() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

        // Save output document
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

## Conversion PDF en PDF/A_3a

```java
public void convertPDFtoPDFa3a() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);

        // Save output document
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

## Conversion de PDF en PDF/A_2a

```java
public void convertPDFtoPDFa2a() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_2A, ConvertErrorAction.Delete);

        // Save output document
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

## Conversion PDF vers PDF/A_3U

```java
 public void convertPDFtoPDFa3u() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");

        document.convert(logFileName.toString(), PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);

        // Save output document
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

## Créer PDF/A-3 et joindre le fichier XML

Aspose.PDF for Android via Java propose la fonction de convertir des fichiers PDF au format PDF/A et prend également en charge la capacité d'ajouter des fichiers en tant que pièce jointe à un document PDF. Si vous avez besoin d'attacher des fichiers au format de conformité PDF/A, nous recommandons d'utiliser la valeur PDF_A_3A de l'énumération com.aspose.pdf.PdfFormat ; le PDF/A_3a est le format qui offre la possibilité d'attacher n'importe quel format de fichier en tant que pièce jointe à un fichier conforme PDF/A. Cependant, une fois le fichier attaché, vous devez le reconvertir au format Pdf-3a afin de corriger les métadonnées. Veuillez consulter le fragment de code suivant.

```java
 public void convertPDFtoPDFa3u_attachXML() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Convert to PDF/A compliant document
        // During conversion process, the validation is also performed
        File logFileName = new File(fileStorage,"PDF-to-PDFA-log.xml");
        File pdfaFileName = new File(fileStorage,"PDF-to-PDFA.pdf");
        File attachment = new File(fileStorage,"sample.xml");

        // Save output document
        try {
            // load XML file
            FileSpecification fileSpecification = new FileSpecification(attachment.toString(), "Sample xml file");
            // Add attachment to document's attachment collection
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

