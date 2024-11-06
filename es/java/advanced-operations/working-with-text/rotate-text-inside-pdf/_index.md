---
title: Rotar Texto Dentro de PDF
linktitle: Rotar Texto Dentro de PDF
type: docs
weight: 50
url: es/java/rotate-text-inside-pdf/
description: Aprenda diferentes maneras de rotar texto en un PDF. Aspose.PDF le permite rotar texto a cualquier ángulo, rotar un fragmento de texto o un párrafo completo.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Rotar Texto Dentro de PDF usando la Propiedad de Rotación

Usando el método [setRotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentState#setRotation-double-) de la Clase [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment), puede rotar texto en varios ángulos. La rotación de texto se puede usar en diferentes escenarios de generación de documentos. Puede especificar el ángulo de rotación en grados para rotar el texto según su necesidad. Por favor, revise los siguientes diferentes escenarios, en los cuales puede implementar la rotación de texto.

## Implementar Rotación usando TextFragment y TextBuilder

```java
public class ExampleRotateText {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ImplementRotationUsingTextFragmentAndTextBuilder() {

        // Inicializar objeto de documento
        Document pdfDocument = new Document();
        // Obtener página particular
        Page pdfPage = pdfDocument.getPages().add();
        // Crear fragmento de texto
        TextFragment textFragment1 = new TextFragment("texto principal");
        textFragment1.setPosition(new Position(100, 600));

        // Establecer propiedades de texto
        textFragment1.getTextState().setFontSize(12);
        textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

        // Crear fragmento de texto rotado
        TextFragment textFragment2 = new TextFragment("texto rotado");
        textFragment2.setPosition(new Position(200, 600));
        // Establecer propiedades de texto
        textFragment2.getTextState().setFontSize(12);
        textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment2.getTextState().setRotation(45);

        // Crear fragmento de texto rotado
        TextFragment textFragment3 = new TextFragment("texto rotado");
        textFragment3.setPosition(new Position(300, 600));

        // Establecer propiedades de texto
        textFragment3.getTextState().setFontSize(12);
        textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment3.getTextState().setRotation(90);

        // crear objeto TextBuilder
        TextBuilder textBuilder = new TextBuilder(pdfPage);
        // Añadir el fragmento de texto a la página PDF
        textBuilder.appendText(textFragment1);
        textBuilder.appendText(textFragment2);
        textBuilder.appendText(textFragment3);

        // Guardar documento
        pdfDocument.save(_dataDir + "TextFragmentTests_Rotated1_out.pdf");
    }
}
```


## Implementar Rotación usando TextParagraph y TextBuilder (Fragmentos Rotados)

```java
public static void ImplementRotationUsingTextParagraphAndTextBuilder_RotatedFragments() {

    // Inicializar objeto documento
    Document pdfDocument = new Document();
    // Obtener una página en particular
    Page pdfPage = (Page) pdfDocument.getPages().add();
    TextParagraph paragraph = new TextParagraph();
    paragraph.setPosition(new Position(200, 600));
    // Crear fragmento de texto
    TextFragment textFragment1 = new TextFragment("texto rotado");
    // Establecer propiedades del texto
    textFragment1.getTextState().setFontSize(12);
    textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    // Establecer rotación
    textFragment1.getTextState().setRotation(45);

    // Crear fragmento de texto
    TextFragment textFragment2 = new TextFragment("texto principal");
    // Establecer propiedades del texto
    textFragment2.getTextState().setFontSize(12);
    textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // Crear fragmento de texto
    TextFragment textFragment3 = new TextFragment("otro texto rotado");
    // Establecer propiedades del texto
    textFragment3.getTextState().setFontSize(12);
    textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    // Establecer rotación
    textFragment3.getTextState().setRotation(-45);

    // Agregar los fragmentos de texto al párrafo
    paragraph.appendLine(textFragment1);
    paragraph.appendLine(textFragment2);
    paragraph.appendLine(textFragment3);
    // Crear objeto TextBuilder
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // Agregar el párrafo de texto a la página PDF
    textBuilder.appendParagraph(paragraph);
    // Guardar documento
    pdfDocument.save(_dataDir + "TextFragmentTests_Rotated2_out.pdf");
}
```


## Implementar Rotación usando TextFragment y Page.Paragraphs

```csharp
public static void ImplementRotationUsingTextFragmentAndPageParagraphs() {
    // Inicializar objeto de documento
    Document pdfDocument = new Document();
    // Obtener página particular
    Page pdfPage = (Page) pdfDocument.getPages().add();
    // Crear fragmento de texto
    TextFragment textFragment1 = new TextFragment("texto principal");
    // Establecer propiedades del texto
    textFragment1.getTextState().setFontSize(12);
    textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // Crear fragmento de texto
    TextFragment textFragment2 = new TextFragment("texto rotado");

    // Establecer propiedades del texto
    textFragment2.getTextState().setFontSize(12);
    textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // Establecer rotación
    textFragment2.getTextState().setRotation(315);

    // Crear fragmento de texto
    TextFragment textFragment3 = new TextFragment("texto rotado");
    // Establecer propiedades del texto
    textFragment3.getTextState().setFontSize(12);
    textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));

    // Establecer rotación
    textFragment3.getTextState().setRotation(270);
    pdfPage.getParagraphs().add(textFragment1);
    pdfPage.getParagraphs().add(textFragment2);
    pdfPage.getParagraphs().add(textFragment3);

    // Guardar documento
    pdfDocument.save(_dataDir + "TextFragmentTests_Rotated3_out.pdf");
    }
```


## Implementar Rotación usando TextParagraph y TextBuilder (Todo el Párrafo Rotado)

```java
public static void ImplementRotationUsingTextParagraphAndTextBuilder() {

    // Inicializar objeto documento
    Document pdfDocument = new Document();
    // Obtener página en particular
    Page pdfPage = pdfDocument.getPages().add();
    for (int i = 0; i < 4; i++) {
        TextParagraph paragraph = new TextParagraph();
        paragraph.setPosition(new Position(200, 600));
        // Especificar rotación
        paragraph.setRotation(i * 90 + 45);
        // Crear fragmento de texto
        TextFragment textFragment1 = new TextFragment("Texto del Párrafo");
        // Crear fragmento de texto
        textFragment1.getTextState().setFontSize(12);
        textFragment1.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment1.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment1.getTextState().setForegroundColor(Color.getBlue());

        // Crear fragmento de texto
        TextFragment textFragment2 = new TextFragment("Segunda línea de texto");
        // Establecer propiedades del texto
        textFragment2.getTextState().setFontSize(12);
        textFragment2.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment2.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment2.getTextState().setForegroundColor(Color.getBlue());

        // Crear fragmento de texto
        TextFragment textFragment3 = new TextFragment("Y algo más de texto...");
        // Establecer propiedades del texto
        textFragment3.getTextState().setFontSize(12);
        textFragment3.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment3.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment3.getTextState().setForegroundColor(Color.getBlue());
        textFragment3.getTextState().setUnderline(true);

        paragraph.appendLine(textFragment1);
        paragraph.appendLine(textFragment2);
        paragraph.appendLine(textFragment3);
        // Crear objeto TextBuilder
        TextBuilder textBuilder = new TextBuilder(pdfPage);
        // Añadir el fragmento de texto a la página PDF
        textBuilder.appendParagraph(paragraph);
    }
    // Guardar documento
    pdfDocument.save(_dataDir + "TextFragmentTests_Rotated4_out.pdf");
}
```