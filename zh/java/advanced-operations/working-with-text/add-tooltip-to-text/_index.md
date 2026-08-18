---
title: 在 Java 中向 PDF 文本添加工具提示
linktitle: PDF 工具提示
type: docs
weight: 20
url: /java/pdf-tooltip/
description: 了解如何使用 Java 将工具提示添加到 PDF 文档中的文本片段。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 将交互式工具提示添加到 PDF 文本片段
Abstract: 本文介绍如何使用 Aspose.PDF for Java 向 PDF 文本添加交互式帮助。它涵盖将工具提示文本附加到放置在匹配文本片段上的不可见按钮字段，以及创建当指针进入触发区域时显示的隐藏文本字段。
---
Aspose.PDF for Java 允许您通过将表单字段放置在文本片段上来添加交互式帮助。

## 将工具提示添加到匹配的文本

当 PDF 中的现有文本应在悬停时显示工具提示时，请使用此示例。

1. 创建示例 PDF 并重新打开它进行编辑。
1. 使用`TextFragmentAbsorber`搜索目标文本片段。
1. 将 `ButtonField` 覆盖层放在匹配的文本上并分配工具提示文本。
1. 保存更新的文档。

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

## 悬停时显示浮动文本块

当将鼠标悬停在文本区域上时应显示隐藏的文本字段，请使用此示例。

1. 创建示例 PDF 并重新打开它进行编辑。
1. 使用`TextFragmentAbsorber`查找触发文本片段。
1. 创建一个隐藏的`TextBoxField` 和一个具有进入和退出操作的`ButtonField`。
1. 保存最终的 PDF。

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
