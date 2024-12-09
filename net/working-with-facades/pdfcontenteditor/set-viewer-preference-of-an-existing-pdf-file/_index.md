---
title: Set Viewer Preference of PDF 
type: docs
weight: 60
url: /net/set-viewer-preference-of-an-existing-pdf-file/
description: This section shows how to set viewer preference of an existing PDF file using PdfContentEditor Class.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set Viewer Preference of PDF",
    "alternativeHeadline": "Customize PDF Viewer Preferences with Ease",
    "abstract": "Enhance the user experience of your PDF documents by utilizing the Set Viewer Preference feature. This functionality allows developers to customize display modes, such as centering the window, hiding the menu bar, and enabling full-screen mode, using the PdfContentEditor class. Streamline document presentation and ensure optimal viewing for your audience with these tailored settings",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "338",
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
    "url": "/net/set-viewer-preference-of-an-existing-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/set-viewer-preference-of-an-existing-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Set Viewer Preference of an existing PDF File

[ViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference) class represents display modes of PDF files; for example, positioning the document window in the center of the screen, hiding viewer application's menu bar etc. 

[ChangeViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference) method in [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) class allows you to change the viewer preference. In order to do that, you need to create an object of [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) class and bind the input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/bindpdf/index) method. 

Ater that, you can call [ChangeViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference)  method to set any preference. Finally, you have to save the updated PDF file using [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) method. The following code snippet shows you how to change viewer preference in an existing PDF file.

For example, we specify the parameter [CenterWindow](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/centerwindow) with which we center the window, after remove the top toolbar with [HideMenubar](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/hidemenubar) and with [PageModeUseNone](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/pagemodeusenone) open full-screen mode.

```csharp
public static void SetViewerPreference()
{
    var document = new Document(dataDir + "Sample.pdf");
    PdfContentEditor editor = new PdfContentEditor(document);

    // Change Viewer Preferences
    editor.ChangeViewerPreference(ViewerPreference.CenterWindow);
    editor.ChangeViewerPreference(ViewerPreference.HideMenubar);
    editor.ChangeViewerPreference(ViewerPreference.PageModeFullScreen);
    
    // Saves the result PDF to file
    editor.Save(dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
    GetViewerPreference();
}
```