---
title: Trabajando con JavaScript
type: docs
url: /es/net/working-with-javascript/
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Trabajando con JavaScript",
    "alternativeHeadline": "Cómo trabajar con JavaScript en PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, javascript en pdf",
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
    "url": "/net/working-with-javascript/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-javascript/"
    },
    "dateModified": "2022-02-04",
    "description": ""
}
</script>
## Añadiendo JavaScript (DOM)

### ¿Qué es Acrobat JavaScript?

Acrobat JavaScript es un lenguaje basado en el núcleo de JavaScript versión 1.5 de ISO-16262, anteriormente conocido como ECMAScript, un lenguaje de scripting orientado a objetos desarrollado por Netscape Communications. JavaScript fue creado para trasladar el procesamiento de páginas web de un servidor a un cliente en aplicaciones basadas en la web. Acrobat JavaScript implementa extensiones, en forma de nuevos objetos y sus métodos y propiedades correspondientes, al lenguaje JavaScript. Estos objetos específicos de Acrobat permiten que un desarrollador gestione la seguridad del documento, se comunique con una base de datos, maneje archivos adjuntos, manipule un archivo PDF para que se comporte como un formulario interactivo y habilitado para la web, y así sucesivamente. Debido a que los objetos específicos de Acrobat se añaden encima del JavaScript núcleo, todavía tienes acceso a sus clases estándar, incluyendo Math, String, Date, Array y RegExp.

### JavaScript de Acrobat vs JavaScript de HTML (Web)

Los documentos PDF tienen una gran versatilidad ya que pueden mostrarse tanto dentro del software de Acrobat como en un navegador web.
Los documentos PDF tienen una gran versatilidad ya que pueden mostrarse tanto dentro del software Acrobat como en un navegador web.

- El JavaScript de Acrobat no tiene acceso a los objetos dentro de una página HTML. De manera similar, el JavaScript de HTML no puede acceder a los objetos dentro de un archivo PDF.
- El JavaScript de HTML puede manipular objetos como Window. El JavaScript de Acrobat no puede acceder a este objeto en particular, pero puede manipular objetos específicos de PDF.

Puedes agregar JavaScript tanto en el nivel del documento como en el nivel de la página utilizando [Aspose.PDF for .NET](/pdf/es/net/). Para agregar JavaScript:

### Agregar JavaScript a la Acción del Documento o Página

1. Declara e instancia un objeto JavascriptAction con la declaración de JavaScript deseada como argumento del constructor.
1. Asigna el objeto JavascriptAction a la acción deseada del documento o página PDF.

El ejemplo a continuación aplica OpenAction a un documento específico.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Working-Document-AddJavaScriptToPage-AddJavaScriptToPage.cs" >}}

### **Agregar/Quitar JavaScript en el Nivel del Documento**
### **Agregar/Quitar JavaScript al Nivel del Documento**

Se ha añadido una nueva propiedad llamada JavaScript en la clase Documento que tiene tipo de colección JavaScript y proporciona acceso a los escenarios de JavaScript por su clave. Esta propiedad se utiliza para agregar JavaScript a nivel de Documento. La colección de JavaScript tiene las siguientes propiedades y métodos:

- string this(string key) – Obtiene o establece JavaScript por su nombre
- IList Keys – proporciona una lista de claves existentes en la colección JavaScript
- bool Remove(string key) – elimina JavaScript por su clave.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Working-Document-AddRemoveJavascriptToDoc-AddRemoveJavascriptToDoc.cs" >}}

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


