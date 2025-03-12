---
title: PDF에서 텍스트 추출 C#
linktitle: PDF에서 텍스트 추출
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/extract-text-from-all-pdf/
description: 이 문서에서는 C#에서 Aspose.PDF를 사용하여 PDF 문서에서 텍스트를 추출하는 다양한 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Text from PDF C#",
    "alternativeHeadline": "Effortlessly Extract Text from PDFs in C#",
    "abstract": "개발자가 PDF 문서에서 텍스트를 손쉽게 추출할 수 있도록 하는 강력한 새로운 기능을 발견하십시오. 이 기능은 모든 페이지 또는 특정 영역에서의 추출을 지원하며, 다중 열 레이아웃을 수용하고, 몇 줄의 코드로 강조된 텍스트를 검색할 수 있게 해줍니다. 이 다재다능한 도구로 문서 처리 기능을 향상시키고 콘텐츠 추출을 간소화하십시오.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "2005",
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
    "url": "/net/extract-text-from-all-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-text-from-all-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

## PDF 문서의 모든 페이지에서 텍스트 추출

PDF 문서에서 텍스트를 추출하는 것은 일반적인 요구 사항입니다. 이 예제에서는 Aspose.PDF for .NET이 PDF 문서의 모든 페이지에서 텍스트를 추출하는 방법을 보여줍니다. **TextAbsorber** 클래스의 객체를 생성해야 합니다. 그 후, **Document** 클래스를 사용하여 PDF를 열고 **Pages** 컬렉션의 **Accept** 메서드를 호출합니다. **TextAbsorber** 클래스는 문서에서 텍스트를 흡수하고 **Text** 속성에서 반환합니다. 다음 코드 스니펫은 PDF 문서의 모든 페이지에서 텍스트를 추출하는 방법을 보여줍니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와도 작동합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextAll.pdf"))
    {
        // Create TextAbsorber object to extract text
        var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();

        // Accept the absorber for all the pages
        document.Pages.Accept(textAbsorber);

        // Get the extracted text
        string extractedText = textAbsorber.Text;

        // Create a writer and open the file
        using (TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt"))
        {
            // Write a line of text to the file
            tw.WriteLine(extractedText);
        }
    }
}
```

Document 객체의 특정 페이지에서 **Accept** 메서드를 호출합니다. 인덱스는 텍스트를 추출해야 하는 특정 페이지 번호입니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와도 작동합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {

        // Create TextAbsorber object to extract text
        var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();

        // Accept the absorber for a particular page
        document.Pages[1].Accept(textAbsorber);

        // Get the extracted text
        string extractedText = textAbsorber.Text;

        // Create a writer and open the file
        using (TextWriter tw = new StreamWriter(dataDir + "extracted-text_out.txt"))
        {
            // Write a line of text to the file
            tw.WriteLine(extractedText);
        }
    }
}
```

## 텍스트 장치를 사용하여 페이지에서 텍스트 추출

**TextDevice** 클래스를 사용하여 PDF 파일에서 텍스트를 추출할 수 있습니다. TextDevice는 구현에서 TextAbsorber를 사용하므로 사실상 동일한 작업을 수행하지만 TextDevice는 페이지에서 이미지를 추출하는 "장치" 접근 방식을 통합하기 위해 구현되었습니다. TextAbsorber는 페이지, 전체 PDF 또는 XForm에서 텍스트를 추출할 수 있으며, 이 TextAbsorber는 더 보편적입니다.

### 모든 페이지에서 텍스트 추출

다음 단계와 코드 스니펫은 텍스트 장치를 사용하여 PDF에서 텍스트를 추출하는 방법을 보여줍니다.

1. 입력 PDF 파일이 지정된 Document 클래스의 객체를 생성합니다.
1. TextDevice 클래스의 객체를 생성합니다.
1. TextExtractOptions 클래스의 객체를 사용하여 추출 옵션을 지정합니다.
1. TextDevice 클래스의 Process 메서드를 사용하여 내용을 텍스트로 변환합니다.
1. 텍스트를 출력 파일에 저장합니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와도 작동합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromPagesWithTextDevice()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    var builder = new System.Text.StringBuilder();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {
        // String to hold extracted text
        string extractedText = "";

        foreach (var page in document.Pages)
        {
            using (MemoryStream textStream = new MemoryStream())
            {
                // Create text device
                var textDevice = new Aspose.Pdf.Devices.TextDevice();

                // Set text extraction options - set text extraction mode (Raw or Pure)
                var textExtOptions = new Aspose.Pdf.Text.TextExtractionOptions(Aspose.Pdf.Text.TextExtractionOptions.TextFormattingMode.Pure);
                textDevice.ExtractionOptions = textExtOptions;

                // Convert a particular page and save text to the stream
                textDevice.Process(page, textStream);
                // Convert a particular page and save text to the stream
                textDevice.Process(document.Pages[1], textStream);

                // Get text from memory stream
                extractedText = System.Text.Encoding.Unicode.GetString(textStream.ToArray());
            }
            builder.Append(extractedText);
        }
    }

    // Save the extracted text in text file
    File.WriteAllText(dataDir + "input_Text_Extracted_out.txt", builder.ToString());
}
```

## 특정 페이지 영역에서 텍스트 추출

**TextAbsorber** 클래스는 PDF 문서의 특정 페이지 또는 모든 페이지에서 텍스트를 추출할 수 있는 기능을 제공합니다. 이 클래스는 추출된 텍스트를 **Text** 속성에서 반환합니다. 그러나 특정 페이지 영역에서 텍스트를 추출해야 하는 경우 **TextSearchOptions**의 **Rectangle** 속성을 사용할 수 있습니다. Rectangle 속성은 Rectangle 객체를 값으로 사용하며, 이 속성을 사용하여 텍스트를 추출해야 하는 페이지의 영역을 지정할 수 있습니다.

텍스트를 추출하기 위해 페이지의 **Accept** 메서드를 호출합니다. **Document** 및 **TextAbsorber** 클래스의 객체를 생성합니다. **Document** 객체의 개별 페이지에서 **Accept** 메서드를 호출합니다. **Index**는 텍스트를 추출해야 하는 특정 페이지 번호입니다. **TextAbsorber** 클래스의 **Text** 속성에서 텍스트를 가져올 수 있습니다. 다음 코드 스니펫은 개별 페이지에서 텍스트를 추출하는 방법을 보여줍니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와도 작동합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromParticularPageRegion()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextAll.pdf"))
    {
        // Create TextAbsorber object to extract text
        var absorber = new Aspose.Pdf.Text.TextAbsorber();
        absorber.TextSearchOptions.LimitToPageBounds = true;
        absorber.TextSearchOptions.Rectangle = new Aspose.Pdf.Rectangle(100, 200, 250, 350);

        // Accept the absorber for first page
        document.Pages[1].Accept(absorber);

        // Get the extracted text
        string extractedText = absorber.Text;

        // Create a writer and open the file
        using (TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt"))
        {
            // Write a line of text to the file
            tw.WriteLine(extractedText);
        }
    }
}
```

## 열 기반으로 텍스트 추출

PDF 파일은 텍스트, 이미지, 주석, 첨부 파일, 그래프 등 요소로 구성될 수 있으며 Aspose.PDF for .NET은 이러한 모든 요소를 추가하고 조작하는 기능을 제공합니다. 이 API는 PDF 문서에서 텍스트 추가 및 추출에 있어 뛰어나며, PDF 문서가 여러 열(다중 열)로 구성된 경우 페이지 내용을 동일한 레이아웃을 유지하면서 추출해야 하는 시나리오에 직면할 수 있습니다. 이 요구 사항을 충족하기 위해 Aspose.PDF for .NET이 적합한 선택입니다. 한 가지 접근 방식은 PDF 문서 내의 내용의 글꼴 크기를 줄인 다음 텍스트 추출을 수행하는 것입니다. 다음 코드 스니펫은 텍스트 크기를 줄이고 PDF 문서에서 텍스트를 추출하는 단계를 보여줍니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와도 작동합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextBasedOnColumns()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    var extractedText = string.Empty;
    // Open PDF document
    using (var sourceDocument = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {

        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        sourceDocument.Pages.Accept(textFragmentAbsorber);
        Aspose.Pdf.Text.TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
        foreach (Aspose.Pdf.Text.TextFragment textFragment in textFragmentCollection)
        {
            // Need to reduce font size at least for 70%
            textFragment.TextState.FontSize = textFragment.TextState.FontSize * 0.7f;
        }
        using (Stream sourceStream = new MemoryStream())
        {
            sourceDocument.Save(sourceStream);
            using (var destDocument = new Aspose.Pdf.Document(sourceStream))
            {
                var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();
                destDocument.Pages.Accept(textAbsorber);
                extractedText = textAbsorber.Text;
                textAbsorber.Visit(destDocument);
            }
        }

        // Save the extracted text in text file
        File.WriteAllText(dataDir + "ExtractColumnsText_out.txt", extractedText);
    }
}
```

### 두 번째 접근 방식 - ScaleFactor 사용

이번 새로운 릴리스에서는 TextAbsorber와 내부 텍스트 형식화 메커니즘에서 여러 가지 개선 사항을 도입했습니다. 따라서 이제 'Pure' 모드를 사용하여 텍스트를 추출할 때 ScaleFactor 옵션을 지정할 수 있으며, 이는 위에서 언급한 접근 방식 외에도 다중 열 PDF 문서에서 텍스트를 추출하는 또 다른 접근 방식이 될 수 있습니다. 이 스케일 팩터는 텍스트 추출 중 내부 텍스트 형식화 메커니즘에 사용되는 그리드를 조정하는 데 설정할 수 있습니다. 1과 0.1(0.1 포함) 사이의 ScaleFactor 값을 지정하면 글꼴 축소와 동일한 효과를 가집니다.

0.1과 -0.1 사이의 ScaleFactor 값은 0 값으로 처리되지만, 텍스트 추출 중에 필요한 스케일 팩터를 자동으로 계산하도록 알고리즘을 작동시킵니다. 이 계산은 페이지에서 가장 인기 있는 글꼴의 평균 글리프 너비를 기반으로 하지만, 추출된 텍스트에서 열의 문자열이 다음 열의 시작에 도달하지 않는 것을 보장할 수는 없습니다. ScaleFactor 값이 지정되지 않으면 기본값 1.0이 사용됩니다. 이는 스케일링이 수행되지 않음을 의미합니다. 지정된 ScaleFactor 값이 10보다 크거나 -0.1보다 작으면 기본값 1.0이 사용됩니다.

우리는 텍스트 콘텐츠 추출을 위해 많은 PDF 파일을 처리할 때 자동 스케일링(ScaleFactor = 0)의 사용을 제안합니다. 또는 그리드 너비의 불필요한 축소를 수동으로 설정합니다(약 ScaleFactor = 0.5). 그러나 특정 문서에 대해 스케일링이 필요한지 여부를 결정해서는 안 됩니다. 문서에 대해 불필요한 그리드 너비 축소를 설정하면(그것이 필요하지 않은 경우) 추출된 텍스트 콘텐츠는 완전히 적절하게 유지됩니다. 다음 코드 스니펫을 참조하십시오.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와도 작동합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExctractTextWithScaleFactor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {

        var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();
        textAbsorber.ExtractionOptions = new Aspose.Pdf.Text.TextExtractionOptions(Aspose.Pdf.Text.TextExtractionOptions.TextFormattingMode.Pure);
        // Setting scale factor to 0.5 is enough to split columns in the majority of documents
        // Setting of zero allows to algorithm choose scale factor automatically
        textAbsorber.ExtractionOptions.ScaleFactor = 0.5; /* 0; */
        document.Pages.Accept(textAbsorber);
        var extractedText = textAbsorber.Text;

        // Save the extracted text in text file
        File.WriteAllText(dataDir + "ExtractTextUsingScaleFactor_out.text", extractedText);
    }
}
```

{{% alert color="primary" %}}

새로운 ScaleFactor와 이전 수동 글꼴 축소 계수 간에는 직접적인 상관관계가 없음을 유의하십시오. 그러나 기본 알고리즘은 내부적인 이유로 인해 이미 축소된 글꼴 크기 값을 고려합니다. 예를 들어, 글꼴 크기를 10에서 7로 줄이는 것은 스케일 팩터를 5/8(= 0.625)로 설정하는 것과 동일한 효과를 가집니다.

{{% /alert %}}

## PDF 문서에서 강조된 텍스트 추출

PDF 문서에서 텍스트를 추출하는 다양한 시나리오에서 PDF 문서에서 강조된 텍스트만 추출해야 하는 요구 사항이 있을 수 있습니다. 이 기능을 구현하기 위해 API에 TextMarkupAnnotation.GetMarkedText() 및 TextMarkupAnnotation.GetMarkedTextFragments() 메서드를 추가했습니다. TextMarkupAnnotation을 필터링하고 언급된 메서드를 사용하여 PDF 문서에서 강조된 텍스트를 추출할 수 있습니다. 다음 코드 스니펫은 PDF 문서에서 강조된 텍스트를 추출하는 방법을 보여줍니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와도 작동합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractHighlightedTextFromDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractHighlightedText.pdf"))
    {
        // Loop through all the annotations
        foreach (Aspose.Pdf.Annotations.Annotation annotation in document.Pages[1].Annotations)
        {
            // Filter TextMarkupAnnotation
            if (annotation is Aspose.Pdf.Annotations.TextMarkupAnnotation)
            {
                var highlightedAnnotation = annotation as Aspose.Pdf.Annotations.TextMarkupAnnotation;
                // Retrieve highlighted text fragments
                Aspose.Pdf.Text.TextFragmentCollection collection = highlightedAnnotation.GetMarkedTextFragments();
                foreach (Aspose.Pdf.Text.TextFragment textFragment in collection)
                {
                    // Display highlighted text
                    Console.WriteLine(textFragment.Text);
                }
            }
        }
    }
}
```

## XML에서 텍스트 조각 및 세그먼트 요소에 접근

때때로 XML에서 생성된 PDF 문서를 처리할 때 TextFragment 또는 TextSegment 항목에 접근해야 할 필요가 있습니다. Aspose.PDF for .NET은 이름으로 이러한 항목에 접근할 수 있는 기능을 제공합니다. 아래 코드 스니펫은 이 기능을 사용하는 방법을 보여줍니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와도 작동합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AccessTextFragmentAndSegmentElementsFromXML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.BindXml(dataDir + "40014.xml");

        // Get page
        var page = (Aspose.Pdf.Page)document.GetObjectById("mainSection");

        // Get elements by Id
        var segment = (Aspose.Pdf.Text.TextSegment)document.GetObjectById("boldHtml");
        segment = (Aspose.Pdf.Text.TextSegment)document.GetObjectById("strongHtml");

        // Save PDF document
        document.Save(dataDir + "DocumentFromXML_out.pdf");
    }
}
```