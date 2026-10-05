---
title: "Java での PDFテキストにツールチップの追加"
linktitle: PDFツールチップ
type: docs
weight: 20
url: /ja/java/pdf-tooltip/
description: JavaでPDFドキュメントのテキストフラグメントにツールチップを追加する方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Javaを使用してPDFテキストフラグメントにインタラクティブなツールチップを追加
Abstract: この記事では、Aspose.PDF for Java を使用して PDF テキストにインタラクティブなヘルプを追加する方法を示します。対象となるテキストフラグメント上に配置された見えないボタンフィールドにツールチップテキストを添付し、ポインタがトリガー領域に入ったときに表示される非表示テキストフィールドを作成することについて説明しています。
---
Aspose.PDF for Java を使用すると、テキストフラグメント上にフォームフィールドを配置してインタラクティブなヘルプを追加できます。

## 一致したテキストにツールチップの追加

PDF の既存テキストにカーソルを合わせたときにツールチップを表示させたい場合は、この例を使用してください。

1. サンプル PDF を作成し、編集のために再度開いてください。
1. 対象テキストフラグメントを検索 `TextFragmentAbsorber`.
1. 場所 `ButtonField` 一致したテキストにオーバーレイを適用し、ツールチップテキストを割り当てます。
1. 更新されたドキュメントを保存してください。

```java
public static void addToolTipToSearchedText(Path outputFile) {
        Document document = new Document();
        document.getPages().add().getParagraphs()
                .add(new TextFragment("Move the mouse cursor here to display a tooltip"));
        document.getPages().get_Item(1).getParagraphs()
                .add(new TextFragment("Move the mouse cursor here to display a very long tooltip"));
        document.save(outputFile.toString());
        document.close();

        document = new Document(outputFile.toString());
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(
                "Move the mouse cursor here to display a tooltip");
        document.getPages().accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            ButtonField field = new ButtonField(fragment.getPage(), fragment.getRectangle());
            field.setAlternateName("Tooltip for text.");
            document.getForm().add(field);
        }

        absorber = new TextFragmentAbsorber("Move the mouse cursor here to display a very long tooltip");
        document.getPages().accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            ButtonField field = new ButtonField(fragment.getPage(), fragment.getRectangle());
            field.setAlternateName("Lorem ipsum dolor sit amet, consectetur adipiscing elit,"
                    + " sed do eiusmod tempor incididunt ut labore et dolore magna"
                    + " aliqua. Ut enim ad minim veniam, quis nostrud exercitation"
                    + " ullamco laboris nisi ut aliquip ex ea commodo consequat."
                    + " Duis aute irure dolor in reprehenderit in voluptate velit"
                    + " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint"
                    + " occaecat cupidatat non proident, sunt in culpa qui officia"
                    + " deserunt mollit anim id est laborum.");
            document.getForm().add(field);
        }

        document.save(outputFile.toString());
        document.close();
    }
```

## ホバー時に浮動テキストブロックを表示する

テキスト領域にカーソルを合わせたときに隠れたテキストフィールドが表示されるように、この例を使用してください。

1. サンプル PDF を作成し、編集のために再度開いてください。
1. トリガーテキストフラグメントを検索する `TextFragmentAbsorber`.
1. 非表示を作成 `TextBoxField` そして a `ButtonField` エントリとエグジットのアクションを伴う。
1. 最終的な PDF を保存してください。

```java
public static void createHiddenTextBlock(Path outputFile) {
    Document document = new Document();
    document.getPages().add().getParagraphs()
            .add(new TextFragment("Move the mouse cursor here to display floating text"));
    document.save(outputFile.toString());
    document.close();

    document = new Document(outputFile.toString());
    TextFragmentAbsorber absorber = new TextFragmentAbsorber(
            "Move the mouse cursor here to display floating text");
    document.getPages().accept(absorber);
    TextFragment fragment = absorber.getTextFragments().get_Item(1);

    TextBoxField floatingField = new TextBoxField(
            fragment.getPage(), new Rectangle(100.0, 700.0, 220.0, 740.0, false));
    floatingField.setValue("This is the \"floating text field\".");
    floatingField.setReadOnly(true);
    floatingField.setFlags(floatingField.getFlags() | AnnotationFlags.Hidden);
    floatingField.setPartialName("FloatingField_1");
    floatingField.setDefaultAppearance(new DefaultAppearance("Helv", 10, java.awt.Color.BLUE));
    floatingField.getCharacteristics().setBackground(java.awt.Color.CYAN);
    floatingField.getCharacteristics().setBorder(java.awt.Color.BLUE);
    floatingField.setBorder(new Border(floatingField));
    floatingField.getBorder().setWidth(1);
    floatingField.setMultiline(true);

    document.getForm().add(floatingField);

    ButtonField buttonField = new ButtonField(fragment.getPage(), fragment.getRectangle());
    buttonField.getAnnotationActions().setOnEnter(new HideAction(floatingField, false));
    buttonField.getAnnotationActions().setOnExit(new HideAction(floatingField));

    document.getForm().add(buttonField);
    document.save(outputFile.toString());
    document.close();
}
```
