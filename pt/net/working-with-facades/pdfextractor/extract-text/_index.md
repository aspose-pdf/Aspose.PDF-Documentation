---
title: Extrair Texto de Arquivo PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /pt/net/extract-text/
description: Esta seção explica como extrair texto de pdf usando a classe PdfExtractor.
lastmod: "2021-06-05"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Text from PDF File",
    "alternativeHeadline": "Effortless Text Extraction from PDF Files",
    "abstract": "A classe PdfExtractor permite a extração eficiente de texto de arquivos PDF através de múltiplos métodos, permitindo que os usuários recuperem texto, imagens e anexos com facilidade. Ao utilizar métodos como ExtractText, GetText e GetNextPageText, os desenvolvedores podem extrair e salvar conteúdo textual de páginas individuais ou de documentos inteiros, simplificando tarefas de manipulação de PDF. Com modos de extração flexíveis disponíveis, este recurso melhora o controle sobre o formato de saída, tornando-se uma ferramenta essencial para quem trabalha com dados PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "441",
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
    "url": "/net/extract-text/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-text/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

Neste artigo, vamos explorar os detalhes da extração de texto de um arquivo PDF. Todos esses recursos de extração estão disponíveis em um só lugar, na classe [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor). Vamos ver como usar esses recursos em nosso código.

A classe [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) fornece três tipos de capacidades de extração. Essas três categorias são Texto, Imagens e Anexos. Para realizar a extração em cada uma dessas três categorias, o PdfExtractor fornece vários métodos que trabalham juntos para fornecer a saída final.

Por exemplo, para extrair texto, você pode usar três métodos, ou seja, [ExtractText, GetText, HasNextPageText e GetNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/index). Agora, para começar a extrair texto, primeiro você precisa chamar o método [ExtractText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extracttext/index); isso extrairá o texto do arquivo PDF e o armazenará na memória. Depois disso, o método [GetText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/gettext/index) pegará esse texto extraído e o salvará no disco em um local especificado em um arquivo. O método [HasNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextpagetext) ajuda você a percorrer cada página e verificar se a próxima página contém algum texto ou não. Se contiver algum texto, o [GetNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getnextpagetext/index) ajudará você a salvar o texto de uma página individual no arquivo.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    bool wholeText = true;
    // Create an object of the PdfExtractor class
    using (var pdfExtractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        pdfExtractor.BindPdf(dataDir + "sample.pdf");

        // ExtractText
        pdfExtractor.ExtractText();

        if (!wholeText)
        {
            pdfExtractor.GetText(dataDir + "sample.txt");
        }
        else
        {
            // Extract the text into separate files
            int pageNumber = 1;
            while (pdfExtractor.HasNextPageText())
            {
                pdfExtractor.GetNextPageText($"{dataDir}\\sample{pageNumber:D3}.txt");
                pageNumber++;
            }
        }
    }
}
```

Para Extrair o Modo de Extração de Texto, use o seguinte código:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextExtractonMode()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    bool wholeText = true;
    // Create an object of the PdfExtractor class
    using (var pdfExtractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        pdfExtractor.BindPdf(dataDir + "ExtractTextExtractonMode.pdf");

        // ExtractText
        // pdfExtractor.ExtractTextMode = 0; // pure mode
        pdfExtractor.ExtractTextMode = 1; // raw mode
        pdfExtractor.ExtractText();

        if (!wholeText)
        {
            pdfExtractor.GetText(dataDir + "ExtractTextExtractonMode_out.txt");
        }
        else
        {
            // Extract the text into separate files
            int pageNumber = 1;
            while (pdfExtractor.HasNextPageText())
            {
                pdfExtractor.GetNextPageText($"{dataDir}\\sample{pageNumber:D3}.txt");
                pageNumber++;
            }
        }
    }
}
```