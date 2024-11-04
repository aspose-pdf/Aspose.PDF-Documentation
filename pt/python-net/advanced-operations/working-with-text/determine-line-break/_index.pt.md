---
title: Determinar Quebra de Linha
linktitle: Determinar Quebra de Linha
type: docs
weight: 70
url: /python-net/determine-line-break/
description: Saiba mais sobre como determinar uma quebra de linha de TextFragment multi-linha usando Python
lastmod: "2024-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Determinar Quebra de Linha",
    "alternativeHeadline": "Como determinar a quebra de linha de TextFragment",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento pdf",
    "keywords": "pdf, python, determinar quebra de linha",
    "wordcount": "302",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Equipe Aspose.PDF Doc",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/determine-line-break/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/determine-line-break/"
    },
    "dateModified": "2024-02-04",
    "description": "Saiba mais sobre como determinar uma quebra de linha de TextFragment multi-linha usando Python"
}
</script>


## Acompanhar Quebra de Linha de TextFragment Multilinha

O próximo trecho de código mostra como acompanhar o comportamento de quebra de linha de um TextFragment multilinha dentro de um documento PDF.

A função track_line_breaking() é definida para demonstrar essa funcionalidade. Ela começa especificando caminhos de arquivo de saída tanto para o documento PDF gerado quanto para um arquivo de texto correspondente que conterá informações sobre a quebra de linha.

Dentro da função, um novo objeto de documento PDF é criado, e uma nova página é adicionada a ele. Subsequentemente, um loop é utilizado para gerar quatro instâncias de um TextFragment contendo um texto com quebras de linha ("\r\n") inseridas dentro da string para simular texto multilinha.

Cada TextFragment é configurado com um tamanho de fonte de 20 pontos antes de ser adicionado aos parágrafos da página.

Depois que todos os TextFragments são adicionados, o documento é salvo.

A função então procede para extrair notificações sobre a quebra de linha da segunda página do documento PDF gerado usando o método get_notifications().
 Estas notificações são escritas em um arquivo de texto especificado anteriormente.

Este trecho de código ilustra como criar um documento PDF contendo texto em várias linhas e, em seguida, extrair informações sobre o comportamento da quebra de linha, fornecendo insights sobre como o texto é disposto dentro do documento.

```python

    import aspose.pdf as ap

    def track_line_breaking():
        """Acompanhar a Quebra de Linha de TextFragment de Múltiplas Linhas"""
        output_pdf = DIR_OUTPUT_TEXTS + "track_line_breaking.pdf"
        output_txt = DIR_OUTPUT_TEXTS + "track_line_breaking.txt"

        # Criar novo objeto de documento
        document = ap.Document()
        page = document.pages.add()

        for i in range(4):
            text = ap.text.TextFragment(
                "Lorem ipsum \r\ndolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
            )
            text.text_state.font_size = 20
            page.paragraphs.add(text)
        document.save(output_pdf)

        notifications = document.pages[1].get_notifications()
        with open(output_txt, "w") as f:
            f.write(notifications)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF para .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>