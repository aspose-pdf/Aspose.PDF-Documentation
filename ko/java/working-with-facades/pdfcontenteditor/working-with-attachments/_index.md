---
title: 첨부 파일 작업하기
type: docs
weight: 50
url: /ko/java/working-with-attachments/
description: 이 섹션에서는 Aspose.PDF Facades를 사용하여 PDF에서 첨부 파일을 작업하는 방법을 설명합니다. 이 도구는 PDF와 관련된 일반적인 작업을 수행하는 도구 모음입니다.
lastmod: "2021-06-24"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PdfContentEditor를 사용하여 첨부 파일 추가하는 방법

```java
public static void AttachmentDemo01()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
    editor.addDocumentAttachment(_dataDir + "file_example_MP3_700KB.mp3", "데모 MP3 파일");
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
    editor.addDocumentAttachment(fileStream, "file_example_MP3_700KB.mp3", "데모 MP3 파일");
    editor.save(_dataDir + "PdfContentEditorDemo08.pdf");
}
```


## 첨부 파일 삭제 방법 PdfContentEditor 사용하기

```java
public static void DeleteAllAttachments()
{
    AttachmentDemo02();
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "PdfContentEditorDemo07.pdf"));
    // 첨부 파일 삭제
    editor.deleteAttachments();
    editor.save(_dataDir + "PdfContentEditorDemo09.pdf");
}
```