---
title: Java에서 PDF 텍스트 형식 지정
linktitle: PDF 내부의 텍스트 서식
type: docs
weight: 70
url: /java/text-formatting-inside-pdf/
description: 간격, 메모, 목록, 다중 열 레이아웃 및 스타일 옵션을 사용하여 Java에서 PDF 문서 내의 텍스트 형식을 지정하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 파일 내 텍스트 서식 지정 및 스타일 지정
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 문서의 텍스트 형식을 지정하는 방법을 설명합니다. 줄 간격, 문자 간격, 글머리 기호 및 번호 매기기 목록, 각주 및 미주, 인라인 단락 콘텐츠, 다중 열 레이아웃, 강제 페이지 나누기 및 사용자 정의 탭 정지를 다룹니다.
---
Aspose.PDF for Java는 간격, 목록, 메모, 인라인 레이아웃 및 다중 열 구성을 위한 텍스트 서식 컨트롤을 제공합니다.


## 
간단한 줄 간격 설정



단락 텍스트에 고정된 줄 간격 값을 사용해야 하는 경우 이 예를 사용하십시오.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
원본 텍스트를 로드하거나 준비하고 `TextFragment`을 만듭니다.
1. 줄 간격을 설정하고 페이지에 조각을 추가한 후 문서를 저장합니다.


```java
public static void specifyLineSpacingSimpleCase(Path outputFile) throws Exception {
        try (Document document = new Document()) {
            Page page = document.getPages().add();

            Path loremPath = dataDir.resolve("lorem.txt");
            String text = Files.exists(loremPath) ? Files.readString(loremPath) : "Lorem ipsum text not found.";

            TextFragment textFragment = new TextFragment(text);
            textFragment.getTextState().setFontSize(12);
            textFragment.getTextState().setLineSpacing(16);
            page.getParagraphs().add(textFragment);

            document.save(outputFile.toString());
        }
    }
```

## 
줄 간격 모드를 사용자 정의 글꼴과 비교



동일한 글꼴에 대해 다양한 서식 모드를 사용하여 줄 간격을 테스트해야 하는 경우 이 예를 사용하세요.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
사용자 정의 글꼴을 로드하고 줄 간격 모드가 다른 두 조각을 준비합니다.
1. 페이지에 두 조각을 모두 추가하고 PDF를 저장합니다.


```java
public static void specifyLineSpacingSpecificCase(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Path fontFile = dataDir.resolve("HPSimplified.ttf");
        Path loremPath = dataDir.resolve("lorem.txt");
        String text = Files.exists(loremPath) ? Files.readString(loremPath) : "Lorem ipsum text not found.";

        try (InputStream fontStream = Files.newInputStream(fontFile)) {
            Font font = FontRepository.openFont(fontStream, FontTypes.TTF);

            TextFragment fragment1 = new TextFragment(text);
            fragment1.getTextState().setFont(font);
            fragment1.getTextState().setFormattingOptions(new TextFormattingOptions());
            fragment1.getTextState().getFormattingOptions().setLineSpacing(TextFormattingOptions.LineSpacingMode.FontSize);
            page.getParagraphs().add(fragment1);

            TextFragment fragment2 = new TextFragment(text);
            fragment2.getTextState().setFont(font);
            fragment2.getTextState().setFormattingOptions(new TextFormattingOptions());
            fragment2.getTextState().getFormattingOptions().setLineSpacing(TextFormattingOptions.LineSpacingMode.FullSize);
            page.getParagraphs().add(fragment2);
        }

        document.save(outputFile.toString());
    }
}
```

## 
텍스트 조각으로 문자 간격 설정



동일한 텍스트를 다른 문자 간격 값으로 표시해야 하는 경우 이 예를 사용하십시오.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
여러 간격 값에 대한 도우미 메서드를 사용하여 텍스트 조각을 만듭니다.
1. 페이지에 조각을 추가하고 문서를 저장합니다.


```java
public static void characterSpacingUsingTextFragment(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        page.getParagraphs().add(makeCharacterSpacingFragment(2.0f));
        page.getParagraphs().add(makeCharacterSpacingFragment(1.0f));
        page.getParagraphs().add(makeCharacterSpacingFragment(0.75f));

        document.save(outputFile.toString());
    }
}

private static TextFragment makeCharacterSpacingFragment(float spacing) {
    TextFragment fragment = new TextFragment("Sample Text with character spacing");
    fragment.getTextState().setFont(FontRepository.findFont("Arial"));
    fragment.getTextState().setFontSize(14);
    fragment.getTextState().setCharacterSpacing(spacing);
    return fragment;
}
```

## 
텍스트 단락 내부의 문자 간격 설정



경계가 지정된 텍스트 단락 내에 문자 간격을 적용해야 하는 경우 이 예를 사용하십시오.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
대상 직사각형과 래핑 옵션을 사용하여 `TextParagraph`을 만듭니다.
1. 스타일이 지정된 텍스트 조각을 추가하고 PDF를 저장합니다.


```java
public static void characterSpacingUsingTextParagraph(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextBuilder builder = new TextBuilder(page);
        TextParagraph paragraph = new TextParagraph();
        paragraph.setRectangle(new Rectangle(100, 700, 500, 750, true));
        paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);

        TextFragment fragment = new TextFragment("Sample Text with character spacing");
        fragment.getTextState().setFont(FontRepository.findFont("Arial"));
        fragment.getTextState().setFontSize(14);
        fragment.getTextState().setCharacterSpacing(2.0f);

        paragraph.appendLine(fragment);
        builder.appendParagraph(paragraph);
        document.save(outputFile.toString());
    }
}
```

## 
HTML로 글머리 기호 목록 만들기



HTML 마크업에서 순서가 지정되지 않은 목록 형식을 생성해야 하는 경우 이 예를 사용하십시오.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
HTML 목록 문자열을 작성합니다.
1. `HtmlFragment`으로 추가하고 문서를 저장하세요.


```java
public static void createBulletListHtmlVersion(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String htmlList = "<ul><li>First item in the list</li>"
                + "<li>Second item with more text to demonstrate wrapping behavior.</li>"
                + "<li>Third item</li><li>Fourth item</li></ul>";
        page.getParagraphs().add(new HtmlFragment(htmlList));
        document.save(outputFile.toString());
    }
}
```

## 
HTML로 번호 매기기 목록 만들기



HTML 마크업에서 순서가 지정된 목록 형식을 생성해야 하는 경우 이 예를 사용하십시오.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
순서가 지정된 HTML 목록 문자열을 작성합니다.
1. `HtmlFragment`으로 추가하고 문서를 저장하세요.


```java
public static void createNumberedListHtmlVersion(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String htmlList = "<ol><li>First item in the list</li>"
                + "<li>Second item with more text to demonstrate wrapping behavior.</li>"
                + "<li>Third item</li><li>Fourth item</li></ol>";
        page.getParagraphs().add(new HtmlFragment(htmlList));
        document.save(outputFile.toString());
    }
}
```

## 
LaTeX로 글머리 기호 목록 만들기



순서가 지정되지 않은 목록 형식을 TeX 마크업에서 렌더링해야 하는 경우 이 예를 사용하십시오.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
`itemize` 환경을 사용하여 TeX 목록 문자열을 준비합니다.
1. `TeXFragment`으로 추가하고 PDF를 저장하세요.


```java
public static void createBulletListLatexVersion(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String texList = "Lists are easy to create: \\begin{itemize}"
                + "\\item First item"
                + "\\item Second item with more text to demonstrate wrapping behavior."
                + "\\item Third item"
                + "\\item Fourth item"
                + "\\end{itemize}";
        page.getParagraphs().add(new TeXFragment(texList));
        document.save(outputFile.toString());
    }
}
```

## 
LaTeX로 번호 매기기 목록 만들기



순서가 지정된 목록 형식을 TeX 마크업에서 렌더링해야 하는 경우 이 예를 사용하세요.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
`enumerate` 환경을 사용하여 TeX 목록 문자열을 준비합니다.
1. `TeXFragment`으로 추가하고 PDF를 저장하세요.


```java
public static void createNumberedListLatexVersion(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String texList = "Lists are easy to create: \\begin{enumerate}"
                + "\\item First item"
                + "\\item Second item with more text to demonstrate wrapping behavior."
                + "\\item Third item"
                + "\\item Fourth item"
                + "\\end{enumerate}";
        page.getParagraphs().add(new TeXFragment(texList));
        document.save(outputFile.toString());
    }
}
```

## 
텍스트 단락이 포함된 글머리 기호 목록 만들기



일반 텍스트 조각으로 수동 글머리 기호 목록을 작성해야 하는 경우 이 예를 사용하십시오.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
`TextParagraph`을 빌드하고 글머리 기호 접두사가 붙은 조각을 추가합니다.
1. 페이지에 단락을 추가하고 문서를 저장합니다.


```java
public static void createBulletList(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String[] items = {
                "First item in the list",
                "Second item with more text to demonstrate wrapping behavior.",
                "Third item",
                "Fourth item"
        };

        TextBuilder builder = new TextBuilder(page);
        TextParagraph paragraph = new TextParagraph();
        paragraph.setRectangle(new Rectangle(80, 200, 400, 800, true));
        paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);

        for (String item : items) {
            TextFragment fragment = new TextFragment("- " + item);
            fragment.getTextState().setFont(FontRepository.findFont("Times New Roman"));
            fragment.getTextState().setFontSize(12);
            paragraph.appendLine(fragment);
        }

        builder.appendParagraph(paragraph);
        document.save(outputFile.toString());
    }
}
```

## 
텍스트 단락이 포함된 번호 매기기 목록 만들기



일반 텍스트 조각으로 수동 번호 목록을 작성해야 하는 경우 이 예를 사용하십시오.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
`TextParagraph`을 빌드하고 번호가 매겨진 조각을 추가합니다.
1. 페이지에 단락을 추가하고 문서를 저장합니다.


```java
public static void createNumberedList(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        String[] items = {
                "First item in the list",
                "Second item with more text to demonstrate wrapping behavior.",
                "Third item",
                "Fourth item"
        };

        TextBuilder builder = new TextBuilder(page);
        TextParagraph paragraph = new TextParagraph();
        paragraph.setRectangle(new Rectangle(80, 200, 400, 800, true));
        paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);

        for (int i = 0; i < items.length; i++) {
            TextFragment fragment = new TextFragment((i + 1) + ". " + items[i]);
            fragment.getTextState().setFont(FontRepository.findFont("Times New Roman"));
            fragment.getTextState().setFontSize(12);
            paragraph.appendLine(fragment);
        }

        builder.appendParagraph(paragraph);
        document.save(outputFile.toString());
    }
}
```

## 
기본 각주 추가



텍스트 조각이 간단한 각주를 참조해야 하는 경우 이 예를 사용하십시오.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
본문 부분을 만들고 `Note`을 각주로 지정합니다.
1. 인라인 연속 텍스트를 추가하고 문서를 저장합니다.


```java
public static void addFootnote(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is a sample text with a footnote.");
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);
        textFragment.setFootNote(new Note("This is the footnote content."));
        page.getParagraphs().add(textFragment);

        TextFragment inlineText = new TextFragment(" This is another text after footnote in the same paragraph.");
        inlineText.setInLineParagraph(true);
        inlineText.getTextState().setFont(FontRepository.findFont("Arial"));
        inlineText.getTextState().setFontSize(14);
        page.getParagraphs().add(inlineText);

        document.save(outputFile.toString());
    }
}
```

## 
사용자 정의 텍스트 스타일로 각주 추가



각주 내용이 자체 글꼴, 크기 및 색상 설정을 사용해야 하는 경우 이 예를 사용하십시오.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
주요 텍스트 조각을 생성하고 스타일이 지정된 각주를 구성합니다.
1. 메모를 첨부하고 PDF를 저장하세요.


```java
public static void addFootnoteCustomTextStyle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is a sample text with a footnote.");
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);

        Note note = new Note("This is the footnote content with custom text style.");
        TextState noteTextState = new TextState();
        noteTextState.setFont(FontRepository.findFont("Times New Roman"));
        noteTextState.setFontSize(10);
        noteTextState.setForegroundColor(Color.getRed());
        noteTextState.setFontStyle(FontStyles.Italic);
        note.setTextState(noteTextState);
        textFragment.setFootNote(note);

        page.getParagraphs().add(textFragment);
        document.save(outputFile.toString());
    }
}
```

## 
사용자 정의 마커 텍스트로 각주 추가



보이는 각주 표시를 사용자 정의 텍스트로 바꿔야 하는 경우 이 예를 사용하십시오.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
각주를 주요 텍스트 부분에 할당하고 해당 마커 텍스트를 재정의합니다.
1. 나머지 내용을 추가하고 문서를 저장합니다.


```java
public static void addFootnoteCustomText(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is a sample text with a footnote.");
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);
        textFragment.setFootNote(new Note("This is the footnote content."));
        textFragment.getFootNote().setText("***");
        page.getParagraphs().add(textFragment);

        TextFragment anotherText = new TextFragment(" This is another text without footnote.");
        anotherText.getTextState().setFont(FontRepository.findFont("Arial"));
        anotherText.getTextState().setFontSize(14);
        page.getParagraphs().add(anotherText);

        document.save(outputFile.toString());
    }
}
```

## 
각주 구분선 사용자 정의



각주와 페이지 콘텐츠를 구분하는 줄의 스타일을 명시적으로 지정해야 하는 경우 이 예를 사용하세요.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
`GraphInfo`을 통해 페이지 노트 선 스타일을 구성합니다.
1. 각주와 함께 텍스트 조각을 추가하고 문서를 저장합니다.


```java
public static void addFootnoteWithCustomLineStyle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        GraphInfo graphInfo = new GraphInfo();
        graphInfo.setLineWidth(2);
        graphInfo.setColor(Color.getRed());
        graphInfo.setDashArray(new int[] {3});
        graphInfo.setDashPhase(1);
        page.setNoteLineStyle(graphInfo);

        TextFragment text1 = new TextFragment("This is a sample text with a footnote.");
        text1.setFootNote(new Note("foot note for text 1"));
        page.getParagraphs().add(text1);

        TextFragment text2 = new TextFragment("This is yet another sample text with a footnote.");
        text2.setFootNote(new Note("foot note for text 2"));
        page.getParagraphs().add(text2);

        document.save(outputFile.toString());
    }
}
```

## 
이미지와 표 내용이 포함된 각주 추가



각주 자체에 이미지, 텍스트, 표 등 풍부한 콘텐츠가 포함되어야 하는 경우 이 예를 사용하세요.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
이미지, 인라인 텍스트 및 테이블을 사용하여 `Note` 개체를 빌드합니다.
1. 이를 본문 부분에 첨부하고 문서를 저장합니다.


```java
public static void addFootnoteWithImageAndTable(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment text = new TextFragment("This is a sample text with a footnote.");
        page.getParagraphs().add(text);

        Note note = new Note();

        Image imageNote = new Image();
        imageNote.setFile(dataDir.resolve("logo.jpg").toString());
        imageNote.setFixHeight(20);
        imageNote.setFixWidth(20);
        note.getParagraphs().add(imageNote);

        TextFragment textNote = new TextFragment("This is the footnote content.");
        textNote.getTextState().setFontSize(20);
        textNote.setInLineParagraph(true);
        note.getParagraphs().add(textNote);

        Table table = new Table();
        table.getRows().add().getCells().add("Cell 1,1");
        table.getRows().add().getCells().add("Cell 1,2");
        note.getParagraphs().add(table);

        text.setFootNote(note);
        document.save(outputFile.toString());
    }
}
```

## 
미주 추가



텍스트 조각이 페이지 각주 대신 미주 콘텐츠를 참조해야 하는 경우 이 예를 사용하세요.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
본문 부분에 미주를 할당하고 지원 본문 텍스트를 추가합니다.
1. 생성된 미주 콘텐츠와 함께 문서를 저장합니다.


```java
public static void addEndnote(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is a sample text with an endnote.");
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);
        textFragment.setEndNote(new Note("This is the EndNote content."));
        page.getParagraphs().add(textFragment);

        String textContent = loremText();
        for (int i = 0; i < 5; i++) {
            TextFragment text = new TextFragment(textContent);
            text.getTextState().setFont(FontRepository.findFont("Arial"));
            text.getTextState().setFontSize(14);
            page.getParagraphs().add(text);
        }

        document.save(outputFile.toString());
    }
}

private static String loremText() throws Exception {
    Path loremPath = dataDir.resolve("lorem.txt");
    return Files.exists(loremPath) ? Files.readString(loremPath) : "Lorem ipsum sample text not found.";
}
```

## 
사용자 정의 마커 텍스트가 포함된 미주 추가



미주 표시자가 사용자 정의 표시 레이블을 사용해야 하는 경우 이 예를 사용하십시오.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
기본 텍스트 부분에 미주를 할당하고 마커 텍스트를 재정의합니다.
1. 나머지 문서 텍스트를 추가하고 PDF를 저장합니다.


```java
public static void addEndnoteCustomText(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("This is a sample text with an endnote.");
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        textFragment.getTextState().setFontSize(14);
        textFragment.setEndNote(new Note("This is the EndNote content."));
        textFragment.getEndNote().setText("***");
        page.getParagraphs().add(textFragment);

        String textContent = loremText();
        for (int i = 0; i < 5; i++) {
            TextFragment text = new TextFragment(textContent);
            text.getTextState().setFont(FontRepository.findFont("Arial"));
            text.getTextState().setFontSize(14);
            page.getParagraphs().add(text);
        }

        document.save(outputFile.toString());
    }
}
```

## 
표 내용을 새 페이지에 강제 적용



서식이 지정된 콘텐츠가 새 페이지에서 명시적으로 시작되어야 하는 경우 이 예를 사용하세요.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
테이블을 작성하고 해당 행을 채웁니다.
1. 새 페이지에서 시작하도록 테이블을 설정하고 문서를 저장합니다.


```java
public static void forceNewPage(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Table table = new Table();
        table.setColumnWidths("150 150 150");
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All));

        for (int i = 0; i < 5; i++) {
            Row row = table.getRows().add();
            row.getCells().add("Row " + (i + 1) + " - Col 1");
            row.getCells().add("Row " + (i + 1) + " - Col 2");
            row.getCells().add("Row " + (i + 1) + " - Col 3");
        }

        table.setInNewPage(true);
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## 
한 단락 흐름 내에 인라인 콘텐츠 혼합



텍스트와 이미지가 동일한 단락 흐름 내에서 계속되어야 하는 경우 이 예를 사용하세요.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
첫 번째 텍스트 조각을 추가한 다음 인라인 이미지를 추가하고 또 다른 인라인 텍스트 조각을 추가합니다.
1. 다음 독립형 단락을 추가하고 문서를 저장합니다.


```java
public static void usingInlineParagraphProperty(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment fragment1 = new TextFragment("This is the first part of the paragraph. ");
        fragment1.getTextState().setFont(FontRepository.findFont("Arial"));
        fragment1.getTextState().setFontSize(14);
        page.getParagraphs().add(fragment1);

        Image image = new Image();
        image.setInLineParagraph(true);
        image.setFile(dataDir.resolve("logo.jpg").toString());
        image.setFixHeight(30);
        image.setFixWidth(30);
        page.getParagraphs().add(image);

        TextFragment fragment2 = new TextFragment("This is the second part of the same paragraph.");
        fragment2.setInLineParagraph(true);
        fragment2.getTextState().setFont(FontRepository.findFont("Arial"));
        fragment2.getTextState().setFontSize(14);
        page.getParagraphs().add(fragment2);

        TextFragment fragment3 = new TextFragment("This is a new paragraph.");
        fragment3.getTextState().setFont(FontRepository.findFont("Arial"));
        fragment3.getTextState().setFontSize(14);
        page.getParagraphs().add(fragment3);

        document.save(outputFile.toString());
    }
}
```

## 
다중 열 텍스트 레이아웃 만들기



기사 스타일 텍스트가 여러 열을 거쳐야 하는 경우 이 예를 사용하십시오.


1. 
새 PDF 문서를 만들고 페이지 여백을 구성합니다.

1. 
제목 콘텐츠를 추가하고 다중 열 `FloatingBox`을 만듭니다.
1. 텍스트로 채우고 최종 PDF를 저장하세요.


```java
public static void createMultiColumnPdf(Path outputFile) throws Exception {
    try (Document document = new Document()) {
        document.getPageInfo().getMargin().setLeft(40);
        document.getPageInfo().getMargin().setRight(40);
        Page page = document.getPages().add();

        com.aspose.pdf.drawing.Graph graph1 = new com.aspose.pdf.drawing.Graph(500.0, 2.0);
        page.getParagraphs().add(graph1);
        graph1.getShapes().addItem(new com.aspose.pdf.drawing.Line(new float[] {1.0f, 2.0f, 500.0f, 2.0f}));

        String html = "<span style=\"font-family: 'Times New Roman'; font-size: 18px;\"><strong>How to Steer Clear of money scams</strong></span>";
        page.getParagraphs().add(new HtmlFragment(html));

        FloatingBox box = new FloatingBox();
        box.getColumnInfo().setColumnCount(2);
        box.getColumnInfo().setColumnSpacing("5");
        box.getColumnInfo().setColumnWidths("105 105");

        TextFragment text1 = new TextFragment("By A Googler (The Official Google Blog)");
        text1.getTextState().setFontSize(8);
        text1.getTextState().setLineSpacing(2);
        box.getParagraphs().add(text1);

        text1.getTextState().setFontSize(10);
        text1.getTextState().setFontStyle(FontStyles.Italic);

        com.aspose.pdf.drawing.Graph graph2 = new com.aspose.pdf.drawing.Graph(50.0, 10.0);
        graph2.getShapes().addItem(new com.aspose.pdf.drawing.Line(new float[] {1.0f, 10.0f, 100.0f, 10.0f}));
        box.getParagraphs().add(graph2);

        String loremText = loremText();
        box.getParagraphs().add(new TextFragment(loremText.repeat(5)));
        page.getParagraphs().add(box);

        document.save(outputFile.toString());
    }
}
```

## 
사용자 정의 탭 정지로 정렬된 텍스트 만들기



탭 정지 위치를 사용하여 텍스트를 간단한 표처럼 정렬해야 하는 경우 이 예를 사용하세요.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
정렬 및 지시선 설정으로 탭 정지를 구성합니다.
1. 해당 탭 정지를 사용하는 텍스트 조각을 만들고 문서를 저장합니다.

```java
public static void customTabStops(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TabStops tabStops = new TabStops();
        TabStop tabStop1 = tabStops.add(100);
        tabStop1.setAlignmentType(TabAlignmentType.Right);
        tabStop1.setLeaderType(TabLeaderType.Solid);

        TabStop tabStop2 = tabStops.add(200);
        tabStop2.setAlignmentType(TabAlignmentType.Center);
        tabStop2.setLeaderType(TabLeaderType.Dash);

        TabStop tabStop3 = tabStops.add(300);
        tabStop3.setAlignmentType(TabAlignmentType.Left);
        tabStop3.setLeaderType(TabLeaderType.Dot);

        TextFragment header = new TextFragment("This is an example of forming table with TAB stops", tabStops);
        TextFragment text0 = new TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", tabStops);
        TextFragment text1 = new TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", tabStops);

        TextFragment text2 = new TextFragment("#$TABdata21 ", tabStops);
        text2.getSegments().add(new TextSegment("#$TAB"));
        text2.getSegments().add(new TextSegment("data22 "));
        text2.getSegments().add(new TextSegment("#$TAB"));
        text2.getSegments().add(new TextSegment("data23"));

        page.getParagraphs().add(header);
        page.getParagraphs().add(text0);
        page.getParagraphs().add(text1);
        page.getParagraphs().add(text2);

        document.save(outputFile.toString());
    }
}
```
