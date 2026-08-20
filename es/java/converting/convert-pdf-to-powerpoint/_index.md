---
title: Convertir PDF a PowerPoint en Java
linktitle: Convertir PDF a PowerPoint
type: docs
weight: 30
url: /java/convert-pdf-to-powerpoint/
description: Aprenda a convertir archivos PDF a PowerPoint en Java con Aspose.PDF, incluidas diapositivas PPTX editables, diapositivas basadas en imágenes y resolución de imagen personalizada.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo convertir PDF a PowerPoint en Java
Abstract: Este artículo explica cómo convertir archivos PDF en presentaciones de PowerPoint usando Aspose.PDF para Java. Cubre la conversión PPTX estándar, la salida de diapositivas como imagen y el control de resolución de imagen a través de `PptxSaveOptions`.
---
Aspose.PDF para Java admite la exportación de páginas PDF a presentaciones editables de PowerPoint con opciones de representación de diapositivas. Utilice [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) para controlar cómo se asignan las páginas PDF a las diapositivas de PowerPoint.


## 
Convertir PDF a PPTX



Utilice este ejemplo cuando deba exportar un documento PDF como una presentación estándar de PowerPoint.


1. 
Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) predeterminado para exportar PowerPoint editable.
1. Llame a `document.save(outputFile.toString(), saveOptions)` para que las páginas PDF se serialicen como una presentación `.pptx`.

1. 
Guarde el archivo PPTX convertido.


```java
public static void convertPdfToPptx(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PptxSaveOptions saveOptions = new PptxSaveOptions();
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convierta PDF a PPTX con diapositivas como imágenes



Utilice este ejemplo cuando cada página PDF deba convertirse en una diapositiva de PowerPoint basada en imágenes.


1. 
Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) y habilite `setSlidesAsImages(true)`.

1. 
Llame a `document.save(outputFile.toString(), saveOptions)` para que cada página PDF se represente como una diapositiva respaldada por una imagen en la presentación.

1. 
Guarde el archivo PPTX generado.


```java
public static void convertPdfToPptxSlidesAsImages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PptxSaveOptions saveOptions = new PptxSaveOptions();
        saveOptions.setSlidesAsImages(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convierta PDF a PPTX con resolución de imagen personalizada



Utilice este ejemplo cuando deba controlar la calidad de la imagen de la diapositiva durante la exportación de PDF a PPTX.

1. Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) y configure `setImageResolution(300)` para obtener una mayor fidelidad de la imagen de la diapositiva.

1. 
Llame a `document.save(outputFile.toString(), saveOptions)` para que se genere contenido de diapositiva rasterizado con la resolución solicitada.

1. 
Guarde la presentación de salida.

```java
public static void convertPdfToPptxImageResolution(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PptxSaveOptions saveOptions = new PptxSaveOptions();
        saveOptions.setImageResolution(300);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
