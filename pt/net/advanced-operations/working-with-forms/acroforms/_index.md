---
title: Trabalhando com AcroForms
linktitle: AcroForms
type: docs
weight: 10
url: /pt/net/acroforms/
description: Com Aspose.PDF para .NET você pode criar um formulário do zero, preencher o campo de formulário em um documento PDF, extrair dados do formulário, e etc.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Trabalhando com AcroForms",
    "alternativeHeadline": "Opções para trabalhar com AcroForms em PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos PDF",
    "keywords": "pdf, c#, acroforms em pdf",
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
    "url": "/net/acroforms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/acroforms/"
    },
    "dateModified": "2022-02-04",
    "description": "Com Aspose.PDF para .NET você pode criar um formulário do zero, preencher o campo de formulário em um documento PDF, extrair dados do formulário, e etc."
}
</script>

## Fundamentos dos AcroForms

**AcroForms** são a tecnologia original de formulários em PDF. AcroForms é um formulário orientado a páginas. Eles foram introduzidos pela primeira vez em 1998. Eles aceitam entrada no Formato de Dados de Formulários ou FDF e Formato de Dados de Formulários XML ou xFDF. Fornecedores terceirizados suportam AcroForms. Quando a Adobe introduziu os AcroForms, eles os chamaram de “formulário PDF que é criado com o Adobe Acrobat Pro/Standard e que não é um tipo especial de formulário XFA estático ou dinâmico. AcroForms são portáteis e funcionam em todas as plataformas.

Você pode usar AcroForms para adicionar páginas adicionais ao documento do formulário PDF. Graças ao conceito de Modelos, você pode usar AcroForms para suportar o preenchimento do formulário com múltiplos registros de banco de dados.

PDF 1.7 suporta dois métodos diferentes para integrar dados e formulários em PDF.

*AcroForms (também conhecidos como formulários Acrobat)*, introduzido e incluído na especificação do formato PDF 1.2.

*Adobe XML Forms Architecture (XFA) forms*, introduzido na especificação do formato PDF 1.5 como um recurso opcional (A especificação XFA não está incluída na especificação PDF, é apenas referenciada.
*Formulários Adobe XML Forms Architecture (XFA)*, introduzidos na especificação do formato PDF 1.5 como um recurso opcional (A especificação XFA não está incluída na especificação do PDF, ela é apenas referenciada.

Para entender **Acroforms** vs **XFA** formulários, precisamos entender os conceitos básicos primeiro. Para começar, ambos são formulários PDF que você pode usar. Acroforms é o mais antigo, criado em 1998, e ainda é referido como o formulário clássico em PDF. Os formulários XFA são páginas da web que você pode salvar como PDF e apareceram em 2003. Demorou algum tempo antes que o PDF começasse a aceitar formulários XFA.

AcroForms têm capacidades não encontradas em XFA e vice-versa, XFA tem algumas capacidades não encontradas em AcroForms. Por exemplo:

- AcroForms suporta o conceito de "Modelos", permitindo que páginas adicionais sejam adicionadas ao documento do formulário PDF para suportar o preenchimento do formulário com múltiplos registros de banco de dados.
- XFA suporta o conceito de reorganização de documentos permitindo que um campo seja redimensionado, se necessário, para acomodar os dados.

Para aprender mais detalhadamente sobre as capacidades da biblioteca Java, veja os seguintes artigos:
Para um aprendizado mais detalhado das capacidades da biblioteca Java, veja os seguintes artigos:

- [Criar AcroForm](/pdf/pt/net/create-form) - criar formulário do zero com C#.
- [Preencher AcroForm](/pdf/pt/net/fill-form) - preencher campo de formulário no seu documento PDF.
- [Extrair AcroForm](/pdf/pt/net/extract-form) - obter valor de todos ou de um campo individual do documento PDF.
- [Modificar AcroForm](/pdf/pt/net/modifing-form) - obter ou definir FieldLimit, definir fonte do campo de formulário e etc.
- [Postar Dados de AcroForm](/pdf/pt/net/posting-acroform-data/) - importar e exportar dados de formulário para um arquivo XML.
- [Importar e Exportar Dados](/pdf/pt/net/import-and-export-data/) - importar e exportar dados usando a Classe Form.

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


