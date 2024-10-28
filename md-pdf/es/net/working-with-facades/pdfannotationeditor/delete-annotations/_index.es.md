---
title: Eliminar Anotaciones (fachadas)
type: docs
weight: 10
url: /net/delete-annotations/
description: Esta sección explica cómo eliminar anotaciones con Aspose.PDF Facades utilizando la clase PdfAnnotationEditor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Eliminar Todas las Anotaciones de un Archivo PDF Existente

[PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) te permite eliminar todas las anotaciones del archivo PDF existente. Primero, crea un objeto [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) y enlaza el archivo PDF de entrada usando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Después de eso, llama al método [DeleteAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/deleteannotations) para eliminar todas las anotaciones del archivo, y luego usa el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) para guardar el archivo PDF actualizado. El siguiente fragmento de código te muestra cómo eliminar todas las anotaciones del archivo PDF.

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
## Eliminar Todas las Anotaciones por Tipo Especificado

Puede usar la clase [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) para eliminar todas las anotaciones, por un tipo de anotación especificado, del archivo PDF existente. En orden de hacer eso, necesitas crear un objeto [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) y vincular el archivo PDF de entrada usando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Después de eso, llama al método [DeleteAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/deleteannotations), con el parámetro de cadena, para eliminar todas las anotaciones del archivo; el parámetro de cadena representa el tipo de anotación a eliminar. Finalmente, usa el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) para guardar el archivo PDF actualizado. El siguiente fragmento de código te muestra cómo eliminar todas las anotaciones por tipo de anotación especificado.

```csharp
    public static void DeleteAnnotation()
        {
            // Abrir documento
            var document = new Document(_dataDir + "sample_cats_dogs.pdf");
            int index;
            for (index = 1; index <= document.Pages[1].Annotations.Count; index++)
            {
                System.Console.WriteLine($"{index}. {document.Pages[1].Annotations[index].Name} {document.Pages[1].Annotations[index].AnnotationType}");
            }
            System.Console.Write("Por favor ingrese número:");
            index = int.Parse(System.Console.ReadLine());

            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(document);
            annotationEditor.DeleteAnnotation(document.Pages[1].Annotations[index].Name);

            // Guardar PDF actualizado
            annotationEditor.Save(_dataDir + "DeleteAnnotation.pdf");
        }
```