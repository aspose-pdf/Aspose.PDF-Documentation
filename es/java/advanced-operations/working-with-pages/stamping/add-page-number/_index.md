---
title: Agregar números de página a PDF en Java
linktitle: Agregar número de página
type: docs
weight: 30
url: /java/add-page-number/
description: Aprenda a agregar sellos de números de página a documentos PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregue sellos de números de página a archivos PDF con Java
Abstract: Este artículo explica cómo agregar sellos de números de página usando Aspose.PDF para Java. Cubre la numeración de páginas estándar con estilo de fuente personalizado y numeración de números romanos con un número inicial configurable.
---
## Agregar un sello de número de página


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree el objeto [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/).

1. 
Configure las opciones de numeración y colocación de sellos requeridas.

1. 
Configure las opciones de formato de texto requeridas, incluidas [FontRepository](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontrepository/) y [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).
1. Agregue el [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/) configurado a la [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) de destino.

1. 
Guarde el [Documento] PDF actualizado(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addPageNumStamp(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageNumberStamp pageNumberStamp = new PageNumberStamp();
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setFormat("Page # of " + document.getPages().size());
        pageNumberStamp.setBottomMargin(10);
        pageNumberStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(1);
        pageNumberStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize(14.0f);
        pageNumberStamp.getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        pageNumberStamp.getTextState().setForegroundColor(Color.getBlueViolet());

        document.getPages().get_Item(1).addStamp(pageNumberStamp);
        document.save(outputFile.toString());
    }
}
```
