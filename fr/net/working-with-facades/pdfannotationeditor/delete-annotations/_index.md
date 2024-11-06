---
title: Supprimer les annotations (facades)
type: docs
weight: 10
url: fr/net/delete-annotations/
description: Cette section explique comment supprimer des annotations avec Aspose.PDF Facades en utilisant la classe PdfAnnotationEditor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Supprimer toutes les annotations d'un fichier PDF existant

[PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) vous permet de supprimer toutes les annotations du fichier PDF existant. First off, create a [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) object and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. After that, call [DeleteAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/deleteannotations) method to delete all the annotations from the file, and then use [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method to save the updated PDF file. The following code snippet shows you how to delete all the annotations from the PDF file.

Tout d'abord, créez un objet [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) et liez le fichier PDF d'entrée en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Après cela, appelez la méthode [DeleteAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/deleteannotations) pour supprimer toutes les annotations du fichier, puis utilisez la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) pour enregistrer le fichier PDF mis à jour. L'extrait de code suivant vous montre comment supprimer toutes les annotations du fichier PDF.

```csharp
   public static void DeleteAllAnnotations()
        {
            // Open document
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
            // Delete all annoations
            annotationEditor.DeleteAnnotations();
            // Save updated PDF
        }   
    
```
## Supprimer toutes les annotations par type spécifié

Vous pouvez utiliser la classe [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) pour supprimer toutes les annotations, par un type d'annotation spécifié, du fichier PDF existant. Dans le but de faire cela, vous devez créer un objet [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) et lier le fichier PDF d'entrée en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Après cela, appelez la méthode [DeleteAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/deleteannotations), avec le paramètre de type chaîne, pour supprimer toutes les annotations du fichier ; le paramètre de type chaîne représente le type d'annotation à supprimer. Enfin, utilisez la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) pour enregistrer le fichier PDF mis à jour. Le code suivant vous montre comment supprimer toutes les annotations par type d'annotation spécifié.

```csharp
    public static void DeleteAnnotation()
        {
            // Ouvrir le document
            var document = new Document(_dataDir + "sample_cats_dogs.pdf");
            int index;
            for (index = 1; index <= document.Pages[1].Annotations.Count; index++)
            {
                System.Console.WriteLine($"{index}. {document.Pages[1].Annotations[index].Name} {document.Pages[1].Annotations[index].AnnotationType}");
            }
            System.Console.Write("Veuillez entrer un numéro:");
            index = int.Parse(System.Console.ReadLine());

            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(document);
            annotationEditor.DeleteAnnotation(document.Pages[1].Annotations[index].Name);

            // Enregistrer le PDF mis à jour
            annotationEditor.Save(_dataDir + "DeleteAnnotation.pdf");
        }
```