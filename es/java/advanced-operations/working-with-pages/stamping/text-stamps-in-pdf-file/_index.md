---
title: Agregar sellos de texto a PDF en Java
linktitle: Sellos de texto en archivo PDF
type: docs
weight: 20
url: /es/java/text-stamps-in-the-pdf-file/
description: Aprenda cómo agregar sellos de texto a documentos PDF en Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar sellos de texto a archivos PDF con Java
Abstract: Este artículo explica cómo agregar sellos de texto a archivos PDF usando Aspose.PDF for Java. Cubre la creación de un sello de texto de fondo, su posicionamiento, rotación y la personalización de Font, tamaño, estilo y color.
---
Utilice sellos de texto cuando necesite agregar etiquetas visibles o marcas de agua a páginas PDF.

## Agregar una marca de texto

Utilice este ejemplo cuando una página debe mostrar una marca de texto rotada con estilo personalizado.

1. Abra el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crear un [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstamp/) y configure su ubicación y apariencia del texto.
1. Agregue el sello a la página objetivo y guarde el documento.

```java
public static void addTextStamp(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextStamp textStamp = new TextStamp("Sample Stamp");
        textStamp.setBackground(true);
        textStamp.setXIndent(100);
        textStamp.setYIndent(100);
        textStamp.setRotate(Rotation.on90);
        textStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        textStamp.getTextState().setFontSize(14.0f);
        textStamp.getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        textStamp.getTextState().setForegroundColor(Color.getDarkGreen());
        document.getPages().get_Item(1).addStamp(textStamp);
        document.save(outputFile.toString());
    }
}
```
