---
title: Заменить текст в PDF на Java
linktitle: Заменить текст в PDF
type: docs
weight: 40
url: /java/replace-text-in-pdf/
description: Узнайте, как заменять, переупорядочивать и удалять текст в документах PDF с помощью Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: Заменяйте, удаляйте и корректируйте текстовое содержимое в PDF с помощью Java.
Abstract: В этой статье описываются рабочие процессы замены текста в PDF-документах с использованием Aspose.PDF для Java. Он охватывает замену текста на всех страницах, ограничение замены выбранной областью, настройку макета замены, использование сопоставления на основе регулярных выражений, замену шрифтов, удаление всего текста и удаление скрытого текста.
---
Aspose.PDF для Java предоставляет как простую замену, так и функции замены с учетом макета с помощью `TextFragmentAbsorber` и опций замены.

## Заменить текст на всех страницах

Используйте этот пример, когда одну и ту же фразу необходимо заменить во всем документе.

1. Откройте исходный PDF-документ.
1. Найдите на всех страницах целевую фразу с помощью `TextFragmentAbsorber`.
1. Замените совпадающий текст и сохраните обновленный PDF-файл.

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

## Заменить текст в определенной области страницы

Используйте этот пример, когда замена должна быть ограничена выбранным прямоугольником на одной странице.

1. Откройте исходный PDF-документ.
1. Настройте `TextSearchOptions` с границами страницы и целевым прямоугольником.
1. Замените совпавший текст внутри этой области и сохраните документ.

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

## Замените текст и отрегулируйте интервал внутри сдвинутого прямоугольника.

Используйте этот пример, когда заменяющий текст должен оставаться на странице с измененным интервалом, но размер шрифта должен оставаться неизменным.

1. Откройте исходный PDF-файл и соберите фрагменты текста с целевой страницы.
1. Измените прямоугольник замены и выберите поведение `AdjustSpaceWidth`.
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

## Заменить текст внутри большего прямоугольника абзаца

Используйте этот пример, когда заменяющий текст должен занять большую область страницы.

1. Откройте исходный PDF-файл и получите первый фрагмент текста с целевой страницы.
1. Создайте замещающий прямоугольник большего размера из медиа-блока страницы.
1. Примените параметры замены и сохраните PDF-файл.

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

## Замените текст и масштабируйте шрифт, чтобы заполнить прямоугольник.

Используйте этот пример, когда текст замены должен увеличиться и заполнить целевую область.

1. Откройте исходный PDF-файл и получите доступ к целевому фрагменту текста.
1. Определите заменяющий прямоугольник и включите настройку шрифта `ScaleToFill`.
1. Установите новый текст и сохраните обновленный документ.

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

## Замените текст и уменьшите его по размеру

Используйте этот пример, когда заменяющий текст должен оставаться внутри исходного текстового прямоугольника.

1. Откройте исходный PDF-файл и выберите целевой фрагмент.
1. Повторно используйте текущий прямоугольник фрагмента и включите `ShrinkToFit`.
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

## Заменить текст регулярным выражением

Используйте этот пример, когда совпадающий текст должен быть найден по шаблону регулярного выражения и изменен во время замены.

1. Откройте исходный PDF-документ.
1. Выполните поиск по странице с помощью `TextFragmentAbsorber` с включенным регулярным выражением.
1. Замените каждое совпадение, обновите стиль текста и сохраните результат.

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

## Замените текст-заполнитель и позвольте странице измениться

Используйте этот пример, когда заполнитель необходимо заменить более длинным действительным значением с сохранением макета страницы.

1. Откройте исходный PDF-файл и найдите текст-заполнитель.
1. Назначьте заменяющий текст и обновите настройки его шрифта.
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

## Заменить один шрифт другим

Используйте этот пример, когда текст, использующий определенный встроенный шрифт, необходимо переключить на другой шрифт.

1. Откройте исходный PDF-файл и соберите все фрагменты текста.
1. Проверьте имя шрифта каждого фрагмента и замените целевой шрифт.
1. Сохраните обновленный PDF-файл.

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

## Замените шрифты и удалите неиспользуемые ресурсы шрифтов.

Используйте этот пример, когда документ необходимо очистить после замены шрифта.

1. Откройте исходный PDF-файл и настройте `TextEditOptions` для удаления неиспользуемых шрифтов.
1. Соберите фрагменты текста и назначьте замещающий шрифт.
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

## Удалите весь текст из документа

Используйте этот пример, когда весь текстовый контент необходимо удалить с каждой страницы.

1. Откройте исходный PDF-документ.
1. Создайте `TextFragmentAbsorber` и позвоните `removeAllText(document)`.
1. Сохраните очищенный PDF-файл.

```java
public static void removeAllTextUsingAbsorber1(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.removeAllText(document);
        document.save(outputFile.toString());
    }
}
```

## Удалите весь текст с одной страницы

Используйте этот пример, когда весь текст необходимо удалить только с определенной страницы.

1. Откройте исходный PDF-документ.
1. Создайте `TextFragmentAbsorber` и удалите текст с целевой страницы.
1. Сохраните обновленный документ.

```java
public static void removeAllTextUsingAbsorber2(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.removeAllText(document.getPages().get_Item(1));
        document.save(outputFile.toString());
    }
}
```

## Удалите текст из выделенного прямоугольника

Используйте этот пример, когда текст необходимо удалить только внутри выбранной области страницы.

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

## Удалите скрытый текст

Используйте этот пример, когда из PDF-файла необходимо удалить невидимые фрагменты текста.

1. Откройте исходный PDF-файл и впитайте все фрагменты текста.
1. Проверьте каждый фрагмент на наличие состояния невидимого текста.
1. Очистите скрытый текст и сохраните документ.

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
