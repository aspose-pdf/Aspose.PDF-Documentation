---
title: PDF에서 텍스트 추출 C#
linktitle: PDF에서 텍스트 추출
type: docs
weight: 10
url: /ko/net/extract-text-from-all-pdf/
description: 이 문서는 C#에서 Aspose.PDF를 사용하여 PDF 문서에서 텍스트를 추출하는 다양한 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 문서의 모든 페이지에서 텍스트 추출

PDF 문서에서 텍스트를 추출하는 것은 일반적인 요구사항입니다. 이 예제에서는 Aspose.PDF for .NET이 PDF 문서의 모든 페이지에서 텍스트를 추출할 수 있게 하는 방법을 보여줍니다. **TextAbsorber** 클래스의 객체를 생성해야 합니다. 그 후, **Document** 클래스를 사용하여 PDF를 열고 **Pages** 컬렉션의 **Accept** 메서드를 호출합니다. **TextAbsorber** 클래스는 문서에서 텍스트를 흡수하고 **Text** 속성에서 반환합니다. 다음 코드 스니펫은 PDF 문서의 모든 페이지에서 텍스트를 추출하는 방법을 보여줍니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리에서도 작동합니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 문서 열기
Document pdfDocument = new Document(dataDir + "ExtractTextAll.pdf");

// 텍스트 추출을 위한 TextAbsorber 객체 생성
TextAbsorber textAbsorber = new TextAbsorber();
// 모든 페이지에 대해 absorber를 적용
pdfDocument.Pages.Accept(textAbsorber);
// 추출된 텍스트 가져오기
string extractedText = textAbsorber.Text;
// 파일을 열기 위한 writer 생성
TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt");
// 파일에 텍스트 라인 쓰기
tw.WriteLine(extractedText);
// 스트림 닫기
tw.Close();
```
**Accept** 메소드를 Document 객체의 특정 페이지에서 호출하세요. Index는 텍스트를 추출해야 하는 특정 페이지 번호입니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리에서도 작동합니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 문서 열기
Document pdfDocument = new Document(dataDir + "ExtractTextPage.pdf");

// 텍스트를 추출하기 위한 TextAbsorber 객체 생성
TextAbsorber textAbsorber = new TextAbsorber();
 
// 특정 페이지에 대한 absorber 수락
pdfDocument.Pages[1].Accept(textAbsorber);

// 추출된 텍스트 가져오기
string extractedText = textAbsorber.Text;

dataDir = dataDir + "extracted-text_out.txt";
// 파일을 열고 작성자 생성
TextWriter tw = new StreamWriter(dataDir);

// 파일에 텍스트 라인 작성
tw.WriteLine(extractedText);

// 스트림 닫기
tw.Close();
```
## 페이지에서 텍스트 추출하기 위해 Text Device 사용

**TextDevice** 클래스를 사용하여 PDF 파일에서 텍스트를 추출할 수 있습니다. TextDevice는 구현에서 TextAbsorber를 사용하므로, 사실상 동일한 작업을 수행하지만 TextDevice는 페이지 ImageDevice, PageDevice 등에서 어떤 것이든 추출하기 위해 "Device" 접근 방식을 통합하기 위해 구현되었습니다. TextAbsorber는 페이지, 전체 PDF 또는 XForm에서 텍스트를 추출할 수 있으므로 이 TextAbsorber는 더 범용적입니다.

### 모든 페이지에서 텍스트 추출

다음 단계와 코드 스니펫은 PDF에서 텍스트 디바이스를 사용하여 텍스트를 추출하는 방법을 보여줍니다.

1. 입력 PDF 파일이 지정된 Document 클래스의 객체를 생성합니다
1. TextDevice 클래스의 객체를 생성합니다
1. 추출 옵션을 지정하기 위해 TextExtractOptions 클래스의 객체를 사용하십시오
1. TextDevice 클래스의 Process 메서드를 사용하여 내용을 텍스트로 변환합니다
1. 텍스트를 출력 파일에 저장합니다

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요
// 문서 디렉토리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 문서 열기
Document pdfDocument = new Document(dataDir + "input.pdf");
System.Text.StringBuilder builder = new System.Text.StringBuilder();
// 추출된 텍스트를 보관할 문자열
string extractedText = "";

foreach (Page pdfPage in pdfDocument.Pages)
{
    using (MemoryStream textStream = new MemoryStream())
    {
        // 텍스트 디바이스 생성
        TextDevice textDevice = new TextDevice();

        // 텍스트 추출 옵션 설정 - 텍스트 추출 모드 설정 (Raw 또는 Pure)
        TextExtractionOptions textExtOptions = new
        TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
        textDevice.ExtractionOptions = textExtOptions;

        // 특정 페이지를 변환하고 텍스트를 스트림에 저장합니다
        textDevice.Process(pdfPage, textStream);
        // 특정 페이지를 변환하고 텍스트를 스트림에 저장합니다
        textDevice.Process(pdfDocument.Pages[1], textStream);

        // 메모리 스트림 닫기
        textStream.Close();

        // 메모리 스트림에서 텍스트 가져오기
        extractedText = Encoding.Unicode.GetString(textStream.ToArray());
    }
    builder.Append(extractedText);
}

dataDir = dataDir + "input_Text_Extracted_out.txt";
// 추출된 텍스트를 텍스트 파일에 저장합니다
File.WriteAllText(dataDir, builder.ToString());
```
## 특정 페이지 영역에서 텍스트 추출

**TextAbsorber** 클래스는 PDF 문서의 특정 페이지 또는 모든 페이지에서 텍스트를 추출할 수 있는 기능을 제공합니다. 이 클래스는 추출된 텍스트를 **Text** 속성에서 반환합니다. 그러나 특정 페이지 영역에서 텍스트를 추출할 필요가 있는 경우, **TextSearchOptions**의 **Rectangle** 속성을 사용할 수 있습니다. Rectangle 속성은 Rectangle 객체를 값으로 받으며, 이 속성을 사용하여 텍스트를 추출할 페이지의 영역을 지정할 수 있습니다.

페이지의 **Accept** 메소드가 텍스트를 추출하기 위해 호출됩니다. **Document** 및 **TextAbsorber** 클래스의 객체를 생성합니다. **Document** 객체의 개별 페이지에 대해 **Accept** 메소드를 호출하세요. **Index**는 텍스트를 추출할 특정 페이지 번호입니다. **TextAbsorber** 클래스의 **Text** 속성에서 텍스트를 가져올 수 있습니다. 다음 코드 스니펫은 개별 페이지에서 텍스트를 추출하는 방법을 보여줍니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.
다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리에서도 작동합니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 문서 열기
Document pdfDocument = new Document(dataDir + "ExtractTextAll.pdf");

// 텍스트 추출을 위한 TextAbsorber 객체 생성
TextAbsorber absorber = new TextAbsorber();
absorber.TextSearchOptions.LimitToPageBounds = true;
absorber.TextSearchOptions.Rectangle = new Aspose.Pdf.Rectangle(100, 200, 250, 350);

// 첫 페이지에 대해 absorber 적용
pdfDocument.Pages[1].Accept(absorber);

// 추출된 텍스트 가져오기
string extractedText = absorber.Text;
// 파일을 열기 위한 작성기 생성
TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt");
// 파일에 텍스트 라인 작성
tw.WriteLine(extractedText);
// 스트림 닫기
tw.Close();
```

## 열 기준으로 텍스트 추출

PDF 파일은 텍스트, 이미지, 주석, 첨부 파일, 그래프 등의 요소로 구성될 수 있으며, Aspose.PDF for .NET은 이러한 모든 요소를 추가하고 조작하는 기능을 제공합니다.
PDF 파일은 텍스트, 이미지, 주석, 첨부 파일, 그래프 등의 요소를 포함할 수 있으며, Aspose.PDF for .NET은 이러한 모든 요소를 추가하고 조작하는 기능을 제공합니다.

다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 문서 열기
Document pdfDocument = new Document(dataDir + "ExtractTextPage.pdf");

TextFragmentAbsorber tfa = new TextFragmentAbsorber();
pdfDocument.Pages.Accept(tfa);
TextFragmentCollection tfc = tfa.TextFragments;
foreach (TextFragment tf in tfc)
{
    // 폰트 크기를 최소 70% 줄일 필요가 있습니다.
    tf.TextState.FontSize = tf.TextState.FontSize * 0.7f;
}
Stream st = new MemoryStream();
pdfDocument.Save(st);
pdfDocument = new Document(st);
TextAbsorber textAbsorber = new TextAbsorber();
pdfDocument.Pages.Accept(textAbsorber);
String extractedText = textAbsorber.Text;
textAbsorber.Visit(pdfDocument);

dataDir = dataDir + "ExtractColumnsText_out.txt";

System.IO.File.WriteAllText(dataDir, extractedText);
```
### 두 번째 접근 방식 - ScaleFactor 사용

이 새로운 릴리스에서는 TextAbsorber와 내부 텍스트 포맷팅 메커니즘에서 여러 개선 사항을 도입했습니다. 따라서 이제 ‘Pure’ 모드를 사용하여 텍스트 추출을 할 때 ScaleFactor 옵션을 지정할 수 있으며, 이는 위에서 언급한 접근 방식 외에 다단 PDF 문서에서 텍스트를 추출하는 또 다른 방법이 될 수 있습니다. 이 스케일 팩터는 텍스트 추출 중 내부 텍스트 포맷팅 메커니즘에 사용되는 그리드를 조정하기 위해 설정될 수 있습니다. ScaleFactor 값을 1과 0.1 사이(0.1 포함)로 지정하면 글꼴 축소와 동일한 효과가 있습니다.

ScaleFactor 값을 0.1과 -0.1 사이로 지정하면 값이 0으로 처리되지만, 텍스트를 추출하는 동안 필요한 스케일 팩터를 자동으로 계산하도록 알고리즘을 만듭니다.
0.1과 -0.1 사이의 ScaleFactor 값을 지정하면 0으로 처리되지만, 텍스트를 자동으로 추출하는 동안 필요한 스케일 팩터를 계산하게 합니다.

텍스트 콘텐츠 추출을 위해 대량의 PDF 파일을 처리할 때 자동 스케일링(ScaleFactor = 0) 사용을 제안합니다. 또는 수동으로 그리드 너비의 중복 감소(대략 ScaleFactor = 0.5)를 설정합니다. 그러나 구체적인 문서에 대해 스케일링이 필요한지 여부를 결정해서는 안 됩니다. 문서에 대해 그리드 너비의 중복 감소를 설정하면(그것이 필요하지 않은 경우), 추출된 텍스트 콘텐츠는 완전히 적절하게 유지됩니다. 다음 코드 조각을 확인하십시오.

다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

```csharp
// 완벽한 예제와 데이터 파일을 보려면 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 으로 이동하세요
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 문서 열기
Document pdfDocument = new Document(dataDir + "ExtractTextPage.pdf");

TextAbsorber textAbsorber = new TextAbsorber();
textAbsorber.ExtractionOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
// 대부분의 문서에서 열을 분리하기에 충분한 스케일 팩터를 0.5로 설정
// 0을 설정하면 알고리즘이 스케일 팩터를 자동으로 선택합니다
textAbsorber.ExtractionOptions.ScaleFactor = 0.5; /* 0; */
pdfDocument.Pages.Accept(textAbsorber);
String extractedText = textAbsorber.Text;
System.IO.File.WriteAllText( dataDir + "ExtractTextUsingScaleFactor_out.text", extractedText);
```
{{% alert color="primary" %}}

새로운 ScaleFactor와 수동으로 폰트 크기를 줄이는 구형 계수 간에는 직접적인 대응이 없습니다. 그러나 기본 알고리즘은 이미 어떤 내부적인 이유로 인해 감소된 폰트 크기의 값을 고려합니다. 예를 들어, 폰트 크기를 10에서 7로 줄이는 것은 스케일 팩터를 5/8 (= 0.625)로 설정하는 것과 동일한 효과가 있습니다.

{{% /alert %}}

## PDF 문서에서 하이라이트된 텍스트 추출하기

PDF 문서에서 텍스트를 추출하는 다양한 시나리오에서 PDF 문서에서 하이라이트된 텍스트만을 추출할 필요가 있을 수 있습니다. 이 기능을 구현하기 위해, API에 TextMarkupAnnotation.GetMarkedText() 및 TextMarkupAnnotation.GetMarkedTextFragments() 메소드를 추가했습니다. TextMarkupAnnotation을 필터링하고 언급된 메소드를 사용하여 PDF 문서에서 하이라이트된 텍스트를 추출할 수 있습니다. 다음 코드 스니펫은 PDF 문서에서 하이라이트된 텍스트를 추출하는 방법을 보여줍니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.
다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리에서도 작동합니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
Document doc = new Document(dataDir + "ExtractHighlightedText.pdf");
// 모든 주석을 순회합니다.
foreach (Annotation annotation in doc.Pages[1].Annotations)
{
    // TextMarkupAnnotation 필터링
    if (annotation is TextMarkupAnnotation)
    {
        TextMarkupAnnotation highlightedAnnotation = annotation as TextMarkupAnnotation;
        // 강조 표시된 텍스트 조각을 검색합니다.
        TextFragmentCollection collection = highlightedAnnotation.GetMarkedTextFragments();
        foreach (TextFragment tf in collection)
        {
            // 강조 표시된 텍스트를 표시합니다.
            Console.WriteLine(tf.Text);
        }
    }
}
```

## XML에서 생성된 PDF 문서를 처리할 때 TextFragment와 TextSegment 요소에 접근하기

때때로, XML에서 생성된 PDF 문서를 처리할 때 TextFragement나 TextSegment 항목에 접근할 필요가 있습니다.
가끔 XML에서 생성된 PDF 문서를 처리할 때 TextFragment나 TextSegment 항목에 접근할 필요가 있습니다.

다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하십시오.
// 문서 디렉토리로의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

string inXml = "40014.xml";
string outFile = "40014_out.pdf";

Document doc = new Document();
doc.BindXml(dataDir + inXml);

Page page = (Page)doc.GetObjectById("mainSection");

TextSegment segment = (TextSegment)doc.GetObjectById("boldHtml");
segment = (TextSegment)doc.GetObjectById("strongHtml");
doc.Save(dataDir + outFile);
```
