---
title: Travailler avec les Pièces Jointes
type: docs
weight: 50
url: /java/working-with-attachments/
description: Cette section explique comment travailler avec des pièces jointes dans votre PDF avec Aspose.PDF Facades - un ensemble d'outils pour les opérations populaires avec PDF.
lastmod: "2021-06-24"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Comment ajouter une pièce jointe en utilisant PdfContentEditor

```java
public static void AttachmentDemo01()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
    editor.addDocumentAttachment(_dataDir + "file_example_MP3_700KB.mp3", "Fichier MP3 de démonstration");
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
    editor.addDocumentAttachment(fileStream, "file_example_MP3_700KB.mp3", "Fichier MP3 de démonstration");
    editor.save(_dataDir + "PdfContentEditorDemo08.pdf");
}
```


## Comment supprimer une pièce jointe à l'aide de PdfContentEditor

```java
public static void DeleteAllAttachments()
{
    AttachmentDemo02();
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "PdfContentEditorDemo07.pdf"));
    // Supprimer toutes les pièces jointes
    editor.deleteAttachments();
    editor.save(_dataDir + "PdfContentEditorDemo09.pdf");
}
```