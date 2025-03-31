---
title: Trabalhando com Anexos - Facades
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /pt/net/working-with-attachments-facades/
description: Esta seção explica como trabalhar com Anexos - Facades usando a classe PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Attachments - Facades",
    "alternativeHeadline": "Enhanced PDF Attachment Management",
    "abstract": "O recurso Trabalhando com Anexos - Facades em Aspose.PDF for .NET permite que os usuários gerenciem facilmente anexos de arquivos dentro de documentos PDF. Com funcionalidades para adicionar, recuperar e remover vários tipos de arquivos programaticamente usando a classe PdfContentEditor, este recurso simplifica o processo de aprimoramento da interatividade do PDF, permitindo que anexos sejam integrados de forma contínua.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "589",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/working-with-attachments-facades/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-attachments-facades/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

Nesta seção, explicaremos como trabalhar com anexos em PDF usando Aspose.PDF for .NET Facades. Um anexo é um arquivo adicional que está anexado a um documento pai, podendo ser uma variedade de tipos de arquivos, como pdf, word, imagem ou outros arquivos. Você aprenderá como adicionar anexos a pdf, obter as informações de um anexo e salvá-lo em um arquivo, excluir o anexo do PDF programaticamente com C#.

## Adicionar Anexo de um Arquivo em um PDF Existente

Você pode adicionar um anexo em um arquivo PDF existente usando a classe [PdfContentEditor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfcontenteditor). O anexo pode ser adicionado de um arquivo no disco usando o caminho do arquivo. Você pode adicionar o anexo usando o método [AddDocumentAttachment](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment). Este método aceita dois argumentos: caminho do arquivo e descrição do anexo. Primeiro, você precisa abrir o arquivo PDF existente e adicionar o anexo a ele. Em seguida, você pode salvar o arquivo PDF de saída usando o método [Save](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document/methods/save/index) da classe [PdfContentEditor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfcontenteditor).

O seguinte trecho de código mostra como adicionar um anexo de um arquivo. Por exemplo, vamos adicionar o arquivo MP3.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAttachment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor =  new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "AddAttachment.pdf")))
    {
        editor.AddDocumentAttachment(dataDir + "Demo_MP3.mp3", "Demo MP3 file");

        // Save PDF document
        editor.Save(dataDir + "AddAttachment_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAttachment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "AddAttachment.pdf"));
    editor.AddDocumentAttachment(dataDir + "Demo_MP3.mp3", "Demo MP3 file");

    // Save PDF document
    editor.Save(dataDir + "AddAttachment_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Adicionar Anexo de um Stream em um PDF Existente

O anexo pode ser adicionado em um arquivo PDF a partir de um stream – FileStream – usando o método [AddDocumentAttachment](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment). Este método aceita três argumentos: stream, nome do anexo e descrição do anexo. Para adicionar um anexo, você precisa criar um objeto da classe [PdfContentEditor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfcontenteditor) e vincular o arquivo PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/facade/methods/bindpdf/index). Depois disso, você pode chamar o método [AddDocumentAttachment](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfcontenteditor/methods/adddocumentattachment) para adicionar o anexo. Finalmente, você pode chamar o método Save para salvar o arquivo PDF atualizado. O seguinte trecho de código mostra como adicionar um anexo de um Stream.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAttachment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "AddAttachment.pdf")))
    {
        var fileStream = File.OpenRead(dataDir + "Demo_MP3.mp3");
        editor.AddDocumentAttachment(fileStream, "Demo_MP3.mp3", "Demo MP3 file");

        // Save PDF document
        editor.Save(dataDir + "AddAttachment_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAttachment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "AddAttachment.pdf"));

    var fileStream = File.OpenRead(dataDir + "Demo_MP3.mp3");
    editor.AddDocumentAttachment(fileStream, "Demo_MP3.mp3", "Demo MP3 file");

    // Save PDF document
    editor.Save(dataDir + "AddAttachment_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Excluir Todos os Anexos de um Arquivo PDF Existente

O método [DeleteAttachments](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments) da classe [PdfContentEditor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfcontenteditor) permite que você exclua todos os anexos de um arquivo PDF existente. Chame o método [DeleteAttachments](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteattachments). Finalmente, você deve chamar o método [Save](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document/methods/save/index) para salvar o arquivo PDF atualizado. O seguinte trecho de código mostra como excluir todos os anexos de um arquivo PDF existente.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteAllAttachments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "DeleteAllAttachments.pdf")))
    {
        editor.DeleteAttachments();

        // Save PDF document
        editor.Save(dataDir + "DeleteAllAttachments_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteAllAttachments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor(new Aspose.Pdf.Document(dataDir + "DeleteAllAttachments.pdf"));
    editor.DeleteAttachments();

    // Save PDF document
    editor.Save(dataDir + "DeleteAllAttachments_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}