---
title: Adding Annotations to existing PDF file
type: docs
weight: 80
url: /es/java/adding-annotations-to-existing-pdf-file/
description: Esta sección explica cómo agregar anotaciones a un archivo PDF existente con Aspose.PDF Facades.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Añadir anotación de texto libre en un archivo PDF existente (facades)

Una anotación de texto libre muestra texto directamente en la página. [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) te permite agregar anotaciones de diferentes tipos en un archivo PDF existente. Puedes usar el método respectivo para agregar una anotación particular. Por ejemplo, en el siguiente fragmento de código, hemos utilizado el método [createFreeText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createFreeText-java.awt.Rectangle-java.lang.String-int-) para agregar una anotación de tipo FreeText.

Cualquier tipo de anotaciones se puede agregar al archivo PDF de la misma manera.
 Primero, necesitas crear un objeto del tipo [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) y vincular el archivo PDF de entrada usando el método bindPdf. En segundo lugar, debes crear un objeto Rectangle para especificar el área de la anotación. Después de eso, puedes llamar al método [createFreeText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createFreeText-java.awt.Rectangle-java.lang.String-int-) para agregar la anotación de texto libre, el número de página en la que se encuentra la anotación, y luego usar el método save para guardar el archivo PDF actualizado.

El siguiente fragmento de código te muestra cómo agregar una anotación de texto libre en un archivo PDF.

```java
  public static void AddFreeTextAnnotation()
    {
        var document = new Document(_dataDir + "sample.pdf");
        PdfContentEditor editor = new PdfContentEditor(document);
        TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
        tfa.visit(document.getPages().get_Item(1));

        java.awt.Rectangle rect = new  java.awt.Rectangle();
        rect.x = (int)tfa.getTextFragments().get_Item(1).getRectangle().getLLX();
        rect.y = (int)tfa.getTextFragments().get_Item(1).getRectangle().getURY() + 5;
        rect.height = 18;
        rect.width = 100;        

        editor.createFreeText(rect, "Free Text Demo", 1); // el último parámetro es un número de página
        editor.save(_dataDir + "PdfContentEditorDemo_FreeTextAnnotation.pdf");
    }
```

## Agregar Anotación de Texto en un Archivo PDF Existente (facades)

En este ejemplo también, necesitas crear un objeto de tipo [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) y vincular el archivo PDF de entrada usando el método [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#bindPdf-java.lang.String-). En segundo lugar, debes crear un objeto Rectangle para especificar el área de la anotación. Después de eso, puedes llamar al método [createFreeText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createFreeText-java.awt.Rectangle-java.lang.String-int-) para agregar una anotación de texto libre, crear el título de tus anotaciones y el número de página en el que se encuentra la anotación.

```java
 public static void AddTextAnnotation()
    {
        var document = new Document(_dataDir + "sample.pdf");
        PdfContentEditor editor = new PdfContentEditor(document);
        TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
        tfa.visit(document.getPages().get_Item(1));

        java.awt.Rectangle rect = new  java.awt.Rectangle();
        rect.x = (int)tfa.getTextFragments().get_Item(1).getRectangle().getLLX();
        rect.y = (int)tfa.getTextFragments().get_Item(1).getRectangle().getURY() + 5;
        rect.height = 18;
        rect.width = 100;        

        editor.createText(rect, "Usuario de Aspose", "PDF es un mejor formato para documentos modernos", false, "Key", 1);
        editor.save(_dataDir + "PdfContentEditorDemo_TextAnnotation.pdf");
    }
```


## Añadir Anotación de Línea en un Archivo PDF Existente (facades)

También especificamos el Rectángulo, las coordenadas del principio y fin de la línea, el número de página, el grosor, el estilo y el color del marco de la anotación, el tipo de guion de línea, el tipo de inicio y fin de la línea.

```java

    public static void AddLineAnnotation()
    {
        var document = new Document(_dataDir + "Appartments.pdf");
        PdfContentEditor editor = new PdfContentEditor(document);
        // Crear Anotación de Línea
        editor.createLine(
            new java.awt.Rectangle(550, 93, 562, 439),
            "Test",
            556, 99, 556, 443, 1, 1,
            java.awt.Color.RED,
            "dash",
            new int[] { 1, 0, 3 },
            new String[] { "Open", "Open" });
        editor.save(_dataDir + "PdfContentEditorDemo_LineAnnotation.pdf");
    }
```