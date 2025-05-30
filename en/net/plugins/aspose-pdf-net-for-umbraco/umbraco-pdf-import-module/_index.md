---
title: Umbraco PDF Import Module
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /net/umbraco-pdf-import-module/
description: Learn how to install and use Umbraco PDF Import Module
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Umbraco PDF Import Module",
    "alternativeHeadline": "Umbraco Module Simplifies PDF Content Import Process",
    "abstract": "The Umbraco PDF Import Module allows developers to seamlessly import PDF content into their Umbraco websites without the need for additional software. This powerful open-source add-on simplifies document handling by providing a user-friendly interface to fetch and display PDF contents instantly, enhancing content management efficiency within .NET applications",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "950",
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
    "url": "/net/umbraco-pdf-import-module/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/umbraco-pdf-import-module/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Introduction

**Aspose.PDF for .NET** is a PDF document creation and manipulation component that enables your .NET applications to read, write and manipulate existing PDF documents without using Adobe Acrobat. It also allows you to create forms and manage form fields embedded in a PDF document.

**Aspose.PDF for .NET** is affordable and offers an incredible wealth of features including PDF compression options; table creation and manipulation; support for graph objects; extensive hyperlink functionality; extended security controls; custom font handling; integration with data sources; add or remove bookmarks; create table of contents; add, update, delete attachments and annotations; import or export PDF form data; add, replace or remove text and images; split, concatenate, extract or inset pages; transform pages to image; print PDF documents and much more.

### **Module Features**

Umbraco PDF Import is an open source add-on from [Aspose](http://www.aspose.com/) that allow developers to get/read contents of any PDF document without requiring any other software. This add-on demonstrates the powerful import feature provided by [Aspose.PDF](https://products.aspose.com/pdf/net/). It adds a simple file browser control and **Import from PDF** button on the page where the add-on is added. When clicking on the button, the document contents are fetched from the file and displayed on the screen immediately.

## System Requirements and Supported Platforms

### **System Requirements**

In order to setup Aspose .NET Pdf Import for Umbraco module you need to have the following requirements met:

- Umbraco 6.0+.

Please feel free to contact us if you wish to install this module on other versions of Umbraco.

### **Supported Platforms**

The module is supported on all versions of

- Umbraco running on ASP.NET 4.0.

## Downloading

You can download Aspose .NET Pdf Import for Umbraco from one of the following locations

- [Github](https://github.com/asposemarketplace/Aspose_for_Umbraco/releases).
- [Sourceforge](https://sourceforge.net/projects/asposeumbraco/files/).
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-umbraco/downloads).
- [Umbraco](https://our.umbraco.com/packages/developer-tools/import-from-pdf-using-asposepdf/).

## Installing

Once downloaded, please follow these steps to install this package into your Umbraco website:

1. Log in to the Umbraco **Developer** section, for example <http://www.myblog.com/umbraco/>.
1. From the tree, expand the **Packages** folder.
   From here there are two ways to install a package: select **Install local package** or browse the **Umbraco Package Respository.**.
1. If you install **local package**, do not unzip the package but load the zip into Umbraco.
1. Follow the instructions on screen.

**Note:** You may get a ‘Maximum request length exceeded’ error when installing. You can easily fix this issue by updating the ‘maxRequestLength’ value in your Umbraco web.config file.

```xml
  <httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" />
```

## Using

After you have installed the macro it is really simple to start using it on your website:

1. Make sure you are logged in to the Umbraco **Developer** section, for example <http://www.myblog.com/umbraco/>.
1. Click **Settings** in the list of sections at the bottom left of the screen.
1. Expand the **Templates** node and select the template that you want to add macro to, for example Blog post.
1. Select the position in the selected template where you want to the button.
1. Click **Insert Macro** on the top ribbon.
1. From **Choose a macro**, select the installed macro and click **OK**.

You have successfully added the template. A button titled **Import from Pdf** now appears on all pages created using this template. Anyone can simply click the button and import the contents of a PDF document.

## Video Demo

Please check [the video](https://www.youtube.com/watch?v=zmZTJ86B25E) below to see the module in action.

## Support, Extend and Contribute

### Support

From the very first days of Aspose, we knew that just giving our customers good products would not be enough. We also needed to deliver good service. We are developers ourselves and understand how frustrating it is when a technical issue or a quirk in the software stops you from doing what you need to do. We're here to solve problems, not create them.

This is why we offer free support. Anyone who uses our product, whether they have bought them or are using an evaluation, deserves our full attention and respect.

You can log any issues or suggestions related to Aspose.PDF .NET for Umbraco Modules using any of the following platforms:

- [Github](https://github.com/asposemarketplace/Aspose_for_Umbraco/issues).
- [Sourceforge](https://sourceforge.net/p/asposeumbraco/tickets/?source=navbar).
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-umbraco/issues?status=new&status=open).


### Extend and Contribute

Aspose .NET PDF Import for Umbraco is open source and its source code is available on the major social coding websites listed below. Developers are encouraged to download the source code and extend the functionality as per their own requirements.

#### Source Code

You can get the latest source code from one of the following locations

- [Github](https://github.com/asposemarketplace/Aspose_for_Umbraco).
- [Sourceforge](https://sourceforge.net/p/asposeumbraco/code/ci/master/tree/).
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-umbraco/src).

#### How to configure the source code

You need to have the following installed in order to open and extend the source code

- Visual Studio 2010 or higher.

Please follow these simple steps to get started

1. Download/Clone the source code.
1. Open Visual Studio 2010 and Choose **File** > **Open Project**.
1. Browse to the latest source code that you have downloaded and open **Aspose.Import from PDF.sln**.
