---
title: Définir la préférence du visualiseur de PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /fr/net/set-viewer-preference-of-an-existing-pdf-file/
description: Cette section montre comment définir la préférence du visualiseur d'un fichier PDF existant en utilisant la classe PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set Viewer Preference of PDF",
    "alternativeHeadline": "Customize PDF Viewer Preferences with Ease",
    "abstract": "Améliorez l'expérience utilisateur de vos documents PDF en utilisant la fonctionnalité Définir la préférence du visualiseur. Cette fonctionnalité permet aux développeurs de personnaliser les modes d'affichage, tels que le centrage de la fenêtre, la dissimulation de la barre de menu et l'activation du mode plein écran, en utilisant la classe PdfContentEditor. Rationalisez la présentation des documents et assurez une visualisation optimale pour votre public avec ces paramètres personnalisés.",
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
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs et développeurs avancés."
}
</script>

## Définir la préférence du visualiseur d'un fichier PDF existant

[ViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference) classe représente les modes d'affichage des fichiers PDF ; par exemple, positionner la fenêtre du document au centre de l'écran, cacher la barre de menu de l'application de visualisation, etc.

La méthode [ChangeViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference) dans la classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) vous permet de changer la préférence du visualiseur. Pour ce faire, vous devez créer un objet de la classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) et lier le fichier PDF d'entrée en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/bindpdf/index).

Après cela, vous pouvez appeler la méthode [ChangeViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference) pour définir n'importe quelle préférence. Enfin, vous devez enregistrer le fichier PDF mis à jour en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index). Le code suivant vous montre comment changer la préférence du visualiseur dans un fichier PDF existant.

Par exemple, nous spécifions le paramètre [CenterWindow](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/centerwindow) avec lequel nous centrons la fenêtre, après avoir retiré la barre d'outils supérieure avec [HideMenubar](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/hidemenubar) et avec [PageModeUseNone](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/pagemodeusenone) ouvrir le mode plein écran.

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