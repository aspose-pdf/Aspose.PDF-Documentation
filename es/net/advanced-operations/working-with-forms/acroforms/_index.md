---
title: Trabajando con AcroForms
linktitle: AcroForms
type: docs
weight: 10
url: es/net/acroforms/
description: Con Aspose.PDF para .NET puedes crear un formulario desde cero, llenar el campo de formulario en un documento PDF, extraer datos del formulario, y etc.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Trabajando con AcroForms",
    "alternativeHeadline": "Opciones para trabajar con AcroForms en PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, acroforms en pdf",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipo de Documentación de Aspose.PDF",
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
                "contactType": "ventas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventas",
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
    "description": "Con Aspose.PDF para .NET puedes crear un formulario desde cero, llenar el campo de formulario en un documento PDF, extraer datos del formulario, y etc."
}
</script>  
## Fundamentos de AcroForms

**AcroForms** son la tecnología original de formularios PDF. AcroForms es un formulario orientado a páginas. Fueron introducidos por primera vez en 1998. Aceptan entradas en Formato de Datos de Formularios o FDF y Formato de Datos de Formularios XML o xFDF. Los proveedores de terceros admiten AcroForms. Cuando Adobe introdujo los AcroForms, se referían a ellos como "formulario PDF que se crea con Adobe Acrobat Pro/Standard y que no es un tipo especial de formulario XFA estático o dinámico. Los AcroForms son portátiles y funcionan en todas las plataformas.

Puedes usar AcroForms para añadir páginas adicionales al documento de formulario PDF. Gracias al concepto de Plantillas, puedes usar AcroForms para apoyar la población del formulario con múltiples registros de bases de datos.

PDF 1.7 soporta dos métodos diferentes para integrar datos y formularios PDF.

*AcroForms (también conocidos como formularios Acrobat)*, introducidos e incluidos en la especificación del formato PDF 1.2.

*Formularios de Arquitectura de Formularios XML de Adobe (XFA)*, introducidos en la especificación del formato PDF 1.5 como una característica opcional (La especificación XFA no está incluida en la especificación PDF, solo se hace referencia a ella).
*Formularios Adobe XML Forms Architecture (XFA)*, introducidos en la especificación del formato PDF 1.5 como una característica opcional (La especificación de XFA no está incluida en la especificación de PDF, solo se hace referencia a ella.

Para entender **Acroforms** vs **formularios XFA**, primero necesitamos entender los conceptos básicos. Ambos son formularios PDF que puedes utilizar. Acroforms es el más antiguo, creado en 1998, y todavía se le conoce como el formulario PDF clásico. Los formularios XFA son páginas web que puedes guardar como un PDF, y aparecieron en 2003. Tomó algún tiempo antes de que PDF comenzara a aceptar formularios XFA.

AcroForms tiene capacidades que no se encuentran en XFA y viceversa, XFA tiene algunas capacidades que no se encuentran en AcroForms. Por ejemplo:

- AcroForms admite el concepto de “Plantillas”, permitiendo añadir páginas adicionales al documento del formulario PDF para apoyar la población del formulario con múltiples registros de base de datos.
- XFA admite el concepto de reflujo del documento permitiendo que un campo se redimensione si es necesario para acomodar los datos.

Para un aprendizaje más detallado de las capacidades de la biblioteca Java, consulta los siguientes artículos:
Para un aprendizaje más detallado de las capacidades de la biblioteca Java, consulte los siguientes artículos:

- [Crear AcroForm](/pdf/net/create-form) - crea un formulario desde cero con C#.
- [Llenar AcroForm](/pdf/net/fill-form) - llena campos de formulario en tu documento PDF.
- [Extraer AcroForm](/pdf/net/extract-form) - obtén el valor de todos o un campo individual del documento PDF.
- [Modificar AcroForm](/pdf/net/modifing-form) - obtén o establece FieldLimit, establece la fuente del campo del formulario y etc.
- [Publicar datos de AcroForm](/pdf/net/posting-acroform-data/) - importa y exporta datos del formulario a un archivo XML y desde este.
- [Importar y Exportar Datos](/pdf/net/import-and-export-data/) - importa y exporta datos usando la Clase Formulario.

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

