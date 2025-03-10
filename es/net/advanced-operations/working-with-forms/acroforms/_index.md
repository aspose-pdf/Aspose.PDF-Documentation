---
title: Trabajando con AcroForms
linktitle: AcroForms
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /es/net/acroforms/
description: Con Aspose.PDF for .NET puedes crear un formulario desde cero, llenar los campos del formulario en un documento PDF, extraer datos del formulario, etc.
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
    "abstract": "Aspose.PDF for .NET introduce capacidades mejoradas para trabajar con AcroForms, permitiendo a los usuarios crear formularios de manera eficiente desde cero, llenar campos PDF y extraer datos sin problemas. Esta poderosa característica admite la integración de múltiples registros de bases de datos, lo que permite una gestión dinámica de formularios y una experiencia de usuario optimizada.",
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
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también enfrentar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Fundamentos de AcroForms

**AcroForms** son la tecnología original de formularios PDF. AcroForms es un formulario orientado a páginas. Se introdujeron por primera vez en 1998. Aceptan entrada en Formato de Datos de Formularios o FDF y Formato de Datos de Formularios XML o xFDF. Los proveedores de terceros admiten AcroForms. Cuando Adobe introdujo los AcroForms, se refirieron a ellos como "formulario PDF que se crea con Adobe Acrobat Pro/Standard y que no es un tipo especial de formulario XFA estático o dinámico". Los AcroForms son portátiles y funcionan en todas las plataformas.

Puedes usar AcroForms para agregar páginas adicionales al documento del formulario PDF. Gracias al concepto de Plantillas, puedes usar AcroForms para admitir la población del formulario con múltiples registros de bases de datos.

PDF 1.7 admite dos métodos diferentes para integrar datos y formularios PDF.

*AcroForms (también conocidos como formularios de Acrobat)*, introducidos e incluidos en la especificación del formato PDF 1.2.

*Formularios de Arquitectura de Formularios XML de Adobe (XFA)*, introducidos en la especificación del formato PDF 1.5 como una característica opcional (la especificación XFA no está incluida en la especificación PDF, solo se hace referencia a ella).

Para entender **Acroforms** vs **formularios XFA**, primero necesitamos comprender los conceptos básicos. Para empezar, ambos son formularios PDF que puedes usar. Acroforms es el más antiguo, creado en 1998, y todavía se le conoce como el formulario PDF clásico. Los formularios XFA son páginas web que puedes guardar como PDF, y aparecieron en 2003. Pasó un tiempo antes de que PDF comenzara a aceptar formularios XFA.

Los AcroForms tienen capacidades que no se encuentran en XFA y, a la inversa, XFA tiene algunas capacidades que no se encuentran en AcroForms. Por ejemplo:

- Los AcroForms admiten el concepto de "Plantillas", permitiendo que se agreguen páginas adicionales al documento del formulario PDF para admitir la población del formulario con múltiples registros de bases de datos.
- XFA admite el concepto de reflujo de documentos, permitiendo que un campo se redimensione si es necesario para acomodar datos.

Para un aprendizaje más detallado de las capacidades de la biblioteca Java, consulta los siguientes artículos:

- [Crear AcroForm](/pdf/es/net/create-form) - crear un formulario desde cero con C#.
- [Llenar AcroForm](/pdf/es/net/fill-form) - llenar el campo del formulario en tu documento PDF.
- [Extraer AcroForm](/pdf/es/net/extract-form) - obtener el valor de todos o de un campo individual del documento PDF.
- [Modificando AcroForm](/pdf/es/net/modifing-form) - obtener o establecer FieldLimit, establecer la fuente del campo del formulario, etc.
- [Publicar Datos de AcroForm](/pdf/es/net/posting-acroform-data/) - importar y exportar datos del formulario a un archivo XML.
- [Importar y Exportar Datos](/pdf/es/net/import-and-export-data/) - importar y exportar datos utilizando la Clase Form.
- [Eliminar Formularios de PDF](/pdf/es/net/remove-form/) - eliminar texto basado en subtipo/formulario, eliminar todos los formularios.
- [Importar y Exportar Datos en JSON](/pdf/es/net/import-export-json/) - importar y exportar datos con JSON

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