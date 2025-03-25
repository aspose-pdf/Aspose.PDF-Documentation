---
title: Rendre WebForms DataGridView en PDF
linktitle: Rendre WebForms DataGridView en PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /fr/net/render-webforms-datagridview-to-pdf/
description: Cet exemple montre comment utiliser la bibliothèque Aspose.PDF pour rendre WebForm en PDF.
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
    "abstract": "La fonctionnalité permet une conversion transparente de WebForms DataGridView en PDF en utilisant la bibliothèque Aspose.PDF for .NET. Cette fonctionnalité simplifie le processus d'exportation des données en intégrant un contrôle d'exportation GridView dédié, garantissant un rendu PDF de haute qualité directement à partir des applications web. Parfait pour les développeurs à la recherche de solutions efficaces de génération de documents",
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
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs et développeurs avancés."
}
</script>

## Comment exporter WebForm en PDF en utilisant Aspose.PDF/Aspose.HTML

### Introduction

En général, pour convertir WebForm en document PDF, des outils supplémentaires sont nécessaires. Cet exemple montre comment utiliser la bibliothèque Aspose.PDF pour rendre WebForm en PDF. Le contrôle Aspose Export GridView To Pdf est également inclus dans cet exemple pour montrer comment rendre _le contrôle GridView en document PDF_.

## Comment rendre WebForm en PDF

L'idée originale pour rendre WebForm en PDF est de créer une classe d'assistance, qui hérite de [System.Web.UI.Page](https://msdn.microsoft.com/en-US/library/System.Web.UI.Page.aspx), et de remplacer une méthode Render.</em></p>

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

Il existe deux outils Aspose qui peuvent être utilisés pour rendre HTML en PDF :

- Aspose.PDF for .NET.
- Contrôle d'exportation Aspose GridView (basé sur Aspose.PDF).

## Fichiers sources

Dans cet exemple, nous avons 2 rapports de démonstration.

- _Default.aspx_ démontre l'exportation en PDF en utilisant Aspose.PDF.
- _Report2.aspx_ démontre l'exportation en PDF en utilisant le contrôle d'exportation Aspose GridView (basé sur Aspose.PDF).

## Fichiers supplémentaires

`Helpers\PdfPage.cs` - contient une classe d'assistance, qui montre comment utiliser l'API Aspose.PDF.</em>

Le projet Aspose.Pdf.GridViewExport contient un contrôle GridView étendu pour la démonstration dans `Report2.aspx`