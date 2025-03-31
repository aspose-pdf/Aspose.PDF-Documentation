---
title: Convertendo um FDF para o formato XML
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /pt/net/converting-an-fdf-to-xml-format/
description: Esta seção explica como você pode converter um FDF para o formato XML com a classe FormDataConverter.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Converting an FDF to XML format",
    "alternativeHeadline": "Convert FDF Files to XML Easily",
    "abstract": "Descubra como converter arquivos FDF para o formato XML de forma eficiente usando a classe FormDataConverter em Aspose.PDF for .NET. Essa funcionalidade simplifica o manuseio de dados ao transformar pares chave/valor de FDF em uma estrutura XML facilmente legível, melhorando a interoperabilidade e o gerenciamento de dados em suas aplicações.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "288",
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
    "url": "/net/converting-an-fdf-to-xml-format/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/converting-an-fdf-to-xml-format/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

{{% alert color="primary" %}}

O [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades) namespace em [Aspose.PDF for .NET](/pdf/pt/net/) suporta muito bem AcroForms. Ele também suporta a importação e exportação de dados de formulário para diferentes formatos de arquivo, como FDF, XFDF e XML. No entanto, às vezes os desenvolvedores podem precisar converter um formato em outro. Este artigo analisa o recurso que converte FDF em XML.

{{% /alert %}}

## Detalhes da implementação

FDF significa Formato de Dados de Formulários, e um arquivo FDF contém os valores do formulário em um par chave/valor. Também sabemos que um arquivo XML contém os valores como tags. Onde, geralmente a chave é representada como o nome da tag e o valor é representado como o valor dentro dessa tag. Agora, [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades) nos fornece a flexibilidade de converter um formato de arquivo FDF em um formato XML.

Podemos usar a classe [FormDataConverter](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/formdataconverter) para esse propósito. Esta classe nos fornece diferentes métodos para converter um formato de dados em outro formato. Neste artigo, usaremos apenas um método chamado [ConvertFdfToXml](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/formdataconverter/methods/convertfdftoxml). Este método recebe um arquivo FDF como entrada ou fluxo de origem e o salva no formato XML.

O seguinte trecho de código mostra como converter um arquivo FDF em um arquivo XML:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ConvertFdftoXml()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    // Create a file stream for FDF file - input file
    using (var fdfInputStream = new FileStream(dataDir + "input.fdf", FileMode.Open))
    {
        // Create a file stream for XML file - output file
        using (var xmlOutputStream = new FileStream(dataDir + "ConvertFdfToXML_out.xml", FileMode.Create))
        {
            FormDataConverter.ConvertFdfToXml(fdfInputStream, xmlOutputStream);
        }
    }
}
```