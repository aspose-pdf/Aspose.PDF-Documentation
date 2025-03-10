---
title: Trabalhando com AcroForms
linktitle: AcroForms
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /pt/net/acroforms/
description: Com Aspose.PDF for .NET você pode criar um formulário do zero, preencher os campos do formulário em um documento PDF, extrair dados do formulário, etc.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with AcroForms",
    "alternativeHeadline": "Enhance PDF forms with flexible AcroForms functionality",
    "abstract": "Aspose.PDF for .NET introduz capacidades aprimoradas para trabalhar com AcroForms, permitindo que os usuários criem formulários do zero, preencham campos PDF e extraiam dados de forma contínua. Este recurso poderoso suporta a integração de múltiplos registros de banco de dados, permitindo uma gestão dinâmica de formulários e uma experiência do usuário simplificada.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "AcroForms, PDF forms technology, create a form, fill form fields, extract data, database records, Templates, modify AcroForms, posting AcroForm data, import and export data",
    "wordcount": "484",
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
    "url": "/net/acroforms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/acroforms/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Fundamentos dos AcroForms

**AcroForms** são a tecnologia original de formulários PDF. AcroForms é um formulário orientado a páginas. Eles foram introduzidos pela primeira vez em 1998. Eles aceitam entrada no Formato de Dados de Formulários ou FDF e no Formato de Dados de Formulários XML ou xFDF. Fornecedores de terceiros suportam AcroForms. Quando a Adobe introduziu os AcroForms, referiu-se a eles como “formulário PDF que é criado com o Adobe Acrobat Pro/Standard e que não é um tipo especial de formulário XFA estático ou dinâmico. AcroForms são portáteis e funcionam em todas as plataformas.

Você pode usar AcroForms para adicionar páginas adicionais ao documento de formulário PDF. Graças ao conceito de Templates, você pode usar AcroForms para suportar o preenchimento do formulário com múltiplos registros de banco de dados.

O PDF 1.7 suporta dois métodos diferentes para integrar dados e formulários PDF.

*AcroForms (também conhecidos como formulários Acrobat)*, introduzidos e incluídos na especificação do formato PDF 1.2.

*Arquitetura de Formulários XML da Adobe (XFA)*, introduzida na especificação do formato PDF 1.5 como um recurso opcional (A especificação XFA não está incluída na especificação PDF, ela é apenas referenciada).

Para entender **Acroforms** vs **XFA** formulários, precisamos entender os fundamentos primeiro. Para começar, ambos são formulários PDF que você pode usar. Acroforms é o mais antigo, criado em 1998, e ainda é referido como o formulário PDF clássico. Os formulários XFA são páginas da web que você pode salvar como PDF e apareceram em 2003. Levou algum tempo até que o PDF começasse a aceitar formulários XFA.

AcroForms têm capacidades que não são encontradas em XFA e, inversamente, XFA tem algumas capacidades que não são encontradas em AcroForms. Por exemplo:

- AcroForms suportam o conceito de “Templates”, permitindo que páginas adicionais sejam adicionadas ao documento de formulário PDF para suportar o preenchimento do formulário com múltiplos registros de banco de dados.
- XFA suporta o conceito de reflow de documento, permitindo que um campo redimensione, se necessário, para acomodar dados.

Para um aprendizado mais detalhado das capacidades da biblioteca Java, veja os seguintes artigos:

- [Criar AcroForm](/pdf/net/create-form) - criar formulário do zero com C#.
- [Preencher AcroForm](/pdf/net/fill-form) - preencher campo de formulário no seu documento PDF.
- [Extrair AcroForm](/pdf/net/extract-form) - obter valor de todos ou de um campo individual do documento PDF.
- [Modificando AcroForm](/pdf/net/modifing-form) - obter ou definir FieldLimit, definir fonte do campo do formulário, etc.
- [Postando Dados AcroForm](/pdf/net/posting-acroform-data/) - importar e exportar dados do formulário para um arquivo XML.
- [Importar e Exportar Dados](/pdf/net/import-and-export-data/) - importar e exportar dados usando a Classe Form.
- [Remover Formulários do PDF](/pdf/net/remove-form/) - remover texto com base em subtipo/formulário, excluir todos os formulários.
- [Importar e Exportar Dados em JSON](/pdf/net/import-export-json/) - importar e exportar dados com JSON

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