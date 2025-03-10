---
title: 복잡한 PDF 만들기
linktitle: 복잡한 PDF 만들기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /ko/net/complex-pdf-example/
description: Aspose.PDF for NET는 이미지, 텍스트 조각 및 테이블을 포함하는 더 복잡한 문서를 생성할 수 있게 해줍니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Creating a complex PDF",
    "alternativeHeadline": "Create Complex PDFs with Images, Text, and Tables in C#",
    "abstract": "Aspose.PDF for .NET은 복잡한 PDF를 생성하기 위한 강력한 기능을 소개하여 개발자가 이미지, 텍스트 조각 및 테이블을 단일 문서에 원활하게 통합할 수 있도록 합니다. 이 기능은 DOM 기반 접근 방식을 활용하여 PDF 생성 시 세부적인 사용자 정의 및 레이아웃 제어를 가능하게 하여 전문적인 품질의 문서를 효율적으로 생성하는 데 이상적입니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "632",
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
    "url": "/net/complex-pdf-example/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/complex-pdf-example/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 단순하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

[안녕하세요, 세계](/pdf/net/hello-world-example/) 예제는 C#과 Aspose.PDF를 사용하여 PDF 문서를 생성하는 간단한 단계를 보여주었습니다. 이 기사에서는 C#과 Aspose.PDF for .NET을 사용하여 더 복잡한 문서를 만드는 방법을 살펴보겠습니다. 예를 들어, 승객 페리 서비스를 운영하는 가상의 회사에서 문서를 가져오겠습니다.
우리 문서에는 이미지, 두 개의 텍스트 조각(헤더 및 단락), 그리고 테이블이 포함될 것입니다. 이러한 문서를 만들기 위해 우리는 DOM 기반 접근 방식을 사용할 것입니다. [DOM API의 기초](/pdf/net/basics-of-dom-api/) 섹션에서 더 읽을 수 있습니다.

문서를 처음부터 만들 경우 특정 단계를 따라야 합니다:

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체를 인스턴스화합니다. 이 단계에서는 일부 메타데이터가 포함된 빈 PDF 문서를 생성하지만 페이지는 포함하지 않습니다.
1. 문서 객체에 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)를 추가합니다. 이제 우리 문서에는 한 페이지가 있습니다.
1. 페이지에 [Image](https://reference.aspose.com/pdf/net/aspose.pdf/image/methods/index)를 추가합니다.
1. 헤더를 위한 [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment)를 생성합니다. 헤더에는 Arial 글꼴을 사용하고 글꼴 크기는 24pt, 정렬은 중앙으로 설정합니다.
1. 페이지의 [Paragraphs](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs)에 헤더를 추가합니다.
1. 설명을 위한 [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment)를 생성합니다. 설명에도 Arial 글꼴을 사용하고 글꼴 크기는 24pt, 정렬은 중앙으로 설정합니다.
1. 페이지의 단락에 (설명)을 추가합니다.
1. 테이블을 생성하고 테이블 속성을 추가합니다.
1. (테이블)을 페이지의 [Paragraphs](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs)에 추가합니다.
1. 문서를 "Complex.pdf"로 저장합니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와도 작동합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreatingComplexPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Add image
        page.AddImage(dataDir + "logo.png", new Aspose.Pdf.Rectangle(20, 730, 120, 830));

        // Add Header
        var header = new Aspose.Pdf.Text.TextFragment("New ferry routes in Fall 2020");
        header.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        header.TextState.FontSize = 24;
        header.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        header.Position = new Aspose.Pdf.Text.Position(130, 720);
        page.Paragraphs.Add(header);

        // Add description
        var descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. Ferry service is operating at half capacity and on a reduced schedule. Expect lineups.";
        var description = new Aspose.Pdf.Text.TextFragment(descriptionText);
        description.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Times New Roman");
        description.TextState.FontSize = 14;
        description.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Left;
        page.Paragraphs.Add(description);

        // Add table
        var table = new Aspose.Pdf.Table
        {
            ColumnWidths = "200",
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1f, Aspose.Pdf.Color.DarkSlateGray),
            DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 0.5f, Aspose.Pdf.Color.Black),
            DefaultCellPadding = new Aspose.Pdf.MarginInfo(4.5, 4.5, 4.5, 4.5),
            Margin =
            {
                Bottom = 10
            },
            DefaultCellTextState =
            {
                Font =  Aspose.Pdf.Text.FontRepository.FindFont("Helvetica")
            }
        };

        var headerRow = table.Rows.Add();
        headerRow.Cells.Add("Departs City");
        headerRow.Cells.Add("Departs Island");
        foreach (Aspose.Pdf.Cell headerRowCell in headerRow.Cells)
        {
            headerRowCell.BackgroundColor = Aspose.Pdf.Color.Gray;
            headerRowCell.DefaultCellTextState.ForegroundColor = Aspose.Pdf.Color.WhiteSmoke;
        }

        var time = new TimeSpan(6, 0, 0);
        var incTime = new TimeSpan(0, 30, 0);
        for (int i = 0; i < 10; i++)
        {
            var dataRow = table.Rows.Add();
            dataRow.Cells.Add(time.ToString(@"hh\:mm"));
            time = time.Add(incTime);
            dataRow.Cells.Add(time.ToString(@"hh\:mm"));
        }

        page.Paragraphs.Add(table);
        // Save PDF document
        document.Save(dataDir + "Complex_out.pdf");
    }
}
```