---
title: Trabalhando com Portfólio em PDF
linktitle: Portfólio
type: docs
weight: 40
url: /pt/net/portfolio/
description: Como Criar um Portfólio em PDF com C#. Você deve usar um Arquivo do Microsoft Excel, um documento Word e um arquivo de imagem para criar um Portfólio em PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Trabalhando com Portfólio em PDF",
    "alternativeHeadline": "Criar Portfólio em documento PDF",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento PDF",
    "keywords": "pdf, c#, portfólio",
    "wordcount": "302",
    "proficiencyLevel": "Iniciante",
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
    "url": "/net/portfolio/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/portfolio/"
    },
    "dateModified": "2022-02-04",
    "description": "Como Criar um Portfólio em PDF com C#. Você deve usar um Arquivo do Microsoft Excel, um documento Word e um arquivo de imagem para criar um Portfólio em PDF."
}
</script>
## Como Criar um Portfólio em PDF

Aspose.PDF permite a criação de documentos de Portfólio em PDF usando a classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Adicione um arquivo em um objeto Document.Collection após obtê-lo com a classe [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification). Quando os arquivos forem adicionados, use o método Save da classe Document para salvar o documento do portfólio.

O exemplo a seguir usa um arquivo Microsoft Excel, um documento Word e um arquivo de imagem para criar um Portfólio em PDF.

O código abaixo resulta no seguinte portfólio.

O trecho de código a seguir também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

### Um Portfólio em PDF criado com Aspose.PDF

![Um Portfólio em PDF criado com Aspose.PDF para .NET](working-with-pdf-portfolio_1.jpg)

```csharp
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

// Instanciar Objeto Documento
Document doc = new Document();

// Instanciar objeto de Coleção de documentos
doc.Collection = new Collection();

// Obter arquivos para adicionar ao Portfólio
FileSpecification excel = new FileSpecification( dataDir + "HelloWorld.xlsx");
FileSpecification word = new FileSpecification( dataDir + "HelloWorld.docx");
FileSpecification image = new FileSpecification(dataDir + "aspose-logo.jpg");

// Fornecer descrição dos arquivos
excel.Description = "Arquivo Excel";
word.Description = "Arquivo Word";
image.Description = "Arquivo de Imagem";

// Adicionar arquivos à coleção de documentos
doc.Collection.Add(excel);
doc.Collection.Add(word);
doc.Collection.Add(image);

// Salvar documento do Portfólio
doc.Save(dataDir + "CreatePDFPortfolio_out.pdf");
```
## Extrair arquivos de Portfólio PDF

Portfólios PDF permitem que você reúna conteúdo de uma variedade de fontes (por exemplo, PDF, Word, Excel, arquivos JPEG) em um único recipiente unificado. Os arquivos originais mantêm suas identidades individuais, mas são montados em um arquivo de Portfólio PDF. Os usuários podem abrir, ler, editar e formatar cada arquivo componente independentemente dos outros arquivos componentes.

Aspose.PDF permite a criação de documentos de Portfólio PDF usando a classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Ele também oferece a capacidade de extrair arquivos de portfólio PDF.

O seguinte trecho de código mostra os passos para extrair arquivos de um portfólio PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

// Carregar o Portfólio PDF de origem
Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "PDFPortfolio.pdf");
// Obter coleção de arquivos embutidos
EmbeddedFileCollection embeddedFiles = pdfDocument.EmbeddedFiles;
// Iterar através de cada arquivo do Portfólio
foreach (FileSpecification fileSpecification in embeddedFiles)
{
    // Obter o anexo e escrever para arquivo ou fluxo
    byte[] fileContent = new byte[fileSpecification.Contents.Length];
    fileSpecification.Contents.Read(fileContent, 0, fileContent.Length);
    string filename = Path.GetFileName(fileSpecification.Name);
    // Salvar o arquivo extraído em algum local
    FileStream fileStream = new FileStream(dataDir + "_out" + filename, FileMode.Create);
    fileStream.Write(fileContent, 0, fileContent.Length);
    // Fechar o objeto de fluxo
    fileStream.Close();
}
```
![Extract files from PDF Portfolio](working-with-pdf-portfolio_2.jpg)

## Remover Arquivos de Portfólio PDF

Para deletar/remover arquivos de um portfólio PDF, tente usar as seguintes linhas de código.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

// Carregar o Portfólio PDF de origem
Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "PDFPortfolio.pdf");
pdfDocument.Collection.Delete();
pdfDocument.Save(dataDir + "No_PortFolio_out.pdf");
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


