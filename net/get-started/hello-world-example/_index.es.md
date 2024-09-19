---
title: Ejemplo de Hola Mundo usando el lenguaje C#
linktitle: Ejemplo de Hola Mundo
type: docs
weight: 40
url: /net/hello-world-example/
description: Este ejemplo demuestra cómo crear un documento PDF simple con el texto Hola Mundo utilizando Aspose.PDF
aliases:
    - /net/hello-world/
lastmod: "2022-02-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Ejemplo de Hola Mundo usando el lenguaje C#",
    "alternativeHeadline": "Ejemplo de Aspose.PDF en C#",
    "author": {
        "@type": "Person",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, generación de documentos",
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
    "url": "http://docs.aspose.com/pdf/net/hello-world-example/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "http://docs.aspose.com/pdf/net/hello-world-example/"
    },
    "dateModified": "2022-02-04",
    "description": "Este ejemplo demuestra cómo crear un documento PDF simple con el texto Hola Mundo utilizando Aspose.PDF",
    "articleBody": "Un ejemplo de \"Hola Mundo\" es tradicionalmente utilizado para introducir características de un lenguaje de programación o software con un caso de uso simple.\nAspose.PDF para .NET es una API de PDF rica en características que permite a los desarrolladores incorporar capacidades de creación, manipulación y conversión de documentos PDF en sus aplicaciones .NET. Admite el trabajo con muchos formatos de archivo populares incluyendo PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX y formatos de archivos de imagen. En este artículo, estamos creando un documento PDF que contiene el texto \"¡Hola Mundo!\". Después de instalar Aspose.PDF para .NET en tu entorno, puedes ejecutar el siguiente ejemplo de código para ver cómo funciona la API de Aspose.PDF.\nEl siguiente fragmento de código sigue estos pasos:\n1. Instanciar un objeto Document\n2. Añadir una Página al objeto documento\n3. Crear un TextFragment\n4. Añadir TextFragment a la colección de párrafos de la página\n5. Guardar el documento PDF resultante\nEl siguiente fragmento de código es un programa de Hola Mundo para exhibir el funcionamiento de la API de Aspose.PDF para .NET."
}
</script>
Un ejemplo de "Hello World" se utiliza tradicionalmente para introducir las características de un lenguaje de programación o software con un caso de uso simple.

Aspose.PDF para .NET es una API de PDF rica en características que permite a los desarrolladores incorporar la creación, manipulación y conversión de documentos PDF en sus aplicaciones .NET. Admite trabajar con muchos formatos de archivo populares incluyendo PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX y formatos de archivo de imagen. En este artículo, estamos creando un documento PDF que contiene el texto "Hello World!". Después de instalar Aspose.PDF para .NET en su entorno, puede ejecutar el siguiente ejemplo de código para ver cómo funciona la API de Aspose.PDF.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

El fragmento de código siguiente sigue estos pasos:

1. Instanciar un objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)
1. Agregar una [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) al objeto del documento
1.
1. Añade TextFragment a la colección [Paragraph](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) de la página.
1. [Guarda](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) el documento PDF resultante.

El siguiente fragmento de código es un programa de Hola Mundo para mostrar el funcionamiento de la API Aspose.PDF para .NET.

```csharp
namespace Aspose.Pdf.Examples
{
    public static class ExampleGetStarted
    {
        private static readonly string _dataDir = "..\\..\\..\\Samples";
        public static void HelloWorld()
        {
            // Inicializar objeto documento
            Document document = new Document();
            // Añadir página
            Page page = document.Pages.Add();
            // Añadir texto a la nueva página
            page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
            // Guardar PDF actualizado
            var outputFileName = System.IO.Path.Combine(_dataDir, "HelloWorld_out.pdf");
            document.Save( outputFileName );
        }
    }
}
```
