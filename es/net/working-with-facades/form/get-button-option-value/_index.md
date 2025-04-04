---
title: Obtener el Valor de Opción del Botón
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /es/net/get-button-option-value/
description: Esta sección explica cómo obtener el Valor de Opción del Botón con Aspose.PDF Facades utilizando la Clase Form.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get Button Option Value",
    "alternativeHeadline": "Retrieve Button Option Values from PDF Efficiently",
    "abstract": "Descubre cómo recuperar de manera eficiente los valores de opción del botón de archivos PDF existentes utilizando las Facades de Aspose.PDF. Con los métodos GetButtonOptionValues y GetButtonOptionCurrentValue de la clase Form, puedes obtener fácilmente todas las opciones disponibles para los botones de opción, así como el valor actualmente seleccionado, mejorando tus capacidades de gestión de formularios PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "275",
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
    "url": "/net/get-button-option-value/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-button-option-value/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Obtener Valores de Opción del Botón de un Archivo PDF Existente

Los botones de opción proporcionan una forma de mostrar diferentes opciones. La clase [Form](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/form) te permite obtener todos los valores de opción del botón para un botón de opción particular. Puedes obtener estos valores utilizando el método [GetButtonOptionValues](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/form/methods/getbuttonoptionvalues). Este método requiere el nombre del botón de opción como parámetro de entrada y devuelve un Hashtable. Puedes iterar a través de este Hashtable para obtener los valores de opción. El siguiente fragmento de código te muestra cómo obtener los valores de opción del botón de un archivo PDF existente.
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void GetButtonOptions()
{    
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "FormField.pdf");

        // Get button option values
        var optionValues = pdfForm.GetButtonOptionValues("Gender");

        IDictionaryEnumerator optionValueEnumerator = optionValues.GetEnumerator();

        while (optionValueEnumerator.MoveNext())
        {
            Console.WriteLine("Key : {0} , Value : {1} ", optionValueEnumerator.Key, optionValueEnumerator.Value);
        }
    }
}
```

## Obtener el Valor de Opción del Botón Actual de un Archivo PDF Existente

Los botones de opción proporcionan una forma de establecer valores de opción, sin embargo, solo uno de ellos puede ser seleccionado a la vez. Si deseas obtener el valor de opción actualmente seleccionado, puedes utilizar el método [GetButtonOptionCurrentValue](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/form/methods/getbuttonoptioncurrentvalue). La clase [Form](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/form) proporciona este método. El método [GetButtonOptionCurrentValue](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/form/methods/getbuttonoptioncurrentvalue) requiere el nombre del botón de opción como parámetro de entrada y devuelve el valor como cadena. El siguiente fragmento de código te muestra cómo obtener el valor de opción del botón actual de un archivo PDF existente.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void GetCurremtButtonOptionValue()
{    
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "FormField.pdf");

        // Get button option values
        string optionValue = pdfForm.GetButtonOptionCurrentValue("Gender");

        Console.WriteLine("Current Value : {0} ", optionValue);
    }
}
```