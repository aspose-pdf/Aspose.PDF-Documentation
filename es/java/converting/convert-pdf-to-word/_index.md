---
title: Convertir PDF a Word en Java
linktitle: Convertir PDF a Word
type: docs
weight: 10
url: /es/java/convert-pdf-to-word/
lastmod: "2026-09-29"
description: Aprende cómo convertir archivos PDF a DOC y DOCX en Java con Aspose.PDF para una edición y reutilización de documentos más fácil.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Convertir PDF a Word en Java
Abstract: Este artículo explica cómo convertir archivos PDF a formatos de Microsoft Word utilizando Aspose.PDF for Java. Cubre la salida DOC, la salida DOCX, la conversión DOCX de flujo mejorado, la preservación de los saltos de línea, el reconocimiento de viñetas y el control de la resolución de imágenes mediante `DocSaveOptions`.
---
Aspose.PDF for Java puede exportar documentos PDF a formatos de Microsoft Word con diferentes opciones de reconocimiento y diseño. Use [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) para controlar cómo se mapean el texto, las listas y las imágenes del PDF en la salida de Word.

## Convertir PDF a DOC

Utilice este ejemplo cuando un documento PDF debe exportarse al formato DOC heredado. El código crea `DocSaveOptions`, establece el formato a `Doc`, y pasa las opciones a un método de guardado compartido.

1. Abra el PDF de origen en una instancia de [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) y establezca el formato a `Doc`.
1. Llame `document.save(outputFile.toString(), saveOptions)` por lo que el PDF se exporta al formato binario de documento de Microsoft Word.
1. Guarde el archivo DOC convertido.

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

Use este ejemplo cuando un documento PDF deba exportarse como un archivo DOCX. DOCX es el formato preferido para la mayoría de los flujos de trabajo de procesamiento de texto nuevos porque está ampliamente soportado y es más fácil de editar.

1. Abra el PDF de origen en una instancia de [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) y establezca el formato a `DocX`.
1. Llame `document.save(outputFile.toString(), saveOptions)` por lo que el contenido del PDF se exporta como un documento Word de Office Open XML.
1. Guarde el archivo DOCX resultante.

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

1. Abra el PDF de origen en una instancia de [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) para `DocX` salida.
1. Habilite `setMode(DocSaveOptions.RecognitionMode.EnhancedFlow)` por lo tanto, el convertidor utiliza reconocimiento de flujo mejorado durante la generación de DOCX.
1. Llame `document.save(outputFile.toString(), saveOptions)` y guarde la salida DOCX convertida.

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

Utilice este ejemplo cuando los retornos de línea del PDF de origen deben conservarse en la salida de Word.

1. Abra el PDF de origen en una instancia de [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) para `DocX` exportar.
1. Habilite `setAddReturnToLineEnd(true)` para que los saltos de línea explícitos se conserven durante la conversión.
1. Llame `document.save(outputFile.toString(), saveOptions)` y guarde el archivo DOCX.

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

Utilice este ejemplo cuando las viñetas de lista del PDF de origen deban reconocerse y preservarse como estructuras de lista en Word.

1. Abra el PDF de origen en una instancia de [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) para `DocX` exportar.
1. Habilite `setRecognizeBullets(true)` por lo que el contenido similar a listas en PDF se reconoce como listas con viñetas durante la conversión.
1. Llame `document.save(outputFile.toString(), saveOptions)` y guarde el archivo DOCX.

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

Utilice este ejemplo cuando la fidelidad de la imagen dentro del DOCX generado deba controlarse durante la conversión.

1. Abra el PDF de origen en una instancia de [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) para `DocX` exportar.
1. Establezca `setImageResolutionX(300)` y `setImageResolutionY(300)` por lo tanto, el contenido raster se genera a la resolución solicitada.
1. Llame `document.save(outputFile.toString(), saveOptions)` y guarde la salida DOCX.

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
