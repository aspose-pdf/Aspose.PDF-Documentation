---
title: Using Aspose.PDF for .NET with Coldfusion
type: docs
weight: 300
url: /net/using-aspose-pdf-for-net-with-coldfusion/
description: You should work with Aspose.PDF for .NET with Coldfusion using PdfFileInfo Class
lastmod: "2021-07-14"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using Aspose.PDF for .NET with Coldfusion",
    "alternativeHeadline": "Integrate Aspose.PDF for .NET with Coldfusion Effortlessly",
    "abstract": "Discover the seamless integration of Aspose.PDF for .NET with Coldfusion, enabling you to manipulate and edit PDF files effortlessly. Learn how to utilize the PdfFileInfo class for extracting essential document information while enhancing your Coldfusion applications with robust PDF functionalities. This guide provides a clear example, ensuring you can easily implement this powerful feature",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "634",
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
    "url": "/net/using-aspose-pdf-for-net-with-coldfusion/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/using-aspose-pdf-for-net-with-coldfusion/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

{{% alert color="primary" %}}

In this article, we will explain how to use Aspose.PDF for .NET with Coldfusion. It’ll help you understand the details of Aspose.PDF for .NET and Coldfusion integration. With the help of a simple example, I’ll show you the process of incorporating the functionality of Aspose.PDF for .NET into your Coldfusion applications.

{{% /alert %}}

## Background

Aspose.PDF for .NET is a component which also provides the capability to edit and manipulate existing PDF files. Aspose provides this component both for .NET and Java, which can be used in your .NET and Java applications respectively, by simply accessing the API of the component. However, the method to integrate Aspose.PDF for .NET with Coldfusion is little bit different. This article will explore it in detail.

## Prerequisite

In order to be able to run the Aspose.PDF for .NET with Coldfusion, you’ll need IIS, .NET 2.0, and Coldfusion. I have tested the component using IIS 5, .NET 2.0, and Colfusion 8. There are two more things which you need to make sure while installing Coldfusion. First, you have to specify which site(s) under IIS will be running Coldfusion. Secondly, you’ll have to select ‘.NET Integration Services’ from the Coldfusion installer. The .NET Integration Services let you access .NET component assembly in Coldfusion applications; in this case the component will be Aspose.PDF for .NET.

## Explanation

First of all, you h ave to copy the DLL (Aspose.PDF .dll) to a location from where you’ll be accessing it for later use; this will be set as a path and assigned to assembly attribute of cfobject tag as shown below:

```html
<cfobject type = ".NET" name = "fileinfo" 
        class = "Aspose.Pdf.Facades.PdfFileInfo" 
        assembly = "C:/Aspose/Net/Assembly/Aspose.PDF.dll">
```

The attribute class in the above tag points to Aspose.PDF Facades class, which in this case is PdfFileInfo. The name attribute is the instance name of the class and will be used later in the code to access class methods or properties. Type attribute specifies the type of the component - in our case it is .NET.

One important point which you’ll have to keep in mind while using the .NET component in Coldfusion is that, when you get or set any property of the class object, you have to follow a specific structure. To set a property you’ll use syntax like Set_propertyname, and to get a property value you’ll use Get_propertyname.

For example, set a property value:

```html
<cfset FilePath = ExpandPath("guide.pdf")>
```

Get a property value:

```html
<cfoutput>#fileinfo.Get_title()#</cfoutput>
```

A basic but complete example to help you understand the process of using Aspose.PDF for .NET in Coldfusion is given below.

### Let us show PDF file info

```html
<!--- create an instance of PdfFileInfo class --->

<cfobject type = ".NET" name = "fileinfo" class = "Aspose.Pdf.Facades.PdfFileInfo"

assembly = "C:/Aspose/Net/Assembly/Aspose.PDF.dll">

<!--- get pdf file path --->

<cfset FilePath = ExpandPath("guide.pdf")>

<!--- assign pdf file path to the class object by setting its inputfile property--->

<cfset fileinfo.Set_inputfile(FilePath)>

<!--- Show file info --->

<cfoutput><b>Title:</b>#fileinfo.Get_title()#</cfoutput><br/>
<cfoutput><b>Subject:</b>#fileinfo.Get_subject()#</cfoutput><br/>
<cfoutput><b>Author:</b>#fileinfo.Get_author()#</cfoutput><br/>
<cfoutput><b>Creator:</b>#fileinfo.Get_Creator()#</cfoutput><br/>

```

## Conclusion

{{% alert color="primary" %}}
In this article, we have seen that if we follow some basic rules of Coldfusion and .NET integration, we can incorporate a lot of functionality and flexibility related to PDF document manipulation, using Aspose.PDF for .NET in our Coldfusion applications.
{{% /alert %}}
