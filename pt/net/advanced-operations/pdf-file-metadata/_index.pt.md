---
title: Trabalhando com Metadados de Arquivos PDF | C#
linktitle: Metadados de Arquivo PDF
type: docs
weight: 140
url: /net/pdf-file-metadata/
description: Esta seção explica como obter informações de arquivos PDF, como obter Metadados XMP de um arquivo PDF, definir informações de arquivo PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Trabalhando com Metadados de Arquivos PDF | C#",
    "alternativeHeadline": "Como obter Metadados de Arquivos PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos PDF",
    "keywords": "pdf, c#, metadados de arquivo pdf",
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
    "url": "/net/pdf-file-metadata/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-file-metadata/"
    },
    "dateModified": "2022-02-04",
    "description": "Esta seção explica como obter informações de arquivos PDF, como obter Metadados XMP de um arquivo PDF, definir informações de arquivo PDF."
}
</script>
O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Obter Informações do Arquivo PDF

Para obter informações específicas de um arquivo PDF, você primeiro precisa obter o objeto [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo) usando a propriedade [Info](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/info) do objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Uma vez que o objeto [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo) é recuperado, você pode obter os valores das propriedades individuais. O seguinte trecho de código mostra como obter informações do arquivo PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Abrir documento
Document pdfDocument = new Document(dataDir + "GetFileInfo.pdf");
// Obter informações do documento
DocumentInfo docInfo = pdfDocument.Info;
// Exibir informações do documento
Console.WriteLine("Autor: {0}", docInfo.Author);
Console.WriteLine("Data de Criação: {0}", docInfo.CreationDate);
Console.WriteLine("Palavras-chave: {0}", docInfo.Keywords);
Console.WriteLine("Data de Modificação: {0}", docInfo.ModDate);
Console.WriteLine("Assunto: {0}", docInfo.Subject);
Console.WriteLine("Título: {0}", docInfo.Title);
```
## Definir Informações do Arquivo PDF

Aspose.PDF para .NET permite que você defina informações específicas do arquivo para um PDF, informações como autor, data de criação, assunto e título. Para definir essas informações:

1. Crie um objeto [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo).
1. Defina os valores das propriedades.
1. Salve o documento atualizado usando o método Save da classe Document.

{{% alert color="primary" %}}

Observe que você não pode definir valores para os campos *Application* e *Producer*, porque Aspose Ltd. e Aspose.PDF para .NET x.x.x serão exibidos nesses campos.

{{% /alert %}}

O seguinte trecho de código mostra como definir as informações do arquivo PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor, acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Abrir documento
Document pdfDocument = new Document(dataDir + "SetFileInfo.pdf");

// Especificar informações do documento
DocumentInfo docInfo = new DocumentInfo(pdfDocument);

docInfo.Author = "Aspose";
docInfo.CreationDate = DateTime.Now;
docInfo.Keywords = "Aspose.Pdf, DOM, API";
docInfo.ModDate = DateTime.Now;
docInfo.Subject = "Informações do PDF";
docInfo.Title = "Definindo Informações do Documento PDF";

dataDir = dataDir + "SetFileInfo_out.pdf";
// Salvar documento de saída
pdfDocument.Save(dataDir);
```
## Obter Metadados XMP de um Arquivo PDF

Aspose.PDF permite que você acesse os metadados XMP de um arquivo PDF. Para obter os metadados de um arquivo PDF:

1. Crie um objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) e abra o arquivo PDF de entrada.
1. Obtenha os metadados do arquivo usando a propriedade [Metadata](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/metadata).

O seguinte trecho de código mostra como obter metadados do arquivo PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Abrir documento
Document pdfDocument = new Document(dataDir + "GetXMPMetadata.pdf");

// Obter propriedades
Console.WriteLine(pdfDocument.Metadata["xmp:CreateDate"]);
Console.WriteLine(pdfDocument.Metadata["xmp:Nickname"]);
Console.WriteLine(pdfDocument.Metadata["xmp:CustomProperty"]);
```

## Definir Metadados XMP em um Arquivo PDF

Aspose.PDF permite que você defina metadados em um arquivo PDF.
Aspose.PDF permite que você defina metadados em um arquivo PDF.

1. Crie um objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Defina valores de metadados usando a propriedade [Metadata](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/metadata).
1. Salve o documento atualizado usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) do objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

O seguinte trecho de código mostra como definir metadados em um arquivo PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Abrir documento
Document pdfDocument = new Document(dataDir + "SetXMPMetadata.pdf");

// Definir propriedades
pdfDocument.Metadata["xmp:CreateDate"] = DateTime.Now;
pdfDocument.Metadata["xmp:Nickname"] = "Nickname";
pdfDocument.Metadata["xmp:CustomProperty"] = "Valor Personalizado";

dataDir = dataDir + "SetXMPMetadata_out.pdf";
// Salvar documento
pdfDocument.Save(dataDir);
```
## Inserir Metadados com Prefixo

Alguns desenvolvedores precisam criar um novo espaço de nomes de metadados com um prefixo. O fragmento de código a seguir mostra como inserir metadados com prefixo.

```csharp
// Para exemplos completos e arquivos de dados, por favor, acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Abrir documento
Document pdfDocument = new Document(dataDir + "SetXMPMetadata.pdf");
pdfDocument.Metadata.RegisterNamespaceUri("xmp", "http:// Ns.adobe.com/xap/1.0/"); // Prefixo Xmlns foi removido
pdfDocument.Metadata["xmp:ModifyDate"] = DateTime.Now;

dataDir = dataDir + "SetPrefixMetadata_out.pdf";
// Salvar documento
pdfDocument.Save(dataDir);
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
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

