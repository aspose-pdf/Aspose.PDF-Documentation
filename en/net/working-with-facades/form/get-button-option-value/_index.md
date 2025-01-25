---
title: Get Button Option Value
type: docs
weight: 40
url: /net/get-button-option-value/
description: This section explains how to get Button Option Value with Aspose.PDF Facades using Form Class.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get Button Option Value",
    "alternativeHeadline": "Retrieve Button Option Values from PDF Efficiently",
    "abstract": "Discover how to efficiently retrieve button option values from existing PDF files using the Aspose.PDF Facades. With the Form class GetButtonOptionValues and GetButtonOptionCurrentValue methods, you can easily obtain all available options for radio buttons, as well as the currently selected value, enhancing your PDF form management capabilities",
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
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Get Button Option Values from an Existing PDF File

The radion buttons provide a way to show different options. The [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) class allows you to get all the button option values for a particular radio button. You can get these values using [GetButtonOptionValues](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getbuttonoptionvalues) method. This method requires the name of the radio button as input parameter and returns a Hashtable. You can iterate through this Hashtable to get the option values. The following code snippet shows you how to get button option values from existing PDF file.
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

## Get Current Button Option Value from an Existing PDF File

Radio buttons provide a way to set option values, however one of them can be selected at a time. If you want to get the currently selected option value then you can use [GetButtonOptionCurrentValue** method. [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) class provides this method. The [GetButtonOptionCurrentValue](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getbuttonoptioncurrentvalue) method requires radio button name as input parameter and returns the value as string. The following code snippet shows you how to get current button option value from an existing PDF file.

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