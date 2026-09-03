---
title: Convertir PDF a Word en Java
linktitle: Convertir PDF a Word
type: docs
weight: 10
url: /java/convert-pdf-to-word/
lastmod: "2026-06-16"
description: Aprenda a convertir archivos PDF a DOC y DOCX en Java con Aspose.PDF para editar y reutilizar documentos más fácilmente.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo convertir PDF a Word en Java
Abstract: Este artículo explica cómo convertir archivos PDF a formatos de Microsoft Word usando Aspose.PDF para Java. Cubre salida DOC, salida DOCX, conversión DOCX de flujo mejorado, saltos de línea preservados, reconocimiento de viñetas y control de resolución de imagen a través de `DocSaveOptions`.
---
Aspose.PDF para Java puede exportar documentos PDF a formatos de Microsoft Word con diferentes opciones de reconocimiento y diseño. Utilice [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) para controlar cómo se asignan el texto, las listas y las imágenes del PDF a la salida de Word.


## 
Convertir PDF a DOC



Utilice este ejemplo cuando deba exportar un documento PDF al formato DOC heredado. El código crea `DocSaveOptions`, establece el formato en `Doc` y pasa las opciones a un método de guardado compartido.


1. Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) y establezca el formato en `Doc`.
1. Llame a `document.save(outputFile.toString(), saveOptions)` para que el PDF se exporte al formato de documento binario de Microsoft Word.

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

## 
Convertir PDF a DOCX



Utilice este ejemplo cuando un documento PDF deba exportarse como un archivo DOCX. DOCX es el formato preferido para la mayoría de los nuevos flujos de trabajo de procesamiento de textos porque es ampliamente compatible y más fácil de editar.


1. Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) y establezca el formato en `DocX`.

1. Llame a `document.save(outputFile.toString(), saveOptions)` para que el contenido del PDF se exporte como un documento de Office Open XML Word.

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

## 
Convierta PDF a DOCX con reconocimiento de flujo mejorado



Utilice este ejemplo cuando la exportación de Word deba favorecer el contenido editable fluido en lugar del diseño visual fijo.

1. Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) para la salida `DocX`.

1. Habilite `setMode(DocSaveOptions.RecognitionMode.EnhancedFlow)` para que el convertidor utilice un reconocimiento de flujo mejorado durante la generación de DOCX.

1. Llame a `document.save(outputFile.toString(), saveOptions)` y guarde la salida DOCX convertida.


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

## 
Convierta PDF a DOCX con saltos de línea conservados

Utilice este ejemplo cuando los finales de línea del PDF de origen deban conservarse en la salida de Word.


1. Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) para exportar `DocX`.

1. Habilite `setAddReturnToLineEnd(true)` para que los saltos de línea explícitos se conserven durante la conversión.

1. Llame a `document.save(outputFile.toString(), saveOptions)` y guarde el archivo DOCX.

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

## Convierta PDF a DOCX con reconocimiento de viñetas



Utilice este ejemplo cuando las viñetas de lista del PDF de origen deban reconocerse y conservarse como estructuras de lista en Word.


1. Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) para exportar `DocX`.

1. Habilite `setRecognizeBullets(true)` para que el contenido PDF tipo lista se reconozca como listas con viñetas durante la conversión.
1. Llame a `document.save(outputFile.toString(), saveOptions)` y guarde el archivo DOCX.


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

## 
Convierta PDF a DOCX con resolución de imagen personalizada



Utilice este ejemplo cuando la fidelidad de la imagen dentro del DOCX generado deba controlarse durante la conversión.


1. Abra el PDF de origen en una instancia [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) para exportar `DocX`.
1. Configure `setImageResolutionX(300)` y `setImageResolutionY(300)` para que el contenido rasterizado se genere con la resolución solicitada.

1. Llame a `document.save(outputFile.toString(), saveOptions)` y guarde la salida DOCX.

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
