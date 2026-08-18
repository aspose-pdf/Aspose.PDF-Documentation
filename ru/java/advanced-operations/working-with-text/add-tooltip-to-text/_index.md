---
title: Добавление всплывающих подсказок в текст PDF в Java
linktitle: PDF-подсказка
type: docs
weight: 20
url: /java/pdf-tooltip/
description: Узнайте, как добавлять всплывающие подсказки к фрагментам текста в PDF-документах на Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавляйте интерактивные подсказки к фрагментам текста PDF с помощью Java.
Abstract: В этой статье показано, как добавить интерактивную справку к тексту PDF с помощью Aspose.PDF для Java. Он охватывает прикрепление текста всплывающей подсказки к невидимым полям кнопок, расположенным над совпадающими фрагментами текста, и создание скрытого текстового поля, которое появляется, когда указатель входит в область триггера.
---
Aspose.PDF для Java позволяет добавлять интерактивную справку, размещая поля формы поверх текстовых фрагментов.

## Добавьте подсказки к совпавшему тексту

Используйте этот пример, когда существующий текст в PDF-файле должен отображать всплывающую подсказку при наведении курсора.

1. Создайте образец PDF-файла и снова откройте его для редактирования.
1. Найдите целевые фрагменты текста с помощью `TextFragmentAbsorber`.
1. Поместите наложения `ButtonField` на совпадающий текст и назначьте текст всплывающей подсказки.
1. Сохраните обновленный документ.

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

## Показывать плавающий текстовый блок при наведении

Используйте этот пример, когда при наведении курсора на текстовую область должно открыться скрытое текстовое поле.

1. Создайте образец PDF-файла и снова откройте его для редактирования.
1. Найдите фрагмент текста триггера с помощью `TextFragmentAbsorber`.
1. Создайте скрытый `TextBoxField` и `ButtonField` с действиями входа и выхода.
1. Сохраните окончательный PDF-файл.

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
