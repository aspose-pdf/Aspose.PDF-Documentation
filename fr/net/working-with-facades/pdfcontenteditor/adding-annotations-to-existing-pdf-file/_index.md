---
title: Ajouter des annotations à un fichier PDF existant
type: docs
weight: 80
url: fr/net/adding-annotations-to-existing-pdf-file/
description: Cette section explique comment ajouter des annotations à un fichier PDF existant avec Aspose.PDF Facades.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ajouter une annotation de texte libre dans un fichier PDF existant (facades)

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) vous permet d'ajouter des annotations de différents types dans un fichier PDF existant. Vous pouvez utiliser la méthode respective pour ajouter une annotation particulière. Par exemple, dans l'extrait de code suivant, nous avons utilisé la méthode [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) pour ajouter une annotation de type [FreeText](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation).

Tout type d'annotations peut être ajouté au fichier PDF de la même manière. Tout d'abord, vous devez créer un objet de type [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) et lier le fichier PDF d'entrée en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Deuxièmement, vous devez créer un objet Rectangle pour spécifier la zone de l'annotation.

Après cela, vous pouvez appeler la méthode [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) pour ajouter une annotation [FreeText](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation), puis utiliser la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) pour enregistrer le fichier PDF mis à jour.

L'extrait de code suivant vous montre comment ajouter une annotation de texte libre dans un fichier PDF.

```csharp
  public static void AddFreeTextAnnotation()
        {
            var document = new Document(_dataDir + "sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
            tfa.Visit(document.Pages[1]);

            var rect = new System.Drawing.Rectangle
            {
                X = (int)tfa.TextFragments[1].Rectangle.LLX,
                Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
                Height = 18,
                Width = 100
            };

            editor.CreateFreeText(rect, "Free Text Demo", 1); // dernier paramètre est un numéro de page
            editor.Save(_dataDir + "PdfContentEditorDemo_FreeTextAnnotation.pdf");
        }
```
## Ajouter une Annotation de Texte dans un Fichier PDF Existant (façades)

Dans cet exemple également, vous devez créer un objet de type [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) et lier le fichier PDF d'entrée en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Deuxièmement, vous devez créer un objet Rectangle pour spécifier la zone de l'annotation. Après cela, vous pouvez appeler la méthode [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) pour ajouter une annotation FreeText, créer le titre de vos annotations et le numéro de page sur lequel l'annotation se trouve.

```csharp
 public static void AddTextAnnotation()
        {
            var document = new Document(_dataDir + "sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
            tfa.Visit(document.Pages[1]);

            var rect = new System.Drawing.Rectangle
            {
                X = (int)tfa.TextFragments[1].Rectangle.LLX,
                Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
                Height = 18,
                Width = 100
            };

            editor.CreateText(rect, "Aspose User", "PDF is a better format for modern documents", false, "Key", 1);
            editor.Save(_dataDir + "PdfContentEditorDemo_TextAnnotation.pdf");
        }
```

## Ajouter une Annotation de Ligne dans un Fichier PDF Existant (facades)

Nous spécifions également le Rectangle, les coordonnées du début et de la fin de la ligne, le numéro de page, l'épaisseur, le style et la couleur du cadre de l'annotation, le type de tiret de ligne, le type de début et de fin de la ligne.

```csharp
  public static void AddLineAnnotation()
        {
            var document = new Document(_dataDir + "Appartments.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            // Create Line Annotation
            editor.CreateLine(
                new System.Drawing.Rectangle(550, 93, 562, 439),
                "Test",
                556, 99, 556, 443, 1, 2,
                System.Drawing.Color.Red,
                "dash",
                new int[] { 1, 0, 3 },
                new[] { "Open", "Open" });
            editor.Save(_dataDir + "PdfContentEditorDemo_LineAnnotation.pdf");
        }
```