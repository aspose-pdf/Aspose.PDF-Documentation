---
title: Adicionar e Excluir um Marcador
linktitle: Adicionar e Excluir um Marcador
type: docs
weight: 10
url: pt/net/add-and-delete-bookmark/
description: Você pode adicionar um marcador a um documento PDF com C#. É possível excluir todos ou determinados marcadores de um documento PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/add-and-delete-a-bookmark/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adicionar e Excluir um Marcador",
    "alternativeHeadline": "Como adicionar e excluir Marcador de PDF",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "geração de documento PDF",
    "keywords": "pdf, c#, excluir marcador, adicionar marcador",
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
    "url": "/net/add-and-delete-bookmark/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-and-delete-bookmark/"
    },
    "dateModified": "2022-02-04",
    "description": "Você pode adicionar um marcador a um documento PDF com C#. É possível excluir todos ou determinados marcadores de um documento PDF."
}
</script>
O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Adicionar um Marcador a um Documento PDF

Os marcadores estão contidos na coleção [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) do objeto Document, que por sua vez está na coleção [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection).

Para adicionar um marcador a um PDF:

1. Abra um documento PDF usando o objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Crie um marcador e defina suas propriedades.
1. Adicione a coleção [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) à coleção de Outlines.

O seguinte trecho de código mostra como adicionar um marcador em um documento PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// Abrir documento
Document pdfDocument = new Document(dataDir + "AddBookmark.pdf");

// Criar um objeto de marcador
OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.Outlines);
pdfOutline.Title = "Test Outline";
pdfOutline.Italic = true;
pdfOutline.Bold = true;
// Definir o número da página de destino
pdfOutline.Action = new GoToAction(pdfDocument.Pages[1]);
// Adicionar marcador na coleção de outline do documento.
pdfDocument.Outlines.Add(pdfOutline);

dataDir = dataDir + "AddBookmark_out.pdf";
// Salvar saída
pdfDocument.Save(dataDir);
```
## Adicionar um Marcador Filho ao Documento PDF

Os marcadores podem ser aninhados, indicando uma relação hierárquica com marcadores pai e filho. Este artigo explica como adicionar um marcador filho, ou seja, um marcador de segundo nível, a um PDF.

Para adicionar um marcador filho a um arquivo PDF, primeiro adicione um marcador pai:

1. Abra um documento.
1. Adicione um marcador à [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection), definindo suas propriedades.
1. Adicione a OutlineItemCollection à coleção [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection) do objeto Document.

O marcador filho é criado da mesma forma que o marcador pai, explicado acima, mas é adicionado à coleção de Outlines do marcador pai.

Os seguintes trechos de código mostram como adicionar um marcador filho a um documento PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor, acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// Abrir documento
Document pdfDocument = new Document(dataDir + "AddChildBookmark.pdf");

// Criar um objeto de marcador pai
OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.Outlines);
pdfOutline.Title = "Parent Outline";
pdfOutline.Italic = true;
pdfOutline.Bold = true;

// Criar um objeto de marcador filho
OutlineItemCollection pdfChildOutline = new OutlineItemCollection(pdfDocument.Outlines);
pdfChildOutline.Title = "Child Outline";
pdfChildOutline.Italic = true;
pdfChildOutline.Bold = true;

// Adicionar marcador filho na coleção do marcador pai
pdfOutline.Add(pdfChildOutline);
// Adicionar marcador pai na coleção de marcadores do documento.
pdfDocument.Outlines.Add(pdfOutline);

dataDir = dataDir + "AddChildBookmark_out.pdf";
// Salvar saída
pdfDocument.Save(dataDir);
```
## Excluir todos os Favoritos de um Documento PDF

Todos os favoritos em um PDF estão contidos na coleção [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection). Este artigo explica como excluir todos os favoritos de um arquivo PDF.

Para excluir todos os favoritos de um arquivo PDF:

1. Chame o método Delete da coleção [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection).
1. Salve o arquivo modificado usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) do objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

Os seguintes trechos de código mostram como excluir todos os favoritos de um documento PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor, visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// Abrir documento
Document pdfDocument = new Document(dataDir + "DeleteAllBookmarks.pdf");

// Excluir todos os favoritos
pdfDocument.Outlines.Delete();

dataDir = dataDir + "DeleteAllBookmarks_out.pdf";
// Salvar arquivo atualizado
pdfDocument.Save(dataDir);
```
## Excluir um Favorito Específico de um Documento PDF

Para excluir um favorito específico de um arquivo PDF:

1. Passe o título do favorito como parâmetro para o método Delete da coleção [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection).
1. Em seguida, salve o arquivo atualizado com o método Save do objeto Document.

A classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) fornece a coleção [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection). O método [Delete](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection/methods/delete) remove qualquer favorito com o título passado para o método.

Os seguintes trechos de código mostram como excluir um favorito específico do documento PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// Abrir documento
Document pdfDocument = new Document(dataDir + "DeleteParticularBookmark.pdf");

// Excluir um favorito específico pelo Título
pdfDocument.Outlines.Delete("Child Outline");

// Salvar o arquivo atualizado
pdfDocument.Save(dataDir + "DeleteParticularBookmark_out.pdf");
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF para .NET Library",
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
    "applicationCategory": "Biblioteca de manipulação de PDF para .NET",
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

