---
title: Travailler avec les Pièces Jointes - Facades
type: docs
weight: 50
url: /net/working-with-attachments-facades/
description: Cette section explique comment travailler avec les pièces jointes - Facades en utilisant la classe PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

Dans cette section, nous expliquerons comment travailler avec les pièces jointes dans un PDF en utilisant Aspose.PDF pour .NET Facades. Une pièce jointe est un fichier supplémentaire qui est attaché à un document parent, il peut s'agir de divers types de fichiers, tels que pdf, word, image ou d'autres fichiers. Vous apprendrez comment ajouter des pièces jointes à un pdf, obtenir les informations d'une pièce jointe, et la sauvegarder dans un fichier, supprimer la pièce jointe du PDF par programmation avec C#.

## Ajouter une Pièce Jointe à partir d'un Fichier dans un PDF Existant

Vous pouvez ajouter une pièce jointe dans un fichier PDF existant en utilisant la classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). L'attachement peut être ajouté à partir d'un fichier sur le disque en utilisant le chemin du fichier. Vous pouvez ajouter une pièce jointe en utilisant la méthode [AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment). Cette méthode prend deux arguments : le chemin du fichier et la description de la pièce jointe. Tout d'abord, vous devez ouvrir le fichier PDF existant et y ajouter la pièce jointe. Ensuite, vous pouvez enregistrer le fichier PDF de sortie en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) de [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor).

Le code suivant vous montre comment ajouter une pièce jointe à partir d'un fichier. Par exemple, ajoutons le fichier MP3.

```csharp
public static void AttachmentDemo01()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        editor.AddDocumentAttachment(@"C:\Samples\file_example_MP3_700KB.mp3","Démo fichier MP3");
        editor.Save(_dataDir + "PdfContentEditorDemo07.pdf");
    }
```
## Ajouter une Pièce Jointe à partir d'un Flux dans un PDF Existant

Une pièce jointe peut être ajoutée dans un fichier PDF à partir d'un flux – FileStream – en utilisant la méthode [AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment). Cette méthode prend trois arguments : le flux, le nom de la pièce jointe et la description de la pièce jointe. Afin d'ajouter une pièce jointe, vous devez créer un objet de la classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) et lier le fichier PDF d'entrée à l'aide de la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Après cela, vous pouvez appeler la méthode [AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment) pour ajouter la pièce jointe. Enfin, vous pouvez appeler la méthode Save pour enregistrer le fichier PDF mis à jour. L'extrait de code suivant vous montre comment ajouter une pièce jointe à partir d'un flux.

```csharp
public static void AttachmentDemo02()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        var fileStream = System.IO.File.OpenRead(@"C:\Samples\file_example_MP3_700KB.mp3");
        editor.AddDocumentAttachment(fileStream, "file_example_MP3_700KB.mp3", "Demo MP3 file");
        editor.Save(_dataDir + "PdfContentEditorDemo08.pdf");
    }
```

## Supprimer toutes les pièces jointes d'un fichier PDF existant

La méthode [DeleteAttachments](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments) de la classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) vous permet de supprimer toutes les pièces jointes d'un fichier PDF existant. Appelez la méthode [DeleteAttachments](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments). Enfin, vous devez appeler la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) pour enregistrer le fichier PDF mis à jour. L'extrait de code suivant vous montre comment supprimer toutes les pièces jointes d'un fichier PDF existant.

```csharp
    public static void DeleteAllAttachments()
    {
        AttachmentDemo02();
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "PdfContentEditorDemo07.pdf"));
        editor.DeleteAttachments();
        editor.Save(_dataDir + "PdfContentEditorDemo09.pdf");
    }
```