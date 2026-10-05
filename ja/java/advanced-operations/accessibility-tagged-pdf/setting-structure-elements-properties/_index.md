---
title: "Java での Tagged PDF構造要素のプロパティの設定"
linktitle: "構造要素のプロパティの設定"
type: docs
weight: 30
url: /ja/java/setting-structure-elements-properties/
description: Java と Aspose.PDF を使用して Tagged PDF の Structure Elements のプロパティを設定する方法を学びます。タイトル、言語、実際のテキスト、代替テキスト、拡張テキスト、リンク、ノート、タグ名が含まれます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
このページでは、Java におけるタグ付けされた PDF の構造要素の一般的なプロパティ設定パターンについて説明します。

## 共通の構造要素プロパティの設定

タグ付けされた構造要素がタイトル、言語、実際のテキスト、代替テキストなどのアクセシビリティメタデータを公開すべき場合に、この例を使用してください。

1. 新しい タグ付き PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、タグ付きコンテンツのメタデータを初期化してください。
1. 構造ツリーにセクションとヘッダー要素を作成してください。
1. ヘッダーのプロパティを設定し、ドキュメントを保存してください。

```java
public static void setProperties(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        StructureElement rootElement = taggedContent.getRootElement();
        SectElement sectionElement = taggedContent.createSectElement();
        rootElement.appendChild(sectionElement, true);

        HeaderElement headerElement = taggedContent.createHeaderElement(1);
        sectionElement.appendChild(headerElement, true);
        headerElement.setText("The Header");

        headerElement.setTitle("Title");
        headerElement.setLanguage("en-US");
        headerElement.setAlternativeText("Alternative Text");
        headerElement.setExpansionText("Expansion Text");
        headerElement.setActualText("Actual Text");

        document.save(outputFile.toString());
    }
}
```

## テキスト要素の設定

シンプルな段落要素をタグ付き構造ツリーに追加する必要があるときは、この例を使用してください。

1. 新しい タグ付き PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成してください。
1. 作成 [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/paragraphelement/) そしてそれのテキストを設定してください。
1. 段落をルート要素に追加し、ドキュメントを保存してください。

```java
public static void setTextElements(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        ParagraphElement paragraphElement = taggedContent.createParagraphElement();
        paragraphElement.setText("Paragraph.");
        taggedContent.getRootElement().appendChild(paragraphElement, true);

        document.save(outputFile.toString());
    }
}
```

## テキストブロック要素の設定

この例では、複数のブロックレベルの構造要素を作成します。そこには、複数レベルの見出しと段落が含まれます。

1. 新しい タグ付き PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成してください。
1. 必要なレベルのヘッダー要素を追加し、その後段落要素を作成してください。
1. ブロック要素をルート構造に追加し、ドキュメントを保存してください。

```java
public static void setTextBlockElements(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        for (int level = 1; level <= 6; level++) {
            HeaderElement header = taggedContent.createHeaderElement(level);
            header.setText("H" + level + ". Header of Level " + level);
            taggedContent.getRootElement().appendChild(header, true);
        }

        ParagraphElement p = taggedContent.createParagraphElement();
        p.setText("P. Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                + "Aenean nec lectus ac sem faucibus imperdiet.");
        taggedContent.getRootElement().appendChild(p, true);

        document.save(outputFile.toString());
    }
}
```

## インライン要素の設定

ブロック構造要素がネストされたインラインスパンを含む必要がある場合は、この例を使用してください。

1. 新しい タグ付き PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成してください。
1. ヘッダー要素を作成し、そこに span の子要素を追加してください。
1. 複数のスパンを持つ段落を作成し、文書を保存してください。

```java
public static void setInlineElements(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        for (int level = 1; level <= 6; level++) {
            HeaderElement header = taggedContent.createHeaderElement(level);
            taggedContent.getRootElement().appendChild(header, true);

            SpanElement span1 = taggedContent.createSpanElement();
            span1.setText("H" + level + ". ");
            header.appendChild(span1, true);

            SpanElement span2 = taggedContent.createSpanElement();
            span2.setText("Level " + level + " Header");
            header.appendChild(span2, true);
        }

        ParagraphElement paragraphElement = taggedContent.createParagraphElement();
        paragraphElement.setText("P. ");
        taggedContent.getRootElement().appendChild(paragraphElement, true);

        for (int index = 1; index <= 10; index++) {
            SpanElement span = taggedContent.createSpanElement();
            span.setText("Span " + index + ". ");
            paragraphElement.appendChild(span, true);
        }

        document.save(outputFile.toString());
    }
}
```

## カスタムタグ名の設定

この例では、タグ付けされた構造内の paragraph 要素と span 要素にカスタムタグ名を割り当てます。

1. 新しい タグ付き PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、section要素を追加してください。
1. 段落とスパンを作成し、各要素にカスタムタグ名を設定してください。
1. 要素をセクションに追加し、ドキュメントを保存してください。

```java
public static void setTagName(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        SectElement sectionElement = taggedContent.createSectElement();
        taggedContent.getRootElement().appendChild(sectionElement, true);

        String[] paragraphTags = {"P1", "Para", "Para", "Paragraph"};
        String[] spanTags = {"SPAN", "Sp", "Sp", "TheSpan"};

        for (int index = 0; index < 4; index++) {
            ParagraphElement paragraph = taggedContent.createParagraphElement();
            paragraph.setText("P" + (index + 1) + ". ");
            paragraph.setTag(paragraphTags[index]);

            SpanElement span = taggedContent.createSpanElement();
            span.setText("Span " + (index + 1) + ".");
            span.setTag(spanTags[index]);

            paragraph.appendChild(span, true);
            sectionElement.appendChild(paragraph, true);
        }

        document.save(outputFile.toString());
    }
}
```

## リンクと図要素の設定

タグ付けされたリンク要素に代替説明、ハイパーリンク、およびレイアウト属性を持つ図コンテンツを含める必要がある場合は、この例を使用してください。

1. 新しいタグ付き PDF を作成する [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 段落内にリンク要素を追加してください。
1. ハイパーリンクのターゲット、代替説明、およびリンクされた図要素を設定してください。
1. 必要なレイアウト属性を設定し、ドキュメントを保存してください。

```java
public static void setElements(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Link Elements Example");
        taggedContent.setLanguage("en-US");

        for (int index = 1; index <= 4; index++) {
            ParagraphElement paragraph = taggedContent.createParagraphElement();
            taggedContent.getRootElement().appendChild(paragraph, true);

            LinkElement link = taggedContent.createLinkElement();
            paragraph.appendChild(link, true);
            link.setHyperlink(new WebHyperlink("http://google.com"));
            link.setText(index == 4 ? "The multiline link: Google Google Google Google" : "Google");
            link.setAlternateDescriptions("Link to Google");
        }

        ParagraphElement paragraph = taggedContent.createParagraphElement();
        taggedContent.getRootElement().appendChild(paragraph, true);

        LinkElement link = taggedContent.createLinkElement();
        paragraph.appendChild(link, true);
        link.setHyperlink(new WebHyperlink("http://google.com"));

        FigureElement figure = taggedContent.createFigureElement();
        figure.setImage(imageFile.toString(), 1200);
        figure.setAlternativeText("Google icon");

        StructureAttributes linkLayoutAttributes = link.getAttributes().getAttributes(AttributeOwnerStandard.Layout);
        StructureAttribute placementAttribute = new StructureAttribute(AttributeKey.Placement);
        placementAttribute.setNameValue(AttributeName.Placement_Block);
        linkLayoutAttributes.setAttribute(placementAttribute);

        link.appendChild(figure, true);
        link.setAlternateDescriptions("Link to Google");

        document.save(outputFile.toString());
    }
}
```

## インラインリンク関連のコンテンツを含む段落の追加

この例は、プレーンテキストと入れ子になった span 要素を組み合わせた段落要素を作成します。

1. 新しい タグ付き PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成してください。
1. 段落要素を作成し、カスタムテキストを含む span 子要素を追加してください。
1. 段落をルート要素に追加し、ドキュメントを保存してください。

```java
public static void addLinkElement(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Text Elements Example");
        taggedContent.setLanguage("en-US");

        for (int paragraphIndex = 1; paragraphIndex <= 4; paragraphIndex++) {
            ParagraphElement paragraph = taggedContent.createParagraphElement();
            taggedContent.getRootElement().appendChild(paragraph, true);

            SpanElement span1 = taggedContent.createSpanElement();
            span1.setText("Span_" + paragraphIndex + "1");
            SpanElement span2 = taggedContent.createSpanElement();
            span2.setText(" and Span_" + paragraphIndex + "2.");

            paragraph.setText("Paragraph with ");
            paragraph.appendChild(span1, true);
            paragraph.appendChild(span2, true);
        }

        document.save(outputFile.toString());
    }
}
```

## ノート要素の設定

自動または明示的な ID でノート構造要素を作成すべき場合は、この例を使用してください。

1. 新しいタグ付き PDF を作成する [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 段落要素を追加してください。
1. 必要に応じてノート要素を作成し、そのテキストと ID を設定してください。
1. ノートを段落に追加し、ドキュメントを保存してください。

```java
public static void setNoteElement(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Sample of Note Elements");
        taggedContent.setLanguage("en-US");

        ParagraphElement paragraph = taggedContent.createParagraphElement();
        taggedContent.getRootElement().appendChild(paragraph, true);

        NoteElement note1 = taggedContent.createNoteElement();
        paragraph.appendChild(note1, true);
        note1.setText("Note with auto generate ID. ");

        NoteElement note2 = taggedContent.createNoteElement();
        paragraph.appendChild(note2, true);
        note2.setText("Note with ID = 'note_002'. ");
        note2.setId("note_002");

        NoteElement note3 = taggedContent.createNoteElement();
        paragraph.appendChild(note3, true);
        note3.setText("Note with ID = 'note_003'. ");
        note3.setId("note_003");

        document.save(outputFile.toString());
    }
}
```

## 多言語コンテンツの言語とタイトルの設定

この例では、ドキュメントレベルのメタデータを割り当て、その後、異なる言語値を持つ段落を作成します。

1. 新しい タグ付き PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、文書のタイトルと言語を設定してください。
1. ヘッダー要素を追加し、各ローカライズされたフレーズに対して段落を作成してください。
1. 多言語タグ付き文書を保存してください。

```java
public static void setLanguageAndTitle(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Example Tagged Document");
        taggedContent.setLanguage("en-US");

        HeaderElement header = taggedContent.createHeaderElement(1);
        header.setText("Phrase on different languages");
        taggedContent.getRootElement().appendChild(header, true);

        addParagraph(taggedContent, "Hello, World!", "en-US");
        addParagraph(taggedContent, "Hallo Welt!", "de-DE");
        addParagraph(taggedContent, "Bonjour le monde!", "fr-FR");
        addParagraph(taggedContent, "Hola Mundo!", "es-ES");

        document.save(outputFile.toString());
    }
}
```

## タグ付けされたコンテンツ用の段落ヘルパーの追加

このヘルパーメソッドは段落を作成し、その言語を割り当て、ルート構造に追加します。

1. 作成 [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/paragraphelement/)。
1. 要素のテキストと言語を設定してください。
1. 段落をタグ付けされたコンテンツのルート要素に追加してください。

```java
private static void addParagraph(ITaggedContent taggedContent, String text, String language) {
    ParagraphElement paragraph = taggedContent.createParagraphElement();
    paragraph.setText(text);
    paragraph.setLanguage(language);
    taggedContent.getRootElement().appendChild(paragraph, true);
}
```
