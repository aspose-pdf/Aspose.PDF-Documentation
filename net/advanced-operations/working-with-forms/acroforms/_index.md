---
title: Working with AcroForms
linktitle: AcroForms
type: docs
weight: 10
url: /net/acroforms/
description: With Aspose.PDF for .NET you may create a form from scratch, fill the form field in a PDF document, extract data from the form, and etc.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with AcroForms",
    "alternativeHeadline": "Options for working with AcroForms in PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, acroforms in pdf",
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
    "url": "/net/acroforms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/acroforms/"
    },
    "dateModified": "2022-02-04",
    "description": "With Aspose.PDF for .NET you may create a form from scratch, fill the form field in a PDF document, extract data from the form, and etc."
}
</script>

## Fundamentals of AcroForms

**AcroForms** are the original PDF forms technology. AcroForms is a page oriented form. They were first introduced in 1998. They accept input in Forms Data Format or FDF and XML Forms Data Format or xFDF. Third party vendors support AcroForms. When Adobe introduced the AcroForms, they referred to them as “PDF form that is authored with Adobe Acrobat Pro/Standard and that is not a special type of static or dynamic XFA form. Acroforms are portable and they work on all platforms.

You can use AcroForms to add additional pages to the PDF form document. Thanks to the concept of Templates, you can use AcroForms to support populating the form with multiple database records.

PDF 1.7 supports two different methods for integrating data and PDF forms.

*AcroForms (also known as Acrobat forms)*, introduced and included in the PDF 1.2 format specification.

*Adobe XML Forms Architecture (XFA) forms*, introduced in the PDF 1.5 format specification as an optional feature (The XFA specification is not included in the PDF specification, it is only referenced.

In order to understand **Acroforms** vs **XFA** forms, we need to understand the basics first. For starters, both are PDF forms that you can use. Acroforms is the older one, created back in 1998, and it is still referred as the classic PDF form. XFA forms are webpages you can save as a PDF, and appeared back in 2003. It took some time before PDF started accepting XFA forms.

AcroForms have capabilities not found in XFA and conversely XFA has some capabilities not found in AcroForms.  For example:

- AcroForms support the concept of “Templates”, allowing additional pages to be added to the PDF form document to support populating the form with multiple database records.
- XFA supports the concept of document reflow allowing a field to resize if needed to accommodate data.

For more detailed learning of the capabilities of the Java library, see the following articles:

- [Create AcroForm](/pdf/net/create-form) - create form from scratch with C#.
- [Fill AcroForm](/pdf/net/fill-form) - fill form field in your PDF document.
- [Extract AcroForm](/pdf/net/extract-form) - get value from all or an individual field of PDF document.
- [Modifing AcroForm](/pdf/net/modifing-form) - get or set FieldLimit, set form field font and etc.
- [Posting AcroForm Data](/pdf/net/posting-acroform-data/) -  import and export form data to and XML file.

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
