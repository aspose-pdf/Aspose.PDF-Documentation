---
title: FloatingBox를 사용한 텍스트 생성
linktitle: FloatingBox 사용하기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ko/net/floating-box/
description: 이 페이지는 플로팅 박스 내에서 텍스트를 형식화하는 방법을 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using FloatingBox for text generation",
    "alternativeHeadline": "FloatingBox Enhances PDF Text Layout Options",
    "abstract": "FloatingBox 기능은 사용자가 다중 열 레이아웃 및 조정 가능한 오프셋을 포함하여 텍스트 배치를 정밀하게 관리할 수 있도록 하여 PDF 텍스트 형식을 향상시킵니다. 텍스트 클리핑, 배경 색상 및 페이지 간 콘텐츠 반복 옵션을 지원하여 구조적이고 시각적으로 매력적인 문서를 만드는 데 유용한 도구입니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "682",
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
    "url": "/net/floating-box/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/floating-box/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

이 기능은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리에서도 작동합니다.

## FloatingBox 도구 사용의 기초

Floating Box 도구는 PDF 페이지에 텍스트 및 기타 콘텐츠를 배치하기 위한 특별한 도구입니다. 이 도구의 주요 기능은 FloatingBox의 크기를 초과할 때 텍스트를 클리핑하는 것입니다.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateAndAddFloatingBox()
{
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        // Create and fill box
        var box = new Aspose.Pdf.FloatingBox(400, 30)
        {
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1.5f, Aspose.Pdf.Color.DarkGreen),
            IsNeedRepeating = false,
        };
        box.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("text example"));
        // Add box
        page.Paragraphs.Add(box);
    }
}
```  

위의 예제에서는 너비가 400 pt이고 높이가 30 pt인 FloatingBox를 생성하고 있습니다.
또한 이 예제에서는 주어진 크기에 맞지 않는 더 많은 텍스트를 의도적으로 생성했습니다.
결과적으로 텍스트가 잘렸습니다.

![Image 1](image01.png)

`IsNeedRepeating` 속성이 `false` 값으로 설정되면 텍스트는 1페이지로 제한됩니다.

이 속성을 `true`로 설정하면 텍스트가 같은 위치에서 다음 페이지로 재배치됩니다.

![Image 2](image02.png)

## FloatingBox의 고급 기능

### 다중 열 지원

#### 다중 열 레이아웃 (간단한 경우)

`FloatingBox`는 다중 열 레이아웃을 지원합니다. 이러한 레이아웃을 만들려면 ColumnInfo 속성의 값을 정의해야 합니다.

* `ColumnWidths`는 pt 단위의 너비 열거형 문자열입니다.
* `ColumnSpacing`은 열 사이의 간격 너비를 나타내는 문자열입니다.
* `ColumnCount`는 열의 수입니다.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MultiColumnLayout()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tooltip();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Set margin settings
        page.PageInfo.Margin = new Aspose.Pdf.MarginInfo(36, 18, 36, 18);
        var columnCount = 3;
        var spacing = 10;
        var width = page.PageInfo.Width
            - page.PageInfo.Margin.Left
            - page.PageInfo.Margin.Right
            - (columnCount - 1) * spacing;
        var columnWidth = width / 3;
        // Create FloatingBox
        var box = new Aspose.Pdf.FloatingBox()
        {
            IsNeedRepeating = true
        };
        box.ColumnInfo.ColumnWidths = $"{columnWidth} {columnWidth} {columnWidth}";
        box.ColumnInfo.ColumnSpacing = $"{spacing}";
        box.ColumnInfo.ColumnCount = 3;

        var phrase = "text example";
        var paragraphs = new string[10]
        {
            phrase, phrase, phrase, phrase, phrase,
            phrase, phrase, phrase, phrase, phrase,
        };
        foreach (var paragraph in paragraphs)
        {
            box.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment(paragraph));
        }
        // Add a box to a page
        page.Paragraphs.Add(box);
        // Save PDF document
        document.Save(dataDir + "MultiColumnLayout_out.pdf");
    }
}
```

위의 예제에서는 추가 라이브러리 LoremNET을 사용하여 20개의 단락을 생성했습니다. 이 단락들은 세 개의 열로 나누어졌고 텍스트가 소진될 때까지 다음 페이지를 채웠습니다.

#### 강제 열 시작이 있는 다중 열 레이아웃

이전 예제와 동일한 방식으로 다음 예제를 수행할 것입니다. 차이점은 3개의 단락을 생성했다는 것입니다. FloatingBox가 각 단락을 새 열에 렌더링하도록 강제할 수 있습니다. 이를 위해 FloatingBox 객체에 텍스트를 추가할 때 `IsFirstParagraphInColumn`을 설정해야 합니다.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MultiColumnLayout2()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tooltip();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Set margin settings
        page.PageInfo.Margin = new Aspose.Pdf.MarginInfo(36, 18, 36, 18);
        var columnCount = 3;
        var spacing = 10;
        var width = page.PageInfo.Width
            - page.PageInfo.Margin.Left
            - page.PageInfo.Margin.Right
            - (columnCount - 1) * spacing;
        var columnWidth = width / 3;
        // Create the FloatingBox
        var box = new Aspose.Pdf.FloatingBox()
        {
            IsNeedRepeating = true
        };
        box.ColumnInfo.ColumnWidths = $"{columnWidth} {columnWidth} {columnWidth}";
        box.ColumnInfo.ColumnSpacing = $"{spacing}";
        box.ColumnInfo.ColumnCount = 3;

        var phrase = "text example";
        var paragraphs = new string[10]
        {
            phrase, phrase, phrase, phrase, phrase,
            phrase, phrase, phrase, phrase, phrase,
        };
        foreach (var paragraph in paragraphs)
        {
            var text = new Aspose.Pdf.Text.TextFragment(paragraph)
            {
                IsFirstParagraphInColumn = true
            };
            box.Paragraphs.Add(text);
        }

        // Add a box to a page
        page.Paragraphs.Add(box);
        // Save PDF document
        document.Save(dataDir + "MultiColumnLayout2_out.pdf");
    }
}
```

### 배경 지원

원하는 배경 색상을 `BackgroundColor` 속성을 사용하여 설정할 수 있습니다.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void BackgroundSupport()
{
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        var page = document.Pages.Add();
        var box = new Aspose.Pdf.FloatingBox(400, 60)
        {
            IsNeedRepeating = false,
            BackgroundColor = Aspose.Pdf.Color.LightGreen,
        };
        var text = "text example";
        box.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment(text));
        page.Paragraphs.Add(box);
    }
}
```

### 위치 지정 지원

생성된 페이지에서 FloatingBox의 위치는 `PositioningMode`, `Left`, `Top` 속성에 의해 결정됩니다.
`PositioningMode` 값이 다음과 같을 때
- `ParagraphPositioningMode.Default` (기본값)
	위치는 이전에 배치된 요소에 의해 결정됩니다.
	요소를 추가할 때 후속 요소의 위치를 결정하는 데 고려됩니다.
	Left, Top 속성 중 하나라도 0이 아닌 값이면 이들도 고려되지만, 이는 그리 명확하지 않은 논리를 사용하므로 사용하지 않는 것이 좋습니다.

- `ParagraphPositioningMode.Absolute`
	위치는 Left 및 Top 값으로 지정되며, 이전 요소에 의존하지 않고 후속 요소의 위치에도 영향을 미치지 않습니다.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OffsetSupport()
{
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create FloatingBox
        var box = new Aspose.Pdf.FloatingBox()
        {
            Top = 45,
            Left = 15,
            PositioningMode = Aspose.Pdf.ParagraphPositioningMode.Absolute
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 1.5f, Aspose.Pdf.Color.DarkGreen)
        };
        box.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("text example 1"));

        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("text example 2"));
        // Add the box to the page
        page.Paragraphs.Add(box);
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("text example 3"));
    }
}
```