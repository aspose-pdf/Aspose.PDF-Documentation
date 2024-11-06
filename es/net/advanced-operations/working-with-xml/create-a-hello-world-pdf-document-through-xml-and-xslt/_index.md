---
title: Creación de PDF a partir de XML usando XSLT
linktitle: Crear PDF a partir de XML usando XSLT
type: docs
weight: 10
url: es/net/create-a-hello-world-pdf-document-through-xml-and-xslt/
description: La biblioteca de C# proporciona la capacidad de convertir un archivo XML en un documento PDF requiriendo que el archivo XML de entrada siga el esquema Aspose.PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Creación de PDF a partir de XML usando XSLT",
    "alternativeHeadline": "Cómo crear PDF a partir de XML usando XSLT",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, c#, crear pdf xml, pdf con xslt",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/create-a-hello-world-pdf-document-through-xml-and-xslt/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-a-hello-world-pdf-document-through-xml-and-xslt/"
    },
    "dateModified": "2022-02-04",
    "description": "La biblioteca de C# proporciona la capacidad de convertir un archivo XML en un documento PDF requiriendo que el archivo XML de entrada siga el esquema Aspose.PDF."
}
</script>
El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

A veces puede tener archivos XML existentes que contienen datos de la aplicación y desea generar un informe PDF utilizando estos archivos. Puede utilizar XSLT para transformar su documento XML existente a un documento XML compatible con Aspose.Pdf y luego generar un archivo PDF. Hay 3 pasos para generar PDF usando XML y XSLT.

Siga estos pasos para convertir un archivo XML en un documento PDF usando XSLT:

* Crear una instancia de la clase PDF que representa un documento PDF
* Si ha comprado una licencia, entonces también debe incrustar el código para usar esa licencia con la ayuda de la clase License en el espacio de nombres Aspose.Pdf
* Vincule los archivos XML y XSLT de entrada a la instancia de la clase PDF llamando a su método BindXML
* Guarde el XML vinculado con la instancia de PDF como un documento PDF

## Archivo XML de Entrada

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Contents>
  <Content>Hello World!</Content>
</Contents>
```

## Archivo XSLT de Entrada

```xml
<?xml version="1.0" encoding="utf-8" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="text()"/>
    <xsl:template match="/Contents">
    <html>
      <Document xmlns="Aspose.Pdf" IsAutoHyphenated="false">
        <PageInfo>
          <DefaultTextState
                            Font = "Helvetica" FontSize="8" LineSpacing="4"/>
          <Margin Left="5cm" Right="5cm" Top="3cm" Bottom="15cm" />
        </PageInfo>
        <Page id="mainSection">
          <TextFragment>
            <TextSegment>
              <xsl:value-of select="Content"/>
            </TextSegment>
          </TextFragment>
        </Page>
      </Document>
    </html>
</xsl:template>
</xsl:stylesheet>
```

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Working-Document-HelloWorldPDFUsingXmlAndXslt-HelloWorldPDFUsingXmlAndXslt.cs" >}}

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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Biblioteca de Manipulación de PDF para .NET",
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
```

---
id: build-release-run
title: Construir, Liberar, Ejecutar
sidebar_label: Construir, Liberar, Ejecutar
description: Construir y liberar software de manera eficiente.
---

import useBaseUrl from '@docusaurus/useBaseUrl';

## Introducción

En el desarrollo de software moderno, construir, liberar y ejecutar son tres aspectos esenciales para garantizar que el software se entregue de manera eficiente y con alta calidad. Este documento proporciona una guía sobre cómo realizar estas actividades de manera efectiva.

## Construir

La fase de construcción implica convertir el código fuente en un formato ejecutable. Esto puede incluir compilación, minificación y otras formas de transformación del código.

- **Compilación:** Convertir código fuente en binarios ejecutables.
- **Minificación:** Reducir el tamaño de los archivos para mejorar el rendimiento.

## Liberar

Liberar el software implica empaquetarlo y distribuirlo a los usuarios o a un entorno de producción.

- **Versionado:** Asignar números de versión para rastrear cambios.
- **Empaquetado:** Crear archivos de distribución como tarballs o instaladores.

## Ejecutar

Ejecutar el software implica desplegarlo en un entorno y mantenerlo en funcionamiento.

- **Despliegue:** Instalar el software en un entorno de producción.
- **Monitoreo:** Supervisar el rendimiento y la disponibilidad del software.

## Conclusión

Construir, liberar y ejecutar son procesos críticos en el ciclo de vida del desarrollo de software. Siguiendo prácticas efectivas, se puede garantizar que el software se entregue de manera eficiente y con alta calidad.

changefreq: "monthly"
type: docs
```
