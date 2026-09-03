---
title: Convertir PDF a PowerPoint en Java
linktitle: Convertir PDF a PowerPoint
type: docs
weight: 30
url: /es/java/convert-pdf-to-powerpoint/
description: Aprenda cómo convertir archivos PDF a PowerPoint en Java con Aspose.PDF, incluyendo diapositivas PPTX editables, diapositivas basadas en imágenes y resolución de imagen personalizada.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo convertir PDF a PowerPoint en Java
Abstract: Este artículo explica cómo convertir archivos PDF en presentaciones PowerPoint usando Aspose.PDF for Java. Cubre la conversión estándar a PPTX, la salida de diapositiva como imagen y el control de la resolución de imagen mediante `PptxSaveOptions`.
---
Aspose.PDF for Java admite exportar páginas PDF a presentaciones PowerPoint editables con opciones de renderizado de diapositivas. Utilice [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) para controlar cómo se asignan las páginas PDF a las diapositivas de PowerPoint.

## Convertir PDF a PPTX

Utilice este ejemplo cuando un documento PDF debe exportarse como una presentación estándar de PowerPoint.

1. Abra el PDF de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear predeterminado [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) para exportación editable de PowerPoint.
1. Llamar `document.save(outputFile.toString(), saveOptions)` por lo que las páginas del PDF se serializan como un `.pptx` presentación.
1. Guarde el archivo PPTX convertido.

```java
public static void convertPdfToPptx(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PptxSaveOptions saveOptions = new PptxSaveOptions();
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir PDF a PPTX con diapositivas como imágenes

Utilice este ejemplo cuando cada página de PDF deba convertirse en una diapositiva de PowerPoint basada en imágenes.

1. Abra el PDF de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) y habilitar `setSlidesAsImages(true)`.
1. Llamar `document.save(outputFile.toString(), saveOptions)` por lo que cada página del PDF se renderiza como una diapositiva respaldada por una imagen en la presentación.
1. Guarde el archivo PPTX generado.

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

## Convertir PDF a PPTX con resolución de imagen personalizada

Utilice este ejemplo cuando la calidad de la imagen de la diapositiva deba controlarse durante la exportación de PDF a PPTX.

1. Abra el PDF de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) y establecer `setImageResolution(300)` para mayor fidelidad de imagen de diapositiva.
1. Llamar `document.save(outputFile.toString(), saveOptions)` por lo tanto, el contenido rasterizado de la diapositiva se genera a la resolución solicitada.
1. Guarde la presentación resultante.

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
