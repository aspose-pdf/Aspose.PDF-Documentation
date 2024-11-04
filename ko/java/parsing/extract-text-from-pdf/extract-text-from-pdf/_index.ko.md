---
title: PDF 파일에서 원시 텍스트 추출 
linktitle: PDF에서 텍스트 추출
type: docs
weight: 10
url: /java/extract-text-from-all-pdf/
description: 이 문서는 Aspose.PDF for Java를 사용하여 PDF 문서에서 텍스트를 추출하는 다양한 방법을 설명합니다. 전체 페이지에서, 특정 부분에서, 열을 기준으로 등.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 문서의 모든 페이지에서 텍스트 추출

PDF 문서에서 텍스트를 추출하는 것은 일반적인 요구 사항입니다. 이 예제에서는 Aspose.PDF for Java가 PDF 문서의 모든 페이지에서 텍스트를 추출할 수 있는 방법을 살펴보겠습니다.
모든 PDF 페이지에서 텍스트를 추출하려면:

1. [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) 클래스의 객체를 생성합니다.

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스를 사용하여 PDF를 열고 [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 컬렉션의 [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) 메서드를 호출합니다.
2. [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) 클래스는 문서에서 텍스트를 흡수하고 **Text** 속성으로 반환합니다.

다음 코드 스니펫은 PDF 문서의 모든 페이지에서 텍스트를 추출하는 방법을 보여줍니다.

```java
public static void ExtractFromAllPages(){
    // 문서 디렉토리 경로
    String _dataDir = "/home/admin1/pdf-examples/Samples/";
    String filePath = _dataDir + "ExtractTextAll.pdf";

    // 문서 열기
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);

    // 텍스트 추출을 위한 TextAbsorber 객체 생성
    com.aspose.pdf.TextAbsorber textAbsorber = new com.aspose.pdf.TextAbsorber();
    
    // 모든 페이지에 흡수기 적용
    pdfDocument.getPages().accept(textAbsorber);
    
    // 추출된 텍스트 가져오기
    String extractedText = textAbsorber.getText();                
    try {
        java.io.FileWriter writer = new java.io.FileWriter(_dataDir + "extracted-text.txt", true);
        // 파일에 텍스트 한 줄 쓰기
        writer.write(extractedText);            
        // 스트림 닫기
        writer.close();
    } catch (java.io.IOException e) {
        e.printStackTrace();
    }

}
```


## 페이지에서 텍스트 추출하기 - 텍스트 디바이스 사용

**TextDevice** 클래스를 사용하여 PDF 파일에서 텍스트를 추출할 수 있습니다. TextDevice는 [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber)를 구현에 사용하며, 실제로 같은 작업을 수행하지만, TextDevice는 페이지 이미지 디바이스, 페이지 디바이스 등에서 "디바이스" 접근 방식을 통합해 구현되었습니다. TextAbsorber는 페이지, 전체 PDF 또는 XForm에서 텍스트를 추출할 수 있으며, 이 TextAbsorber는 더 보편적입니다.

### 모든 페이지에서 텍스트 추출하기

다음 단계와 코드 스니펫은 텍스트 디바이스를 사용하여 PDF에서 텍스트를 추출하는 방법을 보여줍니다.

1. 입력 PDF 파일을 지정하여 Document 클래스의 객체를 생성합니다.
1. TextDevice 클래스의 객체를 생성합니다.
1. TextExtractOptions 클래스의 객체를 사용하여 추출 옵션을 지정합니다.
1. TextDevice 클래스의 Process 메서드를 사용하여 내용을 텍스트로 변환합니다.
1. 텍스트를 출력 파일에 저장합니다.

```java
public static void extractTextFromAllPagesOfPDF() throws IOException {
    // 문서 열기
    Document pdfDocument = new Document("input.pdf");
    // 추출된 텍스트가 저장될 텍스트 파일
    java.io.OutputStream text_stream = new java.io.FileOutputStream("ExtractedText.txt", false);
    // PDF 파일의 모든 페이지를 반복
    for (Page page : (Iterable<Page>) pdfDocument.getPages()) {
        // 텍스트 디바이스 생성
        TextDevice textDevice = new TextDevice();
        // 텍스트 추출 옵션 설정 - 텍스트 추출 모드 설정 (Raw 또는
        // Pure)
        TextExtractionOptions textExtOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Raw);
        textDevice.setExtractionOptions(textExtOptions);
        // PDF 페이지에서 텍스트를 가져와 OutputStream 객체에 저장
        textDevice.process(page, text_stream);
    }
    // 스트림 객체 닫기
    text_stream.close();
}
```


## 특정 페이지 영역에서 텍스트 추출

[TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) 클래스는 PDF 문서의 특정 또는 모든 페이지에서 텍스트를 추출할 수 있는 기능을 제공합니다. 이 클래스는 추출된 텍스트를 **Text** 속성에 반환합니다. 그러나 특정 페이지 영역에서 텍스트를 추출해야 하는 경우, [TextSearchOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextSearchOptions)의 **Rectangle** 속성을 사용할 수 있습니다. Rectangle 속성은 Rectangle 객체를 값으로 취하며, 이 속성을 사용하여 텍스트를 추출해야 하는 페이지의 영역을 지정할 수 있습니다.

페이지의 [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) 메소드는 텍스트를 추출하기 위해 호출됩니다.
 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 및 [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) 클래스의 객체를 만듭니다. **Document** 객체의 개별 페이지, 즉 **Page** 인덱스에 대해 [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) 메서드를 호출합니다. **Index**는 텍스트를 추출해야 하는 특정 페이지 번호입니다. [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) 클래스의 **Text** 속성에서 텍스트를 가져올 수 있습니다. 다음 코드 스니펫은 개별 페이지에서 텍스트를 추출하는 방법을 보여줍니다.

```java
public static void ExtractTextFromParticularPageRegion(String[] args) throws IOException {
    // 문서 열기
    Document doc = new Document("page_0001.pdf");
    // 텍스트 추출을 위한 TextAbsorber 객체 생성
    TextAbsorber absorber = new TextAbsorber();
    absorber.getTextSearchOptions().setLimitToPageBounds(true);
    absorber.getTextSearchOptions().setRectangle(new Rectangle(100, 200, 250, 350));
    // 첫 번째 페이지에 대해 absorber 수락
    doc.getPages().get_Item(1).accept(absorber);
    // 추출된 텍스트 가져오기
    String extractedText = absorber.getText();
    // 작성자 생성 및 파일 열기
    BufferedWriter writer = new BufferedWriter(new FileWriter(new java.io.File("ExtractedText.txt")));
    // 추출된 내용 작성
    writer.write(extractedText);
    // 작성자 닫기
    writer.close();
}
```

## 열을 기반으로 텍스트 추출하기

PDF 파일은 텍스트, 이미지, 주석, 첨부 파일, 그래프 등 요소들로 구성될 수 있으며, Aspose.PDF for .NET은 이러한 모든 요소들을 추가하고 조작하는 기능을 제공합니다. 이 API는 PDF 문서에서 텍스트 추가 및 추출에 탁월하며, 여러 개의 열(다중 열)로 구성된 PDF 문서에서 동일한 레이아웃을 유지하면서 페이지 콘텐츠를 추출해야 하는 시나리오가 있을 수 있습니다. 이 요구사항을 충족시키기에 Aspose.PDF for .NET은 적합한 선택입니다. 한 가지 접근 방식은 PDF 문서 내의 콘텐츠의 글꼴 크기를 줄이고 텍스트 추출을 수행하는 것입니다. 다음 코드 스니펫은 글꼴 크기를 줄이고 PDF 문서에서 텍스트를 추출하는 단계를 보여줍니다.

```java
public static void ExtractTextBasedOnColumns() throws IOException {
    // 문서 열기
    Document doc = new Document("page_0001.pdf");
    // 텍스트 추출을 위한 TextAbsorber 객체 생성
    TextAbsorber absorber = new TextAbsorber();
    absorber.getTextSearchOptions().setLimitToPageBounds(true);
    absorber.getTextSearchOptions().setRectangle(new Rectangle(100, 200, 250, 350));
    // 첫 번째 페이지에 흡수기 수락
    doc.getPages().get_Item(1).accept(absorber);
    // 추출된 텍스트 가져오기
    String extractedText = absorber.getText();
    // 작성자 생성 및 파일 열기
    BufferedWriter writer = new BufferedWriter(new FileWriter(new java.io.File("ExtractedText.txt")));
    // 추출된 내용 작성
    writer.write(extractedText);
    // 작성자 닫기
    writer.close();
}
```


### 두 번째 접근 방식 - ScaleFactor 사용

이 새로운 릴리스에서는 TextAbsorber와 내부 텍스트 포맷팅 메커니즘에 몇 가지 개선 사항을 도입했습니다. 그래서 이제 'Pure' 모드를 사용하여 텍스트를 추출하는 동안 ScaleFactor 옵션을 지정할 수 있으며, 이는 위에서 언급한 접근 방식 외에 다중 열 PDF 문서에서 텍스트를 추출하는 또 다른 방법이 될 수 있습니다. 이 스케일 팩터는 텍스트 추출 중 내부 텍스트 포맷팅 메커니즘에 사용되는 그리드를 조정하도록 설정할 수 있습니다. ScaleFactor 값을 1과 0.1(0.1 포함) 사이로 지정하면 폰트를 줄이는 것과 동일한 효과를 가집니다.

ScaleFactor 값을 0.1에서 -0.1 사이로 지정하면 0 값으로 처리되지만, 텍스트를 추출하는 동안 필요한 스케일 팩터를 자동으로 계산하도록 알고리즘이 작동합니다. 이 계산은 페이지에서 가장 많이 사용되는 글꼴의 평균 글리프 너비를 기반으로 하지만, 추출된 텍스트에서 열의 시작이 다음 열에 도달하지 않는다는 보장은 할 수 없습니다. ScaleFactor 값이 지정되지 않으면 기본값인 1.0이 사용됩니다. 이는 스케일링이 수행되지 않음을 의미합니다. 지정된 ScaleFactor 값이 10보다 크거나 -0.1보다 작은 경우 기본값인 1.0이 사용됩니다.

We propose the usage of auto-scaling (ScaleFactor = 0) when processing a large number of PDF files for text content extraction. Or manually set redundant reducing of grid width ( about ScaleFactor = 0.5). However, you must not determine whether scaling is necessary for concrete documents or not. If You set redundant reducing of grid width for the document (that doesn't need in it), the extracted text content will remain fully adequate. Please take a look at the following code snippet.

우리는 텍스트 콘텐츠 추출을 위해 많은 PDF 파일을 처리할 때 자동 크기 조정(ScaleFactor = 0)의 사용을 제안합니다. 또는 수동으로 그리드 너비를 불필요하게 줄이도록 설정합니다(약 ScaleFactor = 0.5). 그러나 특정 문서에 크기 조정이 필요한지 여부를 결정해서는 안 됩니다. 문서에 대해 불필요하게 그리드 너비를 줄이는 설정을 하면(그것이 필요하지 않은 경우) 추출된 텍스트 콘텐츠는 완전히 적절하게 유지됩니다. 다음 코드 스니펫을 살펴보십시오.

```java
public static void usingSetScaleFactorMethod() {
    Document pdfDocument = new Document("inputFile.pdf");
    TextAbsorber textAbsorber = new TextAbsorber();
    textAbsorber.setExtractionOptions(new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure));
    // Setting scale factor to 0.5 is enough to split columns in the majority of documents
    // Setting of zero allows to algorithm choose scale factor automatically
    textAbsorber.getExtractionOptions().setScaleFactor((double) 0.5);
    pdfDocument.getPages().accept(textAbsorber);
    String extractedText = textAbsorber.getText();
}
```


{{% alert color="primary" %}}

새로운 ScaleFactor와 기존의 수동 폰트 축소 계수 간에는 직접적인 대응 관계가 없음을 유의하세요. 그러나 기본 알고리즘은 내부적인 이유로 이미 축소된 폰트 크기 값을 고려합니다. 예를 들어, 폰트 크기를 10에서 7로 줄이는 것은 스케일 팩터를 5/8 (= 0.625)로 설정하는 것과 동일한 효과가 있습니다.

{{% /alert %}}

## PDF 문서에서 강조 표시된 텍스트 추출

PDF 문서에서 텍스트를 추출하는 다양한 시나리오에서 PDF 문서에서 강조 표시된 텍스트만 추출해야 하는 요구가 있을 수 있습니다. 이 기능을 구현하기 위해 API에 TextMarkupAnnotation.GetMarkedText() 및 TextMarkupAnnotation.GetMarkedTextFragments() 메서드를 추가했습니다. TextMarkupAnnotation을 필터링하고 언급된 메서드를 사용하여 PDF 문서에서 강조 표시된 텍스트를 추출할 수 있습니다. 다음 코드 스니펫은 PDF 문서에서 강조 표시된 텍스트를 추출하는 방법을 보여줍니다.

```java
public static void ExtractHighlightedText() {
    Document doc = new Document(_dataDir + "ExtractHighlightedText.pdf");
    // 모든 주석을 반복
    for (Annotation annotation : doc.getPages().get_Item(1).getAnnotations())
    {
        // TextMarkupAnnotation 필터링
        if (annotation.getAnnotationType()==AnnotationType.Highlight)
        {
            HighlightAnnotation highlightedAnnotation = (HighlightAnnotation) annotation;
            // 강조 표시된 텍스트 조각 검색
            TextFragmentCollection collection = highlightedAnnotation.getMarkedTextFragments();
            for (TextFragment tf : collection)
            {
                // 강조 표시된 텍스트 출력
                System.out.println(tf.getText());
            }
        }
    }        
}
```


## XML에서 텍스트 프래그먼트 및 세그먼트 요소 접근하기

때때로 우리는 XML에서 생성된 PDF 문서를 처리할 때 TextFragment 또는 TextSegment 항목에 접근해야 합니다. Aspose.PDF for .NET은 이름으로 이러한 항목에 접근할 수 있는 기능을 제공합니다. 아래 코드 스니펫은 이 기능을 사용하는 방법을 보여줍니다.

```java
public static void AccessTextFragmentAndSegmentElements() {
    String inXml = "40014.xml";        
    Document doc = new Document();
    doc.bindXml(_dataDir + inXml);

    TextSegment segment = (TextSegment) doc.getObjectById("boldHtml");
    segment = (TextSegment) doc.getObjectById("strongHtml");

    System.out.println(segment.getText());
    
}
```