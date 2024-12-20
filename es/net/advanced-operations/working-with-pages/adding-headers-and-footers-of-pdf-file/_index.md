---
title: Añadir Encabezado y Pie de página al PDF
linktitle: Añadir Encabezado y Pie de página al PDF
type: docs
weight: 70
url: /es/net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF para .NET te permite añadir encabezados y pies de página a tu archivo PDF utilizando la clase TextStamp.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Añadir Encabezado y Pie de página al PDF",
    "alternativeHeadline": "Cómo añadir Encabezado y Pie de página a un Archivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, añadir encabezado, añadir pie de página en pdf",
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
    "url": "/net/add-headers-and-footers-of-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-headers-and-footers-of-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF para .NET te permite añadir encabezados y pies de página a tu archivo PDF utilizando la clase TextStamp."
}
</script>
**Aspose.PDF para .NET** te permite agregar encabezados y pies de página en tu archivo PDF existente. Puedes agregar imágenes o texto a un documento PDF. También, intenta agregar diferentes encabezados en un archivo PDF con C#.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

## Agregando Texto en el Encabezado de un Archivo PDF

Puedes usar la clase [TextStamp](https://reference.aspose.com/pdf/net/aspose.pdf/textstamp) para agregar texto en el encabezado de un archivo PDF. La clase TextStamp proporciona propiedades necesarias para crear un sello basado en texto como tamaño de fuente, estilo de fuente y color de fuente, etc. Para agregar texto en el encabezado, necesitas crear un objeto Document y un objeto TextStamp usando las propiedades requeridas. Después de eso, puedes llamar al método AddStamp de la Página para agregar el texto en el encabezado del PDF.

Necesitas configurar la propiedad TopMargin de tal manera que ajuste el texto en el área del encabezado de tu PDF. También necesitas configurar la Alineación Horizontal a Centro y la Alineación Vertical a Superior.

El siguiente fragmento de código te muestra cómo agregar texto en el encabezado de un archivo PDF con C#.
El siguiente fragmento de código muestra cómo agregar texto en el encabezado de un archivo PDF con C#.

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Abrir documento
Document pdfDocument = new Document(dataDir+ "TextinHeader.pdf");

// Crear encabezado
TextStamp textStamp = new TextStamp("Texto del Encabezado");
// Establecer propiedades del sello
textStamp.TopMargin = 10;
textStamp.HorizontalAlignment = HorizontalAlignment.Center;
textStamp.VerticalAlignment = VerticalAlignment.Top;
// Agregar encabezado en todas las páginas
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(textStamp);
}
// Guardar el documento actualizado
pdfDocument.Save(dataDir+ "TextinHeader_out.pdf");
```

## Agregar Texto en el Pie de Página de un Archivo PDF

Puedes usar la clase TextStamp para agregar texto en el pie de página de un archivo PDF.
Puedes usar la clase TextStamp para agregar texto en el pie de página de un archivo PDF.

{{% alert color="primary" %}}

Necesitas configurar la propiedad de Margen Inferior de tal manera que ajuste el texto en el área del pie de página de tu PDF. También debes configurar HorizontalAlignment en Centro y VerticalAlignment en Inferior

{{% /alert %}}

El siguiente fragmento de código te muestra cómo agregar texto en el pie de página de un archivo PDF con C#.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Abrir documento
Document pdfDocument = new Document(dataDir+ "TextinFooter.pdf");
// Crear pie de página
TextStamp textStamp = new TextStamp("Texto del pie de página");
// Configurar propiedades del sello
textStamp.BottomMargin = 10;
textStamp.HorizontalAlignment = HorizontalAlignment.Center;
textStamp.VerticalAlignment = VerticalAlignment.Bottom;
// Agregar pie de página en todas las páginas
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(textStamp);
}
// Guardar archivo de salida
doc.Save(dataDir + "TextinFooter_out.pdf");
```
## Agregando Imagen en el Encabezado de un Archivo PDF

Puede usar la clase [ImageStamp](https://reference.aspose.com/pdf/net/aspose.pdf/ImageStamp) para agregar una imagen en el encabezado de un archivo PDF. La clase Image Stamp proporciona propiedades necesarias para crear un sello basado en imagen como tamaño de fuente, estilo de fuente y color de fuente, etc. Para agregar una imagen en el encabezado, necesita crear un objeto Document y un objeto Image Stamp usando las propiedades requeridas. Después de eso, puede llamar al método [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) de la página para agregar la imagen en el encabezado del PDF.

{{% alert color="primary" %}}

Necesita configurar la propiedad TopMargin de tal manera que ajuste la imagen en el área del encabezado de su PDF. También necesita configurar HorizontalAlignment en Center y VerticalAlignment en Top.

{{% /alert %}}

El siguiente fragmento de código le muestra cómo agregar una imagen en el encabezado de un archivo PDF con C#.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Abrir documento
Document pdfDocument = new Document(dataDir+ "ImageinHeader.pdf");

// Crear encabezado
ImageStamp imageStamp = new ImageStamp(dataDir+ "aspose-logo.jpg");
// Configurar propiedades del sello
imageStamp.TopMargin = 10;
imageStamp.HorizontalAlignment = HorizontalAlignment.Center;
imageStamp.VerticalAlignment = VerticalAlignment.Top;
// Agregar encabezado en todas las páginas
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(imageStamp);
}
// Guardar archivo de salida
doc.Save(dataDir + "ImageinHeader_out.pdf");
```
## Agregando Imagen en el Pie de Página de un Archivo PDF

Puedes usar la clase Image Stamp para agregar una imagen en el pie de página de un archivo PDF. La clase Image Stamp proporciona propiedades necesarias para crear un sello basado en imagen como tamaño de fuente, estilo de fuente y color de fuente, etc. Para agregar una imagen en el pie de página, necesitas crear un objeto Document y un objeto Image Stamp utilizando las propiedades requeridas. Después de eso, puedes llamar al método AddStamp de la Página para agregar la imagen en el pie de página del PDF.

{{% alert color="primary" %}}

Necesitas configurar la propiedad [BottomMargin](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/bottommargin) de tal manera que ajuste la imagen en el área del pie de página de tu PDF. También necesitas configurar [HorizontalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/horizontalalignment) a `Center` y [VerticalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf/stamp/properties/verticalalignment) a `Bottom`.

{{% /alert %}}

El siguiente fragmento de código te muestra cómo agregar una imagen en el pie de página de un archivo PDF con C#.
El siguiente fragmento de código te muestra cómo agregar una imagen en el pie de página de un archivo PDF con C#.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Abrir documento
Document pdfDocument = new Document(dataDir+ "ImageInFooter.pdf");
// Crear pie de página
ImageStamp imageStamp = new ImageStamp(dataDir+ "aspose-logo.jpg");
// Establecer propiedades del sello
imageStamp.BottomMargin = 10;
imageStamp.HorizontalAlignment = HorizontalAlignment.Center;
imageStamp.VerticalAlignment = VerticalAlignment.Bottom;
// Agregar pie de página en todas las páginas
foreach (Page page in pdfDocument.Pages)
{
    page.AddStamp(imageStamp);
}
// Guardar archivo de salida
pdfDocument.Save(dataDir + "ImageInFooter_out.pdf");
```

## Agregando diferentes encabezados en un solo archivo PDF

Sabemos que podemos agregar TextStamp en la sección de encabezado/pie de página del documento utilizando las propiedades TopMargin o Bottom Margin, pero a veces podemos tener la necesidad de agregar múltiples encabezados/pies de página en un solo documento PDF.
Sabemos que podemos agregar TextStamp en la sección de encabezado/pie de página del documento utilizando las propiedades TopMargin o BottomMargin, pero a veces podemos tener la necesidad de agregar múltiples encabezados/pies de página en un solo documento PDF.

Para lograr este requisito, crearemos objetos TextStamp individuales (el número de objetos depende de la cantidad de encabezados/pies de página requeridos) y los agregaremos al documento PDF. También podemos especificar diferente información de formato para cada objeto de sello. En el siguiente ejemplo, hemos creado un objeto Document y tres objetos TextStamp y luego hemos utilizado el método [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) de la página para agregar el texto en la sección de encabezado del PDF. El siguiente fragmento de código te muestra cómo agregar una imagen en el pie de página de un archivo PDF con Aspose.PDF para .NET.

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Abrir documento fuente
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir+ "AddingDifferentHeaders.pdf");

// Crear tres sellos
Aspose.Pdf.TextStamp stamp1 = new Aspose.Pdf.TextStamp("Encabezado 1");
Aspose.Pdf.TextStamp stamp2 = new Aspose.Pdf.TextStamp("Encabezado 2");
Aspose.Pdf.TextStamp stamp3 = new Aspose.Pdf.TextStamp("Encabezado 3");

// Establecer la alineación del sello (colocar sello en la parte superior de la página, centrado horizontalmente)
stamp1.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
stamp1.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// Especificar el estilo de fuente como Negrita
stamp1.TextState.FontStyle = FontStyles.Bold;
// Establecer la información de color de primer plano del texto como rojo
stamp1.TextState.ForegroundColor = Color.Red;
// Especificar el tamaño de fuente como 14
stamp1.TextState.FontSize = 14;

// Ahora necesitamos establecer la alineación vertical del segundo objeto sello como Top
stamp2.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
// Establecer información de alineación horizontal para sello como centrado
stamp2.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// Establecer el factor de zoom para el objeto sello
stamp2.Zoom = 10;

// Establecer el formato del tercer objeto sello
// Especificar la información de alineación vertical para el objeto sello como TOP
stamp3.VerticalAlignment = Aspose.Pdf.VerticalAlignment.Top;
// Establecer la información de alineación horizontal para el objeto sello como centrado
stamp3.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// Establecer el ángulo de rotación para el objeto sello
stamp3.RotateAngle = 35;
// Establecer el color de fondo rosa para el sello
stamp3.TextState.BackgroundColor = Color.Pink;
// Cambiar la información de la fuente del sello a Verdana
stamp3.TextState.Font = FontRepository.FindFont("Verdana");
// El primer sello se agrega en la primera página;
doc.Pages[1].AddStamp(stamp1);
// El segundo sello se agrega en la segunda página;
doc.Pages[2].AddStamp(stamp2);
// El tercer sello se agrega en la tercera página.
doc.Pages[3].AddStamp(stamp3);
// Guardar el documento actualizado
doc.Save(dataDir + "MultiHeader_out.pdf");
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF para la biblioteca .NET",
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
```

