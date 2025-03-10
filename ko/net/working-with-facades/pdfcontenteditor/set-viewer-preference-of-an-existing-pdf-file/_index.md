---
title: PDF의 뷰어 기본 설정 설정
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /ko/net/set-viewer-preference-of-an-existing-pdf-file/
description: 이 섹션에서는 PdfContentEditor 클래스를 사용하여 기존 PDF 파일의 뷰어 기본 설정을 설정하는 방법을 보여줍니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set Viewer Preference of PDF",
    "alternativeHeadline": "Customize PDF Viewer Preferences with Ease",
    "abstract": "Set Viewer Preference 기능을 활용하여 PDF 문서의 사용자 경험을 향상시키세요. 이 기능은 개발자가 PdfContentEditor 클래스를 사용하여 창 중앙 배치, 메뉴 바 숨기기, 전체 화면 모드 활성화와 같은 표시 모드를 사용자 정의할 수 있게 해줍니다. 이러한 맞춤 설정으로 문서 프레젠테이션을 간소화하고 청중에게 최적의 보기 환경을 보장하세요.",
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
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

## 기존 PDF 파일의 뷰어 기본 설정 설정

[ViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference) 클래스는 PDF 파일의 표시 모드를 나타냅니다. 예를 들어, 문서 창을 화면 중앙에 배치하거나 뷰어 애플리케이션의 메뉴 바를 숨기는 등의 기능이 있습니다.

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 클래스의 [ChangeViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference) 메서드를 사용하면 뷰어 기본 설정을 변경할 수 있습니다. 이를 위해서는 [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 클래스의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/bindpdf/index) 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다.

그 후, [ChangeViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference) 메서드를 호출하여 원하는 기본 설정을 설정할 수 있습니다. 마지막으로, [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) 메서드를 사용하여 업데이트된 PDF 파일을 저장해야 합니다. 다음 코드 스니펫은 기존 PDF 파일에서 뷰어 기본 설정을 변경하는 방법을 보여줍니다.

예를 들어, [CenterWindow](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/centerwindow) 매개변수를 지정하여 창을 중앙에 배치하고, [HideMenubar](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/hidemenubar)로 상단 툴바를 제거한 후, [PageModeUseNone](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/pagemodeusenone)로 전체 화면 모드를 엽니다.

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