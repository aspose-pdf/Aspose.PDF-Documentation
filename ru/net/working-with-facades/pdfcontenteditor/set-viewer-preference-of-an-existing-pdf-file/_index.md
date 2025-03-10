---
title: Установить предпочтения просмотра PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /ru/net/set-viewer-preference-of-an-existing-pdf-file/
description: Этот раздел показывает, как установить предпочтения просмотра существующего PDF-файла с помощью класса PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set Viewer Preference of PDF",
    "alternativeHeadline": "Customize PDF Viewer Preferences with Ease",
    "abstract": "Улучшите пользовательский опыт ваших PDF-документов, используя функцию установки предпочтений просмотра. Эта функциональность позволяет разработчикам настраивать режимы отображения, такие как центрирование окна, скрытие панели меню и включение полноэкранного режима, с помощью класса PdfContentEditor. Упрощайте представление документов и обеспечьте оптимальное отображение для вашей аудитории с этими индивидуальными настройками",
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
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для опытных пользователей и разработчиков."
}
</script>

## Установить предпочтения просмотра существующего PDF-файла

[ViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference) класс представляет режимы отображения PDF-файлов; например, позиционирование окна документа в центре экрана, скрытие панели меню приложения просмотра и т.д.

[ChangeViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference) метод в классе [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) позволяет вам изменить предпочтения просмотра. Для этого вам нужно создать объект класса [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) и связать входной PDF-файл с помощью метода [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/bindpdf/index).

После этого вы можете вызвать метод [ChangeViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference), чтобы установить любые предпочтения. Наконец, вам нужно сохранить обновленный PDF-файл с помощью метода [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index). Следующий фрагмент кода показывает, как изменить предпочтения просмотра в существующем PDF-файле.

Например, мы указываем параметр [CenterWindow](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/centerwindow), с помощью которого мы центрируем окно, затем скрываем верхнюю панель инструментов с помощью [HideMenubar](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/hidemenubar) и с помощью [PageModeUseNone](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/pagemodeusenone) открываем полноэкранный режим.

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