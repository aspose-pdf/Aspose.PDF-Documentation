---
title: Obtener Preferencia del Visor de un Archivo PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /es/net/get-viewer-preference-of-an-existing-pdf-file/
description: Esta sección muestra cómo obtener la preferencia del visor de un archivo PDF existente utilizando la clase PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get Viewer Preference of PDF File",
    "alternativeHeadline": "Retrieve PDF Viewer Preferences Easily",
    "abstract": "Descubre cómo recuperar las preferencias del visor de archivos PDF existentes con la clase PdfContentEditor. Esta funcionalidad permite a los usuarios acceder a la configuración del modo de visualización, como la posición de la ventana y la visibilidad del menú, mejorando la experiencia de visualización del PDF. Maximiza la presentación de tu documento gestionando eficazmente sus preferencias de visor.",
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
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también enfrentar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Obtener Preferencia del Visor de un Archivo PDF Existente

[ViewerPreference](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/viewerpreference) la clase representa los modos de visualización de archivos PDF; por ejemplo, posicionar la ventana del documento en el centro de la pantalla, ocultar la barra de menú de la aplicación del visor, etc.

Para leer la configuración, utilizamos la clase [GetViewerPreference](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdfcontenteditor/methods/getviewerpreference). Este método devuelve una variable donde se guardan todas las configuraciones.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetViewerPreference()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetViewerPreference.pdf"))
    {
        // Instantiate PdfContentEditor object
        var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

        // Get Viewer Preferences
        var preferences = editor.GetViewerPreference();

        if ((preferences & Aspose.Pdf.Facades.ViewerPreference.CenterWindow) != 0)
        {
            Console.WriteLine("CenterWindow");
        }

        if ((preferences & Aspose.Pdf.Facades.ViewerPreference.HideMenubar) != 0)
        {
            Console.WriteLine("Menu bar hided");
        }

        if ((preferences & Aspose.Pdf.Facades.ViewerPreference.PageModeFullScreen) != 0)
        {
            Console.WriteLine("Page Mode Full Screen");
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetViewerPreference()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "SetViewerPreference.pdf");

    // Instantiate PdfContentEditor object
    var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

    // Get Viewer Preferences
    var preferences = editor.GetViewerPreference();

    if ((preferences & Aspose.Pdf.Facades.ViewerPreference.CenterWindow) != 0)
    {
        Console.WriteLine("CenterWindow");
    }

    if ((preferences & Aspose.Pdf.Facades.ViewerPreference.HideMenubar) != 0)
    {
        Console.WriteLine("Menu bar hided");
    }

    if ((preferences & Aspose.Pdf.Facades.ViewerPreference.PageModeFullScreen) != 0)
    {
        Console.WriteLine("Page Mode Full Screen");
    }
}
```
{{< /tab >}}
{{< /tabs >}}