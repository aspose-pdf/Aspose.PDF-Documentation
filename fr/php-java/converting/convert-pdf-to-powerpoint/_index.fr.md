---
title: Convertir un PDF en Microsoft PowerPoint 
linktitle: Convertir PDF en PowerPoint
type: docs
weight: 30
url: /php-java/convert-pdf-to-powerpoint/
lastmod: "2024-05-20"
description: Aspose.PDF vous permet de convertir des PDF en format PowerPoint en utilisant PHP. Il est possible de convertir un PDF en PPTX avec les diapositives sous forme d'images.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF pour PHP** vous permet de suivre la progression de la conversion de PDF en PPTX. Nous avons une API nommée Aspose.Slides qui offre la fonctionnalité de créer ainsi que de manipuler des présentations PPT/PPTX. Cette API fournit également la fonctionnalité de convertir des fichiers PPT/PPTX en format PDF. Dans Aspose.PDF pour PHP, nous avons introduit une fonctionnalité pour transformer des documents PDF en format PPTX. Pendant cette conversion, les pages individuelles du fichier PDF sont converties en diapositives séparées dans le fichier PPTX.

Lors de la conversion de PDF en PPTX, le texte est rendu en tant que texte que vous pouvez sélectionner/mettre à jour, au lieu d'être rendu sous forme d'image.
 Veuillez noter que pour convertir des fichiers PDF en format PPTX, Aspose.PDF fournit une classe nommée PptxSaveOptions. Un objet de la classe [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) est passé en tant que deuxième argument à la méthode [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..).

Vérifiez le snippet de code suivant pour résoudre vos tâches de conversion de PDF au format PowerPoint :

```php
// Charger le document PDF d'entrée
$document = new Document($inputFile);

// Créer une instance de PptxSaveOptions
$saveOption = new PptxSaveOptions();

// Enregistrer le document PDF en tant que fichier PPTX
$document->save($outputFile, $saveOption);
```

## Convertir un PDF en PPTX avec des diapositives sous forme d'images

Dans le cas où vous avez besoin de convertir un PDF consultable en PPTX sous forme d'images au lieu de texte sélectionnable, Aspose.PDF fournit une telle fonctionnalité via la classe [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions). Pour y parvenir, définissez la propriété SlidesAsImages de la classe [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) à 'true' comme indiqué dans l'exemple de code suivant.

L'extrait de code suivant montre le processus de conversion des fichiers PDF au format PPTX Slides en tant qu'Images.

```php
// Charger le document PDF d'entrée
$document = new Document($inputFile);

// Créer une instance de PptxSaveOptions
$saveOption = new PptxSaveOptions();
$saveOption->setSlidesAsImages(true);

// Enregistrer le document PDF en tant que fichier PPTX
$document->save($outputFile, $saveOption);

    public static void ConvertPDFtoPPTX_SlideAsImages() {
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "PDFToPPTX.pdf").toString();
        String pptxDocumentFileName = Paths.get(_dataDir.toString(), "PDFToPPTX_out.pptx").toString();

        // Charger le document PDF
        Document doc = new Document(pdfDocumentFileName);
        // Instancier une instance de PptxSaveOptions
        PptxSaveOptions pptx_save = new PptxSaveOptions();
        // Enregistrer la sortie au format PPTX
        pptx_save.setSlidesAsImages(true);

        doc.save(pptxDocumentFileName, pptx_save);
    }
```

{{% alert color="success" %}}
**Essayez de convertir un PDF en PowerPoint en ligne**

Aspose.PDF pour PHP vous présente une application en ligne gratuite ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en PPTX avec application gratuite](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}