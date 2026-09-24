---
title: Java에서 PDF에 텍스트 추가
linktitle: PDF에 텍스트 추가
type: docs
weight: 10
url: /java/add-text-to-pdf-file/
description: Java로 PDF 문서에 텍스트, HTML 조각, 목록, 링크 및 사용자 정의 글꼴을 추가하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 파일에 텍스트, 링크, HTML 및 글꼴 추가
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서에 텍스트를 추가하고 스타일을 지정하는 방법을 설명합니다. 간단한 텍스트 삽입, 단락 레이아웃, 하이퍼링크, 오른쪽에서 왼쪽으로 쓰는 텍스트, 글꼴 스타일, 투명도, 테두리, HTML 및 LaTeX 조각, 그라데이션 텍스트, 파일이나 스트림에서 로드된 사용자 정의 글꼴 등을 다룹니다.
---
Java용 Aspose.PDF는 일반 텍스트 삽입, 고급 레이아웃, 스타일, 그라디언트, HTML, LaTeX 및 사용자 정의 글꼴을 지원합니다.


## 
간단한 텍스트 조각 추가



짧은 텍스트 문자열을 고정된 페이지 좌표에 배치해야 하는 경우 이 예를 사용하십시오.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
`TextFragment`을 만들고 위치를 설정합니다.
1. 페이지에 추가하고 문서를 저장하세요.


```java
public static void addTextSimpleCase(Path outputFile) {
      try (Document document = new Document()) {
          Page page = document.getPages().add();

          TextFragment textFragment = new TextFragment("Hello, Aspose!");
          textFragment.setPosition(new Position(100, 600));

          page.getParagraphs().add(textFragment);
          document.save(outputFile.toString());
      }
  }
```

## 
직사각형 안에 단락 추가



더 큰 텍스트 블록이 경계 영역 내부에 배치되어야 하는 경우 이 예를 사용하십시오.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
소스 텍스트를 로드하고 `TextParagraph` 직사각형 및 줄 바꿈 모드를 구성합니다.
1. `TextBuilder`을 통해 조각을 추가하고 PDF를 저장합니다.


```java
public static void addParagraph(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        String text = Files.exists(loremPath)
                ? Files.readString(loremPath)
                : "Lorem ipsum sample text not found.";

        TextBuilder builder = new TextBuilder(page);
        TextParagraph paragraph = new TextParagraph();
        paragraph.setFirstLineIndent(20);
        paragraph.setRectangle(new Rectangle(80, 800, 400, 200, true));
        paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.DiscretionaryHyphenation);

        TextFragment fragment = new TextFragment(text);
        fragment.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        fragment.getTextState().setFontSize(12);

        paragraph.appendLine(fragment);
        builder.appendParagraph(paragraph);

        document.save(outputFile.toString());
    }
}
```

## 
다른 들여쓰기 설정으로 단락 추가



첫 번째 줄과 후속 줄에서 다른 들여쓰기 규칙을 사용해야 하는 경우 이 예를 사용하세요.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
공유 텍스트 조각을 준비하고 여러 `TextParagraph` 개체를 만듭니다.
1. 각 단락의 들여쓰기를 구성하고 추가한 후 문서를 저장합니다.


```java
public static void addParagraphsIndents(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        String text = Files.exists(loremPath)
                ? Files.readString(loremPath)
                : "Lorem ipsum sample text not found.";

        TextFragment fragment = new TextFragment(text);
        fragment.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        fragment.getTextState().setFontSize(12);

        TextBuilder builder = new TextBuilder(page);
        TextParagraph paragraph1 = new TextParagraph();
        paragraph1.setFirstLineIndent(20);
        paragraph1.setRectangle(new Rectangle(80, 800, 300, 50, true));
        paragraph1.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);
        paragraph1.appendLine(fragment);
        builder.appendParagraph(paragraph1);

        TextParagraph paragraph2 = new TextParagraph();
        paragraph2.setSubsequentLinesIndent(20);
        paragraph2.setRectangle(new Rectangle(320, 800, 500, 50, true));
        paragraph2.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);
        paragraph2.appendLine(fragment);
        builder.appendParagraph(paragraph2);

        document.save(outputFile.toString());
    }
}
```

## 
수동 줄 바꿈을 사용하여 텍스트 삽입



하나의 텍스트 조각에 명시적인 새 줄이 포함되어야 하는 경우 이 예를 사용하세요.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
줄 바꿈을 포함하는 `TextFragment`을 만들고 해당 스타일을 구성합니다.
1. `TextParagraph`을 통해 추가하고 PDF를 저장하세요.


```java
public static void addNewLine(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("Applicant Name: " + System.lineSeparator() + " Joe Smoe");
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment.getTextState().setForegroundColor(Color.getRed());

        TextParagraph paragraph = new TextParagraph();
        paragraph.appendLine(textFragment);
        paragraph.setPosition(new Position(100, 600));

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendParagraph(paragraph);

        document.save(outputFile.toString());
    }
}
```

## 
감지된 줄바꿈 검사



텍스트 레이아웃 및 줄 바꿈과 관련된 알림 출력을 검토해야 할 때 이 예를 사용하십시오.


1. 
새 PDF 문서를 만들고 알림 로깅을 활성화합니다.

1. 
여러 개의 긴 텍스트 조각을 페이지에 추가합니다.
1. 알림을 검사하고 문서를 저장합니다.


```java
public static void determineLineBreak(Path outputFile) {
    try (Document document = new Document()) {
        document.setEnableNotificationLogging(true);

        Page page = document.getPages().add();
        for (int i = 0; i < 4; i++) {
            TextFragment text = new TextFragment(
                    "Lorem ipsum \r\ndolor sit amet, consectetur adipiscing elit, "
                            + "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
                            + "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "
                            + "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in "
                            + "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla "
                            + "pariatur. Excepteur sint occaecat cupidatat non proident, sunt in "
                            + "culpa qui officia deserunt mollit anim id est laborum.");
            text.getTextState().setFontSize(20);
            page.getParagraphs().add(text);
        }

        System.out.println(document.getPages().get_Item(1).getNotifications());
        document.save(outputFile.toString());
    }
}
```

## 
텍스트 너비를 동적으로 측정



레이아웃 결정을 내리기 전에 문자 및 문자열 너비를 측정해야 하는 경우 이 예를 사용하십시오.


1. 
대상 글꼴을 확인하고 `TextState`을 만듭니다.

1. 
문자를 측정하고 글꼴 및 텍스트 상태 API의 결과를 비교합니다.
1. 검증을 위해 불일치를 출력합니다.


```java
public static void getTextWidthDynamically(Path outputFile) {
    Font font = FontRepository.findFont("Arial");
    TextState textState = new TextState();
    textState.setFont(font);
    textState.setFontSize(14);

    if (Math.abs(font.measureString("A", 14) - 9.337) > 0.001) {
        System.out.println("Unexpected font string measure!");
    }

    if (Math.abs(textState.measureString("z") - 7.0) > 0.001) {
        System.out.println("Unexpected font string measure!");
    }

    for (char c = 'A'; c <= 'z'; c++) {
        double fontMeasure = font.measureString(String.valueOf(c), 14);
        double textStateMeasure = textState.measureString(String.valueOf(c));
        if (Math.abs(fontMeasure - textStateMeasure) > 0.001) {
            System.out.println("Font and state string measuring doesn't match!");
        }
    }
}
```

## 
하이퍼링크 세그먼트로 텍스트 추가



텍스트 조각의 한 부분이 웹 링크로 작동해야 하는 경우 이 예를 사용하십시오.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
여러 `TextSegment` 개체를 사용하여 `TextFragment`을 빌드합니다.
1. 대상 세그먼트에 하이퍼링크와 스타일을 할당한 다음 문서를 저장합니다.


```java
public static void addTextWithHyperlink(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment fragment = new TextFragment("Sample Text Fragment");
        fragment.getSegments().add(new TextSegment(" ... Text Segment 1..."));

        TextSegment segment = new TextSegment("Link to Aspose");
        fragment.getSegments().add(segment);
        segment.setHyperlink(new WebHyperlink("https://products.aspose.com/pdf"));
        segment.getTextState().setForegroundColor(Color.getBlue());
        segment.getTextState().setFontStyle(FontStyles.Italic);

        fragment.getSegments().add(new TextSegment("TextSegment without hyperlink"));

        page.getParagraphs().add(fragment);
        document.save(outputFile.toString());
    }
}
```

## 
오른쪽에서 왼쪽으로 텍스트 추가



문서가 오른쪽에서 왼쪽으로 올바른 정렬로 스크립트 내용을 표시해야 하는 경우 이 예를 사용하십시오.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
대상 RTL 텍스트로 `TextFragment`을 만들고 해당 글꼴과 정렬을 구성합니다.
1. 페이지에 추가하고 PDF를 저장하세요.


```java
public static void addTextWithRtlText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment(
                "يعتبر خوجا نصر الدين شخصية فولكلورية من الشرق الإسلامي وبعض شعوب البحر الأبيض المتوسط ​​والبلقان، وهو بطل القصص والحكايات القصيرة الفكاهية والساخرة، وأحيانًا الحكايات اليومية.");
        textFragment.getTextState().setFont(FontRepository.findFont("Tahoma"));
        textFragment.getTextState().setFontSize(14);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.setHorizontalAlignment(HorizontalAlignment.Right);

        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## 
스타일이 지정된 텍스트 및 수식과 유사한 세그먼트 추가



일반 텍스트와 아래 첨자 형태의 세그먼트가 하나의 출력에서 서로 다른 텍스트 상태를 사용해야 하는 경우 이 예를 사용하세요.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
기본 스타일 조각을 만들고 도우미 세그먼트를 사용하여 수식을 구성합니다.
1. 페이지에 두 조각을 모두 추가하고 문서를 저장합니다.


```java
public static void addTextWithFontStyling(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment formula = new TextFragment();
        TextFragment textFragment = new TextFragment("Hello, Aspose!");
        textFragment.setPosition(new Position(100, 600));
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        textFragment.getTextState().setUnderline(true);
        textFragment.setHorizontalAlignment(HorizontalAlignment.Left);

        TextState textStateLetters = new TextState();
        textStateLetters.setFont(FontRepository.findFont("Arial"));
        textStateLetters.setFontSize(14);
        textStateLetters.setForegroundColor(Color.getBlue());
        textStateLetters.setFontStyle(FontStyles.Bold);

        TextState textStateIndex = new TextState();
        textStateIndex.setFont(FontRepository.findFont("Arial"));
        textStateIndex.setFontSize(14);
        textStateIndex.setForegroundColor(Color.getDarkRed());
        textStateIndex.setSubscript(true);

        Position position = new Position(100, 500);
        addSegment(formula, "S = a", textStateLetters, position);
        addSegment(formula, "2n", textStateIndex, position);
        addSegment(formula, " + a", textStateLetters, position);
        addSegment(formula, "2n+1", textStateIndex, position);
        addSegment(formula, " + a", textStateLetters, position);
        addSegment(formula, "2n+2", textStateIndex, position);
        formula.setHorizontalAlignment(HorizontalAlignment.Left);

        page.getParagraphs().add(textFragment);
        page.getParagraphs().add(formula);
        document.save(outputFile.toString());
    }
}

private static void addSegment(TextFragment formula, String text, TextState state, Position position) {
    TextSegment segment = new TextSegment(text);
    segment.setTextState(state);
    segment.setPosition(position);
    formula.getSegments().add(segment);
}
```

## 
밑줄 친 텍스트 추가



텍스트 조각에서 눈에 띄게 밑줄 스타일을 사용해야 하는 경우 이 예를 사용하세요.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
텍스트 조각을 만들고 글꼴과 밑줄 상태를 구성하고 위치를 설정합니다.
1. `TextBuilder`을 추가하고 결과를 저장합니다.


```java
public static void addUnderlineText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        TextBuilder textBuilder = new TextBuilder(page);

        TextFragment fragment = new TextFragment("Hello, ASPOSE.PDF!");
        fragment.getTextState().setFont(FontRepository.findFont("Arial"));
        fragment.getTextState().setFontSize(10);
        fragment.getTextState().setUnderline(true);
        fragment.setPosition(new Position(10, 800));
        textBuilder.appendText(fragment);

        document.save(outputFile.toString());
    }
}
```

## 
색상이 지정된 도형 위에 투명한 텍스트 추가



텍스트가 배경 그래픽 위에 투명하게 표시되어야 하는 경우 이 예를 사용하십시오.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
배경 모양을 그리고 반투명 텍스트 조각을 만듭니다.
1. 페이지에 두 요소를 모두 추가하고 문서를 저장합니다.


```java
public static void addTextTransparent(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        com.aspose.pdf.drawing.Graph canvas = new com.aspose.pdf.drawing.Graph(100.0, 400.0);
        com.aspose.pdf.drawing.Rectangle rectangle = new com.aspose.pdf.drawing.Rectangle(100, 100, 400, 400);
        rectangle.getGraphInfo().setFillColor(Color.fromArgb(128, 0xC5, 0xB5, 0xFF));
        canvas.getShapes().addItem(rectangle);
        canvas.setChangePosition(false);
        page.getParagraphs().add(canvas);

        TextFragment text = new TextFragment(
                "This is the transparent text. This is the transparent text. This is the transparent text.");
        text.getTextState().setForegroundColor(Color.fromArgb(30, 0, 255, 0));
        page.getParagraphs().add(text);

        document.save(outputFile.toString());
    }
}
```

## 
보이지 않는 텍스트 추가



눈에 보이는 렌더링 없이 검색 가능하거나 숨겨진 텍스트가 있어야 하는 경우 이 예를 사용하십시오.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
보이는 텍스트 조각과 보이지 않는 플래그가 활성화된 두 번째 조각을 추가합니다.
1. 문서를 저장합니다.


```java
public static void addTextInvisible(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment text1 = new TextFragment(
            "This is the visible text. This is the visible text. This is the visible text.");
        page.getParagraphs().add(text1);

        TextFragment text2 = new TextFragment(
            "This is the invisible text. This is the invisible text. This is the invisible text.");
        text2.getTextState().setInvisible(true);
        page.getParagraphs().add(text2);

        document.save(outputFile.toString());
    }
}
```

## 
직사각형 테두리가 있는 텍스트 추가



텍스트를 경계 사각형과 함께 그려야 하는 경우 이 예를 사용하십시오.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
`TextFragment` 스타일을 만들고 텍스트 직사각형 테두리 그리기를 활성화합니다.
1. `TextBuilder`을 추가하고 PDF를 저장하세요.


```java
public static void addTextBorder(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is sample text with border.");
        textFragment.setPosition(new Position(10, 700));
        textFragment.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment.getTextState().setForegroundColor(Color.getRed());
        textFragment.getTextState().setStrokingColor(Color.getDarkRed());
        textFragment.getTextState().setDrawTextRectangleBorder(true);

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendText(textFragment);

        document.save(outputFile.toString());
    }
}
```

## 
취소선 텍스트 추가



텍스트에 취소선 서식을 사용해야 하는 경우 이 예를 사용하세요.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
취소선이 활성화된 스타일이 지정된 텍스트 조각을 만듭니다.
1. 페이지에 추가하고 문서를 저장합니다.


```java
public static void addStrikeoutText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is sample strikeout text.");
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment.getTextState().setBackgroundColor(Color.getLightGray());
        textFragment.getTextState().setForegroundColor(Color.getRed());
        textFragment.getTextState().setStrikeOut(true);
        textFragment.getTextState().setFontStyle(FontStyles.Bold);
        textFragment.setPosition(new Position(100, 600));

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendText(textFragment);

        document.save(outputFile.toString());
    }
}
```

## 
텍스트에 축 그라데이션 음영 적용



텍스트가 단색 대신 선형 그라데이션 채우기를 사용해야 하는 경우 이 예를 사용하세요.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
텍스트 조각을 만들고 전경색에 축 그라데이션을 할당합니다.
1. 페이지에 추가하고 PDF를 저장하세요.


```java
public static void applyGradientAxialShadingToText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("PDF TITLE");
        textFragment.setPosition(new Position(100, 600));
        textFragment.getTextState().setFontSize(36);
        textFragment.getTextState().setFont(FontRepository.findFont("Arial Bold"));
        textFragment.getTextState().setForegroundColor(new Color());
        textFragment.getTextState().getForegroundColor()
                .setPatternColorSpace(new GradientAxialShading(Color.getRed(), Color.getBlue()));
        textFragment.getTextState().setUnderline(true);

        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## 
텍스트에 방사형 그라데이션 음영 적용



텍스트에 방사형 그래디언트 채우기를 사용해야 하는 경우 이 예를 사용하세요.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
텍스트 조각을 만들고 전경색에 방사형 그래디언트를 할당합니다.
1. 페이지에 추가하고 문서를 저장하세요.


```java
public static void applyGradientRadialShadingToText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("PDF TITLE");
        textFragment.setPosition(new Position(100, 600));
        textFragment.getTextState().setFontSize(36);
        textFragment.getTextState().setFont(FontRepository.findFont("Arial Bold"));
        textFragment.getTextState().setForegroundColor(new Color());
        textFragment.getTextState().getForegroundColor()
                .setPatternColorSpace(new GradientRadialShading(Color.getRed(), Color.getBlue()));
        textFragment.getTextState().setUnderline(true);

        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## 
인라인 HTML 스타일 형식의 텍스트 추가



HTML 마크업을 통해 위 첨자와 아래 첨자 형식을 삽입해야 하는 경우 이 예를 사용하세요.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
필요한 인라인 마크업을 사용하여 `HtmlFragment`을 만듭니다.
1. 페이지에 추가하고 PDF를 저장하세요.


```java
public static void addTextHtmlFragment(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        HtmlFragment textFragment = new HtmlFragment("<pre>S=a<sub>2n</sub>+a<sup>2</sup><pre>");
        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## 
LaTeX 텍스트 조각 추가



수학 또는 TeX 형식의 콘텐츠를 PDF 내에서 렌더링해야 하는 경우 이 예를 사용하세요.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
필수 표현식을 사용하여 `TeXFragment`을 생성합니다.
1. 페이지에 추가하고 문서를 저장하세요.


```java
public static void addTextLatexFragment(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TeXFragment textFragment = new TeXFragment(
                "\\underbrace{\\overbrace{a+b}^6 \\cdot \\overbrace{c+d}^7}_\\text{example of text} = 42");
        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## 
풍부한 HTML 조각 추가



페이지가 제목, 단락, 링크와 같은 구조화된 HTML 콘텐츠를 렌더링해야 하는 경우 이 예제를 사용하세요.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
HTML 콘텐츠 문자열을 준비하고 `HtmlFragment`을 만듭니다.
1. 페이지에 추가하고 PDF를 저장하세요.


```java
public static void addHtmlFragment(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String htmlContent = """
                <h1 style='color:blue;'>Hello, Aspose!</h1>
                <p>This is a sample paragraph with <b>bold</b>, <i>italic</i>, and <u>underlined</u> text.</p>
                <p style='color:green;'>This paragraph is green.</p>
                <a href='https://www.aspose.com' style='font-size:16px;'>Visit Aspose</a>
                """;
        HtmlFragment htmlFragment = new HtmlFragment(htmlContent);
        page.getParagraphs().add(htmlFragment);
        document.save(outputFile.toString());
    }
}
```

## 
재정의된 텍스트 상태로 HTML 조각 추가



가져온 HTML 컨텐츠가 제어된 글꼴 및 색상 설정을 상속해야 하는 경우 이 예를 사용하십시오.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
HTML 콘텐츠를 준비하고 `HtmlFragment`을 만듭니다.
1. 사용자 정의 `TextState`을 할당하고 조각을 추가한 다음 문서를 저장합니다.


```java
public static void addHtmlFragmentOverrideTextState(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String htmlContent = """
                <h1 style='color:blue;font-family:Verdana'>Hello, Aspose!</h1>
                <p>This is a sample paragraph with <b>bold</b>, <i>italic</i>, and <u>underlined</u> text.</p>
                <p style='color:green;'>This paragraph is green.</p>
                <a href='https://www.aspose.com' style='font-size:16px;'>Visit Aspose</a>
                """;
        HtmlFragment htmlFragment = new HtmlFragment(htmlContent);
        TextState textState = new TextState();
        textState.setFont(FontRepository.findFont("Arial"));
        textState.setFontSize(14);
        textState.setForegroundColor(Color.getRed());
        htmlFragment.setTextState(textState);

        page.getParagraphs().add(htmlFragment);
        document.save(outputFile.toString());
    }
}
```

## 
파일에서 로드된 사용자 정의 글꼴 사용



텍스트가 글꼴 파일 경로에서 직접 로드된 글꼴을 사용해야 하는 경우 이 예를 사용하십시오.


1. 
사용자 정의 글꼴 파일 경로를 확인합니다.

1. 
텍스트 조각을 만들고 `FontRepository.openFont`을 통해 글꼴을 로드합니다.
1. 글꼴 설정을 적용하고 문서를 저장합니다.


```java
public static void useCustomFontFromFile(Path outputFile) {
    Path fontPath = fontDir.resolve("BriosoPro Italic.otf");
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment fragment = new TextFragment("Hello, Aspose!");
        fragment.setPosition(new Position(100, 600));
        fragment.getTextState().setFont(FontRepository.openFont(fontPath.toString()));
        fragment.getTextState().setFontSize(24);
        fragment.getTextState().setForegroundColor(Color.getBlue());
        fragment.getTextState().setFontStyle(FontStyles.Italic);

        page.getParagraphs().add(fragment);
        document.save(outputFile.toString());
    }
}
```

## 
스트림에서 로드된 사용자 정의 글꼴 사용



사용자 정의 글꼴을 스트림에서 열고 PDF에 포함해야 하는 경우 이 예를 사용하십시오.


1. 
글꼴 파일을 스트림으로 열고 `FontRepository`을 사용하여 로드합니다.

1. 
텍스트 조각을 만들고 포함된 글꼴을 할당합니다.
1. 페이지에 조각을 추가하고 문서를 저장합니다.

```java
public static void useCustomFontFromStream(Path outputFile) throws Exception {
    Path fontPath = fontDir.resolve("BriosoPro Italic.otf");
    try (InputStream fontStream = Files.newInputStream(fontPath)) {
        Font font = FontRepository.openFont(fontStream, FontTypes.OTF);
        font.setEmbedded(true);

        try (Document document = new Document()) {
            Page page = document.getPages().add();

            TextFragment fragment = new TextFragment("Hello, Aspose!");
            fragment.setPosition(new Position(100, 600));
            fragment.getTextState().setFont(font);
            fragment.getTextState().setFontSize(14);
            fragment.getTextState().setForegroundColor(Color.getBlue());
            fragment.getTextState().setFontStyle(FontStyles.Italic);

            page.getParagraphs().add(fragment);
            document.save(outputFile.toString());
        }
    }
}
```
