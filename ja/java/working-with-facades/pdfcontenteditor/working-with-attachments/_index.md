---
title: 添付ファイルの操作
type: docs
weight: 50
url: ja/java/working-with-attachments/
description: このセクションでは、Aspose.PDF Facades を使用して PDF 内の添付ファイルを操作する方法を説明します。これは、PDF に対する一般的な操作のためのツールセットです。
lastmod: "2021-06-24"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PdfContentEditorを使用して添付ファイルを追加する方法

```java
public static void AttachmentDemo01()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
    editor.addDocumentAttachment(_dataDir + "file_example_MP3_700KB.mp3", "デモ MP3 ファイル");
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
    editor.addDocumentAttachment(fileStream, "file_example_MP3_700KB.mp3", "デモ MP3 ファイル");
    editor.save(_dataDir + "PdfContentEditorDemo08.pdf");
}
```


## 添付ファイルを削除する方法 PdfContentEditor を使用する

```java
public static void DeleteAllAttachments()
{
    AttachmentDemo02();
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "PdfContentEditorDemo07.pdf"));
    editor.deleteAttachments();
    editor.save(_dataDir + "PdfContentEditorDemo09.pdf");
}
```