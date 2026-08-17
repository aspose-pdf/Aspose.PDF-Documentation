---
title: Java에서 PDF 텍스트에 도구 설명 추가
linktitle: PDF 툴팁
type: docs
weight: 20
url: /java/pdf-tooltip/
description: Java에서 PDF 문서의 텍스트 조각에 도구 설명을 추가하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF 텍스트 조각에 대화형 도구 설명 추가
Abstract: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF 텍스트에 대화형 도움말을 추가하는 방법을 보여줍니다. 일치하는 텍스트 조각 위에 배치된 보이지 않는 버튼 필드에 도구 설명 텍스트를 첨부하고 포인터가 트리거 영역에 들어갈 때 나타나는 숨겨진 텍스트 필드를 만드는 방법을 다룹니다.
---

Aspose.PDF for Java를 사용하면 텍스트 조각 위에 양식 필드를 배치하여 대화형 도움말을 추가할 수 있습니다.


## 
일치하는 텍스트에 도구 설명 추가



PDF의 기존 텍스트에 마우스를 올리면 도구 설명이 표시되어야 하는 경우 이 예를 사용하세요.


1. 
샘플 PDF를 생성하고 편집을 위해 다시 엽니다.

1. 
`TextFragmentAbsorber`으로 대상 텍스트 조각을 검색합니다.

1. 
일치하는 텍스트에 `ButtonField` 오버레이를 배치하고 툴팁 텍스트를 할당합니다.

1. 
업데이트된 문서를 저장합니다.


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

## 
마우스를 올리면 부동 텍스트 블록 표시



텍스트 영역 위로 마우스를 가져가면 숨겨진 텍스트 필드가 표시될 때 이 예를 사용하십시오.


1. 
샘플 PDF를 생성하고 편집을 위해 다시 엽니다.

1. 
`TextFragmentAbsorber`이 포함된 트리거 텍스트 조각을 찾습니다.

1. 
Enter 및 Exit 작업을 사용하여 숨겨진 `TextBoxField` 및 `ButtonField`을 만듭니다.

1. 
최종 PDF를 저장합니다.

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
