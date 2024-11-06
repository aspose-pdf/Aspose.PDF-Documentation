---
title: Impresión de documentos PDF
linktitle: Impresión de documentos
type: docs
weight: 160
url: es/net/printing-document/
description: Técnicas de impresión de PDF en C# y guía para configuraciones de impresora PDF en C# y consejos para proyectos .NET
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/working-with-pdf-printing-facades/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Impresión de documentos PDF",
    "alternativeHeadline": "Cómo imprimir documentos PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, imprimir pdf",
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
    "url": "/net/printing-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/printing-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Técnicas de impresión de PDF en C# y guía para configuraciones de impresora PDF en C# y consejos para proyectos .NET"
}
</script>
## Cómo imprimir archivos PDF en C#

- [Imprimir PDF en .NET Framework](/pdf/net/printing-pdf-in-net-framework/)
- [Imprimir PDF en una impresora XPS (Facades)](/pdf/net/printing-pdf-to-an-xps-printer-facades/)
- [Conversión de PDF a PostScript, Verificación del estado del trabajo de impresión](/pdf/net/pdf-to-postscript-conversion/)
- [Imprimir PDF en .NET Core](/pdf/net/print-dotnetcore/)
- [Imprimir documento PDF en una aplicación WPF](/pdf/net/print-pdf-document-in-wpf-application/)

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
    "applicationCategory": "Biblioteca de manipulación de PDF para .NET",
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
# Guía de Inicio Rápido

Bienvenido a nuestro software. Esta guía te ayudará a configurar y comenzar a usar la aplicación en poco tiempo.

## Requisitos del sistema

Antes de instalar, verifica que tu sistema cumpla con estos requisitos:

- **Sistema Operativo:** Windows 10 o superior, MacOS Mojave o superior
- **Memoria:** 4GB RAM mínimo
- **Espacio en Disco:** 500MB de espacio libre

## Instalación

Sigue estos pasos para instalar el software:

1. Descarga el instalador desde nuestro sitio web.
2. Ejecuta el archivo descargado.
3. Sigue las instrucciones en pantalla para completar la instalación.

## Configuración Inicial

Después de instalar, realiza estos pasos para configurar la aplicación:

```bash
# Configura tu entorno
$ setup --init
```

## Cómo usar

Para empezar a usar la aplicación, sigue estos simples pasos:

- Abre la aplicación desde el menú de inicio.
- Inicia sesión con tus credenciales.
- Configura tus preferencias iniciales.

## Soporte

Si encuentras algún problema, por favor visita nuestro centro de soporte en:

[Centro de Soporte](https://support.nuestrositio.com)

type: docs
changefreq: "monthly"

