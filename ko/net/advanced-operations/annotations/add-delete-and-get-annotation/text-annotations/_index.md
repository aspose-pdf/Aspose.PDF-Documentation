---
title: PDF에 텍스트 주석 사용하기
linktitle: 텍스트 주석
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/text-annotation/
description: Aspose.PDF for .NET를 사용하면 PDF 문서에서 텍스트 주석을 추가, 가져오기 및 삭제할 수 있습니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using Text Annotation for PDF",
    "alternativeHeadline": "Enhance PDFs with Dynamic Text Annotations",
    "abstract": "Aspose.PDF for .NET는 고급 텍스트 주석 기능을 도입하여 사용자가 PDF 문서 내에서 텍스트 주석을 쉽게 추가, 검색 또는 제거할 수 있도록 합니다. 이 기능은 주석의 정확한 배치 및 사용자 정의를 가능하게 하여 PDF 편집 프로세스를 향상시키고 문서 상호작용 및 사용성을 개선합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Text Annotation, PDF document generation, Aspose.PDF for .NET, Add Annotation, Delete Annotation, Free Text Annotation, Popup Annotation, StrikeOutAnnotation, AnnotationCollection, Aspose.PDF library",
    "wordcount": "2636",
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
    "url": "/net/text-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF for .NET를 사용하면 PDF 문서에서 텍스트 주석을 추가, 가져오기 및 삭제할 수 있습니다."
}
</script>

## 기존 PDF 파일에 텍스트 주석 추가하는 방법

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

텍스트 주석은 PDF 문서의 특정 위치에 첨부된 주석입니다. 닫힐 때 주석은 아이콘으로 표시되며, 열릴 때는 독자가 선택한 글꼴과 크기로 된 노트 텍스트가 포함된 팝업 창이 표시되어야 합니다.

주석은 특정 페이지의 [Annotations](https://reference.aspose.com/pdf/net/aspose.pdf.annotations) 컬렉션에 포함됩니다. 이 컬렉션은 해당 개별 페이지의 주석만 포함하며, 모든 페이지는 고유한 Annotations 컬렉션을 가지고 있습니다.

특정 페이지에 주석을 추가하려면 [Add](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection/methods/add) 메서드를 사용하여 해당 페이지의 Annotations 컬렉션에 추가합니다.

1. 먼저 PDF에 추가할 주석을 생성합니다.
1. 그런 다음 입력 PDF를 엽니다.
1. 주석을 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 객체의 Annotations 컬렉션에 추가합니다.

다음 코드 스니펫은 PDF 페이지에 주석을 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextAnnotationToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddAnnotation.pdf"))
    {
        // Create text annotation
        var textAnnotation = new Aspose.Pdf.Annotations.TextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(200, 400, 400, 600));
        textAnnotation.Title = "Sample Annotation Title";
        textAnnotation.Subject = "Sample Subject";
        textAnnotation.SetReviewState(Aspose.Pdf.Annotations.AnnotationState.Accepted);
        textAnnotation.Contents = "Sample contents for the annotation";
        textAnnotation.Open = true;
        textAnnotation.Icon = Aspose.Pdf.Annotations.TextIcon.Key;

        // Set border for the annotation
        var border = new Aspose.Pdf.Annotations.Border(textAnnotation);
        border.Width = 5;
        border.Dash = new Aspose.Pdf.Annotations.Dash(1, 1);
        textAnnotation.Border = border;
        textAnnotation.Rect = new Aspose.Pdf.Rectangle(200, 400, 400, 600);

        // Add annotation to the annotations collection of the page
        document.Pages[1].Annotations.Add(textAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddAnnotation_out.pdf");
    }
}
```

## 팝업 주석 추가하는 방법

팝업 주석은 입력 및 편집을 위해 팝업 창에 텍스트를 표시합니다. 단독으로 나타나지 않고 마크업 주석과 연결되어 있으며, 부모 주석의 텍스트를 편집하는 데 사용됩니다.

자신의 외관 스트림이나 관련 작업이 없으며, 부모의 주석 사전에서 Popup 항목으로 식별됩니다.

다음 코드 스니펫은 부모의 [Line annotation](/pdf/ko/net/figures-annotation/#how-to-add-line-annotation-into-existing-pdf-file)을 추가하는 예제를 사용하여 PDF 페이지에 [Popup Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/popupannotation)을 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddLineAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments.pdf"))
    {
        // Create Line Annotation
        var lineAnnotation = new Aspose.Pdf.Annotations.LineAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(550, 93, 562, 439),
            new Aspose.Pdf.Point(556, 99), new Aspose.Pdf.Point(556, 443))
        {
            Title = "John Smith",
            Color = Aspose.Pdf.Color.Red,
            Width = 3,
            StartingStyle = Aspose.Pdf.Annotations.LineEnding.OpenArrow,
            EndingStyle = Aspose.Pdf.Annotations.LineEnding.OpenArrow,
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(842, 124, 1021, 266))
        };

        // Add annotation to the page
        document.Pages[1].Annotations.Add(lineAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddLineAnnotation_out.pdf");
    }
}
```

## 새로운 자유 텍스트 주석 추가(또는 생성)하는 방법

자유 텍스트 주석은 페이지에 직접 텍스트를 표시합니다. [PdfContentEditor.CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) 메서드를 사용하여 이 유형의 주석을 생성할 수 있습니다. 다음 스니펫에서는 문자열의 첫 번째 발생 위에 자유 텍스트 주석을 추가합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFreeTextAnnotationDemo()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "pdf-sample.pdf"))
    {
        var pdfContentEditor = new Aspose.Pdf.Facades.PdfContentEditor(document);

        // Assuming tfa is an instance of TextFragmentAbsorber or similar
        var tfa = new Aspose.Pdf.Text.TextFragmentAbsorber();
        tfa.Visit(document.Pages[1]);

        if (tfa.TextFragments.Count <= 0)
        {
            return;
        }

        // Define the rectangle for the free text annotation
        var rect = new System.Drawing.Rectangle
        {
            X = (int)tfa.TextFragments[1].Rectangle.LLX,
            Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
            Height = 18,
            Width = 100
        };

        // Create free text annotation
        pdfContentEditor.CreateFreeText(rect, "Free Text Demo", 1); // Last param is the page number

        // Save PDF document
        pdfContentEditor.Save(dataDir + "pdf-sample-0.pdf");
    }
}
```

### FreeTextAnnotation의 Callout 속성 설정

PDF 문서에서 주석을 보다 유연하게 구성하기 위해 Aspose.PDF for .NET는 [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) 클래스의 [Callout](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation/properties/callout) 속성을 제공하여 호출선의 점 배열을 지정할 수 있습니다. 다음 코드 스니펫은 이 기능을 사용하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFreeTextCalloutAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create default appearance for the annotation
        var da = new Aspose.Pdf.Annotations.DefaultAppearance();
        da.TextColor = System.Drawing.Color.Red;
        da.FontSize = 10;

        // Create free text annotation with callout
        var fta = new Aspose.Pdf.Annotations.FreeTextAnnotation(page, new Aspose.Pdf.Rectangle(422.25, 645.75, 583.5, 702.75), da);
        fta.Intent = Aspose.Pdf.Annotations.FreeTextIntent.FreeTextCallout;
        fta.EndingStyle = Aspose.Pdf.Annotations.LineEnding.OpenArrow;
        fta.Callout = new Aspose.Pdf.Point[]
        {
            new Aspose.Pdf.Point(428.25, 651.75),
            new Aspose.Pdf.Point(462.75, 681.375),
            new Aspose.Pdf.Point(474, 681.375)
        };

        // Add the annotation to the page
        page.Annotations.Add(fta);

        // Set rich text for the annotation
        fta.RichText = "<body xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:xfa=\"http://www.xfa.org/schema/xfa-data/1.0/\" xfa:APIVersion=\"Acrobat:11.0.23\" xfa:spec=\"2.0.2\"  style=\"color:#FF0000;font-weight:normal;font-style:normal;font-stretch:normal\"><p dir=\"ltr\"><span style=\"font-size:9.0pt;font-family:Helvetica\">This is a sample</span></p></body>";

        // Save PDF document
        document.Save(dataDir + "SetCalloutProperty_out.pdf");
    }
}
```

### XFDF 파일의 Callout 속성 설정

XFDF 파일에서 가져오는 경우 Callout 대신 호출선 이름을 사용하십시오. 다음 코드 스니펫은 이 기능을 사용하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportAnnotationsFromXfdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddAnnotation.pdf"))
    {
        // Create an XFDF string builder
        var xfdf = new StringBuilder();
        xfdf.AppendLine("<?xml version=\"1.0\" encoding=\"UTF-8\"?><xfdf xmlns=\"http://ns.adobe.com/xfdf/\" xml:space=\"preserve\"><annots>");

        // Call the method to create XFDF content
        CreateXfdf(ref xfdf);

        xfdf.AppendLine("</annots></xfdf>");

        // Import annotations from the XFDF string
        document.ImportAnnotationsFromXfdf(new MemoryStream(Encoding.UTF8.GetBytes(xfdf.ToString())));

        // Save PDF document
        document.Save(dataDir + "SetCalloutPropertyXfdf_out.pdf");
    }
}
```

다음 메서드는 CreateXfdf를 생성하는 데 사용됩니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateXfdf(ref StringBuilder pXfdf)
{
    pXfdf.Append("<freetext");
    pXfdf.Append(" page=\"0\"");
    pXfdf.Append(" rect=\"422.25,645.75,583.5,702.75\"");
    pXfdf.Append(" intent=\"FreeTextCallout\"");
    pXfdf.Append(" callout-line=\"428.25,651.75,462.75,681.375,474,681.375\"");
    pXfdf.Append(" tail=\"OpenArrow\"");
    pXfdf.AppendLine(">");
    pXfdf.Append("<contents-richtext><body ");
    pXfdf.Append(" style=\"font-size:10.0pt;text-align:left;color:#FF0000;font-weight:normal;font-style:normal;font-family:Helvetica;font-stretch:normal\">");
    pXfdf.Append("<p dir=\"ltr\">This is a sample</p>");
    pXfdf.Append("</body></contents-richtext>");
    pXfdf.AppendLine("<defaultappearance>/Helv 12 Tf 1 0 0 rg</defaultappearance>");
    pXfdf.AppendLine("</freetext>");
}
```

### 자유 텍스트 주석을 보이지 않게 만들기

때때로 문서를 볼 때 보이지 않지만 문서를 인쇄할 때는 보이도록 하는 워터마크를 생성해야 할 필요가 있습니다. 이 목적을 위해 주석 플래그를 사용하십시오. 다음 코드 스니펫은 그 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddInvisibleAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create a free text annotation
        var annotation = new Aspose.Pdf.Annotations.FreeTextAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(50, 600, 250, 650),
            new Aspose.Pdf.Annotations.DefaultAppearance("Helvetica", 16, System.Drawing.Color.Red)
        );

        annotation.Contents = "ABCDEFG";
        annotation.Characteristics.Border = System.Drawing.Color.Red;
        annotation.Flags = Aspose.Pdf.Annotations.AnnotationFlags.Print | Aspose.Pdf.Annotations.AnnotationFlags.NoView;

        // Add the annotation to the page
        document.Pages[1].Annotations.Add(annotation);

        // Save PDF document
        document.Save(dataDir + "InvisibleAnnotation_out.pdf");
    }
}
```

### FreeTextAnnotation의 서식 설정

이 부분에서는 자유 텍스트 주석의 텍스트를 서식 지정하는 방법을 살펴봅니다.

주석은 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 객체의 [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) 컬렉션에 포함됩니다. PDF 문서에 [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation)을 추가할 때 글꼴, 크기, 색상 등의 서식 정보를 [DefaultAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/defaultappearance/methods/index) 클래스를 사용하여 지정할 수 있습니다. 또한 TextStyle 속성을 사용하여 서식 정보를 지정할 수도 있습니다. 게다가, PDF 문서에 이미 있는 모든 FreeTextAnnotation의 서식을 업데이트할 수 있습니다.

[TextStyle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/textstyle) 클래스는 기본 스타일 항목과 함께 작업하는 것을 지원합니다. 이 클래스는 색상, 글꼴 크기 및 글꼴 이름을 설정할 수 있습니다:

- FontName 속성은 글꼴 이름(string)을 가져오거나 설정합니다.
- FontSize 속성은 기본 텍스트 크기(double)를 가져오거나 설정합니다.
- System.Drawing.Color 속성은 텍스트 색상(color)을 가져오거나 설정합니다.
- TextAlignment 속성은 주석의 텍스트 정렬(alignment)을 가져오거나 설정합니다.

다음 코드 스니펫은 특정 텍스트 서식으로 FreeTextAnnotation을 추가하는 방법을 보여줍니다.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFreeAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetFreeTextAnnotationFormatting.pdf"))
    {
        // Instantiate DefaultAppearance object
        var defaultAppearance = new Aspose.Pdf.Annotations.DefaultAppearance("Arial", 28, System.Drawing.Color.Red);

        // Create annotation
        var freetext = new Aspose.Pdf.Annotations.FreeTextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(200, 400, 400, 600), defaultAppearance);

        // Specify the contents of annotation
        freetext.Contents = "Free Text";

        // Add annotation to annotations collection of page
        document.Pages[1].Annotations.Add(freetext);

        // Save PDF document
        document.Save(dataDir + "SetFreeTextAnnotationFormatting_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFreeAnnotation(string fontName = "Arial", float fontSize = 28)
{
     // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
	
    using (var document = new Aspose.Pdf.Document(dataDir + "SetFreeTextAnnotationFormatting.pdf"))
    {
        // Set default values
        var textColor = System.Drawing.Color.Red;
        var position = new Aspose.Pdf.Rectangle(200, 400, 400, 600);

        // Instantiate DefaultAppearance object
        Aspose.Pdf.Annotations.DefaultAppearance defaultAppearance = new(fontName, fontSize, textColor);
        // Create annotation
        var freetext = new Aspose.Pdf.Annotations.FreeTextAnnotation(document.Pages[1], position, defaultAppearance)
        {
            // Specify the contents of annotation
            Contents = "Free Text"
        };
        // Add anootation to annotations collection of page
        document.Pages[1].Annotations.Add(freetext);

        // Save PDF document
        document.Save(dataDir + "SetFreeTextAnnotationFormatting_out.pdf");
    }
}
```
{{< /tab >}}
{{< /tabs >}}

{{% alert color="primary" %}}

자유 텍스트 주석의 내용이나 텍스트 스타일을 변경하면 주석의 외관이 변경 사항을 반영하도록 재생성됩니다.

{{% /alert %}}

### StrikeOutAnnotation을 사용하여 단어 삭제하기

Aspose.PDF for .NET는 PDF 문서에서 주석을 추가, 삭제 및 업데이트할 수 있습니다. 특정 클래스를 사용하여 주석을 삭제할 수도 있습니다. 이는 문서에서 하나 이상의 텍스트 조각을 삭제하고자 할 때 유용합니다. 주석은 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 객체의 [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) 컬렉션에 포함됩니다. [StrikeOutAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/strikeoutannotation)이라는 클래스를 사용하여 PDF 문서에 스트라이크 아웃 주석을 추가할 수 있습니다.

특정 TextFragment를 삭제하려면:

1. PDF 파일에서 TextFragment를 검색합니다.
1. TextFragment 객체의 좌표를 가져옵니다.
1. 좌표를 사용하여 StrikeOutAnnotation 객체를 인스턴스화합니다.

다음 코드 스니펫은 특정 TextFragment를 검색하고 해당 객체에 StrikeOutAnnotation을 추가하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private void StrikeOutTextInDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "pdf-sample.pdf"))
    {
        // Create TextFragment Absorber instance to search for a particular text fragment
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber("Estoque");

        // Iterate through pages of PDF document
        foreach (var page in document.Pages)
        {
            // Accept the absorber for the current page
            page.Accept(textFragmentAbsorber);
        }

        // Get the collection of absorbed text fragments
        var textFragmentCollection = textFragmentAbsorber.TextFragments;

        // Iterate through the collection of text fragments
        foreach (Aspose.Pdf.Text.TextFragment textFragment in textFragmentCollection)
        {
            // Get rectangular dimensions of the TextFragment object
            var rect = new Aspose.Pdf.Rectangle(
                (float)textFragment.Position.XIndent,
                (float)textFragment.Position.YIndent,
                (float)textFragment.Position.XIndent + (float)textFragment.Rectangle.Width,
                (float)textFragment.Position.YIndent + (float)textFragment.Rectangle.Height);

            // Instantiate StrikeOut Annotation instance
            var strikeOut = new Aspose.Pdf.Annotations.StrikeOutAnnotation(textFragment.Page, rect)
            {
                // Set opacity for annotation
                Opacity = 0.80f,

                // Set the color of annotation
                Color = Aspose.Pdf.Color.Red
            };

            // Set the border for annotation instance
            strikeOut.Border = new Aspose.Pdf.Annotations.Border(strikeOut);

            // Add annotation to the annotations collection of the TextFragment's page
            textFragment.Page.Annotations.Add(strikeOut);
        }

        // Save PDF document
        document.Save(dataDir + "StrikeOutWords_out.pdf");
    }
}
```

## PDF 파일의 페이지에서 모든 주석 삭제하기

[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 객체의 [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) 컬렉션은 해당 특정 페이지의 모든 주석을 포함합니다. 페이지에서 모든 주석을 삭제하려면 AnnotationCollectoin 컬렉션의 *Delete* 메서드를 호출합니다.

다음 코드 스니펫은 특정 페이지에서 모든 주석을 삭제하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteAllAnnotationsFromPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DeleteAllAnnotationsFromPage.pdf"))
    {
        // Delete all annotations from the first page
        document.Pages[1].Annotations.Delete();

        // Save PDF document
        document.Save(dataDir + "DeleteAllAnnotationsFromPage_out.pdf");
    }
}
```

## PDF 파일에서 특정 주석 삭제하기

{{% alert color="primary" %}}

Aspose.PDF의 품질을 확인하고 이 링크에서 결과를 온라인으로 확인할 수 있습니다:
[products.aspose.app/pdf/annotation](https://products.aspose.app/pdf/annotation)

{{% /alert %}}

Aspose.PDF는 PDF 파일에서 특정 주석을 제거할 수 있습니다. 이 주제에서는 그 방법을 설명합니다.

PDF에서 특정 주석을 삭제하려면 [AnnotationCollection 컬렉션의 Delete 메서드](https://reference.aspose.com/pdf/net/aspose.pdf.annotations.annotationcollection/delete/methods/1)를 호출합니다. 이 컬렉션은 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 객체에 속합니다. Delete 메서드는 삭제할 주석의 인덱스를 요구합니다. 그런 다음 업데이트된 PDF 파일을 저장합니다. 다음 코드 스니펫은 특정 주석을 삭제하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteParticularAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DeleteParticularAnnotation.pdf"))
    {
        // Delete a particular annotation by index (e.g., the first annotation on the first page)
        document.Pages[1].Annotations.Delete(1);

        // Save PDF document
        document.Save(dataDir + "DeleteParticularAnnotation_out.pdf");
    }
}
```

## PDF 문서의 페이지에서 모든 주석 가져오기

Aspose.PDF는 전체 문서 또는 특정 페이지에서 주석을 가져올 수 있습니다. PDF 문서의 페이지에서 모든 주석을 가져오려면 원하는 페이지 리소스의 [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) 컬렉션을 반복합니다. 다음 코드 스니펫은 페이지의 모든 주석을 가져오는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetAllAnnotationsFromPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetAllAnnotationsFromPage.pdf"))
    {
        // Loop through all the annotations on the first page
        foreach (Aspose.Pdf.Annotations.MarkupAnnotation annotation in document.Pages[1].Annotations)
        {
            // Get annotation properties
            Console.WriteLine("Title : {0} ", annotation.Title);
            Console.WriteLine("Subject : {0} ", annotation.Subject);
            Console.WriteLine("Contents : {0} ", annotation.Contents);
        }
    }
}
```

전체 PDF에서 모든 주석을 가져오려면 문서의 PageCollection 클래스 컬렉션을 반복한 다음 AnnotationCollection 클래스 컬렉션으로 이동해야 합니다. 컬렉션의 각 주석을 MarkupAnnotation 클래스라는 기본 주석 유형으로 가져온 다음 해당 속성을 표시할 수 있습니다.

## PDF 파일에서 특정 주석 가져오기

주석은 개별 페이지와 연결되어 있으며 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 객체의 [AnnotationCOllection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) 컬렉션에 저장됩니다. 특정 주석을 가져오려면 인덱스를 지정합니다. 이렇게 하면 특정 주석 유형으로 캐스팅해야 하는 [Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotation) 객체가 반환됩니다. 예를 들어 [TextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/textannotation)입니다. 다음 코드 스니펫은 특정 주석과 그 속성을 가져오는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetParticularAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetParticularAnnotation.pdf"))
    {
        // Get a particular annotation by index (e.g., the first annotation on the first page)
        var textAnnotation = (Aspose.Pdf.Annotations.TextAnnotation)document.Pages[1].Annotations[1];

        // Get annotation properties
        Console.WriteLine("Title : {0} ", textAnnotation.Title);
        Console.WriteLine("Subject : {0} ", textAnnotation.Subject);
        Console.WriteLine("Contents : {0} ", textAnnotation.Contents);
    }
}
```

## 주석의 리소스 가져오기

Aspose.PDF는 전체 문서 또는 특정 페이지에서 주석의 리소스를 가져올 수 있습니다. 다음 코드 스니펫은 입력 PDF 파일의 [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification) 객체로 주석의 리소스를 가져오는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAndGetResourceOfAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddAnnotation.pdf"))
    {
        // Create a screen annotation with a SWF file
        var sa = new Aspose.Pdf.Annotations.ScreenAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(100, 400, 300, 600), dataDir + "AddSwfFileAsAnnotation.swf");
        document.Pages[1].Annotations.Add(sa);

        // Save PDF document with the new annotation
        document.Save(dataDir + "GetResourceOfAnnotation_out.pdf");

        // Open the updated document
        var document1 = new Aspose.Pdf.Document(dataDir + "GetResourceOfAnnotation_Out.pdf");

        // Get the action of the annotation
        var action = (document1.Pages[1].Annotations[1] as Aspose.Pdf.Annotations.ScreenAnnotation).Action as Aspose.Pdf.Annotations.RenditionAction;

        // Get the rendition of the rendition action
        var rendition = action.Rendition;

        // Get the media clip
        var clip = (rendition as Aspose.Pdf.Annotations.MediaRendition).MediaClip;
        var data = (clip as Aspose.Pdf.Annotations.MediaClipData).Data;

        // Read the media data
        using (var ms = new MemoryStream())
        {
            byte[] buffer = new byte[1024];
            int read = 0;

            // Data of media are accessible in FileSpecification.Contents
            using (var source = data.Contents)
            {
                while ((read = source.Read(buffer, 0, buffer.Length)) > 0)
                {
                    ms.Write(buffer, 0, read);
                }
            }

            Console.WriteLine(rendition.Name);
            Console.WriteLine(action.RenditionOperation);
        }
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