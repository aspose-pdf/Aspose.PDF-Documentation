---
title: Agregar sellos de página a PDF en Java
linktitle: Agregar sellos de página
type: docs
weight: 30
url: /es/java/page-stamps-in-the-pdf-file/
description: Aprenda a agregar sellos de página PDF como superposiciones o fondos en Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregue sellos basados en página a archivos PDF con Java
Abstract: Este artículo explica cómo agregar una marca de página a un documento PDF usando Aspose.PDF for Java. El ejemplo carga otra página PDF como una marca, la configura como fondo y la aplica a una página objetivo.
---
Aspose.PDF for Java puede aplicar una página de otro PDF como una marca o agregar superposiciones de numeración de página.

## Agregar una marca de página desde otro PDF

Utilice este ejemplo cuando se deba usar una página de un PDF separado como una marca de fondo.

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree un [`PdfPageStamp`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfpagestamp/) de la página PDF externa.
1. Configure el sello y agréguelo a la página objetivo, luego guarde el resultado.

```java
public static void addPageStamp(Path inputFile, Path pageStampFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PdfPageStamp pageStamp = new PdfPageStamp(pageStampFile.toString(), 1);
        pageStamp.setBackground(true);
        document.getPages().get_Item(1).addStamp(pageStamp);
        document.save(outputFile.toString());
    }
}
```

## Agregar una marca de número de página estándar

Utilice este ejemplo cuando la página de destino debe mostrar el número actual con formato de texto personalizado.

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree y configure un [`PageNumberStamp`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/).
1. Agregue el sello a la página y guarde el documento.

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

## Agregar un sello de número de página en numeración romana

Utilice este ejemplo cuando la numeración de páginas debe comenzar desde un valor personalizado y usar numerales romanos en mayúsculas.

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree un [`PageNumberStamp`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/) y configure la numeración con numerales romanos.
1. Agregue el sello a todas las páginas y guarde el PDF.

```java
public static void addPageNumStampRoman(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageNumberStamp pageNumberStamp = new PageNumberStamp();
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setBottomMargin(10);
        pageNumberStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(42);
        pageNumberStamp.setNumberingStyle(NumberingStyle.NumeralsRomanUppercase);
        pageNumberStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize(14.0f);
        pageNumberStamp.getTextState().setFontStyle(FontStyles.Bold);
        pageNumberStamp.getTextState().setForegroundColor(Color.getBlueViolet());

        for (Page page : document.getPages()) {
            page.addStamp(pageNumberStamp);
        }
        document.save(outputFile.toString());
    }
}
```
