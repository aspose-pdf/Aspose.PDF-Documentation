---
title: Decorar Campo de Formulario en PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /es/net/decorate-form-field/
description: Explora cómo decorar campos de formulario en un documento PDF, añadiendo mejoras visuales como bordes, en .NET con Aspose.PDF.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Decorate Form Field in PDF",
    "alternativeHeadline": "Enhance PDF Forms with Custom Field Decorations",
    "abstract": "Presentamos una poderosa característica que mejora la gestión de formularios PDF: la capacidad de decorar campos de formulario individuales o todos los campos de formulario utilizando la Clase FormEditor. Esta funcionalidad permite a los usuarios personalizar atributos de campo como estilo de fuente, tamaño, color de borde y alineación, agilizando el proceso de creación de formularios PDF visualmente atractivos y bien estructurados. Mejora tus flujos de trabajo PDF con este método de decoración intuitivo para una presentación de documentos más pulida.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "609",
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
    "url": "/net/decorate-form-field/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/decorate-form-field/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios avanzados y desarrolladores."
}
</script>

## Decorar un Campo de Formulario Particular en un Archivo PDF Existente

El método [DecorateField](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formeditor/methods/decoratefield) presente en la clase [FormEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formeditor) te permite decorar un campo de formulario particular en un archivo PDF. Si deseas decorar un campo particular, debes pasar el nombre del campo a este método. Sin embargo, antes de llamar a este método, necesitas crear objetos de las clases [FormEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formeditor) y [FormFieldFacade](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formfieldfacade). También necesitas asignar el objeto [FormFieldFacade](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formfieldfacade) a la propiedad [Facade](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/facade/properties/index) del objeto [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). Después de eso, puedes establecer cualquier atributo proporcionado por el objeto [FormFieldFacade](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formfieldfacade). Una vez que hayas establecido los atributos, puedes llamar al método [DecorateField](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formeditor/methods/decoratefield) y finalmente guardar el PDF actualizado utilizando el método [Save](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/form/methods/save/index) de la clase [FormEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formeditor).
El siguiente fragmento de código te muestra cómo decorar un campo de formulario particular.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DecorateField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor to manipulate form fields
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "Sample-Form-01.pdf");

        // Create a FormFieldFacade object to define decoration properties for the field
        var cityDecoration = new Aspose.Pdf.Facades.FormFieldFacade
        {
            // Set the font style to Courier
            Font = Aspose.Pdf.Facades.FontStyle.Courier,
            // Set the font size to 12
            FontSize = 12,
            // Set the border color to black
            BorderColor = System.Drawing.Color.Black,
            // Set the border width to 2
            BorderWidth = 2
        };

        // Assign the decoration facade to the FormEditor
        editor.Facade = cityDecoration;

        // Apply the decoration to the field named "City"
        editor.DecorateField("City");

        // Save PDF document
        editor.Save(dataDir + "Sample-Form-02.pdf");
    }
}
```

## Decorar Todos los Campos de un Tipo Particular en un Archivo PDF Existente

El método [DecorateField](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) te permite decorar todos los campos de formulario de un tipo particular en un archivo PDF a la vez. Si deseas decorar todos los campos de un tipo particular, debes pasar el tipo de campo a este método. Sin embargo, antes de llamar a este método, necesitas crear objetos de las clases [FormEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formeditor) y [FormFieldFacade](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formfieldfacade). También necesitas asignar el objeto [FormFieldFacade](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formfieldfacade) a la propiedad [Facade](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/facade/properties/index) del objeto [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). Después de eso, puedes establecer cualquier atributo proporcionado por el objeto [FormFieldFacade](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formfieldfacade). Una vez que hayas establecido los atributos, puedes llamar al método [DecorateField](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) y finalmente guardar el PDF actualizado utilizando el método [Save](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/form/methods/save/index) de la clase [FormEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/formeditor). El siguiente fragmento de código te muestra cómo decorar todos los campos de un tipo particular.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DecorateField2()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor to manipulate form fields
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "Sample-Form-01.pdf");

        // Create a FormFieldFacade object to define alignment properties for text fields
        var textFieldDecoration = new Aspose.Pdf.Facades.FormFieldFacade
        {
            // Set text alignment to center
            Alignment = Aspose.Pdf.Facades.FormFieldFacade.AlignCenter
        };

        // Assign the decoration facade to the FormEditor
        editor.Facade = textFieldDecoration;

        // Apply the alignment decoration to all text fields in the PDF
        editor.DecorateField(Aspose.Pdf.Facades.FieldType.Text);

        // Save PDF document
        editor.Save(dataDir + "Sample-Form-01-align-text.pdf");
    }
}
```