---
title: Convertir PDF en PowerPoint
linktitle: Convertir PDF en PowerPoint
type: docs
weight: 110
url: /fr/androidjava/convert-pdf-to-powerpoint/
description: Aspose.PDF vous permet de convertir un PDF au format PowerPoint. Il est possible de convertir un PDF en PPTX avec les diapositives sous forme d'images.
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Nous disposons d’une API nommée Aspose.Slides qui offre la possibilité de créer ainsi que de manipuler des présentations PPT/PPTX. Cette API permet également de convertir des fichiers PPT/PPTX au format PDF. Dans Aspose.PDF for Java, nous avons introduit une fonction permettant de transformer des documents PDF en format PPTX. Au cours de cette conversion, les pages individuelles du fichier PDF sont converties en diapositives distinctes dans le fichier PPTX.

{{% alert color="primary" %}}

Essayez en ligne. Vous pouvez vérifier la qualité de la conversion Aspose.PDF et voir les résultats en ligne à ce lien [products.aspose.app/pdf/conversion/pdf-to-pptx](https://products.aspose.app/pdf/conversion/pdf-to-pptx)

{{% /alert %}}

Lors de la conversion de PDF en PPTX, le texte est rendu en tant que texte que vous pouvez sélectionner/mise à jour, au lieu d’être rendu sous forme d’image. Veuillez noter que pour convertir des fichiers PDF au format PPTX, Aspose.PDF fournit une classe nommée PptxSaveOptions. Un objet de la [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) classe est passée en deuxième argument à la [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..) méthode.

Vérifiez le fragment de code suivant pour résoudre vos tâches avec la conversion PDF vers le format PowerPoint :

```java
 public void convertPDFtoPowerPoint() {
        // Load PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        PptxSaveOptions pptxSaveOptions = new PptxSaveOptions();


        // Save the output in PPTX
        File xlsFileName = new File(fileStorage, "PDF-to-Powerpoint.pptx");
        try {
            // Save the file into PPTX format
            document.save(xlsFileName.toString(), pptxSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

