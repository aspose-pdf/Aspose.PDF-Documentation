---
title: Extract AcroForm - Extraer Datos de Formulario de un PDF en C#
linktitle: Extract AcroForm
type: docs
weight: 30
url: /net/extract-form/
keywords: extract form data from pdf c#
description: Extraiga el formulario de su documento PDF con la biblioteca Aspose.PDF para .NET. Obtenga el valor de un campo individual del archivo PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract AcroForm",
    "alternativeHeadline": "Cómo extraer AcroForm de un PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, extract acroform",
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
    "url": "/net/extract-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-form/"
    },
    "dateModified": "2022-02-04",
    "description": "Extraiga el formulario de su documento PDF con la biblioteca Aspose.PDF para .NET. Obtenga el valor de un campo individual del archivo PDF."
}
</script>
El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Extraer datos de un formulario

### Obtener valores de todos los campos del documento PDF

Para obtener valores de todos los campos en un documento PDF, necesitas navegar a través de todos los campos del formulario y luego obtener el valor utilizando la propiedad Value. Obtén cada campo de la colección Form, en el tipo de campo base llamado Field y accede a su propiedad Value.

Los siguientes fragmentos de código C# muestran cómo obtener los valores de todos los campos de un documento PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Abrir documento
Document pdfDocument = new Document(dataDir + "GetValuesFromAllFields.pdf");

// Obtener valores de todos los campos
foreach (Field formField in pdfDocument.Form)
{
    Console.WriteLine("Nombre del Campo : {0} ", formField.PartialName);
    Console.WriteLine("Valor : {0} ", formField.Value);
}
```
### Obtener Valor de un Campo Individual de un Documento PDF

La propiedad Value del campo del formulario permite obtener el valor de un campo específico. Para obtener el valor, obtén el campo del formulario de la colección Form del objeto Document. Este ejemplo en C# selecciona un [TextBoxField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/textboxfield) y recupera su valor utilizando la propiedad Value.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Abrir documento
Document pdfDocument = new Document(dataDir + "GetValueFromField.pdf");

// Obtener un campo
TextBoxField textBoxField = pdfDocument.Form["textbox1"] como TextBoxField;

// Obtener el valor del campo
Console.WriteLine("PartialName : {0} ", textBoxField.PartialName);
Console.WriteLine("Value : {0} ", textBoxField.Value);
```

Para obtener la URL del botón de envío, utiliza las siguientes líneas de código.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Abrir documento
Document pdfDocument = new Document(dataDir + "GetValueFromField.pdf");
SubmitFormAction act = pdfDocument.Form[1].OnActivated como SubmitFormAction;
if(act != null)
Console.WriteLine(act.Url.Name);
```
### Obtener Campos de Formulario de una Región Específica del Archivo PDF

A veces, puedes saber dónde en un documento se encuentra un campo de formulario, pero no conocer su nombre. Por ejemplo, si todo lo que tienes es un esquema de un formulario impreso. Con Aspose.PDF para .NET, esto no es un problema. Puedes descubrir qué campos están en una región dada de un archivo PDF. Para obtener campos de formulario de una región específica de un archivo PDF:

1. Abre el archivo PDF utilizando el objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Obtén el formulario de la colección de Formularios del documento.
1. Especifica la región rectangular y pásala al método GetFieldsInRect del objeto Formulario. Se devuelve una colección de Campos.
1. Utiliza esto para manipular los campos.

El siguiente fragmento de código C# muestra cómo obtener campos de formulario en una región rectangular específica de un archivo PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Abrir archivo pdf
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "GetFieldsFromRegion.pdf");

// Crear objeto rectángulo para obtener campos en esa área
Aspose.Pdf.Rectangle rectangle = new Aspose.Pdf.Rectangle(35, 30, 500, 500);

// Obtener el formulario PDF
Aspose.Pdf.Forms.Form form = doc.Form;

// Obtener campos en el área rectangular
Aspose.Pdf.Forms.Field[] fields = form.GetFieldsInRect(rectangle);

// Mostrar nombres y valores de los campos
foreach (Field field in fields)
{
    // Mostrar propiedades de colocación de la imagen para todas las colocaciones
    Console.Out.WriteLine("Nombre del Campo: " + field.FullName + "-" + "Valor del Campo: " + field.Value);
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Biblioteca Aspose.PDF para .NET",
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

