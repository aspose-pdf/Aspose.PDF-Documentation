---
title: Renderizar WebForms DataGridView a PDF
linktitle: Renderizar WebForms DataGridView a PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /es/net/render-webforms-datagridview-to-pdf/
description: Esta muestra muestra cómo usar la biblioteca Aspose.PDF para renderizar WebForm a PDF.
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
    "abstract": "La función permite la conversión sin problemas de WebForms DataGridView a PDF utilizando la biblioteca Aspose.PDF for .NET. Esta funcionalidad simplifica el proceso de exportación de datos al integrar un control de exportación de GridView dedicado, asegurando una renderización de PDF de alta calidad directamente desde aplicaciones web. Perfecto para desarrolladores que buscan soluciones eficientes de generación de documentos.",
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
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Cómo exportar WebForm a PDF usando Aspose.PDF/Aspose.HTML

### Introducción

Generalmente, para convertir WebForm a documento PDF se utilizan herramientas adicionales. Esta muestra muestra cómo usar la biblioteca Aspose.PDF para renderizar WebForm a PDF. El control Aspose Export GridView To Pdf también está incluido en esta muestra para mostrar cómo renderizar _el control GridView a un documento PDF_.

## Cómo renderizar WebForm a PDF

La idea original para renderizar WebForm a PDF es crear una clase auxiliar, que herede de [System.Web.UI.Page](https://msdn.microsoft.com/en-US/library/System.Web.UI.Page.aspx), y sobrescribir un método Render.</em></p>

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

Hay dos herramientas de Aspose que se pueden usar para renderizar HTML a PDF:

- Aspose.PDF for .NET.
- Control de exportación de Aspose GridView (basado en Aspose.PDF).

## Archivos fuente

En esta muestra tenemos 2 informes de demostración.

- _Default.aspx_ demuestra la exportación a PDF usando Aspose.PDF.
- _Report2.aspx_ demuestra la exportación a PDF usando el control de exportación de Aspose GridView (basado en Aspose.PDF).

## Archivos adicionales

`Helpers\PdfPage.cs` - contiene una clase auxiliar, que muestra cómo usar la API de Aspose.PDF.</em>

El proyecto Aspose.Pdf.GridViewExport contiene un control GridView extendido para demostración en `Report2.aspx`.