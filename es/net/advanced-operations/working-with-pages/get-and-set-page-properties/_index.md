---
title: Obtener y Establecer Propiedades de Página
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
url: /es/net/get-and-set-page-properties/
description: Aprenda cómo obtener y establecer propiedades de página para documentos PDF utilizando Aspose.PDF for .NET, permitiendo una formateo de documento personalizado.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get and Set Page Properties",
    "alternativeHeadline": "Manage PDF Page Properties with Ease",
    "abstract": "La función Obtener y Establecer Propiedades de Página en Aspose.PDF for .NET permite a los desarrolladores acceder y manipular sin esfuerzo los atributos de página PDF. Esta funcionalidad permite a los usuarios recuperar información crítica, como el conteo de páginas y propiedades específicas como tipos de color, cajas de medios y cajas de recorte, todo con solo unas pocas líneas de código. Mejore sus capacidades de gestión de documentos PDF hoy aprovechando esta robusta característica para una manipulación eficiente de PDF en aplicaciones .NET",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1117",
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
    "url": "/net/get-and-set-page-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-and-set-page-properties/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también hacer frente a objetivos más complejos. Consulte la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

Aspose.PDF for .NET le permite leer y establecer propiedades de páginas en un archivo PDF en sus aplicaciones .NET. Esta sección muestra cómo obtener el número de páginas en un archivo PDF, obtener información sobre las propiedades de página PDF, como el color y establecer propiedades de página. Los ejemplos dados están en C#, pero puede usar cualquier lenguaje .NET, como VB.NET, para lograr lo mismo.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Obtener Número de Páginas en un Archivo PDF

Al trabajar con documentos, a menudo desea saber cuántas páginas contienen. Con Aspose.PDF, esto no toma más de dos líneas de código.

Para obtener el número de páginas en un archivo PDF:

1. Abra el archivo PDF utilizando la clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Luego, use la propiedad Count de la colección [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) (del objeto Document) para obtener el número total de páginas en el documento.

El siguiente fragmento de código muestra cómo obtener el número de páginas de un archivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetNumberOfPagesInAPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetNumberofPages.pdf"))
    {
        // Get page count
        System.Console.WriteLine("Page Count : {0}", document.Pages.Count);
    }
}
```

### Obtener conteo de páginas sin guardar el documento

A veces generamos los archivos PDF sobre la marcha y durante la creación del archivo PDF, podemos encontrarnos con la necesidad (creando Tabla de Contenidos, etc.) de obtener el conteo de páginas del archivo PDF sin guardar el archivo en el sistema o en un flujo. Por lo tanto, para atender esta necesidad, se ha introducido un método [ProcessParagraphs](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/processparagraphs) en la clase Document. Por favor, eche un vistazo al siguiente fragmento de código que muestra los pasos para obtener el conteo de páginas sin guardar el documento.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetPageCountWithoutSavingTheDocument()
{
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create loop instance
        for (var i = 0; i < 300; i++)
        {
            // Add TextFragment to paragraphs collection of page object
            page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Pages count test"));
        }
        // Process the paragraphs in PDF file to get accurate page count
        document.ProcessParagraphs();
        // Print number of pages in document
        Console.WriteLine("Number of pages in document = " + document.Pages.Count);
    }
}
```

## Obtener Propiedades de Página

Cada página en un archivo PDF tiene un número de propiedades, como el ancho, la altura, el sangrado, la caja de recorte y la caja de recorte final. Aspose.PDF le permite acceder a estas propiedades.

### **Entendiendo las Propiedades de Página: la Diferencia entre Artbox, BleedBox, CropBox, MediaBox, TrimBox y la propiedad Rect**

- **Media box**: La media box es la caja de página más grande. Corresponde al tamaño de la página (por ejemplo, A4, A5, Carta de EE. UU., etc.) seleccionado cuando se imprimió el documento en PostScript o PDF. En otras palabras, la media box determina el tamaño físico del medio en el que se muestra o imprime el documento PDF.
- **Bleed box**: Si el documento tiene sangrado, el PDF también tendrá una bleed box. El sangrado es la cantidad de color (o arte) que se extiende más allá del borde de una página. Se utiliza para asegurarse de que cuando el documento se imprime y se corta a tamaño (“recortado”), la tinta llegue hasta el borde de la página. Incluso si la página está mal recortada - cortada ligeramente fuera de las marcas de recorte - no aparecerán bordes blancos en la página.
- **Trim box**: La trim box indica el tamaño final de un documento después de imprimir y recortar.
- **Art box**: La art box es la caja dibujada alrededor del contenido real de las páginas en sus documentos. Esta caja de página se utiliza al importar documentos PDF en otras aplicaciones.
- **Crop box**: La crop box es el tamaño de “página” en el que se muestra su documento PDF en Adobe Acrobat. En la vista normal, solo se muestran los contenidos de la crop box en Adobe Acrobat.
  Para descripciones detalladas de estas propiedades, lea la especificación de Adobe.Pdf, particularmente 10.10.1 Límites de Página.
- **Page.Rect**: la intersección (rectángulo comúnmente visible) de la MediaBox y la DropBox. La imagen a continuación ilustra estas propiedades.

Para más detalles, visite [esta página](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### **Accediendo a las Propiedades de Página**

La clase [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) proporciona todas las propiedades relacionadas con una página PDF en particular. Todas las páginas de los archivos PDF están contenidas en la colección [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) del objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

Desde allí, es posible acceder a objetos Page individuales utilizando su índice, o recorrer la colección, utilizando un bucle foreach, para obtener todas las páginas. Una vez que se accede a una página individual, podemos obtener sus propiedades. El siguiente fragmento de código muestra cómo obtener propiedades de página.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AccessingPageProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetProperties.pdf"))
    {
        // Get page collection
        var pageCollection = document.Pages;
        // Get particular page
        var pdfPage = pageCollection[1];
        // Get page properties
        System.Console.WriteLine("ArtBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.ArtBox.Height, pdfPage.ArtBox.Width, pdfPage.ArtBox.LLX,
            pdfPage.ArtBox.LLY, pdfPage.ArtBox.URX, pdfPage.ArtBox.URY);
        System.Console.WriteLine("BleedBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.BleedBox.Height, pdfPage.BleedBox.Width, pdfPage.BleedBox.LLX,
            pdfPage.BleedBox.LLY, pdfPage.BleedBox.URX, pdfPage.BleedBox.URY);
        System.Console.WriteLine("CropBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.CropBox.Height, pdfPage.CropBox.Width, pdfPage.CropBox.LLX,
            pdfPage.CropBox.LLY, pdfPage.CropBox.URX, pdfPage.CropBox.URY);
        System.Console.WriteLine("MediaBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.MediaBox.Height, pdfPage.MediaBox.Width, pdfPage.MediaBox.LLX,
            pdfPage.MediaBox.LLY, pdfPage.MediaBox.URX, pdfPage.MediaBox.URY);
        System.Console.WriteLine("TrimBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.TrimBox.Height, pdfPage.TrimBox.Width, pdfPage.TrimBox.LLX,
            pdfPage.TrimBox.LLY, pdfPage.TrimBox.URX, pdfPage.TrimBox.URY);
        System.Console.WriteLine("Rect : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.Rect.Height, pdfPage.Rect.Width, pdfPage.Rect.LLX, pdfPage.Rect.LLY,
            pdfPage.Rect.URX, pdfPage.Rect.URY);
        System.Console.WriteLine("Page Number : {0}", pdfPage.Number);
        System.Console.WriteLine("Rotate : {0}", pdfPage.Rotate);
    }
}
```

## Obtener una Página Particular del Archivo PDF

Aspose.PDF le permite [dividir un PDF en páginas individuales](/pdf/net/split-pdf-document/) y guardarlas como archivos PDF. Obtener una página especificada en un archivo PDF y guardarla como un nuevo PDF es una operación muy similar: abrir el documento fuente, acceder a la página, crear un nuevo documento y agregar la página a este.

La colección [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) del objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) contiene las páginas en el archivo PDF. Para obtener una página particular de esta colección:

1. Especifique el índice de la página utilizando la propiedad Pages.
1. Cree un nuevo objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Agregue el objeto [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) al nuevo objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Guarde la salida utilizando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

El siguiente fragmento de código muestra cómo obtener una página particular de un archivo PDF y guardarla como un nuevo archivo.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetAParticularPageOfThePdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get particular page
        var pdfPage = document.Pages[2];
        // Save the page as PDF file
        using (var newDocument = new Aspose.Pdf.Document())
        {
            newDocument.Pages.Add(pdfPage);
            // Save PDF document
            newDocument.Save(dataDir + "GetParticularPage_out.pdf");
        }
    }
}
```

## Determinar el Color de Página

La clase [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) proporciona las propiedades relacionadas con una página particular en un documento PDF, incluyendo qué tipo de color - RGB, blanco y negro, escala de grises o indefinido - utiliza la página.

Todas las páginas de los archivos PDF están contenidas en la colección [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection). La propiedad ColorType especifica el color de los elementos en la página. Para obtener o determinar la información de color para una página PDF particular, use la propiedad [ColorType](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/colortype) del objeto [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).

El siguiente fragmento de código muestra cómo iterar a través de cada página individual de un archivo PDF para obtener información de color.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeterminePageColor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Iterate through all the page of PDF file
        for (var pageCount = 1; pageCount <= document.Pages.Count; pageCount++)
        {
            // Get the color type information for particular PDF page
            Aspose.Pdf.ColorType pageColorType = document.Pages[pageCount].ColorType;
            switch (pageColorType)
            {
                case Aspose.Pdf.ColorType.BlackAndWhite:
                    Console.WriteLine("Page # -" + pageCount + " is Black and white..");
                    break;
                case Aspose.Pdf.ColorType.Grayscale:
                    Console.WriteLine("Page # -" + pageCount + " is Gray Scale...");
                    break;
                case Aspose.Pdf.ColorType.Rgb:
                    Console.WriteLine("Page # -" + pageCount + " is RGB..", pageCount);
                    break;
                case Aspose.Pdf.ColorType.Undefined:
                    Console.WriteLine("Page # -" + pageCount + " Color is undefined..");
                    break;
            }
        }
    }
}
```

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