---
title: PDF 문서의 페이지에서 텍스트 검색 및 가져오기
linktitle: 검색 및 텍스트 가져오기
type: docs
weight: 60
url: /ko/java/search-and-get-text-from-pdf/
description: 이 문서는 PDF 문서에서 텍스트를 검색하고 가져오는 다양한 도구 사용 방법을 설명합니다. 특정 페이지나 전체 페이지에서 정규 표현식을 사용하여 검색할 수 있습니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF 문서의 모든 페이지에서 텍스트 검색 및 가져오기

TextFragmentAbsorber를 사용하여 PDF 문서의 모든 페이지에서 특정 구문과 일치하는 텍스트를 찾을 수 있습니다.

문서 전체에서 텍스트를 검색하려면 [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 컬렉션의 accept() 메서드를 호출하십시오.
 [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) 메서드는 TextFragmentAbsorber 객체를 매개변수로 받아 TextFragment 객체의 컬렉션을 반환합니다. 모든 조각을 순회하여 예를 들어 Text, Position, XIndent, YIndent, FontName, FontSize, IsAccessible, IsEmbedded, IsSubset, ForegroundColor 등의 속성을 가져옵니다.

다음 코드 스니펫은 전체 문서를 검색하고 콘솔에 모든 일치를 표시하는 방법을 보여줍니다.

```java
// 문서 열기
Document pdfDocument = new Document("input.pdf");

// 입력 검색 구문의 모든 인스턴스를 찾기 위해 TextAbsorber 객체 생성
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("sample");

// 모든 페이지에 대해 흡수기 허용
pdfDocument.getPages().accept(textFragmentAbsorber);

// 추출된 텍스트 조각을 컬렉션으로 가져오기
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

// 조각을 순회
for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
    System.out.println("Text :- " + textFragment.getText());
    System.out.println("Position :- " + textFragment.getPosition());
    System.out.println("XIndent :- " + textFragment.getPosition().getXIndent());
    System.out.println("YIndent :- " + textFragment.getPosition().getYIndent());
    System.out.println("Font - Name :- " + textFragment.getTextState().getFont().getFontName());
    System.out.println("Font - IsAccessible :- " + textFragment.getTextState().getFont().isAccessible());
    System.out.println("Font - IsEmbedded - " + textFragment.getTextState().getFont().isEmbedded());
    System.out.println("Font - IsSubset :- " + textFragment.getTextState().getFont().isSubset());
    System.out.println("Font Size :- " + textFragment.getTextState().getFontSize());
    System.out.println("Foreground Color :- " + textFragment.getTextState().getForegroundColor());
}
```

특정 페이지에서 텍스트를 검색하고 관련 속성을 가져오려면 페이지 인덱스를 제공합니다:

```java
// 문서의 첫 번째 페이지에 대해 흡수기를 수락
pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber);
```

## PDF 페이지에서 텍스트 세그먼트 검색 및 가져오기

문서의 모든 페이지에서 텍스트 세그먼트를 검색하려면 문서의 TextFragment 객체를 가져옵니다.

TextFragmentAbsorber는 PDF 문서의 모든 페이지에서 특정 구문과 일치하는 텍스트를 찾을 수 있게 해줍니다. 문서 전체에서 텍스트를 검색하려면 [Pages](https://reference.aspose.com/pdf//java/com.aspose.pdf/pagecollection) 컬렉션의 [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) 메서드를 호출하세요. [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) 메서드는 TextFragmentAbsorber 객체를 매개변수로 받아서 TextFragment 객체의 컬렉션을 반환합니다.

{{% alert color="primary" %}}

문서에서 TextFragmentCollection 컬렉션을 가져오면, 각 TextFragment 객체의 TextSegmentCollection 컬렉션을 얻기 위해 이를 반복합니다.
 그 후, 개별 TextSegment 객체의 속성을 가져올 수 있습니다.

{{% /alert %}}

다음 코드 스니펫은 모든 페이지에서 텍스트 세그먼트를 검색하는 방법을 보여줍니다.

```java
// 문서 열기
Document pdfDocument = new Document("input.pdf");

// 입력 검색어의 모든 인스턴스를 찾기 위한 TextAbsorber 객체 생성
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("sample");

// 문서의 첫 번째 페이지에 흡수기 적용
pdfDocument.getPages().accept(textFragmentAbsorber);

// 추출된 텍스트 조각을 컬렉션에 가져오기
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

// 텍스트 조각을 반복 처리
for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
    // 텍스트 세그먼트를 반복 처리
    for (TextSegment textSegment : (Iterable<TextSegment>) textFragment.getSegments()) {
        System.out.println("텍스트 :- " + textSegment.getText());
        System.out.println("위치 :- " + textSegment.getPosition());
        System.out.println("XIndent :- " + textSegment.getPosition().getXIndent());
        System.out.println("YIndent :- " + textSegment.getPosition().getYIndent());
        System.out.println("글꼴 - 이름 :- " + textSegment.getTextState().getFont().getFontName());
        System.out.println("글꼴 - 접근 가능 여부 :- " + textSegment.getTextState().getFont().isAccessible());
        System.out.println("글꼴 - 포함 여부 - " + textSegment.getTextState().getFont().isEmbedded());
        System.out.println("글꼴 - 서브셋 여부 :- " + textSegment.getTextState().getFont().isSubset());
        System.out.println("글꼴 크기 :- " + textSegment.getTextState().getFontSize());
        System.out.println("전경색 :- " + textSegment.getTextState().getForegroundColor());
    }
}
```

특정 텍스트 세그먼트를 검색하고 관련 속성을 얻으려면 검색하려는 페이지의 페이지 인덱스를 지정하십시오:

```java
// 문서의 첫 번째 페이지에 대한 흡수기를 허용합니다.
pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber);
```

## 정규 표현식을 사용하여 페이지에서 텍스트 검색 및 가져오기

TextFragmentAbsorber는 정규 표현식을 기반으로 문서의 모든 페이지에서 텍스트를 검색하고 검색할 수 있도록 도와줍니다.

문서에서 텍스트를 검색하고 가져오려면:

1. 검색어를 정규 표현식으로 TextFragmentAbsorber 생성자에 전달합니다.
1. TextFragmentAbsorber 객체의 TextSearchOptions 속성을 설정합니다.
   이 속성은 TextSearchOptions 객체를 필요로 하며, 새 객체를 생성할 때 생성자에 true를 전달합니다.
1. 모든 페이지에서 일치하는 텍스트를 검색하려면 [Pages](https://reference.aspose.com/pdf//java/com.aspose.pdf/pagecollection) 컬렉션의 [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) 메서드를 호출합니다.

   TextFragmentAbsorber는 정규 표현식에 의해 지정된 기준과 일치하는 모든 조각을 포함하는 TextFragmentCollection을 반환합니다.

다음 코드 스니펫은 문서의 모든 페이지를 검색하고 정규 표현식을 기반으로 텍스트를 가져오는 방법을 보여줍니다.

```java
// 문서 열기
Document pdfDocument = new Document("source.pdf");

// 입력 검색 구문의 모든 인스턴스를 찾기 위해 TextAbsorber 객체 생성
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // 예: 1999-2000

// 정규 표현식 사용을 지정하기 위해 텍스트 검색 옵션 설정
TextSearchOptions textSearchOptions = new TextSearchOptions(true);
textFragmentAbsorber.setTextSearchOptions(textSearchOptions);

// 문서의 첫 번째 페이지에 대한 흡수기 승인
pdfDocument.getPages().accept(textFragmentAbsorber);

// 추출된 텍스트 조각을 컬렉션에 가져오기
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

// 조각을 반복
for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
    System.out.println("텍스트 :- " + textFragment.getText());
    System.out.println("위치 :- " + textFragment.getPosition());
    System.out.println("X 들여쓰기 :- " + textFragment.getPosition().getXIndent());
    System.out.println("Y 들여쓰기 :- " + textFragment.getPosition().getYIndent());
    System.out.println("글꼴 - 이름 :- " + textFragment.getTextState().getFont().getFontName());
    System.out.println("글꼴 - 접근 가능 여부 :- " + textFragment.getTextState().getFont().isAccessible());
    System.out.println("글꼴 - 임베디드 여부 - " + textFragment.getTextState().getFont().isEmbedded());
    System.out.println("글꼴 - 하위 집합 여부 :- " + textFragment.getTextState().getFont().isSubset());
    System.out.println("글꼴 크기 :- " + textFragment.getTextState().getFontSize());
    System.out.println("전경색 :- " + textFragment.getTextState().getForegroundColor());
}
```


특정 페이지에서 텍스트를 검색하고 해당 속성을 가져오려면 페이지 인덱스를 지정하십시오:

```java
// 문서의 첫 번째 페이지에 흡수기를 적용합니다.
pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber)
```

대소문자 구분 없이 문자열을 검색하려면 정규 표현식을 사용하는 것을 고려할 수 있습니다.

```java
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("(?i)Line", new TextSearchOptions(true));
```

예:

```java
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("[\\S]+");
```