---
title: Trabajando con Archivos Adjuntos
type: docs
weight: 50
url: /java/working-with-attachments/
description: Esta sección explica cómo trabajar con archivos adjuntos en tu PDF con Aspose.PDF Facades - un conjunto de herramientas para operaciones populares con PDF.
lastmod: "2021-06-24"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Cómo agregar un archivo adjunto usando PdfContentEditor

```java
public static void AttachmentDemo01()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
    editor.addDocumentAttachment(_dataDir + "file_example_MP3_700KB.mp3", "Archivo MP3 de demostración");
    editor.save(_dataDir + "PdfContentEditorDemo07.pdf");
}
```

```java
public static void AttachmentDemo02()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
    FileInputStream fileStream=null;
    try {
        fileStream = new FileInputStream(_dataDir + "file_example_MP3_700KB.mp3");
    } catch (FileNotFoundException e) {            
        e.printStackTrace();
    }
    editor.addDocumentAttachment(fileStream, "file_example_MP3_700KB.mp3", "Archivo MP3 de demostración");
    editor.save(_dataDir + "PdfContentEditorDemo08.pdf");
}
```


## Cómo eliminar un adjunto usando PdfContentEditor

```java
public static void DeleteAllAttachments()
{
    AttachmentDemo02();
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "PdfContentEditorDemo07.pdf"));
    editor.deleteAttachments(); // Eliminar adjuntos
    editor.save(_dataDir + "PdfContentEditorDemo09.pdf"); // Guardar el documento
}
```