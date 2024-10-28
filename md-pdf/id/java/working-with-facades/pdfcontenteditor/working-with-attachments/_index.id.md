---
title: Bekerja dengan Lampiran
type: docs
weight: 50
url: /java/working-with-attachments/
description: Bagian ini menjelaskan cara bekerja dengan lampiran dalam PDF Anda dengan Aspose.PDF Facades - seperangkat alat untuk operasi populer dengan PDF.
lastmod: "2021-06-24"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Cara menambahkan lampiran menggunakan PdfContentEditor

```java
public static void AttachmentDemo01()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
    editor.addDocumentAttachment(_dataDir + "file_example_MP3_700KB.mp3", "File MP3 Demo");
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
    editor.addDocumentAttachment(fileStream, "file_example_MP3_700KB.mp3", "File MP3 Demo");
    editor.save(_dataDir + "PdfContentEditorDemo08.pdf");
}
```


## Cara menghapus lampiran menggunakan PdfContentEditor

```java
public static void DeleteAllAttachments()
{
    AttachmentDemo02();
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "PdfContentEditorDemo07.pdf"));
    // Menghapus semua lampiran
    editor.deleteAttachments();
    editor.save(_dataDir + "PdfContentEditorDemo09.pdf");
}
```