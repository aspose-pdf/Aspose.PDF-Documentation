---
title: Working with Attachments
type: docs
weight: 50
url: /java/working-with-attachments/
description: This section explains how to work with attachments in your PDF with Aspose.PDF Facades - a toolset for popular operations with PDF.
lastmod: "2021-06-24"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## How to add attachment using PdfContentEditor

```java
public static void AttachmentDemo01()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
    editor.addDocumentAttachment(_dataDir + "file_example_MP3_700KB.mp3", "Demo MP3 file");
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
    editor.addDocumentAttachment(fileStream, "file_example_MP3_700KB.mp3", "Demo MP3 file");
    editor.save(_dataDir + "PdfContentEditorDemo08.pdf");
}
```

## How to delete attachment using PdfContentEditor

```java
public static void DeleteAllAttachments()
{
    AttachmentDemo02();
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "PdfContentEditorDemo07.pdf"));
    editor.deleteAttachments();
    editor.save(_dataDir + "PdfContentEditorDemo09.pdf");
}
```
