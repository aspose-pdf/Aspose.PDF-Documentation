---
title: Convertendo um XML para o formato FDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /pt/net/converting-an-xml-to-fdf-format/
description: Esta seção explica como você pode converter um XML para o formato FDF com o FormDataConverter.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Converting an XML to FDF format",
    "alternativeHeadline": "Convert XML Files to FDF Format Easily",
    "abstract": "O recurso permite que os desenvolvedores convertam arquivos XML para o formato FDF usando a classe FormDataConverter em Aspose.PDF for .NET. Essa funcionalidade melhora a troca de dados entre formatos de documento, facilitando a gestão eficiente de dados de formulários em aplicações",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "274",
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
    "url": "/net/converting-an-xml-to-fdf-format/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/converting-an-xml-to-fdf-format/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

{{% alert color="primary" %}}

O [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades) namespace em [Aspose.PDF for .NET](/pdf/pt/net/) suporta AcroForms muito bem. Ele também suporta a importação e exportação de dados de formulários para diferentes formatos de arquivo, como FDF, XFDF e XML. No entanto, às vezes um desenvolvedor precisa converter um formato para outro. Neste artigo, vamos explorar o recurso que nos permite converter um formato FDF em XML.

{{% /alert %}}

## Detalhes da implementação

FDF significa Formato de Dados de Formulários, e um arquivo FDF contém os valores do formulário em um par chave/valor. Também sabemos que um arquivo XML contém os valores como tags. Onde, na maioria das vezes, a chave é representada como o nome da tag e o valor é representado como o valor dentro dessa tag. Agora, [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades) fornece a flexibilidade para converter um formato de arquivo XML em formato FDF.

Use a classe [FormDataConverter](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/FormDataConverter) para esse propósito. Esta classe fornece diferentes métodos para converter um formato de dados em outro. Este artigo mostra como usar um método, ConvertXmlToFdf(..), que recebe um arquivo FDF como entrada ou fluxo de origem e o salva em formato XML. O seguinte trecho de código mostra como converter um arquivo FDF em um arquivo XML.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ConvertXmlToFdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    using (var src = new FileStream(dataDir + "log.xml", FileMode.Open, FileAccess.Read))
    {
        using (var dest = new FileStream(dataDir + "XMLToPdf_out.pdf", FileMode.Create, FileAccess.ReadWrite))
        {
            FormDataConverter.ConvertXmlToFdf(src, dest);
        }
    }
}
```