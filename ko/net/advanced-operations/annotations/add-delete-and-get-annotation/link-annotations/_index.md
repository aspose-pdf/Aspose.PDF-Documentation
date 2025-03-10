---
title: PDF에서 링크 주석 사용하기
linktitle: 링크 주석
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /ko/net/link-annotations/
description: Aspose.PDF for .NET을 사용하여 PDF 문서에서 링크 주석을 추가, 가져오기 및 삭제할 수 있습니다.
lastmod: "2024-07-28"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using Link Annotation for PDF",
    "alternativeHeadline": "How to add Link Annotation in PDF",
    "abstract": "Aspose.PDF for .NET은 PDF 문서 내에서 링크 주석을 관리하기 위한 강력한 기능을 소개하며, 사용자가 하이퍼링크를 원활하게 추가, 검색 및 제거할 수 있도록 합니다. 이 기능은 링크가 특정 페이지, 외부 파일 또는 웹 URL을 열 수 있도록 하여 문서의 상호작용성을 향상시키며, 다양한 스타일과 동작으로 사용자 정의할 수 있습니다. 이 강력한 주석 기능으로 PDF 탐색 및 사용자 참여를 위한 새로운 가능성을 열어보세요.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, text annotation",
    "wordcount": "302",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/link-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/link-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NET을 사용하여 PDF 문서에서 텍스트 주석을 추가, 가져오기 및 삭제할 수 있습니다."
}
</script>

## 기존 PDF 파일에 링크 주석 추가하기

> 다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

[링크 주석](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation)은 하이퍼링크, 다른 곳의 목적지 및 문서를 나타냅니다. PDF 표준에 따르면, 링크 주석은 페이지 보기 열기, 파일 열기 및 웹 페이지 열기라는 세 가지 경우에 사용할 수 있습니다.

### 페이지 보기를 열기 위한 링크 주석 사용하기

주석을 생성하기 위해 몇 가지 추가 단계를 수행했습니다. 우리는 데모를 위해 2개의 TextFragmentAbsorbers를 사용하여 조각을 찾았습니다. 첫 번째는 링크 주석 텍스트를 위한 것이고, 두 번째는 문서 내의 몇몇 위치를 나타냅니다.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Link Annotation Demo.pdf"))
    {
        // Get first page
        var page = document.Pages[1];

        // Define regular expressions for text fragments
        var regEx1 = new Regex(@"Link Annotation Demo \d");
        var regEx2 = new Regex(@"Sample text \d");

        // Create TextFragmentAbsorber for the first regular expression
        var textFragmentAbsorber1 = new Aspose.Pdf.Text.TextFragmentAbsorber(regEx1);
        textFragmentAbsorber1.Visit(document);

        // Create TextFragmentAbsorber for the second regular expression
        var textFragmentAbsorber2 = new Aspose.Pdf.Text.TextFragmentAbsorber(regEx2);
        textFragmentAbsorber2.Visit(document);

        // Get the text fragments for both absorbers
        var linkFragments = textFragmentAbsorber1.TextFragments;
        var sampleTextFragments = textFragmentAbsorber2.TextFragments;

        // Create a LinkAnnotation
        var linkAnnotation1 = new Aspose.Pdf.Annotations.LinkAnnotation(page, linkFragments[1].Rectangle)
        {
            Action = new Aspose.Pdf.Annotations.GoToAction(
                new Aspose.Pdf.Annotations.XYZExplicitDestination(
                    sampleTextFragments[1].Page,
                    sampleTextFragments[1].Rectangle.LLX,
                    sampleTextFragments[1].Rectangle.URX, 1.5))
        };

        // Add the link annotation to the page
        page.Annotations.Add(linkAnnotation1);

        // Save PDF document
        document.Save(dataDir + "AddLinkAnnotation_out.pdf");
    }
}
```

주석을 생성하기 위해 우리는 특정 단계를 따랐습니다:

1. `LinkAnnotation`을 생성하고 페이지 객체와 주석에 해당하는 텍스트 조각의 사각형을 전달합니다.
1. `Action`을 `GoToAction`으로 설정하고 원하는 목적지로 `XYZExplicitDestination`을 전달합니다. 우리는 페이지, 왼쪽 및 위쪽 좌표와 확대/축소를 기반으로 `XYZExplicitDestination`을 생성했습니다.
1. 페이지 주석 컬렉션에 주석을 추가합니다.
1. 문서를 저장합니다.

### 명명된 목적지와 함께 링크 주석 사용하기

다양한 문서를 처리할 때, 입력 중에 주석이 어디를 가리킬지 모르는 상황이 발생합니다.
이 경우 특별한 (명명된) 목적지를 사용할 수 있으며, 코드는 다음과 같이 보일 것입니다:

```cs
var destinationName = "Link2";
var linkAnnotation2 = new LinkAnnotation(page, linkFragments[2].Rectangle)
{
    Action = new GoToAction(document, destinationName)
};
```

다른 곳에서 명명된 목적지를 생성할 수 있습니다.

```cs
document.NamedDestinations.Add(destinationName,
    new XYZExplicitDestination(
        sampleTextFragments[2].Page,
        sampleTextFragments[2].Rectangle.LLX,
        sampleTextFragments[2].Rectangle.URX, 1));
```

### 파일 열기를 위한 링크 주석 사용하기

파일을 열기 위한 주석을 생성할 때는 위의 예와 동일한 접근 방식을 사용합니다.

```cs
var linkAnnotation3 = new LinkAnnotation(page, linkFragments[3].Rectangle)
{
    Action = new GoToRemoteAction("another.pdf", 2)
};
```

차이점은 `GoToAction` 대신 `GoToRemoteAction`을 사용할 것이라는 점입니다. GoToRemoteAction의 생성자는 두 개의 매개변수: 파일 이름과 페이지 번호를 받습니다.
또한 다른 형식을 사용하여 파일 이름과 일부 목적지를 전달할 수 있습니다. 분명히, 사용하기 전에 그러한 목적지를 생성해야 합니다.

### 웹 페이지 열기를 위한 링크 주석 사용하기

웹 페이지를 열기 위해서는 `Action`을 `GoToURIAction` 객체로 설정하면 됩니다.
하이퍼링크를 생성자 매개변수로 전달하거나 다른 종류의 URI를 전달할 수 있습니다. 예를 들어, 전화번호를 호출하는 동작을 구현하기 위해 `callto`를 사용할 수 있습니다.

```cs
var linkAnnotation4 = new LinkAnnotation(page, linkFragments[4].Rectangle)
{
    Action = new GoToURIAction("https://products.aspose.com/pdf/net"),
    // Create Link Annotation and set the action to call a phone number
    //Action = new GoToURIAction("callto:678-555-0103")
    Color = Color.Blue
};
```

## 장식된 링크 주석 추가하기

테두리를 사용하여 링크 주석을 사용자 정의할 수 있습니다. 아래 예제에서는 3pt 너비의 파란색 점선 테두리를 생성합니다.

```cs
var linkAnnotation4 = new LinkAnnotation(page, linkFragments[4].Rectangle)
{
    Action = new GoToURIAction("https://products.aspose.com/pdf/net"),    
    Color = Color.Blue
};

linkAnnotation4.Border = new Border(linkAnnotation4)
{
    Style = BorderStyle.Dashed,
    Dash = new Dash(5, 5),
    Width = 3
};
```

또 다른 예제는 브라우저 스타일을 시뮬레이션하고 링크에 밑줄을 사용하는 방법을 보여줍니다.

```cs
var linkAnnotation5 = new LinkAnnotation(page, linkFragments[5].Rectangle)
{
    Color = Color.Blue
};
linkAnnotation5.Border = new Border(linkAnnotation5)
{
    Style = BorderStyle.Underline,
    Width = 3
};
```

### 링크 주석 가져오기

다음 코드 스니펫을 사용하여 PDF 문서에서 LinkAnnotation을 가져와 보세요.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetLinkAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume_mod.pdf"))
    {
        // Get all Link annotations from the first page
        var linkAnnotations = document.Pages[1].Annotations.Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Link);

        // Iterate through each Link annotation
        foreach (Aspose.Pdf.Annotations.Annotation annot in linkAnnotations)
        {
            // Print the URL of each Link Annotation
            Console.WriteLine("URI: " + ((annot as Aspose.Pdf.Annotations.LinkAnnotation).Action as Aspose.Pdf.Annotations.GoToURIAction).URI);

            // Create a TextAbsorber to extract text within the annotation's rectangle
            var absorber = new Aspose.Pdf.Text.TextAbsorber();
            absorber.TextSearchOptions.LimitToPageBounds = true;
            absorber.TextSearchOptions.Rectangle = annot.Rect;

            // Accept the absorber for the first page
            document.Pages[1].Accept(absorber);

            // Extract and print the text associated with the hyperlink
            string extractedText = absorber.Text;
            Console.WriteLine(extractedText);
        }
    }
}
```

### 링크 주석 삭제하기

다음 코드 스니펫은 PDF 파일에서 링크 주석을 삭제하는 방법을 보여줍니다. 이를 위해 우리는 첫 번째 페이지에서 모든 링크 주석을 찾아 제거해야 합니다. 그 후 주석이 제거된 문서를 저장할 것입니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteLinkAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume_mod.pdf"))
    {
        // Find and delete all link annotations on the 1st page
        var linkAnnotations = document.Pages[1].Annotations.Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Link);

        foreach (var la in linkAnnotations)
        {
            document.Pages[1].Annotations.Delete(la);
        }

        // Save PDF document
        document.Save(dataDir + "DeleteLinkAnnotations_out.pdf");
    }
}
```