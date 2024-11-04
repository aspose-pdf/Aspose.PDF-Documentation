---
title: Adding Annotations to existing PDF file
type: docs
weight: 80
url: /net/adding-annotations-to-existing-pdf-file/
description: Esta sección explica cómo agregar anotaciones a un archivo PDF existente con Aspose.PDF Facades.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Agregar Anotación de Texto Libre en un Archivo PDF Existente (facades)

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) te permite agregar anotaciones de diferentes tipos en un archivo PDF existente. Puedes usar el método correspondiente para agregar una anotación particular. Por ejemplo, en el siguiente fragmento de código, hemos utilizado el método [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) para agregar una anotación de tipo [FreeText](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation).

Cualquier tipo de anotaciones puede ser agregado al archivo PDF de la misma manera. Primero, necesitas crear un objeto de tipo [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) y vincular el archivo PDF de entrada usando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). En segundo lugar, tienes que crear un objeto Rectángulo para especificar el área de la anotación.

Después de eso, puedes llamar al método [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) para añadir una anotación de [FreeText](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation), y luego usar el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) para guardar el archivo PDF actualizado.

El siguiente fragmento de código te muestra cómo añadir una anotación de texto libre en un archivo PDF.

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

            editor.CreateFreeText(rect, "Free Text Demo", 1); // el último parámetro es un número de página
            editor.Save(_dataDir + "PdfContentEditorDemo_FreeTextAnnotation.pdf");
        }
```
## Añadir Anotación de Texto en un Archivo PDF Existente (facades)

En este ejemplo también, necesitas crear un objeto de tipo [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) y vincular el archivo PDF de entrada usando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). En segundo lugar, tienes que crear un objeto Rectangle para especificar el área de la anotación. Después de eso, puedes llamar al método [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) para añadir una anotación de texto libre, crear el título de tus anotaciones y el número de página en el que se encuentra la anotación.

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

            editor.CreateText(rect, "Aspose User", "PDF es un mejor formato para documentos modernos", false, "Key", 1);
            editor.Save(_dataDir + "PdfContentEditorDemo_TextAnnotation.pdf");
        }
```

## Añadir Anotación de Línea en un Archivo PDF Existente (facades)

También especificamos el Rectángulo, las coordenadas del inicio y fin de la línea, número de página, grosor, estilo y color del marco de anotación, tipo de guion de línea, tipo de inicio y fin de la línea.

```csharp
  public static void AddLineAnnotation()
        {
            var document = new Document(_dataDir + "Appartments.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            // Crear Anotación de Línea
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