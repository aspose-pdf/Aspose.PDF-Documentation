---
title: Trabajando con formularios XFA
linktitle: Formularios XFA
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /es/net/xfa-forms/
description: Aspose.PDF for .NET API te permite trabajar con campos XFA y XFA Acroform en un documento PDF. El Aspose.Pdf.Facades.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with XFA Forms",
    "alternativeHeadline": "Enhance PDF handling with XFA form support",
    "abstract": "Aspose.PDF for .NET ahora ofrece capacidades avanzadas para trabajar con formularios XFA, permitiendo a los desarrolladores llenar, convertir y gestionar campos XFA Acroform dentro de documentos PDF. Esta característica simplifica la manipulación de formularios dinámicos, permitiendo un acceso fluido a los valores y propiedades de los campos mientras proporciona una conversión eficiente de XFA a AcroForms estándar. Mejora tu flujo de trabajo de procesamiento de PDF con esta robusta solución para manejar estructuras de formularios complejas",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "XFA Forms, Aspose.PDF for .NET, fill XFA form, convert XFA to Acroform, get XFA field properties, dynamic forms, XML Forms Architecture, manipulate XFA fields, AcroForm fields, PDF document generation",
    "wordcount": "684",
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
    "url": "/net/xfa-forms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/xfa-forms/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF for .NET API te permite trabajar con campos XFA y XFA Acroform en un documento PDF. El Aspose.Pdf.Facades."
}
</script>

{{% alert color="primary" %}}

Los formularios dinámicos se basan en una especificación XML conocida como XFA, la “Arquitectura de Formularios XML”. También puede convertir formularios dinámicos XFA a Acroform estándar. La información sobre el formulario (en lo que respecta a PDF) es muy vaga: especifica que existen campos, con propiedades y eventos de JavaScript, pero no especifica ningún renderizado. Los objetos del formulario XFA se dibujan en el momento de cargar el documento.

{{% /alert %}}

La clase Form proporciona la capacidad de tratar con AcroForm estático y puedes obtener una instancia de campo particular utilizando el método GetFieldFacade(..) de la clase Form. Sin embargo, los campos XFA no pueden ser accedidos a través del método Form.GetFieldFacade(..). En su lugar, utiliza [Document.Form.XFA](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form/properties/xfa) para obtener/establecer valores de campo y manipular la plantilla de campo XFA (establecer propiedades de campo).

El siguiente fragmento de código también trabaja con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Llenar campos XFA

El siguiente fragmento de código te muestra cómo llenar campos en un formulario XFA.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FillXFAFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "FillXFAFields.pdf"))
    {
        // Get names of XFA form fields
        var names = document.Form.XFA.FieldNames;

        // Set field values
        if (names.Length > 0)
        {
            document.Form.XFA[names[0]] = "Field 0";
        }
        if (names.Length > 1)
        {
            document.Form.XFA[names[1]] = "Field 1";
        }

        // Save PDF document
        document.Save(dataDir + "FilledXfa_out.pdf");
    }
}
```

## Convertir XFA a Acroform

{{% alert color="primary" %}}

Prueba en línea
Puedes comprobar la calidad de la conversión de Aspose.PDF y ver los resultados en línea en este enlace: [products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

Los formularios dinámicos se basan en una especificación XML conocida como XFA, la “Arquitectura de Formularios XML”. La información sobre el formulario (en lo que respecta a un PDF) es muy vaga: especifica que existen campos, con propiedades y eventos de JavaScript, pero no especifica ningún renderizado.

Actualmente, PDF admite dos métodos diferentes para integrar datos y formularios PDF:

- AcroForms (también conocidos como formularios Acrobat), introducidos e incluidos en la especificación del formato PDF 1.2.
- Formularios de Arquitectura de Formularios XML de Adobe (XFA), introducidos en la especificación del formato PDF 1.5 como una característica opcional (La especificación XFA no está incluida en la especificación PDF, solo se hace referencia a ella).

No podemos extraer o manipular páginas de formularios XFA, porque el contenido del formulario se genera en tiempo de ejecución (durante la visualización del formulario XFA) dentro de la aplicación que intenta mostrar o renderizar el formulario XFA. Aspose.PDF tiene una característica que permite a los desarrolladores convertir formularios XFA a AcroForms estándar.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertDynamicXFAToAcroForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Load dynamic XFA form
    using (var document = new Aspose.Pdf.Document(dataDir + "DynamicXFAToAcroForm.pdf"))
    {
        // Set the form fields type as standard AcroForm
        document.Form.Type = Aspose.Pdf.Forms.FormType.Standard;

        // Save PDF document
        document.Save(dataDir + "StandardAcroForm_out.pdf");
    }
}
```

## Obtener propiedades de campo XFA

Para acceder a las propiedades del campo, primero utiliza Document.Form.XFA.Template para acceder a la plantilla del campo. El siguiente fragmento de código muestra los pasos para obtener las coordenadas X e Y de un campo de formulario XFA.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetXFAProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetXFAProperties.pdf"))
    {
        // Get names of XFA form fields
        var names = document.Form.XFA.FieldNames;

        // Set field values
        if (names.Length > 0)
        {
            document.Form.XFA[names[0]] = "Field 0";
        }
        if (names.Length > 1)
        {
            document.Form.XFA[names[1]] = "Field 1";
        }

        // Get field position
        if (names.Length > 0)
        {
            Console.WriteLine(document.Form.XFA.GetFieldTemplate(names[0]).Attributes["x"].Value);
            Console.WriteLine(document.Form.XFA.GetFieldTemplate(names[0]).Attributes["y"].Value);
        }

        // Save PDF document
        document.Save(dataDir + "FilledXfa_out.pdf");
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