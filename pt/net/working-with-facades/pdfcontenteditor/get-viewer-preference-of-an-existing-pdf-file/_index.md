---
title: Obter Preferência do Visualizador de Arquivo PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /pt/net/get-viewer-preference-of-an-existing-pdf-file/
description: Esta seção mostra como obter a preferência do visualizador de um arquivo PDF existente usando a classe PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get Viewer Preference of PDF File",
    "alternativeHeadline": "Retrieve PDF Viewer Preferences Easily",
    "abstract": "Descubra como recuperar as preferências do visualizador de arquivos PDF existentes com a classe PdfContentEditor. Essa funcionalidade permite que os usuários acessem configurações de modo de exibição, como posicionamento da janela e visibilidade do menu, aprimorando a experiência de visualização do PDF. Maximize a apresentação do seu documento gerenciando efetivamente suas preferências de visualizador",
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
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Obter Preferência do Visualizador de um Arquivo PDF Existente

[Aspose.PDF](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/viewerpreference) representa modos de exibição de arquivos PDF; por exemplo, posicionar a janela do documento no centro da tela, ocultar a barra de menu do aplicativo visualizador, etc.

Para ler as configurações, usamos a classe [GetViewerPreference](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfcontenteditor/methods/getviewerpreference). Este método retorna uma variável onde todas as configurações são salvas.

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