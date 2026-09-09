---
title: Java에서 PDF 텍스트 검색 및 추출
linktitle: 검색 및 텍스트 가져오기
type: docs
weight: 60
url: /java/search-and-get-text-from-pdf/
description: Java로 PDF 문서에서 텍스트를 검색, 검사 및 추출하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF 텍스트 검색 및 Java에서 추출된 조각 검사
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서에서 텍스트를 검색하고 추출하는 방법을 설명합니다. 지역 기반 추출, 페이지별 검색, 정규식 및 구문 일치, 하이퍼링크 삽입, 스타일 텍스트 검사 및 조각 강조 표시를 포함하여 TextAbsorber 및 TextFragmentAbsorber를 다룹니다.
---
Aspose.PDF for Java는 좌표, 스타일 및 정규식 일치를 통해 원시 텍스트 추출 및 조각 수준 검색을 지원합니다.


## 
TextAbsorber를 사용하여 모든 페이지에서 텍스트 추출



모든 페이지에 걸쳐 선택한 문서 영역에서 일반 추출된 텍스트가 필요한 경우 이 예를 사용하십시오.


1. 
소스 PDF 문서를 엽니다.

1. 
`TextExtractionOptions` 및 지역 기반 `TextSearchOptions`을 만듭니다.
1. 모든 페이지에 `TextAbsorber`을 실행하고 추출된 텍스트를 출력합니다.


```java
public static void textAbsorberSearch(Path inputFile) {
        try (Document document = new Document(inputFile.toString())) {
            TextExtractionOptions textExtractionOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
            TextSearchOptions textSearchOptions = new TextSearchOptions(new Rectangle(0, 0, 842, 250, true));
            TextAbsorber absorber = new TextAbsorber(textExtractionOptions, textSearchOptions);

            document.getPages().accept(absorber);
            System.out.println("Text fragments found: " + absorber.getText());
        }
    }
```

## 
TextAbsorber를 사용하여 한 페이지에서 텍스트 추출



일반 텍스트 추출을 한 페이지로 제한해야 하는 경우 이 예를 사용하십시오.


1. 
소스 PDF 문서를 엽니다.

1. 
대상 지역으로 텍스트 추출 및 검색 옵션을 구성합니다.
1. 선택한 페이지에서 `TextAbsorber`을 실행하고 결과를 출력합니다.


```java
public static void textAbsorberSearchPage(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextExtractionOptions textExtractionOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
        TextSearchOptions textSearchOptions = new TextSearchOptions(new Rectangle(0, 0, 842, 250, true));
        TextAbsorber absorber = new TextAbsorber(textExtractionOptions, textSearchOptions);

        document.getPages().get_Item(2).accept(absorber);
        System.out.println("Text fragments found: " + absorber.getText());
    }
}
```

## 
문서의 모든 텍스트 조각을 검사하세요.



글꼴, 위치, 색상 메타데이터와 함께 텍스트 콘텐츠가 필요한 경우 이 예를 사용하세요.


1. 
소스 PDF 문서를 엽니다.

1. 
모든 페이지에서 `TextFragmentAbsorber`을 실행하세요.
1. 조각을 반복하고 해당 메타데이터를 출력합니다.


```java
public static void textFragmentAbsorberSearch(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        document.getPages().accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            System.out.println("Text: " + fragment.getText());
            System.out.println("Position: " + fragment.getPosition());
            System.out.println("XIndent: " + fragment.getPosition().getXIndent());
            System.out.println("YIndent: " + fragment.getPosition().getYIndent());
            System.out.println("Font - Name: " + fragment.getTextState().getFont().getFontName());
            System.out.println("Font - IsAccessible: " + fragment.getTextState().getFont().isAccessible());
            System.out.println("Font - IsEmbedded: " + fragment.getTextState().getFont().isEmbedded());
            System.out.println("Font - IsSubset: " + fragment.getTextState().getFont().isSubset());
            System.out.println("Font Size: " + fragment.getTextState().getFontSize());
            System.out.println("Foreground Color: " + fragment.getTextState().getForegroundColor());
        }
    }
}
```

## 
특정 페이지에서 하나의 구문 검색



선택한 페이지에서만 대상 단어를 찾아야 하는 경우 이 예를 사용하세요.


1. 
소스 PDF 문서를 엽니다.

1. 
타겟 문구로 `TextFragmentAbsorber`을 생성합니다.
1. 선택한 페이지를 방문하여 일치하는 조각 위치를 출력하세요.


```java
public static void textFragmentAbsorberSearchPage(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("whale");
        document.getPages().get_Item(2).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            System.out.println("Text: " + fragment.getText());
            System.out.println("Position: " + fragment.getPosition());
        }
    }
}
```

## 
여러 페이지에서 순차적 검색 계속



한 페이지 검색에서 다음 페이지 검색으로 이동하는 동안 하나의 흡수체를 재사용하려는 경우 이 예를 사용하십시오.


1. 
원본 PDF 문서를 열고 재사용 가능한 흡수체를 만듭니다.

1. 
첫 번째 페이지를 검색하고 결과를 살펴보세요.
1. 계속해서 추가 페이지를 검색하고 업데이트된 일치 항목을 검토하세요.


```java
public static void textFragmentAbsorberSequentialSearch(Path inputFile) {
    Document document = new Document(inputFile.toString());
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    absorber.setPhrase("whale");

    document.getPages().get_Item(1).accept(absorber);
    for (TextFragment fragment : absorber.getTextFragments()) {
        System.out.println("Text: " + fragment.getText());
        System.out.println("Page: " + fragment.getPage().getNumber());
        System.out.println("Position: " + fragment.getPosition());
    }

    System.out.println("--");

    document.getPages().get_Item(2).accept(absorber);
    absorber.visit(document);

    for (TextFragment fragment : absorber.getTextFragments()) {
        System.out.println("Text: " + fragment.getText());
        System.out.println("Page: " + fragment.getPage().getNumber());
        System.out.println("Position: " + fragment.getPosition());
    }
}
```

## 
선택한 직사각형 안의 문구 검색



구문 검색을 한 페이지의 특정 지역으로 제한해야 하는 경우 이 예를 사용하세요.


1. 
소스 PDF 문서를 엽니다.

1. 
타겟 구문과 직사각형 기반의 `TextSearchOptions`을 사용하여 `TextFragmentAbsorber`을 생성합니다.
1. 페이지를 방문하여 일치하는 조각 위치를 출력하세요.


```java
public static void textFragmentAbsorberSearchPhrase(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(
                "elephant", new TextSearchOptions(new Rectangle(0, 0, 842, 250, true)));

        document.getPages().get_Item(2).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            System.out.println("Text: " + fragment.getText());
            System.out.println("Position: " + fragment.getPosition());
        }
    }
}
```

## 
정규식으로 텍스트 검색



고정 문구 대신 정규식 패턴으로 일치 항목을 찾아야 하는 경우 이 예를 사용하세요.


1. 
소스 PDF 문서를 엽니다.

1. 
정규식이 활성화된 `TextFragmentAbsorber`을 만듭니다.
1. 대상 페이지를 방문하여 일치하는 조각을 출력합니다.


```java
public static void textFragmentAbsorberSearchRegex(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(
                Pattern.compile("\\d+\\.\\d+"), new TextSearchOptions(true));

        document.getPages().get_Item(2).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            System.out.println("Text: " + fragment.getText());
            System.out.println("Position: " + fragment.getPosition());
        }
    }
}
```

## 
정규식 패턴으로 구문 목록 검색



한 번에 여러 대상 문구를 찾아야 하는 경우 이 예를 사용하세요.


1. 
소스 PDF 문서를 엽니다.

1. 
정규식 패턴 배열을 만들어 `TextFragmentAbsorber`에 전달합니다.
1. 문서를 방문하여 그룹화된 정규식 결과를 검사하세요.


```java
public static void textFragmentAbsorberSearchListOfPhrases(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Pattern[] patterns = new Pattern[] {
                Pattern.compile("whale"),
                Pattern.compile("elephant")
        };
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(patterns, new TextSearchOptions(true));
        document.getPages().accept(absorber);

        for (TextFragmentCollection fragments : absorber.getRegexResults().values()) {
            for (TextFragment fragment : fragments) {
                System.out.println("Text: " + fragment.getText());
                System.out.println("Position: " + fragment.getPosition());
            }
        }
    }
}
```

## 
텍스트를 찾아 하이퍼링크로 변환



일치하는 단어를 강조 표시하고 클릭 가능한 링크로 변환해야 하는 경우 이 예를 사용하세요.


1. 
소스 PDF 문서를 엽니다.

1. 
정규식 검색을 활성화하여 대상 단어를 검색합니다.
1. 텍스트 스타일을 업데이트하고, 하이퍼링크를 첨부하고, 수정된 PDF를 저장하세요.


```java
public static void textFragmentAbsorberSearchAndAddHyperlink(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("whale|elephant");
        absorber.setTextSearchOptions(new TextSearchOptions(true));
        absorber.visit(document.getPages().get_Item(1));

        for (TextFragment fragment : absorber.getTextFragments()) {
            fragment.getTextState().setForegroundColor(Color.getBlue());
            fragment.getTextState().setUnderline(true);
            fragment.setHyperlink(new WebHyperlink("https://en.wikipedia.org/wiki/" + fragment.getText()));
        }

        document.save(inputFile.toString().replace("in.pdf", "out.pdf"));
    }
}
```

## 
스타일 특성으로 텍스트 검색



굵은 텍스트나 보이지 않는 텍스트 등의 서식을 기반으로 조각을 검사해야 하는 경우 이 예를 사용하세요.


1. 
소스 PDF 문서를 엽니다.

1. 
대상 페이지에서 `TextFragmentAbsorber`을 실행합니다.
1. 각 조각 스타일을 확인하고 일치하는 항목을 출력합니다.


```java
public static void textFragmentAbsorberSearchStyledText(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.setTextSearchOptions(new TextSearchOptions(true));
        absorber.visit(document.getPages().get_Item(1));

        for (TextFragment fragment : absorber.getTextFragments()) {
            if (fragment.getTextState().getFontStyle() == FontStyles.Bold) {
                System.out.println("Bold: " + fragment.getText());
            }
            if (fragment.getTextState().isInvisible()) {
                System.out.println("Invisible: " + fragment.getText());
            }
        }
    }
}
```

## 
렌더링된 페이지 미리보기에서 검색 결과 강조 표시



시각적 검사를 위해 텍스트 일치를 렌더링된 페이지 이미지와 연관시켜야 하는 경우 이 예를 사용하십시오.


1. 
필요한 해상도로 PNG 장치를 만듭니다.

1. 
`TextFragmentAbsorber`으로 각 페이지를 검색하고 페이지를 이미지 스트림으로 렌더링합니다.
1. 검사를 위해 페이지 미리보기 이미지와 출력 조각 좌표를 작성합니다.

```java
public static void textFragmentAbsorberSearchAndHighlight(Path inputFile) throws Exception {
    int resolution = 150;
    PngDevice pngDevice = new PngDevice(new Resolution(resolution, resolution));

    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(Pattern.compile("[\\S]+"));
        absorber.setTextSearchOptions(new TextSearchOptions(true));

        for (int pageNumber = 1; pageNumber <= document.getPages().size(); pageNumber++) {
            Page page = document.getPages().get_Item(pageNumber);
            page.accept(absorber);

            try (ByteArrayOutputStream stream = new ByteArrayOutputStream()) {
                pngDevice.process(page, stream);
                Path output = Path.of(inputFile.toString().replace("_in.pdf", page.getNumber() + "_out.png"));
                Files.write(output, stream.toByteArray());
            }

            for (TextFragment textFragment : absorber.getTextFragments()) {
                Rectangle pageRect = page.getPageRect(true);
                System.out.println("TextFragment = " + textFragment.getText()
                        + " Page URY = " + pageRect.getURY()
                        + " TextFragment URY = " + textFragment.getRectangle().getURY());
            }
        }
    }
}
```
