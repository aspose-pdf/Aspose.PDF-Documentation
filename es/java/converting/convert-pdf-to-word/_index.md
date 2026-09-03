---
title: Convertir PDF a Word en Java
linktitle: Convertir PDF a Word
type: docs
weight: 10
url: /es/java/convert-pdf-to-word/
lastmod: "2026-09-03"
description: Aprenda cómo convertir archivos PDF a DOC y DOCX en Java con Aspose.PDF para una edición y reutilización más fácil de documentos.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo convertir PDF a Word en Java
Abstract: Este artículo explica cómo convertir archivos PDF a formatos de Microsoft Word usando Aspose.PDF for Java. Cubre la salida DOC, la salida DOCX, la conversión DOCX de flujo mejorado, la preservación de saltos de línea, el reconocimiento de viñetas y el control de la resolución de imágenes a través de `DocSaveOptions`.
---
Aspose.PDF for Java puede exportar documentos PDF a formatos de Microsoft Word con diferentes opciones de reconocimiento y diseño. Utilice [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) para controlar cómo el texto, las listas y las imágenes de PDF se asignan a la salida de Word.

## Convertir PDF a DOC

Utilice este ejemplo cuando un documento PDF debe exportarse al formato DOC legado. El código crea `DocSaveOptions`, establece el formato a `Doc`, y pasa las opciones a un método de guardado compartido.

1. Abra el PDF de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) y establecer el formato a `Doc`.
1. Llamar `document.save(outputFile.toString(), saveOptions)` por lo tanto, el PDF se exporta al formato de documento binario de Microsoft Word.
1. Guarda el archivo DOC convertido.

```java
public static void convertPdfToDoc(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.Doc);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir PDF a DOCX

Utilice este ejemplo cuando un documento PDF deba exportarse como un archivo DOCX. DOCX es el formato preferido para la mayoría de los flujos de trabajo de procesamiento de texto nuevos porque está ampliamente soportado y es más fácil de editar.

1. Abra el PDF de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) y establecer el formato a `DocX`.
1. Llamar `document.save(outputFile.toString(), saveOptions)` por lo que el contenido del PDF se exporta como un documento de Word de Office Open XML.
1. Guarda el archivo DOCX resultante.

```java
public static void convertPdfToDocx(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir PDF a DOCX con reconocimiento de flujo mejorado

Utilice este ejemplo cuando la exportación a Word deba favorecer contenido editable fluido en lugar de un diseño visual fijo.

1. Abra el PDF de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) para `DocX` salida.
1. Habilitar `setMode(DocSaveOptions.RecognitionMode.EnhancedFlow)` por lo tanto, el conversor utiliza reconocimiento de flujo mejorado durante la generación de DOCX.
1. Llamar `document.save(outputFile.toString(), saveOptions)` y guarda la salida DOCX convertida.

```java
public static void convertPdfToDocxAdvanced(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setMode(DocSaveOptions.RecognitionMode.EnhancedFlow);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir PDF a DOCX con saltos de línea preservados

Utilice este ejemplo cuando se deban conservar los saltos de línea del PDF de origen en la salida de Word.

1. Abra el PDF de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) para `DocX` exportar.
1. Habilitar `setAddReturnToLineEnd(true)` de modo que los saltos de línea explícitos se conserven durante la conversión.
1. Llamar `document.save(outputFile.toString(), saveOptions)` y guarde el archivo DOCX.

```java
public static void convertPdfToDocxWithLineBreaks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setAddReturnToLineEnd(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir PDF a DOCX con reconocimiento de viñetas

Utilice este ejemplo cuando los viñetas de la lista del PDF de origen deben ser reconocidas y conservadas como estructuras de lista en Word.

1. Abra el PDF de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) para `DocX` exportar.
1. Habilitar `setRecognizeBullets(true)` por lo que el contenido tipo lista del PDF se reconoce como listas con viñetas durante la conversión.
1. Llamar `document.save(outputFile.toString(), saveOptions)` y guarde el archivo DOCX.

```java
public static void convertPdfToDocxWithBulletRecognition(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setRecognizeBullets(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir PDF a DOCX con resolución de imagen personalizada

Utilice este ejemplo cuando la fidelidad de la imagen dentro del DOCX generado debe controlarse durante la conversión.

1. Abra el PDF de origen en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) para `DocX` exportar.
1. Establecer `setImageResolutionX(300)` y `setImageResolutionY(300)` Así que el contenido raster se genera a la resolución solicitada.
1. Llamar `document.save(outputFile.toString(), saveOptions)` y guarde la salida DOCX.

```java
public static void convertPdfToDocxWithImageResolution(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setImageResolutionX(300);
        saveOptions.setImageResolutionY(300);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
