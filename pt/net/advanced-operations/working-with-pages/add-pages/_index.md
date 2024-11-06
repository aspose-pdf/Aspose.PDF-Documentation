---
title: Adicionar Páginas ao Documento PDF
linktitle: Adicionar Páginas
type: docs
weight: 10
url: pt/net/add-pages/
description: Este artigo ensina como inserir (adicionar) uma página na localização desejada no arquivo PDF. Aprenda como mover, remover (deletar) páginas de um arquivo PDF usando C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/insert-pdf-pages/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adicionar Páginas em PDF com C#",
    "alternativeHeadline": "Como adicionar Páginas em um documento PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos PDF",
    "keywords": "pdf, c#, adicionar página pdf, inserir página pdf",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipe de Documentação Aspose.PDF",
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
                "contactType": "vendas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "vendas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "vendas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/add-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "Este artigo ensina como inserir (adicionar) uma página na localização desejada no arquivo PDF. Aprenda como mover, remover (deletar) páginas de um arquivo PDF usando C#."
}
</script>
Aspose.PDF para .NET API oferece total flexibilidade para trabalhar com páginas em um documento PDF usando C# ou qualquer outra linguagem .NET. Ele mantém todas as páginas de um documento PDF em [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) que pode ser usado para trabalhar com páginas PDF.
Aspose.PDF para .NET permite inserir uma página em um documento PDF em qualquer local do arquivo, bem como adicionar páginas ao final de um arquivo PDF.
Esta seção mostra como adicionar páginas a um PDF usando C#.

## Adicionar ou Inserir Página em um Arquivo PDF

Aspose.PDF para .NET permite inserir uma página em um documento PDF em qualquer local do arquivo, bem como adicionar páginas ao final de um arquivo PDF.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

### Inserir Página Vazia em um Arquivo PDF no Local Desejado

Para inserir uma página vazia em um arquivo PDF:

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) com o arquivo PDF de entrada.
1.
1. Salve o PDF de saída usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

O seguinte trecho de código mostra como inserir uma página em um arquivo PDF.

```cs
// Para exemplos completos e arquivos de dados, por favor acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// Abrir documento
Document pdfDocument = new Document(dataDir + "InsertEmptyPage.pdf");

// Inserir uma página vazia no PDF
pdfDocument.Pages.Insert(2);
// Salvar arquivo de saída
pdfDocument.Save(dataDir + "InsertEmptyPage_out.pdf");
```

No exemplo acima, adicionamos uma página vazia com parâmetros padrão. Se você precisar fazer com que o tamanho da página seja o mesmo que outra página no documento, você deve adicionar algumas linhas de código:

```cs
var page = pdfDocument.Pages.Insert(2);
//copiar parâmetros de página da página 1
page.ArtBox = pdfDocument.Pages[1].ArtBox;
page.BleedBox = pdfDocument.Pages[1].BleedBox;
page.CropBox = pdfDocument.Pages[1].CropBox;
page.MediaBox = pdfDocument.Pages[1].MediaBox;
page.TrimBox = pdfDocument.Pages[1].TrimBox;
```
### Adicionar uma Página Vazia ao Final de um Arquivo PDF

Às vezes, você deseja garantir que um documento termine em uma página vazia. Este tópico explica como inserir uma página vazia no final do documento PDF.

Para inserir uma página vazia no final de um arquivo PDF:

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) com o arquivo PDF de entrada.
1. Chame o método [Add](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) da coleção [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection), sem nenhum parâmetro.
1. Salve o PDF de saída usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

O seguinte trecho de código mostra como inserir uma página vazia no final de um arquivo PDF.

```cs
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// Abrir documento
Document pdfDocument = new Document(dataDir + "InsertEmptyPageAtEnd.pdf");

// Inserir uma página vazia no final de um arquivo PDF
pdfDocument.Pages.Add();

// Salvar o arquivo de saída
pdfDocument.Save(dataDir + "InsertEmptyPageAtEnd_out.pdf");
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
                "contactType": "vendas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "vendas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "vendas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Biblioteca de Manipulação de PDF para .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

