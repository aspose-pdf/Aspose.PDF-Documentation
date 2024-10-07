---
title: Modifing AcroForm
linktitle: Modifing AcroForm
type: docs
weight: 40
url: /net/modifing-form/
description: Modificando el formulario en su archivo PDF con la biblioteca Aspose.PDF para .NET. Puede agregar o eliminar campos en el formulario existente, obtener y establecer el límite del campo, etc.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Modifing AcroForm",
    "alternativeHeadline": "How to Modifing AcroForm",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, modifing acroform",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
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
    "url": "/net/modifing-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/modifing-form/"
    },
    "dateModified": "2022-02-04",
    "description": "Modificando el formulario en su archivo PDF con la biblioteca Aspose.PDF para .NET. Puede agregar o eliminar campos en el formulario existente, obtener y establecer el límite del campo, etc."
}
</script>

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Obtener o Establecer el Límite de Campo

El método SetFieldLimit(campo, límite) de la clase FormEditor te permite establecer un límite de campo, el número máximo de caracteres que se pueden ingresar en un campo.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Agregando campo con límite
FormEditor form = new FormEditor();

form.BindPdf(dataDir + "input.pdf");
form.SetFieldLimit("textbox1", 15);
dataDir = dataDir + "SetFieldLimit_out.pdf";
form.Save(dataDir);
```

De manera similar, Aspose.PDF tiene un método que obtiene el límite de campo usando el enfoque DOM. El siguiente fragmento de código muestra los pasos.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
// Obteniendo el límite máximo de campo usando DOM
Document doc = new Document(dataDir + "FieldLimit.pdf");
Console.WriteLine("Límite: " + (doc.Form["textbox1"] as TextBoxField).MaxLen);
```
También puedes obtener el mismo valor usando el espacio de nombres *Aspose.PDF.Facades* usando el siguiente fragmento de código.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
// Obteniendo el límite máximo del campo usando Facades
Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
form.BindPdf(dataDir + "FieldLimit.pdf");
Console.WriteLine("Límite: " + form.GetFieldLimit("textbox1"));
```

## Establecer Fuente Personalizada para el Campo del Formulario

Los campos de formulario en archivos PDF de Adobe pueden configurarse para usar fuentes predeterminadas específicas.
Los campos de formulario en archivos PDF de Adobe pueden configurarse para usar fuentes predeterminadas específicas.

El siguiente fragmento de código muestra cómo configurar la fuente predeterminada para los campos de formulario PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Abrir documento
Document pdfDocument = new Document(dataDir + "FormFieldFont14.pdf");

// Obtener un campo de formulario específico del documento
Aspose.Pdf.Forms.Field field = pdfDocument.Form["textbox1"] as Aspose.Pdf.Forms.Field;

// Crear objeto de fuente
Aspose.Pdf.Text.Font font = FontRepository.FindFont("ComicSansMS");

// Establecer la información de la fuente para el campo de formulario
// Field.DefaultAppearance = new Aspose.Pdf.Forms.in.DefaultAppearance(font, 10, System.Drawing.Color.Black);

dataDir = dataDir + "FormFieldFont14_out.pdf";
// Guardar documento actualizado
pdfDocument.Save(dataDir);
```

## Añadir/eliminar campos en un formulario existente

Todos los campos de formulario están contenidos en la colección Form del objeto Document.
Todos los campos del formulario están contenidos en la colección Form del objeto Document.

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Abrir documento
Document pdfDocument = new Document(dataDir + "DeleteFormField.pdf");

// Eliminar un campo específico por nombre
pdfDocument.Form.Delete("textbox1");
dataDir = dataDir + "DeleteFormField_out.pdf";
// Guardar documento modificado
pdfDocument.Save(dataDir);
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


