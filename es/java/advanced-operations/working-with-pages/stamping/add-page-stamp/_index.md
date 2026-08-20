---
title: Agregar sellos de página a PDF en Java
linktitle: Agregar sellos de página
type: docs
weight: 30
url: /java/page-stamps-in-the-pdf-file/
description: Aprenda a agregar sellos de páginas PDF como superposiciones o fondos en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregue sellos basados en páginas a archivos PDF con Java
Abstract: Este artículo explica cómo agregar un sello de página a un documento PDF usando Aspose.PDF para Java. El ejemplo carga otra página PDF como sello, la configura como fondo y la aplica a una página de destino.
---
Aspose.PDF para Java puede aplicar una página de otro PDF como sello o agregar superposiciones de numeración de páginas.


## 
Agregar un sello de página desde otro PDF



Utilice este ejemplo cuando deba utilizar una página de un PDF independiente como sello de fondo.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree un [PdfPageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfpagestamp/) desde la página PDF externa.
1. Configure el sello y agréguelo a la página de destino, luego guarde el resultado.


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

## 
Agregar un sello de número de página estándar



Utilice este ejemplo cuando la página de destino deba mostrar el número actual con formato de texto personalizado.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree y configure un [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/).
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

## 
Agregar un sello de número de página con números romanos



Utilice este ejemplo cuando la numeración de páginas deba comenzar a partir de un valor personalizado y utilizar números romanos en mayúsculas.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree un [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/) y configure la numeración de números romanos.
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
