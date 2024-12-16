---
title: PDF 파일에서 원시 텍스트 추출 
linktitle: PDF에서 텍스트 추출
type: docs
weight: 10
url: /ko/androidjava/extract-text-from-all-pdf/
description: 이 문서는 Aspose.PDF for Android via Java를 사용하여 PDF 문서에서 텍스트를 추출하는 다양한 방법을 설명합니다. 전체 페이지에서, 특정 부분에서, 열을 기반으로 등.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 문서의 모든 페이지에서 텍스트 추출

PDF 문서에서 텍스트를 추출하는 것은 일반적인 요구 사항입니다. 이 예제에서는 Aspose.PDF for Java가 PDF 문서의 모든 페이지에서 텍스트를 추출하는 방법을 보여줍니다.
모든 PDF 페이지에서 텍스트를 추출하려면:

1. [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) 클래스의 객체를 생성합니다.

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스와 [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 컬렉션의 [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) 메서드를 호출하여 PDF를 엽니다.  
2. [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) 클래스는 문서에서 텍스트를 흡수하고 **Text** 속성에서 반환합니다.  

다음 코드 스니펫은 PDF 문서의 모든 페이지에서 텍스트를 추출하는 방법을 보여줍니다.  

```java
public static void ExtractFromAllPages() {
        // 문서 디렉토리 경로입니다.

        String filePath = _dataDir + "ExtractTextAll.pdf";

        // 문서 열기
        Document pdfDocument = new com.aspose.pdf.Document(filePath);

        // 텍스트 추출을 위한 TextAbsorber 객체 생성
        TextAbsorber textAbsorber = new com.aspose.pdf.TextAbsorber();

        // 모든 페이지에 대해 흡수기 수락
        pdfDocument.getPages().accept(textAbsorber);

        // 추출된 텍스트 가져오기
        String extractedText = textAbsorber.getText();
        try {
            java.io.FileWriter writer = new java.io.FileWriter(_dataDir + "extracted-text.txt", true);
            // 파일에 한 줄의 텍스트 쓰기
            writer.write(extractedText);
            // 스트림 닫기
            writer.close();
        } catch (java.io.IOException e) {
            e.printStackTrace();
        }

    }
```


## PDF 문서에서 강조된 텍스트 추출하기

PDF 문서에서 텍스트를 추출하는 다양한 시나리오에서 PDF 문서에서 강조된 텍스트만 추출해야 할 요구사항이 있을 수 있습니다. 이 기능을 구현하기 위해 API에 TextMarkupAnnotation.GetMarkedText() 및 TextMarkupAnnotation.GetMarkedTextFragments() 메서드를 추가했습니다. TextMarkupAnnotation을 필터링하고 언급된 메서드를 사용하여 PDF 문서에서 강조된 텍스트를 추출할 수 있습니다. 다음 코드 스니펫은 PDF 문서에서 강조된 텍스트를 추출하는 방법을 보여줍니다.

```java
public static void ExtractHighlightedText() {
        Document doc = new Document(_dataDir + "ExtractHighlightedText.pdf");
        // 모든 주석을 반복
        for (Annotation annotation : doc.getPages().get_Item(1).getAnnotations()) {
            // TextMarkupAnnotation 필터링
            if (annotation.getAnnotationType() == AnnotationType.Highlight) {
                HighlightAnnotation highlightedAnnotation = (HighlightAnnotation) annotation;
                // 강조된 텍스트 조각 가져오기
                TextFragmentCollection collection = highlightedAnnotation.getMarkedTextFragments();
                for (TextFragment tf : collection) {
                    // 강조된 텍스트 표시
                    System.out.println(tf.getText());
                }
            }
        }
    }
```


## XML에서 텍스트 조각 및 세그먼트 요소에 접근하기

때때로 XML로 생성된 PDF 문서를 처리할 때 TextFragement 또는 TextSegment 항목에 접근해야 할 때가 있습니다. Aspose.PDF for Android via Java는 이러한 항목에 이름으로 접근할 수 있는 기능을 제공합니다. 아래 코드 스니펫은 이 기능을 사용하는 방법을 보여줍니다.

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