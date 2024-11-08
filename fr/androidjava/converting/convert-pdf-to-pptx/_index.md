---
title: Convertir PDF en PowerPoint 
linktitle: Convertir PDF en PowerPoint
type: docs
weight: 110
url: /fr/androidjava/convert-pdf-to-powerpoint/
description: Aspose.PDF vous permet de convertir un PDF au format PowerPoint. Il est possible de convertir un PDF en PPTX avec les diapositives sous forme d'images. 
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Nous avons une API nommée Aspose.Slides qui offre la fonctionnalité de créer ainsi que de manipuler les présentations PPT/PPTX. Cette API fournit également la fonctionnalité de convertir des fichiers PPT/PPTX au format PDF. Dans Aspose.PDF pour Java, nous avons introduit une fonctionnalité permettant de transformer des documents PDF en format PPTX. Au cours de cette conversion, les pages individuelles du fichier PDF sont converties en diapositives séparées dans le fichier PPTX.

{{% alert color="primary" %}}

Essayez en ligne. Vous pouvez vérifier la qualité de la conversion Aspose.PDF et voir les résultats en ligne à ce lien [products.aspose.app/pdf/conversion/pdf-to-pptx](https://products.aspose.app/pdf/conversion/pdf-to-pptx)

{{% /alert %}}

Pendant la conversion de PDF à PPTX, le texte est rendu comme un texte où vous pouvez le sélectionner/le mettre à jour, au lieu d'être rendu comme une image. Veuillez noter que pour convertir des fichiers PDF en format PPTX, Aspose.PDF fournit une classe nommée PptxSaveOptions. Un objet de la classe [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) est passé comme deuxième argument à la méthode [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..).

Consultez l'extrait de code suivant pour résoudre vos tâches avec la conversion PDF en format PowerPoint :

```java
 public void convertPDFtoPowerPoint() {
        // Charger le document PDF
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instancier l'objet ExcelSave Option
        PptxSaveOptions pptxSaveOptions = new PptxSaveOptions();


        // Sauvegarder le résultat en PPTX
        File xlsFileName = new File(fileStorage, "PDF-to-Powerpoint.pptx");
        try {
            // Enregistrer le fichier au format PPTX
            document.save(xlsFileName.toString(), pptxSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```