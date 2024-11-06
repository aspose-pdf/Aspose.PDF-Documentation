---
title: Generar Imágenes en Miniatura desde PDF
linktitle: Generar Imágenes en Miniatura
type: docs
weight: 110
url: es/net/generate-thumbnail-images-from-pdf-documents/
description: Esta sección describe cómo generar imágenes en miniatura desde documentos PDF
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Generar Imágenes en Miniatura desde PDF",
    "alternativeHeadline": "Cómo generar Imágenes en Miniatura desde un archivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, generar imágenes en miniatura",
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
    "url": "/net/generate-thumbnail-images-from-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/generate-thumbnail-images-from-pdf-documents/"
    },
    "dateModified": "2022-02-04",
    "description": "Esta sección describe cómo generar imágenes en miniatura desde documentos PDF"
}
</script>
{{% alert color="primary" %}}

El SDK de Adobe Acrobat es un conjunto de herramientas que te ayudan a desarrollar software que interactúa con la tecnología de Acrobat. El SDK contiene archivos de cabecera, bibliotecas de tipos, utilidades simples, código de muestra y documentación.

Utilizando el SDK de Acrobat, puedes desarrollar software que se integra con Acrobat y Adobe Reader de varias maneras:

- **JavaScript** — Escribe scripts, ya sea en un documento PDF individual o externamente, para extender la funcionalidad de Acrobat o Adobe Reader.
- **Plug-ins** — Crea plug-ins que están vinculados dinámicamente y extienden la funcionalidad de Acrobat o Adobe Reader.
- **Comunicación entre aplicaciones** — Escribe un proceso de aplicación separado que utiliza comunicación entre aplicaciones (IAC) para controlar la funcionalidad de Acrobat. DDE y OLE son compatibles en Microsoft® Windows®, y eventos de Apple/AppleScript en Mac OS®. IAC no está disponible en UNIX®.

Aspose.PDF para .NET ofrece mucha de la misma funcionalidad, liberándote de la dependencia de la Automatización de Adobe Acrobat.
Aspose.PDF para .NET proporciona muchas de las mismas funcionalidades, liberándote de la dependencia de la automatización de Adobe Acrobat.

{{% /alert %}}

## Desarrollando aplicaciones utilizando la API de comunicación interaplicación de Acrobat

Piensa en la API de Acrobat como si tuviera dos capas distintas que utilizan objetos de comunicación interaplicación de Acrobat (IAC):

- La capa de la aplicación Acrobat (AV). La capa AV te permite controlar cómo se visualiza el documento. Por ejemplo, la vista de un objeto de documento reside en la capa asociada con Acrobat.
- La capa de documento portátil (PD). La capa PD proporciona acceso a la información dentro de un documento, como una página. Desde la capa PD puedes realizar manipulaciones básicas de documentos PDF, como eliminar, mover o reemplazar páginas, así como cambiar atributos de anotación. También puedes imprimir páginas de PDF, seleccionar texto, acceder a texto manipulado y crear o eliminar miniaturas.

Dado que nuestro objetivo es convertir páginas de PDF en imágenes de miniaturas, nos estamos enfocando más en IAC.
Como nuestro objetivo es convertir páginas PDF en imágenes en miniatura, estamos enfocándonos más en IAC.

### Enfoque Acrobat

Para generar las imágenes en miniatura de cada documento, hemos utilizado el SDK de Adobe Acrobat 7.0 y el Microsoft .NET 2.0 Framework.

El [SDK de Acrobat](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/) combinado con la versión completa de Adobe Acrobat expone una biblioteca COM de objetos (lamentablemente, el Adobe Reader gratuito no expone las interfaces COM) que se pueden utilizar para manipular y acceder a la información de los PDF. Utilizando estos objetos COM a través de COM Interop, carga el documento PDF, obtén la primera página y renderiza esa página al portapapeles. Luego, con el .NET Framework, copia esto a un bitmap, escala y combina la imagen y guarda el resultado como un archivo GIF o PNG.

Una vez que Adobe Acrobat está instalado, usa regedit.exe y busca bajo HKEY_CLASSES_ROOT una entrada llamada AcroExch.PDDoc.

**El registro que muestra la entrada AcroExch.PDDDoc**

![todo:image_alt_text](generate-thumbnail-images-from-pdf-documents_1.png)
![todo:image_alt_text](generate-thumbnail-images-from-pdf-documents_1.png)

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-CreateThumbnailImagesUsingAdobe-CreateThumbnailImagesUsingAdobe.cs" >}}

## Enfoque de Aspose.PDF para .NET

Aspose.PDF para .NET ofrece un soporte extenso para trabajar con documentos PDF. También soporta la capacidad de convertir las páginas de documentos PDF en una variedad de formatos de imagen. La funcionalidad descrita anteriormente se puede lograr fácilmente utilizando Aspose.PDF para .NET.

Aspose.PDF tiene beneficios distintos:

- No necesitas tener Adobe Acrobat instalado en tu sistema para trabajar con archivos PDF.
- Usar Aspose.PDF para .NET es simple y fácil de entender en comparación con la Automatización de Acrobat.

Si necesitamos convertir páginas PDF en JPEGs, el espacio de nombres [Aspose.PDF.Devices](https://reference.aspose.com/pdf/net/aspose.pdf.devices) proporciona una clase llamada [JpegDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/jpegdevice) para renderizar páginas PDF en imágenes JPEG.
Si necesitamos convertir páginas de PDF a JPEGs, el espacio de nombres [Aspose.PDF.Devices](https://reference.aspose.com/pdf/net/aspose.pdf.devices) proporciona una clase llamada [JpegDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/jpegdevice) para renderizar páginas de PDF en imágenes JPEG.

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-CreateThumbnailImages-CreateThumbnailImages.cs" >}}

{{% alert color="primary" %}}

- Gracias a CodeProject por [Generar imagen en miniatura desde documento PDF](https://www.codeproject.com/Articles/5887/Generate-Thumbnail-Images-from-PDF-Documents).
- Gracias a Acrobat por la [referencia del SDK de Acrobat](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/documentation.html).

{{% /alert %}}

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

