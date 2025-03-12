---
title: Renderizar WebForms DataGridView para PDF
linktitle: Renderizar WebForms DataGridView para PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /pt/net/render-webforms-datagridview-to-pdf/
description: Este exemplo mostra como usar a biblioteca Aspose.PDF para renderizar WebForm em PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Render WebForms DataGridView to PDF",
    "alternativeHeadline": "Effortlessly Convert WebForms DataGridView to PDF",
    "abstract": "O recurso permite a conversão sem interrupções de WebForms DataGridView para PDF usando a biblioteca Aspose.PDF for .NET. Essa funcionalidade simplifica o processo de exportação de dados integrando um controle de exportação GridView dedicado, garantindo uma renderização de PDF de alta qualidade diretamente de aplicativos da web. Perfeito para desenvolvedores que buscam soluções eficientes de geração de documentos",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "266",
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
    "url": "/net/render-webforms-datagridview-to-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/render-webforms-datagridview-to-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Como exportar WebForm para PDF usando Aspose.PDF/Aspose.HTML

### Introdução

Geralmente, para converter WebForm em documento PDF, são usadas ferramentas adicionais. Este exemplo mostra como usar a biblioteca Aspose.PDF para renderizar WebForm em PDF. O Controle de Exportação Aspose GridView para PDF também está incluído neste exemplo para mostrar como renderizar _o controle GridView em documento PDF._

## Como renderizar WebForm para PDF

A ideia original para renderizar WebForm em PDF é criar uma classe auxiliar, que herda de [System.Web.UI.Page](https://msdn.microsoft.com/en-US/library/System.Web.UI.Page.aspx), e sobrescrever um método Render.</em></p>

```csharp
void Render(HtmlTextWriter writer)
{
    if (RenderToPDF)
    {
        // render web page for PDF document
    }
    else
    {
        // render web page in browser
        base.Render(writer);
    }
}
```

Existem duas ferramentas Aspose que podem ser usadas para renderizar HTML em PDF:

- Aspose.PDF for .NET.
- Controle de Exportação Aspose GridView (baseado em Aspose.PDF).

## Arquivos Fonte

Neste exemplo, temos 2 relatórios de demonstração.

- _Default.aspx_ demonstra a exportação para PDF usando Aspose.PDF.
- _Report2.aspx_ demonstra a exportação para PDF usando o controle de Exportação Aspose GridView (baseado em Aspose.PDF).

## Arquivos adicionais

`Helpers\PdfPage.cs` - contém uma classe auxiliar, que mostra como usar a API Aspose.PDF.</em>

O projeto Aspose.Pdf.GridViewExport contém um controle GridView estendido para demonstração em `Report2.aspx`