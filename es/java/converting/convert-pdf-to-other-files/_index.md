---
title: Convierta PDF a EPUB, texto, XPS y más en Java
linktitle: Convertir PDF a otros formatos
type: docs
weight: 90
url: /java/convert-pdf-to-other-files/
lastmod: "2026-06-16"
description: Aprenda a convertir archivos PDF a EPUB, LaTeX, Markdown, texto, XPS y MobiXML en Java con Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Cómo convertir PDF a otros formatos en Java
Abstract: Este artículo explica cómo convertir archivos PDF a formatos EPUB, TeX, Markdown, texto, XPS y MobiXML utilizando Aspose.PDF para Java, con opciones de guardado específicas del formato cuando sea necesario.
---
Aspose.PDF para Java puede exportar documentos PDF a formatos de salida de texto, libros electrónicos, impresos y orientados a marcas.


## 
Convertir PDF a EPUB



Utilice este ejemplo cuando un documento PDF deba exportarse al formato de libro electrónico EPUB.


1. 
Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree [`EpubSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubsaveoptions/) y establezca el modo de reconocimiento en `Flow`.
1. Llame a `document.save(outputFile.toString(), saveOptions)` para que el contenido del PDF se exporte como formato EPUB ajustable.

1. 
Guarde el archivo EPUB convertido.


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

## 
Convertir PDF a TeX



Utilice este ejemplo cuando el contenido PDF deba exportarse al formato TeX.


1. 
Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree [`TeXSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/texsaveoptions/) para la serialización TeX.

1. 
Llame a `document.save(outputFile.toString(), saveOptions)` para que el contenido del PDF se emita como marcado TeX.

1. 
Guarde el archivo TeX resultante.


```java
public static void convertPdfToTex(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), new TeXSaveOptions());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir PDF a texto sin formato



Utilice este ejemplo cuando un documento PDF deba exportarse como un archivo de texto.

1. Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree un [`TextDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/textdevice/) para extraer contenido textual de páginas PDF.

1. 
Llame a `device.process(document.getPages().get_Item(1), outputFile.toString())` para escribir la primera página como texto sin formato.

1. 
Guarde el archivo de salida de texto.


```java
public static void convertPdfToTxt(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextDevice device = new TextDevice();
        device.process(document.getPages().get_Item(1), outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir PDF a XPS

Utilice este ejemplo cuando un documento PDF deba convertirse al formato XPS.


1. 
Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree [`XpsSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xpssaveoptions/) y habilite las fuentes TrueType incrustadas.

1. 
Llame a `document.save(outputFile.toString(), saveOptions)` para que el PDF se serialice como XPS con recursos de fuentes integrados.

1. 
Guarde el archivo XPS convertido.

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

## Convertir PDF a rebajas



Utilice este ejemplo cuando el contenido PDF deba exportarse como Markdown.


1. 
Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree [`MarkdownSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/markdownsaveoptions/) y configure el directorio de recursos de imágenes más la salida de etiqueta de imagen HTML.

1. 
Llame a `document.save(outputFile.toString(), saveOptions)` para que el contenido del PDF se emita como Markdown con recursos de imágenes externos.
1. Guarde el archivo Markdown generado.


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

## 
Convertir PDF a Mobi XML



Utilice este ejemplo cuando el contenido PDF deba exportarse a XML compatible con Mobi.


1. 
Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Seleccione [`SaveFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/saveformat/) `MobiXml` como formato de serialización de destino.
1. Llame a `document.save(outputFile.toString(), SaveFormat.MobiXml)` para que el PDF se exporte como XML compatible con Mobi.

1. 
Guarde el archivo convertido.

```java
public static void convertPdfToMobiXml(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), SaveFormat.MobiXml);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
