---
title: C#를 사용한 PDF 하이라이트 주석
linktitle: 하이라이트 주석
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ko/net/highlights-annotation/
description: Aspose.PDF를 사용하여 .NET에서 PDF 문서에 하이라이트 주석을 추가하는 방법을 배우고 텍스트 강조 및 검토를 수행하세요.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF Highlight Annotation using C#",
    "alternativeHeadline": "PDF Annotations with Customizable Highlighting Options",
    "abstract": "C#를 사용한 새로운 PDF 하이라이트 주석 기능은 사용자가 PDF 문서에 텍스트 마크업 주석을 원활하게 추가하고 사용자 정의할 수 있도록 합니다. 이 기능에는 하이라이트, 밑줄, 취소선 및 물결 모양의 밑줄 옵션이 포함되어 있으며, 모두 색상, 불투명도 및 메타데이터를 편집할 수 있어 문서의 상호작용성과 명확성을 향상시킵니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF Highlight Annotation, C#, text markup annotation, highlight settings, strikethrough settings, underline settings, add annotation, delete annotation, Aspose.PDF.Drawing, markup annotations",
    "wordcount": "958",
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
    "url": "/net/highlights-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/highlights-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "마크업 주석은 문서의 텍스트에서 하이라이트, 밑줄, 취소선 또는 물결 모양의 밑줄로 표시됩니다."
}
</script>

텍스트 마크업 주석은 문서의 텍스트에서 하이라이트, 밑줄, 취소선 또는 물결 모양의 밑줄로 나타납니다. 열면 관련 메모의 텍스트가 포함된 팝업 창이 표시됩니다.

PDF 문서의 텍스트 마크업 주석 속성은 PDF 뷰어 컨트롤에서 제공하는 속성 창을 사용하여 편집할 수 있습니다. 텍스트 마크업 주석의 색상, 불투명도, 작성자 및 주제를 수정할 수 있습니다.

하이라이트 주석의 설정을 가져오거나 설정할 수 있는 highlightSettings 속성을 사용할 수 있습니다. highlightSettings 속성은 하이라이트 주석의 색상, 불투명도, 작성자, 주제, 수정 날짜 및 잠금 여부 속성을 설정하는 데 사용됩니다.

취소선 주석의 설정을 가져오거나 설정할 수 있는 strikethroughSettings 속성도 가능합니다. strikethroughSettings 속성은 취소선 주석의 색상, 불투명도, 작성자, 주제, 수정 날짜 및 잠금 여부 속성을 설정하는 데 사용됩니다.

다음 기능은 underlineSettings 속성을 사용하여 밑줄 주석의 설정을 가져오거나 설정할 수 있는 기능입니다. underlineSettings 속성은 밑줄 주석의 색상, 불투명도, 작성자, 주제, 수정 날짜 및 잠금 여부 속성을 설정하는 데 사용됩니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

## 텍스트 마크업 주석 추가

PDF 문서에 텍스트 마크업 주석을 추가하려면 다음 작업을 수행해야 합니다:

1. PDF 파일 로드 - 새로운 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체.
1. 주석 생성:
    - [HighlightAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/highlightannotation) 및 매개변수 설정 (제목, 색상).
    - [StrikeOutAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/strikeoutannotation) 및 매개변수 설정 (제목, 색상).
    - [SquigglyAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/squigglyannotation) 및 매개변수 설정 (제목, 색상).
    - [UnderlineAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/underlineannotation) 및 매개변수 설정 (제목, 색상).
1. 모든 주석을 페이지에 추가해야 합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextMarkupAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        // Create a TextFragmentAbsorber to find the text "PDF"
        var tfa = new Aspose.Pdf.Text.TextFragmentAbsorber("PDF");
        tfa.Visit(document.Pages[1]);

        // Create annotations for the found text fragments
        var highlightAnnotation = new Aspose.Pdf.Annotations.HighlightAnnotation(document.Pages[1], tfa.TextFragments[1].Rectangle)
        {
            Title = "Aspose User",
            Color = Aspose.Pdf.Color.LightGreen
        };

        var strikeOutAnnotation = new Aspose.Pdf.Annotations.StrikeOutAnnotation(document.Pages[1], tfa.TextFragments[2].Rectangle)
        {
            Title = "Aspose User",
            Color = Aspose.Pdf.Color.Blue
        };

        var squigglyAnnotation = new Aspose.Pdf.Annotations.SquigglyAnnotation(document.Pages[1], tfa.TextFragments[3].Rectangle)
        {
            Title = "Aspose User",
            Color = Aspose.Pdf.Color.Red
        };

        var underlineAnnotation = new Aspose.Pdf.Annotations.UnderlineAnnotation(document.Pages[1], tfa.TextFragments[4].Rectangle)
        {
            Title = "Aspose User",
            Color = Aspose.Pdf.Color.Violet
        };

        // Add annotations to the page
        document.Pages[1].Annotations.Add(highlightAnnotation);
        document.Pages[1].Annotations.Add(squigglyAnnotation);
        document.Pages[1].Annotations.Add(strikeOutAnnotation);
        document.Pages[1].Annotations.Add(underlineAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddTextMarkupAnnotations_out.pdf");
    }
}
```

여러 줄의 조각을 강조 표시하려면 고급 예제를 사용해야 합니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHighlightAnnotationAdvanced()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample_mod.pdf"))
    {
        var page = document.Pages[1];
        var tfa = new TextFragmentAbsorber(@"Adobe\W+Acrobat\W+Reader", new TextSearchOptions(true));
        tfa.Visit(page);
        foreach (var textFragment in tfa.TextFragments)
        {
            var highlightAnnotation = HighLightTextFragment(page, textFragment, Color.Yellow);
            page.Annotations.Add(highlightAnnotation);
        }

        // Save PDF document
        document.Save(dataDir + "AddHighlightAnnotationAdvanced_out.pdf");
    }
}

private static HighlightAnnotation HighLightTextFragment(Page page,
    Aspose.Pdf.Text.TextFragment textFragment, Aspose.Pdf.Color color)
{
    if (textFragment.Segments.Count == 1)
    {
        return new Aspose.Pdf.Annotations.HighlightAnnotation(page, textFragment.Segments[1].Rectangle)
        {
            Title = "Aspose User",
            Color = color,
            Modified = DateTime.Now,
            QuadPoints = new Aspose.Pdf.Point[]
            {
                new Aspose.Pdf.Point(textFragment.Segments[1].Rectangle.LLX, textFragment.Segments[1].Rectangle.URY),
                new Aspose.Pdf.Point(textFragment.Segments[1].Rectangle.URX, textFragment.Segments[1].Rectangle.URY),
                new Aspose.Pdf.Point(textFragment.Segments[1].Rectangle.LLX, textFragment.Segments[1].Rectangle.LLY),
                new Aspose.Pdf.Point(textFragment.Segments[1].Rectangle.URX, textFragment.Segments[1].Rectangle.LLY)
            }
        };
    }

    var offset = 0;
    var quadPoints = new Aspose.Pdf.Point[textFragment.Segments.Count * 4];
    foreach (Aspose.Pdf.Text.TextSegment segment in textFragment.Segments)
    {
        quadPoints[offset + 0] = new Aspose.Pdf.Point(segment.Rectangle.LLX, segment.Rectangle.URY);
        quadPoints[offset + 1] = new Aspose.Pdf.Point(segment.Rectangle.URX, segment.Rectangle.URY);
        quadPoints[offset + 2] = new Aspose.Pdf.Point(segment.Rectangle.LLX, segment.Rectangle.LLY);
        quadPoints[offset + 3] = new Aspose.Pdf.Point(segment.Rectangle.URX, segment.Rectangle.LLY);
        offset += 4;
    }

    var llx = quadPoints.Min(pt => pt.X);
    var lly = quadPoints.Min(pt => pt.Y);
    var urx = quadPoints.Max(pt => pt.X);
    var ury = quadPoints.Max(pt => pt.Y);
    return new Aspose.Pdf.Annotations.HighlightAnnotation(page, new Aspose.Pdf.Rectangle(llx, lly, urx, ury))
    {
        Title = "Aspose User",
        Color = color,
        Modified = DateTime.Now,
        QuadPoints = quadPoints
    };
}

private static void GetHighlightedText()
{
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample_mod.pdf"))
    {
        var highlightAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Highlight)
            .Cast<Aspose.Pdf.Annotations.HighlightAnnotation>();
        foreach (var ta in highlightAnnotations)
        {
            Console.WriteLine($"[{ta.GetMarkedText()}]");
        }
    }
}
```

## 텍스트 마크업 주석 가져오기

다음 코드 스니펫을 사용하여 PDF 문서에서 텍스트 마크업 주석을 가져와 보세요.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetTextMarkupAnnotation()
{
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample_mod.pdf"))
    {
        var textMarkupAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Highlight
            || a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Squiggly)
            .Cast<Aspose.Pdf.Annotations.TextMarkupAnnotation>();
        foreach (var ta in textMarkupAnnotations)
        {
            Console.WriteLine($"[{ta.AnnotationType} {ta.Rect}]");
        }
    }
}
```

## 텍스트 마크업 주석 삭제

다음 코드 스니펫은 PDF 파일에서 텍스트 마크업 주석을 삭제하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteTextMarkupAnnotation()
{
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample_mod.pdf"))
    {
        var textMarkupAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Highlight
            ||a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Squiggly)
            .Cast<Aspose.Pdf.Annotations.TextMarkupAnnotation>();
        foreach (var ta in textMarkupAnnotations)
        {
            document.Pages[1].Annotations.Delete(ta);
        }
        
        // Save PDF document
        document.Save(dataDir + "DeleteTextMarkupAnnotation_out.pdf");
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>