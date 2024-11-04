---
title: Trabalhando com Anexos
type: docs
weight: 50
url: /java/working-with-attachments/
description: Esta seção explica como trabalhar com anexos em seu PDF com Aspose.PDF Facades - um conjunto de ferramentas para operações populares com PDF.
lastmod: "2021-06-24"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Como adicionar anexo usando PdfContentEditor

```java
public static void AttachmentDemo01()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
    editor.addDocumentAttachment(_dataDir + "file_example_MP3_700KB.mp3", "Arquivo MP3 de demonstração");
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
    editor.addDocumentAttachment(fileStream, "file_example_MP3_700KB.mp3", "Arquivo MP3 de demonstração");
    editor.save(_dataDir + "PdfContentEditorDemo08.pdf");
}
```


## Como excluir anexos usando PdfContentEditor

```java
public static void DeleteAllAttachments()
{
    AttachmentDemo02();
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "PdfContentEditorDemo07.pdf"));
    // Exclui todos os anexos
    editor.deleteAttachments();
    editor.save(_dataDir + "PdfContentEditorDemo09.pdf");
}
```