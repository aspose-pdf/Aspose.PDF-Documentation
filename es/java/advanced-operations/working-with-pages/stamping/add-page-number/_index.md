---
title: Agregar números de página al PDF en Java
linktitle: Agregar número de página
type: docs
weight: 30
url: /es/java/add-page-number/
description: Aprenda cómo agregar sellos de número de página a documentos PDF en Java.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar sellos de número de página a archivos PDF con Java
Abstract: Este artículo explica cómo agregar sellos de número de página usando Aspose.PDF for Java. Cubre la numeración de página estándar con estilo de fuente personalizado y la numeración en números romanos con un número de inicio configurable.
---
## Agregar un sello de número de página

1. Abra el PDF de origen [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree el objeto [`PageNumberStamp`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/).
1. Configure la ubicación requerida del sello y las opciones de numeración.
1. Establezca las opciones de formato de texto requeridas, incluyendo [`FontRepository`](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontrepository/) y [`Color`](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).
1. Agregue lo configurado [`PageNumberStamp`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/) al objetivo [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Guarde el PDF actualizado [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
