---
title: Get Viewer Preference of PDF File
type: docs
weight: 70
url: /net/get-viewer-preference-of-an-existing-pdf-file/
description: This section shows how to get viewer preference of an existing PDF file using PdfContentEditor Class.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get Viewer Preference of PDF File",
    "alternativeHeadline": "Retrieve PDF Viewer Preferences Easily",
    "abstract": "Discover how to retrieve the viewer preferences of existing PDF files with the PdfContentEditor Class. This functionality allows users to access display mode settings, such as window positioning and menu visibility, enhancing the PDF viewing experience. Maximize your document presentation by effectively managing its viewer preferences",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "174",
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
    "url": "/net/get-viewer-preference-of-an-existing-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-viewer-preference-of-an-existing-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Get Viewer Preference of an existing PDF File

[ViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference) class represents display modes of PDF files; for example, positioning the document window in the center of the screen, hiding viewer application's menu bar etc. 

In order to read the settings we use [GetViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/getviewerpreference) class. This method returns a variable where all settings are saved.

```csharp
public static void GetViewerPreference()
{
    var document = new Document(dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
    PdfContentEditor editor = new PdfContentEditor(document);

    // Change Viewer Preferences
    var preferences = editor.GetViewerPreference();
    if ((preferences & ViewerPreference.CenterWindow) != 0)
    {
        Console.WriteLine("CenterWindow");
    }

    if ((preferences & ViewerPreference.HideMenubar) != 0)
    {
        Console.WriteLine("Menu bar hided");
    }

    if ((preferences & ViewerPreference.PageModeFullScreen) != 0)
    {
        Console.WriteLine("Page Mode Full Screen");
    }
}
```