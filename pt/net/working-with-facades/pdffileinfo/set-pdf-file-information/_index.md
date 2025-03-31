---
title: Definir Informações do Arquivo PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /pt/net/set-pdf-file-information/
description: Esta seção explica como definir informações do arquivo PDF com Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set PDF File Information",
    "alternativeHeadline": "Set Custom Metadata for PDF Files Effortlessly",
    "abstract": "Melhore a gestão do seu arquivo PDF com a nova funcionalidade em Aspose.PDF for .NET que permite definir e atualizar facilmente informações específicas do arquivo, como Autor, Título e Palavras-chave. Utilize a classe PdfFileInfo para modificar seus PDFs de forma eficiente, adicionando metadados valiosos para melhorar a organização e a capacidade de busca. Otimize seu fluxo de trabalho salvando essas atualizações de forma contínua com o método SaveNewInfo",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "251",
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
    "url": "/net/set-pdf-file-information/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/set-pdf-file-information/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

A classe [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) permite que você defina informações específicas do arquivo de um arquivo PDF. Você precisa criar um objeto da classe [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) e, em seguida, definir diferentes propriedades específicas do arquivo, como Autor, Título, Palavra-chave e Criador, etc. Por fim, salve o arquivo PDF atualizado usando o método [SaveNewInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileinfo/savenewinfo/methods/1) do objeto [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo).

O seguinte trecho de código mostra como definir informações do arquivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPdfInfo()
{
    // Define the directory for input and output files
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create PdfFileInfo object to work with PDF metadata
    using (var fileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "sample.pdf"))
    {
        // Set PDF information
        fileInfo.Author = "Aspose";
        fileInfo.Title = "Hello World!";
        fileInfo.Keywords = "Peace and Development";
        fileInfo.Creator = "Aspose";
        
        // Save the PDF with updated information
        fileInfo.SaveNewInfo(dataDir + "SetFileInfo_out.pdf");
    }
}
```

## Definir Meta Informações

O método [SetMetaInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/methods/setmetainfo) permite que você adicione qualquer informação. No nosso exemplo, adicionamos um campo. Confira o próximo trecho de código:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetMetaInfo()
{
    // Define the directory for input and output files
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of the PdfFileInfo object
    using (var fileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "sample.pdf"))
    {
        // Set a new custom attribute as meta info
        fileInfo.SetMetaInfo("Reviewer", "Aspose.PDF user");

        // Save the updated file
        fileInfo.SaveNewInfo(dataDir + "SetMetaInfo_out.pdf");
    }
}
```