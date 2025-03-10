---
title: Modificando AcroForm
linktitle: Modificando AcroForm
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /es/net/modifing-form/
description: Modificando formularios en su archivo PDF con la biblioteca Aspose.PDF for .NET. Puede agregar o eliminar campos en formularios existentes, obtener y establecer límites de campo, etc.
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
    "alternativeHeadline": "Modify and Manage AcroForm Fields in PDF",
    "abstract": "La nueva función de Modificación de AcroForm en la biblioteca Aspose.PDF for .NET permite a los usuarios agregar o eliminar campos de formularios PDF existentes sin problemas. Esta funcionalidad también incluye establecer límites de campo y personalizar las apariencias de fuente para una experiencia de usuario refinada, mejorando la gestión e interacción de formularios PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Modifing AcroForm, Aspose.PDF for .NET, PDF form fields, SetFieldLimit, custom font, Add/remove fields, Document Form collection, DefaultAppearance, manage form fields, PDF manipulation",
    "wordcount": "601",
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
    "url": "/net/modifing-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/modifing-form/"
    },
    "dateModified": "2024-11-25",
    "description": "Modificando formularios en su archivo PDF con la biblioteca Aspose.PDF for .NET. Puede agregar o eliminar campos en formularios existentes, obtener y establecer límites de campo, etc."
}
</script>

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Obtener o establecer límite de campo

El método SetFieldLimit(field, limit) de la clase FormEditor le permite establecer un límite de campo, el número máximo de caracteres que se pueden ingresar en un campo.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetFieldLimit()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create FormEditor instance
    using (var form = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "input.pdf");

        // Set field limit for "textbox1"
        form.SetFieldLimit("textbox1", 15);

        // Save PDF document
        form.Save(dataDir + "SetFieldLimit_out.pdf");
    }
}
```

De manera similar, Aspose.PDF tiene un método que obtiene el límite de campo utilizando el enfoque DOM. El siguiente fragmento de código muestra los pasos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetFieldLimitUsingDOM()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "FieldLimit.pdf"))
    {
        // Get the field and its maximum limit
        if (document.Form["textbox1"] is Aspose.Pdf.Forms.TextBoxField textBoxField)
        {
            Console.WriteLine("Limit: " + textBoxField.MaxLen);
        }
    }
}
```

También puede obtener el mismo valor utilizando el espacio de nombres *Aspose.Pdf.Facades* con el siguiente fragmento de código.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetFieldLimitUsingFacades()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create Form instance
    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "FieldLimit.pdf");

        // Get the field limit for "textbox1"
        Console.WriteLine("Limit: " + form.GetFieldLimit("textbox1"));
    }
}
```

## Establecer fuente personalizada para el campo del formulario

Los campos de formulario en archivos PDF de Adobe pueden configurarse para usar fuentes predeterminadas específicas. En las primeras versiones de Aspose.PDF, solo se admitían las 14 fuentes predeterminadas. Las versiones posteriores permitieron a los desarrolladores aplicar cualquier fuente. Para establecer y actualizar la fuente predeterminada utilizada para los campos de formulario, utilice la clase DefaultAppearance(Font font, double size, Color color). Esta clase se puede encontrar en el espacio de nombres Aspose.Pdf.InteractiveFeatures. Para usar este objeto, utilice la propiedad DefaultAppearance de la clase Field.

El siguiente fragmento de código muestra cómo establecer la fuente predeterminada para los campos de formulario PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetFormFieldFont()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "FormFieldFont14.pdf"))
    {
        // Get particular form field from document
        if (document.Form["textbox1"] is Aspose.Pdf.Forms.Field field)
        {
            // Create font object
            var font = Aspose.Pdf.Text.FontRepository.FindFont("ComicSansMS");

            // Set the font information for form field
            field.DefaultAppearance = new Aspose.Pdf.Annotations.DefaultAppearance(font, 10, System.Drawing.Color.Black);
        }

        // Save PDF document
        document.Save(dataDir + "FormFieldFont14_out.pdf");
    }
}
```

## Agregar/eliminar campos en un formulario existente

Todos los campos de formulario están contenidos en la colección Form del objeto Document. Esta colección proporciona diferentes métodos que gestionan los campos de formulario, incluido el método Delete. Si desea eliminar un campo en particular, pase el nombre del campo como parámetro al método Delete y luego guarde el documento PDF actualizado. El siguiente fragmento de código muestra cómo eliminar un campo en particular de un documento PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteFormField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DeleteFormField.pdf"))
    {
        // Delete a particular field by name
        document.Form.Delete("textbox1");

        // Save PDF document
        document.Save(dataDir + "DeleteFormField_out.pdf");
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