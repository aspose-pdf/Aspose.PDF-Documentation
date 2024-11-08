---
title: Trabalhando com Anexos - Facades
type: docs
weight: 50
url: /pt/net/working-with-attachments-facades/
description: Esta seção explica como trabalhar com Anexos - Facades usando a Classe PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

Nesta seção, explicaremos como trabalhar com anexos em PDF usando Aspose.PDF para .NET Facades. Um anexo é um arquivo adicional que é anexado a um documento pai, podendo ser de vários tipos de arquivos, como pdf, word, imagem ou outros arquivos. Você aprenderá como adicionar anexos a pdf, obter informações de um anexo e salvá-lo em arquivo, excluir o anexo do PDF programaticamente com C#.

## Adicionar Anexo a partir de um Arquivo em um PDF Existente

Você pode adicionar um anexo em um arquivo PDF existente usando a classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). O anexo pode ser adicionado a partir de um arquivo no disco usando o caminho do arquivo. Você pode adicionar um anexo usando o método [AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment). Este método recebe dois argumentos: caminho do arquivo e descrição do anexo. Primeiro, você precisa abrir o arquivo PDF existente e adicionar o anexo a ele. Em seguida, você pode salvar o arquivo PDF de saída usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) de [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor).

O trecho de código a seguir mostra como adicionar um anexo a partir de um arquivo. Por exemplo, vamos adicionar o arquivo MP3.

```csharp
public static void AttachmentDemo01()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        editor.AddDocumentAttachment(@"C:\Samples\file_example_MP3_700KB.mp3","Arquivo MP3 de demonstração");
        editor.Save(_dataDir + "PdfContentEditorDemo07.pdf");
    }
```
## Adicionar Anexo a partir de um Stream em um PDF Existente

Anexo pode ser adicionado em um arquivo PDF a partir de um stream – FileStream – usando o método [AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment). Este método leva três argumentos: stream, nome do anexo e descrição do anexo. Para adicionar o anexo, você precisa criar um objeto da classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) e vincular o arquivo PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Depois disso, você pode chamar o método [AddDocumentAttachment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment) para adicionar o anexo. Finalmente, você pode chamar o método Save para salvar o arquivo PDF atualizado. O trecho de código a seguir mostra como adicionar um anexo a partir de um Stream.

```csharp
public static void AttachmentDemo02()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        var fileStream = System.IO.File.OpenRead(@"C:\Samples\file_example_MP3_700KB.mp3");
        editor.AddDocumentAttachment(fileStream, "file_example_MP3_700KB.mp3", "Arquivo MP3 de Demonstração");
        editor.Save(_dataDir + "PdfContentEditorDemo08.pdf");
    }
```

## Excluir Todos os Anexos de um Arquivo PDF Existente

O método [DeleteAttachments](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments) da classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) permite que você exclua todos os anexos de um arquivo PDF existente. Chame o método [DeleteAttachments](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments). Finalmente, você deve chamar o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) para salvar o arquivo PDF atualizado. O trecho de código a seguir mostra como excluir todos os anexos de um arquivo PDF existente.

```csharp
    public static void DeleteAllAttachments()
    {
        AttachmentDemo02();
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "PdfContentEditorDemo07.pdf"));
        editor.DeleteAttachments();
        editor.Save(_dataDir + "PdfContentEditorDemo09.pdf");
    }
```