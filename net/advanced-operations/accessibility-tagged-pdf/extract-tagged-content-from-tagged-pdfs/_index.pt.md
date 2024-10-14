---
title: Extrair Conteúdo Marcado de PDF
linktitle: Extrair Conteúdo Marcado
type: docs
weight: 20
url: /net/extract-tagged-content-from-tagged-pdfs/
description: Este artigo explica como extrair conteúdo marcado de um documento PDF usando Aspose.PDF para .NET
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extrair Conteúdo Marcado de PDF",
    "alternativeHeadline": "Como marcar imagem em PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos PDF",
    "keywords": "marcar, pdf, extrair",
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
    "url": "/net/extract-tagged-content-from-tagged-pdfs/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-tagged-content-from-tagged-pdfs/"
    },
    "dateModified": "2022-02-04",
    "description": "Este artigo explica como extrair conteúdo marcado de um documento PDF usando Aspose.PDF para .NET"
}
</script>
Neste artigo, você aprenderá como extrair conteúdo marcado de um documento PDF usando C#.

O trecho de código a seguir também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Obtendo Conteúdo de PDF Marcado

Para obter o conteúdo de um Documento PDF com Texto Marcado, Aspose.PDF oferece a propriedade [TaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/taggedcontent) da classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

O seguinte trecho de código mostra como obter o conteúdo de um documento PDF com Texto Marcado:

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Criar Documento Pdf
Document document = new Document();

// Obter Conteúdo para trabalhar com TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

//
// Trabalhar com conteúdo de Pdf marcado
//

// Definir Título e Idioma para o Documento
taggedContent.SetTitle("Documento Pdf Marcado Simples");
taggedContent.SetLanguage("en-US");

// Salvar Documento Pdf Marcado
document.Save(dataDir + "TaggedPDFContent.pdf");
```
## Obtendo a Estrutura Raiz

Para obter a estrutura raiz de um Documento PDF Tagged, o Aspose.PDF oferece a propriedade [StructTreeRootElement](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/properties/structtreerootelement) da interface [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent) e [StructureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement). O seguinte trecho de código mostra como obter a estrutura raiz de um Documento PDF Tagged:

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Criar Documento Pdf
Document document = new Document();

// Obter Conteúdo para trabalhar com TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// Definir Título e Idioma para o Documento
taggedContent.SetTitle("Documento PDF Tagged");
taggedContent.SetLanguage("en-US");

// As propriedades StructTreeRootElement e RootElement são usadas para acesso ao
// objeto StructTreeRoot do documento pdf e ao elemento de estrutura raiz (elemento de estrutura do Documento).
StructTreeRootElement structTreeRootElement = taggedContent.StructTreeRootElement;
StructureElement rootElement = taggedContent.RootElement;
```
## Acessando Elementos Filhos

Para acessar elementos filhos de um Documento PDF Marcado, Aspose.PDF oferece a classe [ElementList](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/elementlist). O trecho de código a seguir mostra como acessar elementos filhos de um Documento PDF Marcado:

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Abrir Documento Pdf
Document document = new Document(dataDir + "StructureElementsTree.pdf");

// Obter Conteúdo para trabalhar com TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// Acesso ao(s) elemento(s) raiz
ElementList elementList = taggedContent.StructTreeRootElement.ChildElements;
foreach (Element element in elementList)
{
    if (element is StructureElement)
    {
        StructureElement structureElement = element as StructureElement;

        // Obter propriedades
        string title = structureElement.Title;
        string language = structureElement.Language;
        string actualText = structureElement.ActualText;
        string expansionText = structureElement.ExpansionText;
        string alternativeText = structureElement.AlternativeText;
    }
}

// Acesso aos elementos filhos do primeiro elemento na raiz
elementList = taggedContent.RootElement.ChildElements[1].ChildElements;
foreach (Element element in elementList)
{
    if (element is StructureElement)
    {
        StructureElement structureElement = element as StructureElement;

        // Definir propriedades
        structureElement.Title = "title";
        structureElement.Language = "fr-FR";
        structureElement.ActualText = "actual text";
        structureElement.ExpansionText = "exp";
        structureElement.AlternativeText = "alt";
    }
}

// Salvar Documento PDF Marcado
document.Save(dataDir + "AccessChildElements.pdf");
```
## Marcação de Imagens em PDF Existente

Para marcar imagens em um documento PDF existente, o Aspose.PDF oferece o método [FindElements](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/element/methods/findelements/_1) da classe [StructureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement). Você pode adicionar texto alternativo para figuras usando a propriedade [AlternativeText](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement/properties/alternativetext) da classe [FigureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/figureelement).

O seguinte trecho de código mostra como marcar imagens em um documento PDF existente:

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string inFile = dataDir + "TH.pdf";
string outFile = dataDir + "TH_out.pdf";
string logFile = dataDir + "TH_out.xml";

// Abrir documento
Document document = new Document(inFile);

// Obtém o conteúdo marcado e o elemento de estrutura raiz
ITaggedContent taggedContent = document.TaggedContent;
StructureElement rootElement = taggedContent.RootElement;

// Define título para o documento PDF marcado
taggedContent.SetTitle("Documento com imagens");

foreach (FigureElement figureElement in rootElement.FindElements<FigureElement>(true))
{
    // Define o Texto Alternativo para a Figura
    figureElement.AlternativeText = "Texto alternativo da figura (técnica 2)";


    // Criar e Definir Atributo BBox
    StructureAttribute bboxAttribute = new StructureAttribute(AttributeKey.BBox);
    bboxAttribute.SetRectangleValue(new Rectangle(0.0, 0.0, 100.0, 100.0));

    StructureAttributes figureLayoutAttributes = figureElement.Attributes.GetAttributes(AttributeOwnerStandard.Layout);
    figureLayoutAttributes.SetAttribute(bboxAttribute);
}

// Mover Elemento Span para Parágrafo (encontrar span errado e parágrafo no primeiro TD)
TableElement tableElement = rootElement.FindElements<TableElement>(true)[0];
SpanElement spanElement = tableElement.FindElements<SpanElement>(true)[0];
TableTDElement firstTdElement = tableElement.FindElements<TableTDElement>(true)[0];
ParagraphElement paragraph = firstTdElement.FindElements<ParagraphElement>(true)[0];

// Mover Elemento Span para Parágrafo
spanElement.ChangeParentElement(paragraph);


// Salvar documento
document.Save(outFile);



// Verificando conformidade com PDF/UA para documento de saída
document = new Document(outFile);

bool isPdfUaCompliance = document.Validate(logFile, PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("Conformidade com PDF/UA: {0}", isPdfUaCompliance));
```
```html
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
                "tipo de contato": "vendas",
                "área servida": "US",
                "idioma disponível": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "tipo de contato": "vendas",
                "área servida": "GB",
                "idioma disponível": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "tipo de contato": "vendas",
                "área servida": "AU",
                "idioma disponível": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "moeda do preço": "USD"
    },
    "categoria da aplicação": "Biblioteca de Manipulação de PDF para .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "sistema operacional": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "versão do software": "2022.1",
    "avaliação agregada": {
        "@type": "AggregateRating",
        "valor da avaliação": "5",
        "contagem de avaliações": "16"
    }
}
</script>
```

