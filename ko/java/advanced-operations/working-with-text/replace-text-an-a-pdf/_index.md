---
title: PDF의 텍스트를 Java로 바꾸기
linktitle: PDF에서 텍스트 바꾸기
type: docs
weight: 40
url: /java/replace-text-in-pdf/
description: Java를 사용하여 PDF 문서의 텍스트를 바꾸고, 재배열하고, 제거하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF의 텍스트 내용 바꾸기, 제거 및 조정
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서의 텍스트 교체 작업 과정을 설명합니다. 모든 페이지의 텍스트 바꾸기, 선택한 영역으로 바꾸기 제한, 바꾸기 레이아웃 조정, 정규식 기반 일치 사용, 글꼴 바꾸기, 모든 텍스트 제거 및 숨겨진 텍스트 삭제를 다룹니다.
---
Aspose.PDF for Java는 `TextFragmentAbsorber` 및 교체 옵션을 통해 간단한 교체 기능과 레이아웃 인식 교체 기능을 모두 제공합니다.


## 
모든 페이지의 텍스트 바꾸기



문서 전체에서 동일한 문구를 교체해야 하는 경우 이 예를 사용하세요.


1. 
소스 PDF 문서를 엽니다.

1. 
`TextFragmentAbsorber`을 사용하여 모든 페이지에서 대상 문구를 검색하세요.
1. 일치하는 텍스트를 바꾸고 업데이트된 PDF를 저장합니다.


```java
public static void replaceTextOnAllPages(Path inputFile, Path outputFile) {
        String searchPhrase = "PDF";
        String replacePhrase = "pdf";

        try (Document document = new Document(inputFile.toString())) {
            TextFragmentAbsorber absorber = new TextFragmentAbsorber(searchPhrase);
            document.getPages().accept(absorber);

            for (TextFragment fragment : absorber.getTextFragments()) {
                fragment.setText(replacePhrase);
            }

            document.save(outputFile.toString());
        }
    }
```

## 
특정 페이지 영역의 텍스트 바꾸기



한 페이지에서 선택한 직사각형으로 교체를 제한해야 하는 경우 이 예를 사용하십시오.


1. 
소스 PDF 문서를 엽니다.

1. 
페이지 경계와 대상 직사각형을 사용하여 `TextSearchOptions`을 구성합니다.
1. 해당 영역 내에서 일치하는 텍스트를 바꾸고 문서를 저장합니다.


```java
public static void replaceTextInParticularPageRegion(Path inputFile, Path outputFile) {
    String searchPhrase = "doc";
    String replacePhrase = "DOC";

    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(searchPhrase);
        absorber.getTextSearchOptions().setLimitToPageBounds(true);
        absorber.getTextSearchOptions().setRectangle(new Rectangle(300, 442, 500, 742, true));
        document.getPages().get_Item(1).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            fragment.setText(replacePhrase);
        }

        document.save(outputFile.toString());
    }
}
```

## 
텍스트를 바꾸고 이동된 직사각형 내부의 간격을 조정합니다.



대체 텍스트가 조정된 간격으로 페이지에 유지되어야 하지만 글꼴 크기는 변경되지 않은 상태로 유지되어야 하는 경우 이 예를 사용하십시오.


1. 
소스 PDF를 열고 대상 페이지에서 텍스트 조각을 수집합니다.

1. 
대체 직사각형을 수정하고 `AdjustSpaceWidth` 동작을 선택합니다.
1. 새 텍스트를 설정하고 문서를 저장합니다.


```java
public static void replaceTextAndResizeAndShiftWithoutChangingFontSize(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        TextFragment fragment = absorber.getTextFragments().get_Item(1);
        String text = fragment.getText();
        Rectangle rectangle = fragment.getRectangle();
        rectangle.setLLX(rectangle.getLLX() + 50);
        rectangle.setURX(rectangle.getURX() - 50);
        fragment.getReplaceOptions().setRectangle(rectangle);
        fragment.getReplaceOptions().setReplaceAdjustmentAction(TextReplaceOptions.ReplaceAdjustment.AdjustSpaceWidth);
        fragment.setText(text + " " + text);

        document.save(outputFile.toString());
    }
}
```

## 
더 큰 단락 직사각형 내부의 텍스트 바꾸기



대체 텍스트를 더 큰 페이지 영역으로 확장해야 하는 경우 이 예를 사용하십시오.


1. 
소스 PDF를 열고 대상 페이지에서 첫 번째 텍스트 조각을 가져옵니다.

1. 
페이지 미디어 상자에서 더 큰 대체 직사각형을 만듭니다.
1. 교체 옵션을 적용하고 PDF를 저장합니다.


```java
public static void replaceTextAndResizeAndShiftParagraph(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        TextFragment fragment = absorber.getTextFragments().get_Item(1);
        String text = fragment.getText();
        Rectangle rectangle = document.getPages().get_Item(1).getMediaBox();
        rectangle.setLLX(rectangle.getLLX() + 20);
        rectangle.setURX(rectangle.getURX() - 20);
        rectangle.setURY(rectangle.getURY() - 20);
        fragment.getReplaceOptions().setRectangle(rectangle);
        fragment.getReplaceOptions().setReplaceAdjustmentAction(TextReplaceOptions.ReplaceAdjustment.AdjustSpaceWidth);
        fragment.setText(text + " " + text);

        document.save(outputFile.toString());
    }
}
```

## 
텍스트를 바꾸고 글꼴 크기를 조정하여 사각형을 채웁니다.



대체 텍스트를 확대하여 대상 영역을 채워야 하는 경우 이 예를 사용하십시오.


1. 
소스 PDF를 열고 대상 텍스트 조각에 액세스합니다.

1. 
대체 직사각형을 정의하고 `ScaleToFill` 글꼴 조정을 활성화합니다.
1. 새 텍스트를 설정하고 업데이트된 문서를 저장합니다.


```java
public static void replaceTextAndResizeAndExpandFont(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        TextFragment fragment = absorber.getTextFragments().get_Item(1);
        String text = fragment.getText();
        fragment.getReplaceOptions().setRectangle(new Rectangle(100, 300, 512, 692, true));
        fragment.getReplaceOptions().setReplaceAdjustmentAction(TextReplaceOptions.ReplaceAdjustment.AdjustSpaceWidth);
        fragment.getReplaceOptions().setFontSizeAdjustmentAction(TextReplaceOptions.FontSizeAdjustment.ScaleToFill);
        fragment.setText(text + " " + text);

        document.save(outputFile.toString());
    }
}
```

## 
텍스트를 교체하고 크기에 맞게 축소



대체 텍스트가 원래 텍스트 직사각형 안에 있어야 하는 경우 이 예를 사용하십시오.


1. 
소스 PDF를 열고 대상 조각을 선택합니다.

1. 
현재 조각 직사각형을 재사용하고 `ShrinkToFit`을 활성화합니다.
1. 텍스트를 바꾸고 문서를 저장합니다.


```java
public static void replaceTextAndFitTextIntoRectangle(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        TextFragment fragment = absorber.getTextFragments().get_Item(1);
        String text = fragment.getText();
        fragment.getReplaceOptions().setRectangle(fragment.getRectangle());
        fragment.getReplaceOptions().setFontSizeAdjustmentAction(TextReplaceOptions.FontSizeAdjustment.ShrinkToFit);
        fragment.getReplaceOptions().setReplaceAdjustmentAction(TextReplaceOptions.ReplaceAdjustment.AdjustSpaceWidth);
        fragment.setText(text + " " + text);

        document.save(outputFile.toString());
    }
}
```

## 
정규식으로 텍스트 바꾸기



일치하는 텍스트를 정규식 패턴으로 찾아 교체하는 동안 스타일을 변경해야 하는 경우 이 예를 사용하세요.


1. 
소스 PDF 문서를 엽니다.

1. 
정규식이 활성화된 `TextFragmentAbsorber`을 사용하여 페이지를 검색하세요.
1. 각 일치 항목을 바꾸고 텍스트 스타일을 업데이트한 후 결과를 저장합니다.


```java
public static void replaceTextBasedOnRegex(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(Pattern.compile("\\d{4}-\\d{4}"));
        absorber.setTextSearchOptions(new TextSearchOptions(true));
        document.getPages().get_Item(1).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            fragment.setText("ABC1-2XZY");
            fragment.getTextState().setFont(FontRepository.findFont("Verdana"));
            fragment.getTextState().setFontSize(12);
            fragment.getTextState().setForegroundColor(Color.getBlue());
            fragment.getTextState().setBackgroundColor(Color.getLightGreen());
        }

        document.save(outputFile.toString());
    }
}
```

## 
자리표시자 텍스트를 교체하고 페이지를 다시 정렬하세요.



페이지 레이아웃을 유지하면서 자리 표시자를 더 긴 실제 값으로 바꿔야 하는 경우 이 예를 사용하십시오.


1. 
소스 PDF를 열고 자리 표시자 텍스트를 검색합니다.

1. 
대체 텍스트를 할당하고 글꼴 설정을 업데이트합니다.
1. 레이아웃이 다시 계산되도록 문서를 저장합니다.


```java
public static void automaticallyRearrangePageContents(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("[Long_placeholder_Long_placeholder]");
        document.getPages().accept(absorber);

        for (TextFragment textFragment : absorber.getTextFragments()) {
            textFragment.setText("John Smith, South Development Studio");
            textFragment.getTextState().setFont(FontRepository.findFont("Calibri"));
            textFragment.getTextState().setFontSize(12);
            textFragment.getTextState().setForegroundColor(Color.getNavy());
        }

        document.save(outputFile.toString());
    }
}
```

## 
한 글꼴을 다른 글꼴로 바꾸기



특정 포함 글꼴을 사용하는 텍스트를 다른 글꼴로 전환해야 하는 경우 이 예를 사용하십시오.


1. 
원본 PDF를 열고 모든 텍스트 조각을 수집합니다.

1. 
각 조각의 글꼴 이름을 확인하고 대상 글꼴을 교체하십시오.
1. 업데이트된 PDF를 저장합니다.


```java
public static void replaceFonts(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        document.getPages().accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            if ("Arial-BoldMT".equals(fragment.getTextState().getFont().getFontName())) {
                fragment.getTextState().setFont(FontRepository.findFont("Verdana"));
            }
        }

        document.save(outputFile.toString());
    }
}
```

## 
글꼴 교체 및 사용하지 않는 글꼴 리소스 제거



글꼴 교체 후 문서를 정리해야 하는 경우 이 예를 사용하십시오.


1. 
소스 PDF를 열고 `TextEditOptions`을 구성하여 사용하지 않는 글꼴을 제거합니다.

1. 
텍스트 조각을 흡수하고 대체 글꼴을 할당합니다.
1. 최적화된 문서를 저장합니다.


```java
public static void removeUnusedFonts(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextEditOptions options = new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts);
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(options);
        document.getPages().accept(absorber);

        for (TextFragment textFragment : absorber.getTextFragments()) {
            textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        }

        document.save(outputFile.toString());
    }
}
```

## 
문서에서 모든 텍스트 제거



모든 페이지에서 모든 텍스트 콘텐츠를 삭제해야 하는 경우 이 예를 사용하세요.


1. 
소스 PDF 문서를 엽니다.

1. 
`TextFragmentAbsorber`을 만들고 `removeAllText(document)`으로 전화하세요.
1. 정리된 PDF를 저장합니다.


```java
public static void removeAllTextUsingAbsorber1(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.removeAllText(document);
        document.save(outputFile.toString());
    }
}
```

## 
한 페이지에서 모든 텍스트 제거



특정 페이지에서만 모든 텍스트를 제거해야 하는 경우 이 예를 사용하세요.


1. 
소스 PDF 문서를 엽니다.

1. 
`TextFragmentAbsorber`을 만들고 대상 페이지에서 텍스트를 제거합니다.
1. 업데이트된 문서를 저장합니다.


```java
public static void removeAllTextUsingAbsorber2(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.removeAllText(document.getPages().get_Item(1));
        document.save(outputFile.toString());
    }
}
```

## 
선택한 직사각형에서 텍스트 제거



선택한 페이지 영역 내에서만 텍스트를 삭제해야 하는 경우 이 예를 사용하세요.


1. 
소스 PDF 문서를 엽니다.

1. 
`TextFragmentAbsorber`을 생성하고 정리할 직사각형을 정의합니다.
1. 해당 영역에서 텍스트를 제거하고 문서를 저장합니다.


```java
public static void removeAllTextUsingAbsorber3(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.removeAllText(document.getPages().get_Item(1), new Rectangle(10, 200, 120, 600, true));
        document.save(outputFile.toString());
    }
}
```

## 
숨겨진 텍스트 제거



PDF에서 보이지 않는 텍스트 조각을 제거해야 하는 경우 이 예를 사용하십시오.


1. 
원본 PDF를 열고 모든 텍스트 조각을 흡수하십시오.

1. 
보이지 않는 텍스트 상태에 대해 각 조각을 확인하십시오.
1. 숨겨진 텍스트를 지우고 문서를 저장하세요.

```java
public static void removeHiddenText(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textAbsorber = new TextFragmentAbsorber();
        textAbsorber.setTextReplaceOptions(new TextReplaceOptions(TextReplaceOptions.ReplaceAdjustment.None));
        document.getPages().accept(textAbsorber);

        for (TextFragment fragment : textAbsorber.getTextFragments()) {
            if (fragment.getTextState().isInvisible()) {
                fragment.setText("");
            }
        }

        document.save(outputFile.toString());
    }
}
```
