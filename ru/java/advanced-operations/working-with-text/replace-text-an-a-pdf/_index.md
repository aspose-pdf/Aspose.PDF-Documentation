---
title: Замена текста в PDF с помощью Java
linktitle: Замена текста в PDF
type: docs
weight: 40
url: /ru/java/replace-text-in-pdf/
description: Узнайте, как заменять, переставлять и удалять текст в PDF‑документах с использованием Java.
lastmod: "2026-09-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: Заменяйте, удаляйте и корректируйте текстовое содержимое в PDF с помощью Java
Abstract: В этой статье объясняются рабочие процессы замены текста в PDF‑документах с использованием Aspose.PDF for Java. Она охватывает замену текста на всех страницах, ограничение замены выбранным регионом, настройку макета замены, использование соответствия на основе регулярных выражений, замену шрифтов, удаление всего текста и удаление скрытого текста.
---
Aspose.PDF for Java предоставляет как простые функции замены, так и функции замены с учётом макета через `TextFragmentAbsorber` и параметры замены.

## Замена текста на всех страницах

Используйте этот пример, когда одну и ту же фразу нужно заменить по всему документу.

1. Откройте исходный PDF-документ.
1. Ищите на всех страницах целевую фразу с `TextFragmentAbsorber`.
1. Замените найденный текст и сохраните обновлённый PDF.

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

## Замена текста в определённой области страницы

Используйте этот пример, когда замена должна быть ограничена выбранным прямоугольником на одной странице.

1. Откройте исходный PDF-документ.
1. Настройте `TextSearchOptions` с границами страницы и целевым прямоугольником.
1. Замените найденный текст внутри этой области и сохраните документ.

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

## Замена текста и регулировка интервала внутри смещённого прямоугольника

Используйте этот пример, когда заменяющий текст должен оставаться на странице с отрегулированным интервалом, но размер шрифта должен оставаться неизменным.

1. Откройте исходный PDF и соберите текстовые фрагменты со страницы назначения.
1. Измените прямоугольник замены и выберите режим `AdjustSpaceWidth`.
1. Установите новый текст и сохраните документ.

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

## Замена текста внутри более крупного прямоугольника абзаца

Используйте этот пример, когда заменяющий текст должен расширяться на большую площадь страницы.

1. Откройте исходный PDF и получите первый фрагмент текста со целевой страницы.
1. Создайте больший заменяющий прямоугольник из media box страницы.
1. Примените параметры замены и сохраните PDF.

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

## Замена текста и масштабирование шрифта, чтобы заполнить прямоугольник

Используйте этот пример, когда заменяемый текст должен увеличиваться, чтобы заполнить целевую область.

1. Откройте исходный PDF и получите доступ к целевому фрагменту текста.
1. Определите заменяющий прямоугольник и включите масштабирование шрифта в режиме `ScaleToFill`.
1. Установите новый текст и сохраните обновлённый документ.

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

## Замена текста с уменьшением до размеров области

Используйте этот пример, когда заменяющий текст должен оставаться внутри исходного текстового прямоугольника.

1. Откройте исходный PDF и выберите целевой фрагмент.
1. Используйте повторно текущий прямоугольник фрагмента и включите `ShrinkToFit`.
1. Замените текст и сохраните документ.

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

## Замена текста с помощью регулярного выражения

Используйте этот пример, когда найденный текст должен определяться регулярным выражением и переоформляться при замене.

1. Откройте исходный PDF-документ.
1. Выполните поиск по странице с помощью `TextFragmentAbsorber` с поддержкой регулярных выражений.
1. Замените каждое совпадение, обновите его стиль текста и сохраните результат.

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

## Замена текста-заполнителя с перестроением страницы

Используйте этот пример, когда заполнитель нужно заменить более длинным реальным значением, сохраняя макет страницы.

1. Откройте исходный PDF и выполните поиск текста‑заполнителя.
1. Назначьте заменяющий текст и обновите его настройки шрифта.
1. Сохраните документ, чтобы макет был пересчитан.

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

## Замена одного шрифта на другой

Используйте этот пример, когда текст, использующий определённый встроенный шрифт, должен быть переключён на другой шрифт.

1. Откройте исходный PDF и соберите все текстовые фрагменты.
1. Проверьте имя шрифта каждого фрагмента и замените целевой шрифт.
1. Сохраните обновлённый PDF.

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

## Замена шрифтов и удаление неиспользуемых ресурсов шрифтов

Используйте этот пример, когда документ необходимо очистить после замены шрифта.

1. Откройте исходный PDF и настройте `TextEditOptions` для удаления неиспользуемых шрифтов.
1. Соберите фрагменты текста и назначьте заменяющий шрифт Font.
1. Сохраните оптимизированный документ.

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

## Удаление всего текста из документа

Используйте этот пример, когда весь текстовый контент должен быть удалён со всех страниц.

1. Откройте исходный PDF-документ.
1. Создайте `TextFragmentAbsorber` и вызовите `removeAllText(document)`.
1. Сохраните очищенный PDF.

```java
public static void removeAllTextUsingAbsorber1(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.removeAllText(document);
        document.save(outputFile.toString());
    }
}
```

## Удаление всего текста с одной страницы

Используйте этот пример, когда весь текст следует удалять только с конкретной страницы.

1. Откройте исходный PDF-документ.
1. Создайте `TextFragmentAbsorber` и удалите текст с целевой страницы.
1. Сохраните обновлённый документ.

```java
public static void removeAllTextUsingAbsorber2(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.removeAllText(document.getPages().get_Item(1));
        document.save(outputFile.toString());
    }
}
```

## Удаление текста из выбранного прямоугольника

Используйте этот пример, когда текст должен быть удалён только внутри выбранной области страницы.

1. Откройте исходный PDF-документ.
1. Создайте `TextFragmentAbsorber` и определите прямоугольник для очистки.
1. Удалите текст из этой области и сохраните документ.

```java
public static void removeAllTextUsingAbsorber3(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.removeAllText(document.getPages().get_Item(1), new Rectangle(10, 200, 120, 600, true));
        document.save(outputFile.toString());
    }
}
```

## Удаление скрытого текста

Используйте этот пример, когда необходимо удалить из PDF невидимые фрагменты текста.

1. Откройте исходный PDF и извлеките все фрагменты текста.
1. Проверьте каждый фрагмент на наличие невидимого текста.
1. Удалите скрытый текст и сохраните документ.

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


