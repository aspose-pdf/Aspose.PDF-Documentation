---
title: Convertir PDF a EPUB, Texto, XPS y más en Java
linktitle: Convertir PDF a otros formatos
type: docs
weight: 90
url: /es/java/convert-pdf-to-other-files/
lastmod: "2026-09-03"
description: Aprenda cómo convertir archivos PDF a EPUB, LaTeX, Markdown, texto, XPS y MobiXML en Java con Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Cómo convertir PDF a otros formatos en Java
Abstract: Este artículo explica cómo convertir archivos PDF a formatos EPUB, TeX, Markdown, texto, XPS y MobiXML utilizando Aspose.PDF for Java, con opciones de guardado específicas del formato cuando sea necesario.
---
Aspose.PDF for Java puede exportar documentos PDF a formatos de salida orientados a texto, libros electrónicos, impresión y marcado.

## Convertir PDF a EPUB

Utilice este ejemplo cuando un documento PDF deba exportarse al formato de libro electrónico EPUB.

1. Abra el PDF de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear [`EpubSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubsaveoptions/) y establecer el modo de reconocimiento en `Flow`.
1. Llamar `document.save(outputFile.toString(), saveOptions)` por lo que el contenido del PDF se exporta como marcado EPUB refluible.
1. Guarda el archivo EPUB convertido.

```java
public static void convertPdfToEpub(Path inputFile, Path outputFile) {
        try (Document document = new Document(inputFile.toString())) {
            EpubSaveOptions saveOptions = new EpubSaveOptions();
            saveOptions.setContentRecognitionMode(EpubSaveOptions.RecognitionMode.Flow);
            document.save(outputFile.toString(), saveOptions);
        }
        System.out.println(inputFile + " converted into " + outputFile);
    }
```

## Convertir PDF a TeX

Utilice este ejemplo cuando el contenido del PDF deba exportarse a marcado TeX.

1. Abra el PDF de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear [`TeXSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/texsaveoptions/) para la serialización de TeX.
1. Llamar `document.save(outputFile.toString(), saveOptions)` por lo tanto el contenido del PDF se emite como marcado TeX.
1. Guarda el archivo TeX resultante.

```java
public static void convertPdfToTex(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), new TeXSaveOptions());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir PDF a texto sin formato

Utilice este ejemplo cuando un documento PDF debe exportarse como un archivo de texto.

1. Abra el PDF de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear un [`TextDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/textdevice/) para extraer contenido textual de las páginas PDF.
1. Llamar `device.process(document.getPages().get_Item(1), outputFile.toString())` para escribir la primera página como texto plano.
1. Guardar el archivo de salida de texto.

```java
public static void convertPdfToTxt(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextDevice device = new TextDevice();
        device.process(document.getPages().get_Item(1), outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir PDF a XPS

Utilice este ejemplo cuando se deba convertir un documento PDF al formato XPS.

1. Abra el PDF de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear [`XpsSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xpssaveoptions/) y habilitar fuentes TrueType incrustadas.
1. Llamar `document.save(outputFile.toString(), saveOptions)` por lo que el PDF se serializa como XPS con recursos de Font incrustados.
1. Guarda el archivo XPS convertido.

```java
public static void convertPdfToXps(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        XpsSaveOptions saveOptions = new XpsSaveOptions();
        saveOptions.setUseEmbeddedTrueTypeFonts(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir PDF a Markdown

Utilice este ejemplo cuando el contenido del PDF debe exportarse como Markdown.

1. Abra el PDF de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear [`MarkdownSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/markdownsaveoptions/) y configure el directorio de recursos de imágenes más la salida de etiquetas de imagen HTML.
1. Llamar `document.save(outputFile.toString(), saveOptions)` por lo tanto, el contenido del PDF se emite como Markdown con recursos de imagen externos.
1. Guarda el archivo Markdown generado.

```java
public static void convertPdfToMd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
        saveOptions.setResourcesDirectoryName("images");
        saveOptions.setUseImageHtmlTag(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir PDF a Mobi XML

Utilice este ejemplo cuando el contenido del PDF deba exportarse a XML compatible con Mobi.

1. Abra el PDF de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Seleccionar [`SaveFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/saveformat/) `MobiXml` como el formato de serialización de destino.
1. Llamar `document.save(outputFile.toString(), SaveFormat.MobiXml)` por lo que el PDF se exporta como XML compatible con Mobi.
1. Guarde el archivo convertido.

```java
public static void convertPdfToMobiXml(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), SaveFormat.MobiXml);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
