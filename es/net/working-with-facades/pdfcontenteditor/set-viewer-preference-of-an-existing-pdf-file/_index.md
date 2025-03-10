---
title: Establecer Preferencias de Visualización de PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /es/net/set-viewer-preference-of-an-existing-pdf-file/
description: Esta sección muestra cómo establecer la preferencia de visualización de un archivo PDF existente utilizando la clase PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set Viewer Preference of PDF",
    "alternativeHeadline": "Customize PDF Viewer Preferences with Ease",
    "abstract": "Mejora la experiencia del usuario de tus documentos PDF utilizando la función Establecer Preferencias de Visualización. Esta funcionalidad permite a los desarrolladores personalizar los modos de visualización, como centrar la ventana, ocultar la barra de menú y habilitar el modo de pantalla completa, utilizando la clase PdfContentEditor. Optimiza la presentación de documentos y asegura una visualización óptima para tu audiencia con estas configuraciones personalizadas.",
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
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Establecer Preferencias de Visualización de un Archivo PDF Existente

[ViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference) clase representa los modos de visualización de archivos PDF; por ejemplo, posicionar la ventana del documento en el centro de la pantalla, ocultar la barra de menú de la aplicación del visor, etc.

El método [ChangeViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference) en la clase [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) te permite cambiar la preferencia de visualización. Para hacer eso, necesitas crear un objeto de la clase [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) y vincular el archivo PDF de entrada utilizando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/bindpdf/index).

Después de eso, puedes llamar al método [ChangeViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference) para establecer cualquier preferencia. Finalmente, debes guardar el archivo PDF actualizado utilizando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index). El siguiente fragmento de código te muestra cómo cambiar la preferencia de visualización en un archivo PDF existente.

Por ejemplo, especificamos el parámetro [CenterWindow](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/centerwindow) con el cual centramos la ventana, después eliminamos la barra de herramientas superior con [HideMenubar](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/hidemenubar) y con [PageModeUseNone](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/pagemodeusenone) abrimos el modo de pantalla completa.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetViewerPreference()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Sample.pdf"))
    {
        // Instantiate PdfContentEditor object
        var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

        // Change Viewer Preferences
        editor.ChangeViewerPreference(Aspose.Pdf.Facades.ViewerPreference.CenterWindow);
        editor.ChangeViewerPreference(Aspose.Pdf.Facades.ViewerPreference.HideMenubar);
        editor.ChangeViewerPreference(Aspose.Pdf.Facades.ViewerPreference.PageModeFullScreen);

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo_SetViewerPreference_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetViewerPreference()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
    
    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "Sample.pdf");

    // Instantiate PdfContentEditor object
    var editor = new Aspose.Pdf.Facades.PdfContentEditor(document);

    // Change Viewer Preferences
    editor.ChangeViewerPreference(Aspose.Pdf.Facades.ViewerPreference.CenterWindow);
    editor.ChangeViewerPreference(Aspose.Pdf.Facades.ViewerPreference.HideMenubar);
    editor.ChangeViewerPreference(Aspose.Pdf.Facades.ViewerPreference.PageModeFullScreen);

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo_SetViewerPreference_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}