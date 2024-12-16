---
title: Obtener y Establecer Propiedades de Página
type: docs
url: /es/net/get-and-set-page-properties/
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Obtener y Establecer Propiedades de Página",
    "alternativeHeadline": "Obtención y Establecimiento de Propiedades de Página PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, obtener propiedades de página, establecer propiedades de página",
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
    "url": "/net/get-and-set-page-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-and-set-page-properties/"
    },
    "dateModified": "2022-02-04",
    "description": ""
}
</script
Aspose.PDF para .NET le permite leer y establecer propiedades de las páginas en un archivo PDF en sus aplicaciones .NET. Esta sección muestra cómo obtener el número de páginas en un archivo PDF, obtener información sobre propiedades de la página PDF como el color y establecer propiedades de la página. Los ejemplos dados están en C#, pero puede usar cualquier lenguaje .NET como VB.NET para lograr lo mismo.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

## Obtener el Número de Páginas en un Archivo PDF

Cuando trabaja con documentos, a menudo desea saber cuántas páginas contienen. Con Aspose.PDF esto toma no más de dos líneas de código.

Para obtener el número de páginas en un archivo PDF:

1. Abra el archivo PDF usando la clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Luego use la propiedad Count de la colección [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) (del objeto Document) para obtener el número total de páginas en el documento.

El siguiente fragmento de código muestra cómo obtener el número de páginas de un archivo PDF.
El siguiente fragmento de código muestra cómo obtener el número de páginas de un archivo PDF.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetNumberofPages-GetNumberofPages.cs" >}}

### Obtener el recuento de páginas sin guardar el documento

A veces generamos los archivos PDF al vuelo y durante la creación del archivo PDF, podemos encontrarnos con la necesidad (crear Tabla de Contenidos, etc.) de obtener el recuento de páginas del archivo PDF sin guardar el archivo en el sistema o en un flujo. Para atender a esta necesidad, se ha introducido un método [ProcessParagraphs](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/processparagraphs) en la clase Document. Por favor, mire el siguiente fragmento de código que muestra los pasos para obtener el recuento de páginas sin guardar el documento.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetPageCount-GetPageCount.cs" >}}

## Obtener Propiedades de la Página

Cada página en un archivo PDF tiene una serie de propiedades, como el ancho, la altura y las cajas de sangrado, corte y recorte.
### **Entendiendo las Propiedades de la Página: la Diferencia entre Artbox, BleedBox, CropBox, MediaBox, TrimBox y la propiedad Rect**

- **Media box**: La caja de medios es la caja de página más grande. Corresponde al tamaño de página (por ejemplo, A4, A5, Carta de EE. UU., etc.) seleccionado cuando el documento fue impreso en PostScript o PDF. En otras palabras, la caja de medios determina el tamaño físico de los medios en los cuales se muestra o se imprime el documento PDF.
- **Bleed box**: Si el documento tiene sangría, el PDF también tendrá una caja de sangría. La sangría es la cantidad de color (o arte) que se extiende más allá del borde de una página. Se utiliza para asegurarse de que cuando el documento se imprime y se corta a tamaño (“recortado”), la tinta llegará hasta el borde de la página. Incluso si la página está mal recortada - cortada ligeramente fuera de las marcas de recorte - no aparecerán bordes blancos en la página.
- **Trim box**: La caja de recorte indica el tamaño final de un documento después de imprimirse y recortarse.
- **Trim box**: El trim box indica el tamaño final de un documento después de imprimirlo y recortarlo.
- **Art box**: El art box es el cuadro dibujado alrededor del contenido real de las páginas en sus documentos. Esta caja de página se utiliza al importar documentos PDF en otras aplicaciones.
- **Crop box**: El crop box es el tamaño de “página” en el que se muestra su documento PDF en Adobe Acrobat. En la vista normal, solo se muestran los contenidos del crop box en Adobe Acrobat.
  Para descripciones detalladas de estas propiedades, lea la especificación de Adobe.Pdf, particularmente 10.10.1 Límites de la página.
- **Page.Rect**: la intersección (rectángulo comúnmente visible) del MediaBox y DropBox. La imagen a continuación ilustra estas propiedades.

Para más detalles, por favor visite [esta página](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### **Accediendo a las Propiedades de la Página**

La clase [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) proporciona todas las propiedades relacionadas con una página PDF en particular.
La clase [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) proporciona todas las propiedades relacionadas con una página PDF específica.

Desde allí, es posible acceder a objetos Page individuales usando su índice, o recorrer la colección, utilizando un bucle foreach, para obtener todas las páginas. Una vez que se accede a una página individual, podemos obtener sus propiedades. El siguiente fragmento de código muestra cómo obtener las propiedades de la página.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetProperties-GetProperties.cs" >}}

## Obtener una Página Específica del Archivo PDF

Aspose.PDF permite [dividir un PDF en páginas individuales](/pdf/es/net/split-pdf-document/) y guardarlas como archivos PDF. Obtener una página especificada en un archivo PDF y guardarla como un nuevo PDF es una operación muy similar: abrir el documento fuente, acceder a la página, crear un nuevo documento y agregar la página a este.

El objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) y su [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) contienen las páginas en el archivo PDF.
El objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) contiene la [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) que alberga las páginas del archivo PDF.

1. Especifica el índice de la página usando la propiedad Pages.
1. Crea un nuevo objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Añade el objeto [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) al nuevo objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Guarda el resultado usando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

El siguiente fragmento de código muestra cómo obtener una página particular de un archivo PDF y guardarla como un nuevo archivo.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetParticularPage-GetParticularPage.cs" >}}

## Determinar el Color de la Página

La clase [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) proporciona las propiedades relacionadas con una página particular en un documento PDF, incluyendo qué tipo de color - RGB, blanco y negro, escala de grises o indefinido - utiliza la página.
La clase [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) proporciona las propiedades relacionadas con una página particular en un documento PDF, incluyendo qué tipo de color - RGB, blanco y negro, escala de grises o indefinido - utiliza la página.

Todas las páginas de los archivos PDF están contenidas por la colección [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection). La propiedad ColorType especifica el color de los elementos en la página. Para obtener o determinar la información de color para una página PDF particular, use la propiedad [ColorType](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/colortype) del objeto [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).

El siguiente fragmento de código muestra cómo iterar a través de cada página individual del archivo PDF para obtener información de color.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-DeterminePageColor-DeterminePageColor.cs" >}}

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


