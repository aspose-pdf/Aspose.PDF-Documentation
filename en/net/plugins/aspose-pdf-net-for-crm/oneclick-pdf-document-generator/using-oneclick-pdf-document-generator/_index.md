---
title: Using OneClick PDF Document Generator
type: docs
weight: 10
url: /net/using-oneclick-pdf-document-generator/
description: Learn how to use Aspose.PDF OneClick PDF Document Generator in Microsoft Dynamics
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using OneClick PDF Document Generator",
    "alternativeHeadline": "Streamlined PDF Generation in Microsoft Dynamics",
    "abstract": "Unlock seamless document generation in Microsoft Dynamics with the Aspose.PDF OneClick PDF Document Generator. This innovative feature allows users to create customizable PDF templates directly within CRM, efficiently generate documents with a single click, and easily integrate OneClick buttons into forms for streamlined access. Enhance your data management capabilities and improve productivity with this powerful tool",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "313",
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
    "url": "/net/using-oneclick-pdf-document-generator/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/using-oneclick-pdf-document-generator/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Create Template and Add in CRM

- Open word and create a template.
- Insert MailMerge fields for data comming from CRM.

![Insert MailMerg fields](using-oneclick-pdf-document-generator_1.png)

- Make sure that the Field name matches exactly with the CRM field.
- Templates are specific to use with individual entity.

![Demo Template](using-oneclick-pdf-document-generator_2.png)

- Once the Template is created, Open OneClick PDF Configuration entity in CRM and Create a New record.
- Give the name of the template, select entity the template is defined for and attach the created document in the attachment.

![Select Template](using-oneclick-pdf-document-generator_3.png)

## Generate Document from Ribbon Button

- Open Record where you want to generate document. (Make sure a template is already attached in the configuration for that entity)
- Click OneClick PDF button from the ribbon.

![Click OneClick PDF](using-oneclick-pdf-document-generator_4.png)

- From the Popup: Select template, File Name and Action and Click Generate.
- Check the Downloaded file or Notes, on basis of the selection.

## Configure OneClick Buttons and use them

- In Order to use OneClick Button directly from Form, Open Form Customization.
- Insert WebResource where you want to add OneClick Buttons.
- Select OpenButtonPage in Webresource and give it a Name.
- Configure the Buttons in Data field in the following sample.

![WebResource Properties](using-oneclick-pdf-document-generator_5.png)

- Use seperate line for each button and use the following syntax:
  - Syntax:Template Name |<Action: Download/Note>|Output FileName
  - Example:Demo|Download|My Downloaded File
- Save and publish the customization.
- The button is available on the form.

![The button is available on the form](using-oneclick-pdf-document-generator_6.png)
