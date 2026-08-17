---
title: 다중 열 PDF에서 텍스트 추출 개선
linktitle: 다중 열 PDF에서 텍스트 추출
type: docs
weight: 30
url: /java/text-extraction-from-multi-column-pdf/
description: Java용 Aspose.PDF를 사용하여 다중 열 PDF 레이아웃에서 텍스트 추출을 개선하는 기술을 알아보세요.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

다중 열 레이아웃에는 읽기 순서와 추출 품질을 향상시키기 위해 추가 처리가 필요한 경우가 많습니다.


## 
글꼴 크기를 줄인 후 텍스트 추출



이 기술은 텍스트 조각 글꼴 크기를 업데이트하고 조정된 문서를 메모리에 저장한 다음 변환된 결과에서 텍스트를 추출합니다.


1. 
[문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
[TextFragmentAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragmentabsorber/)를 만들고 모든 문서 페이지를 방문하여 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) 개체를 수집하세요.

1. 
조각을 반복하고 요청된 비율만큼 각 글꼴 크기를 줄여 추출 전에 조밀한 열 레이아웃을 정규화할 수 있습니다.

1. 
조정된 [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 메모리 내 바이트 스트림에 저장합니다.

1. 
해당 메모리 버퍼에서 두 번째 [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)를 다시 엽니다.

1. 
[TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/)를 생성하고 변환된 문서의 모든 페이지를 방문하여 추출된 텍스트를 출력 파일에 씁니다.


```java
public static void extractTextReduceFont(Path inputFile, Path outputFile, double reduceRatio) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber fragmentAbsorber = new TextFragmentAbsorber();
        document.getPages().accept(fragmentAbsorber);
        for (TextFragment fragment : fragmentAbsorber.getTextFragments()) {
            fragment.getTextState().setFontSize((float) (fragment.getTextState().getFontSize() * reduceRatio));
        }

        ByteArrayOutputStream stream = new ByteArrayOutputStream();
        document.save(stream);
        try (Document document2 = new Document(new ByteArrayInputStream(stream.toByteArray()))) {
            TextAbsorber textAbsorber = new TextAbsorber();
            document2.getPages().accept(textAbsorber);
            Files.writeString(outputFile, textAbsorber.getText());
        }
    }
}
```

## 
축척 비율을 사용하여 텍스트 추출



순수 서식 모드에서 `TextExtractionOptions`을 사용하고 열이 많은 레이아웃의 배율을 조정하세요.


1. 
[문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 인스턴스에서 소스 PDF를 엽니다.

1. 
전체 문서 추출을 위해 [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/)를 만듭니다.

1. 
레이아웃에 맞는 추출 동작이 사용되도록 순수 서식 모드에서 [TextExtractionOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/textextractionoptions/)를 만듭니다.

1. 
페이지를 방문하기 전에 스케일 팩터를 설정하고 흡수체에 추출 옵션을 적용하십시오.

1. 
모든 문서 페이지를 방문하고 추출된 텍스트를 출력 파일에 씁니다.

```java
public static void extractTextScaleFactor(Path inputFile, Path outputFile, double scaleFactor) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber textAbsorber = new TextAbsorber();
        TextExtractionOptions extractionOptions =
                new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
        extractionOptions.setScaleFactor(scaleFactor);
        textAbsorber.setExtractionOptions(extractionOptions);
        document.getPages().accept(textAbsorber);
        Files.writeString(outputFile, textAbsorber.getText());
    }
}
```
