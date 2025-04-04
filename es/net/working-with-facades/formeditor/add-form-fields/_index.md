---
title: Agregar Campos de Formulario PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /es/net/add-form-fields/
description: Este tema explica cómo trabajar con Campos de Formulario utilizando la clase FormEditor de Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add PDF Form Fields",
    "alternativeHeadline": "Effortlessly Enhance PDFs with Custom Form Fields",
    "abstract": "Mejora tus documentos PDF con interactividad dinámica al agregar campos de formulario utilizando la clase FormEditor en Aspose.PDF for .NET. Esta función te permite incorporar sin esfuerzo campos de texto, botones de envío con URLs y funcionalidad JavaScript para botones, optimizando la entrada de usuario y la presentación de datos en tus PDFs",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "548",
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
    "url": "/net/add-form-fields/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-form-fields/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Agregar Campo de Formulario en un Archivo PDF Existente

Para agregar un campo de formulario en un archivo PDF existente, necesitas usar el método [AddField](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formeditor/methods/addfield/index) de la clase [FormEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formeditor). Este método requiere que especifiques el tipo de campo que deseas agregar junto con el nombre y la ubicación del campo. Necesitas crear un objeto de la clase [FormEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formeditor), usar el método [AddField](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formeditor/methods/addfield/index) para agregar un nuevo campo en el PDF. Además, puedes especificar un límite en el número de caracteres en tu campo con [SetFieldLimit](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formeditor/methods/setfieldlimit) y finalmente usar el método [Save](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/form/methods/save/index) para guardar el archivo PDF actualizado. El siguiente fragmento de código te muestra cómo agregar un campo de formulario en un archivo PDF existente.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor to manipulate form fields
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "Sample-Form-01.pdf");

        // Add a text field named "Country" to the first page of the PDF
        // Specify the coordinates of the field (left, bottom, right, top)
        editor.AddField(Aspose.Pdf.Facades.FieldType.Text, "Country", 1, 232.56f, 496.75f, 352.28f, 514.03f);

        // Set a character limit for the "Country" field to 20 characters
        editor.SetFieldLimit("Country", 20);

        // Save PDF document
        editor.Save(dataDir + "Sample-Form-01-mod.pdf");
    }
}
```

## Agregar URL de Botón de Envío en un Archivo PDF Existente

El método [AddSubmitBtn](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) te permite establecer la URL del botón de envío en un archivo PDF. Esta es la URL a la que se envían los datos cuando se hace clic en el botón de envío. En nuestro código de ejemplo, especificamos la URL, el nombre de nuestro campo, el número de página en la que queremos agregar y las coordenadas de colocación del botón. El método [AddSubmitBtn](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) requiere el nombre del campo del botón de envío y la URL. Este método es proporcionado por la clase [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). El siguiente fragmento de código te muestra cómo establecer la URL del botón de envío.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void AddSubmitBtn()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Create an instance of FormEditor to manipulate form fields
     using (var editor = new Aspose.Pdf.Facades.FormEditor())
     {
         // Bind PDF document
         editor.BindPdf(dataDir + "Sample-Form-01.pdf");

         // Add a submit button named "Submit" to the first page of the PDF
         // Specify the button text ("Submit"), the URL to which the form data will be submitted,
         // and the coordinates of the button (left, bottom, right, top)
         editor.AddSubmitBtn("Submit", 1, "Submit", "http://localhost:3000", 232.56f, 466.75f, 352.28f, 484.03f);

         // Save PDF document
         editor.Save(dataDir + "Sample-Form-01-mod.pdf");
     }
 }
```

## Agregar JavaScript para Botón de Envío

El método [AddFieldScript](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formeditor/methods/addfieldscript) te permite agregar JavaScript a un botón de envío en un archivo PDF. Este método requiere el nombre del botón de envío y el JavaScript. Este método es proporcionado por la clase [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). El siguiente fragmento de código te muestra cómo establecer JavaScript en un botón de envío.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFieldScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor to manipulate form fields
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "Sample-Form-01.pdf");

        // Add a JavaScript action to the field named "Last Name"
        // The script displays an alert box with the message "Only one last name"
        editor.AddFieldScript("Last Name", "app.alert(\"Only one last name\",3);");

        // Save PDF document
        editor.Save(dataDir + "Sample-Form-01-mod.pdf");
    }
}
```