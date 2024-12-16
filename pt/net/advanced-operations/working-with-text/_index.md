---
title: Trabalhando com Texto em PDF usando C#
linktitle: Trabalhando com Texto
type: docs
weight: 30
url: /pt/net/working-with-text/
description: Esta seção explica várias técnicas de manipulação de texto. Aprenda como adicionar, substituir, rotacionar e pesquisar texto usando Aspose.PDF e C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Trabalhando com Texto em PDF usando C#",
    "alternativeHeadline": "Adicionar, Rotacionar, Pesquisar e Excluir Texto em Arquivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento pdf",
    "keywords": "pdf, c#, adicionar texto, pesquisar texto, excluir texto, manipular texto em pdf",
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
    "url": "/net/working-with-text/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-text/"
    },
    "dateModified": "2022-02-04",
    "description": "Esta seção explica várias técnicas de manipulação de texto. Aprenda como adicionar, substituir, rotacionar e pesquisar texto usando Aspose.PDF e C#."
}
</script>
Todos nós às vezes precisamos adicionar texto a um arquivo PDF. Por exemplo, quando você deseja adicionar uma tradução abaixo do texto principal, colocar uma legenda ao lado de uma imagem ou simplesmente preencher um formulário de inscrição. Também é útil se todos os elementos de texto puderem ser formatados no estilo que você desejar. As manipulações de texto mais populares em seu arquivo PDF são: adicionar texto ao PDF, formatar texto dentro do arquivo PDF, substituir e rotacionar texto em seu documento. **Aspose.PDF for .NET** é a melhor solução que tem tudo o que você precisa para interagir com o conteúdo do PDF.

Você pode fazer o seguinte:

- [Adicionar Texto ao arquivo PDF](/pdf/pt/net/add-text-to-pdf-file/) - adicionar texto ao seu PDF, usar fontes de stream e arquivos, adicionar uma string HTML, adicionar um hiperlink, etc.
- [Tooltip de PDF](/pdf/pt/net/pdf-tooltip/) - você pode adicionar uma dica de ferramenta ao texto pesquisado adicionando um botão invisível usando C#.
- [Formatação de Texto dentro do PDF](/pdf/pt/net/text-formatting-inside-pdf/) - Muitos recursos que você pode adicionar ao seu documento ao formatar o texto dentro dele.
- [Formatação de Texto dentro do PDF](/pdf/pt/net/text-formatting-inside-pdf/) - Muitos recursos que você pode adicionar ao seu documento ao formatar o texto dentro dele.
- [Substituir Texto no PDF](/pdf/pt/net/replace-text-in-pdf/) - para substituir texto em todas as páginas de um documento PDF. Primeiramente, você precisa usar TextFragmentAbsorber.
- [Rotacionar Texto Dentro do PDF](/pdf/pt/net/rotate-text-inside-pdf/) - rotacionar texto dentro do PDF usando a propriedade de rotação da Classe TextFragment.
- [Pesquisar e Obter Texto das Páginas de um Documento PDF](/pdf/pt/net/search-and-get-text-from-pdf/) - você pode usar a classe TextFragmentAbsorber para pesquisar e obter um texto das páginas.
- [Determinar Quebra de Linha](/pdf/pt/net/determine-line-break/) - este tópico explica como acompanhar a quebra de linha de fragmentos de texto de múltiplas linhas.

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


