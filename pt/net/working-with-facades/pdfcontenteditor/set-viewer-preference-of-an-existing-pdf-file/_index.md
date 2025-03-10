---
title: Definir Preferência do Visualizador de PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /pt/net/set-viewer-preference-of-an-existing-pdf-file/
description: Esta seção mostra como definir a preferência do visualizador de um arquivo PDF existente usando a classe PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set Viewer Preference of PDF",
    "alternativeHeadline": "Customize PDF Viewer Preferences with Ease",
    "abstract": "Melhore a experiência do usuário dos seus documentos PDF utilizando o recurso Definir Preferência do Visualizador. Essa funcionalidade permite que os desenvolvedores personalizem modos de exibição, como centralizar a janela, ocultar a barra de menu e habilitar o modo de tela cheia, usando a classe PdfContentEditor. Simplifique a apresentação do documento e garanta uma visualização ideal para seu público com essas configurações personalizadas.",
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
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Definir Preferência do Visualizador de um arquivo PDF existente

[A classe ViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference) representa modos de exibição de arquivos PDF; por exemplo, posicionar a janela do documento no centro da tela, ocultar a barra de menu do aplicativo visualizador, etc.

O método [ChangeViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference) na classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) permite que você altere a preferência do visualizador. Para fazer isso, você precisa criar um objeto da classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) e vincular o arquivo PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/bindpdf/index).

Depois disso, você pode chamar o método [ChangeViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference) para definir qualquer preferência. Finalmente, você deve salvar o arquivo PDF atualizado usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index). O seguinte trecho de código mostra como alterar a preferência do visualizador em um arquivo PDF existente.

Por exemplo, especificamos o parâmetro [CenterWindow](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/centerwindow) com o qual centralizamos a janela, depois removemos a barra de ferramentas superior com [HideMenubar](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/hidemenubar) e com [PageModeUseNone](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/pagemodeusenone) abrimos o modo de tela cheia.

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