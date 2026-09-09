---
title: Поиск и извлечение текста PDF в Java
linktitle: Поиск и получение текста
type: docs
weight: 60
url: /ru/java/search-and-get-text-from-pdf/
description: Узнайте, как искать, проверять и извлекать текст из PDF‑документов на Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ищите текст в PDF и проверяйте извлечённые фрагменты на Java
Abstract: В этой статье объясняется, как выполнять поиск и извлекать текст из PDF‑документов с помощью Aspose.PDF for Java. Рассматриваются TextAbsorber и TextFragmentAbsorber, включая извлечение по региону, поиск на конкретных страницах, соответствие регулярным выражениям и фразам, вставку гиперссылок, проверку стилизованного текста и подсветку фрагментов.
---
Aspose.PDF for Java поддерживает извлечение необработанного текста и поиск на уровне фрагментов с координатами, стилями и сопоставлением по регулярным выражениям.

## Извлеките текст со всех страниц с использованием TextAbsorber

Используйте этот пример, когда вам нужен простой извлечённый текст из выбранного участка документа на всех страницах.

1. Откройте исходный документ PDF.
1. Создайте `TextExtractionOptions` и основанный на регионах `TextSearchOptions`.
1. Запустите `TextAbsorber` на всех страницах и вывести извлечённый текст.

```java
public static void textAbsorberSearch(Path inputFile) {
        try (Document document = new Document(inputFile.toString())) {
            TextExtractionOptions textExtractionOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
            TextSearchOptions textSearchOptions = new TextSearchOptions(new Rectangle(0, 0, 842, 250, true));
            TextAbsorber absorber = new TextAbsorber(textExtractionOptions, textSearchOptions);

            document.getPages().accept(absorber);
            System.out.println("Text fragments found: " + absorber.getText());
        }
    }
```

## Извлеките текст с одной страницы с помощью TextAbsorber

Используйте этот пример, когда извлечение обычного текста должно быть ограничено одной страницей.

1. Откройте исходный документ PDF.
1. Настройте извлечение текста и параметры поиска для целевого региона.
1. Запустите `TextAbsorber` на выбранной странице и вывести результат.

```java
public static void textAbsorberSearchPage(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextExtractionOptions textExtractionOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
        TextSearchOptions textSearchOptions = new TextSearchOptions(new Rectangle(0, 0, 842, 250, true));
        TextAbsorber absorber = new TextAbsorber(textExtractionOptions, textSearchOptions);

        document.getPages().get_Item(2).accept(absorber);
        System.out.println("Text fragments found: " + absorber.getText());
    }
}
```

## Проверьте все текстовые фрагменты в документе

Используйте этот пример, когда вам нужен текстовый контент вместе с метаданными шрифта, позиции и цвета.

1. Откройте исходный документ PDF.
1. Запустите `TextFragmentAbsorber` по всем страницам.
1. Пройдите по фрагментам и выведите их метаданные.

```java
public static void textFragmentAbsorberSearch(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        document.getPages().accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            System.out.println("Text: " + fragment.getText());
            System.out.println("Position: " + fragment.getPosition());
            System.out.println("XIndent: " + fragment.getPosition().getXIndent());
            System.out.println("YIndent: " + fragment.getPosition().getYIndent());
            System.out.println("Font - Name: " + fragment.getTextState().getFont().getFontName());
            System.out.println("Font - IsAccessible: " + fragment.getTextState().getFont().isAccessible());
            System.out.println("Font - IsEmbedded: " + fragment.getTextState().getFont().isEmbedded());
            System.out.println("Font - IsSubset: " + fragment.getTextState().getFont().isSubset());
            System.out.println("Font Size: " + fragment.getTextState().getFontSize());
            System.out.println("Foreground Color: " + fragment.getTextState().getForegroundColor());
        }
    }
}
```

## Найдите одну фразу на определённой странице

Используйте этот пример, когда целевое слово должно быть найдено только на выбранной странице.

1. Откройте исходный документ PDF.
1. Создайте `TextFragmentAbsorber` с целевой фразой.
1. Посетите выбранную страницу и выведите позиции совпадающих фрагментов.

```java
public static void textFragmentAbsorberSearchPage(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("whale");
        document.getPages().get_Item(2).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            System.out.println("Text: " + fragment.getText());
            System.out.println("Position: " + fragment.getPosition());
        }
    }
}
```

## Продолжите последовательный поиск по страницам

Используйте этот пример, когда хотите переиспользовать один поглотитель при переходе от поиска на одной странице к следующей.

1. Откройте исходный PDF‑документ и создайте повторно используемый абсорбер.
1. Поиск на первой странице и проверка результатов.
1. Продолжайте поиск дополнительных страниц и просмотрите обновлённые совпадения.

```java
public static void textFragmentAbsorberSequentialSearch(Path inputFile) {
    Document document = new Document(inputFile.toString());
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    absorber.setPhrase("whale");

    document.getPages().get_Item(1).accept(absorber);
    for (TextFragment fragment : absorber.getTextFragments()) {
        System.out.println("Text: " + fragment.getText());
        System.out.println("Page: " + fragment.getPage().getNumber());
        System.out.println("Position: " + fragment.getPosition());
    }

    System.out.println("--");

    document.getPages().get_Item(2).accept(absorber);
    absorber.visit(document);

    for (TextFragment fragment : absorber.getTextFragments()) {
        System.out.println("Text: " + fragment.getText());
        System.out.println("Page: " + fragment.getPage().getNumber());
        System.out.println("Position: " + fragment.getPosition());
    }
}
```

## Найти фразу внутри выбранного прямоугольника

Используйте этот пример, когда сопоставление фраз должно быть ограничено областью на одной странице.

1. Откройте исходный документ PDF.
1. Создайте `TextFragmentAbsorber` с целевой фразой и основанным на прямоугольнике `TextSearchOptions`.
1. Посетите страницу и выведите позиции совпавших фрагментов.

```java
public static void textFragmentAbsorberSearchPhrase(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(
                "elephant", new TextSearchOptions(new Rectangle(0, 0, 842, 250, true)));

        document.getPages().get_Item(2).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            System.out.println("Text: " + fragment.getText());
            System.out.println("Position: " + fragment.getPosition());
        }
    }
}
```

## Поиск текста по регулярному выражению

Используйте этот пример, когда совпадения должны находиться по шаблону регулярного выражения, а не по фиксированной фразе.

1. Откройте исходный документ PDF.
1. Создайте с поддержкой regex `TextFragmentAbsorber`.
1. Посетите целевую страницу и выведите соответствующие фрагменты.

```java
public static void textFragmentAbsorberSearchRegex(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(
                Pattern.compile("\\d+\\.\\d+"), new TextSearchOptions(true));

        document.getPages().get_Item(2).accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            System.out.println("Text: " + fragment.getText());
            System.out.println("Position: " + fragment.getPosition());
        }
    }
}
```

## Поиск списка фраз по шаблонам регулярных выражений

Используйте этот пример, когда несколько целевых фраз следует найти за один проход.

1. Откройте исходный документ PDF.
1. Создайте массив шаблонов regex и передайте его в `TextFragmentAbsorber`.
1. Посетите документ и проверьте сгруппированные результаты regex.

```java
public static void textFragmentAbsorberSearchListOfPhrases(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Pattern[] patterns = new Pattern[] {
                Pattern.compile("whale"),
                Pattern.compile("elephant")
        };
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(patterns, new TextSearchOptions(true));
        document.getPages().accept(absorber);

        for (TextFragmentCollection fragments : absorber.getRegexResults().values()) {
            for (TextFragment fragment : fragments) {
                System.out.println("Text: " + fragment.getText());
                System.out.println("Position: " + fragment.getPosition());
            }
        }
    }
}
```

## Найдите текст и превратите его в гиперссылки

Используйте этот пример, когда совпадающие слова должны быть выделены и преобразованы в кликабельные ссылки.

1. Откройте исходный документ PDF.
1. Ищите целевые слова с включённым поиском по регулярным выражениям.
1. Обновите стиль текста, добавьте гиперссылки и сохраните изменённый PDF.

```java
public static void textFragmentAbsorberSearchAndAddHyperlink(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("whale|elephant");
        absorber.setTextSearchOptions(new TextSearchOptions(true));
        absorber.visit(document.getPages().get_Item(1));

        for (TextFragment fragment : absorber.getTextFragments()) {
            fragment.getTextState().setForegroundColor(Color.getBlue());
            fragment.getTextState().setUnderline(true);
            fragment.setHyperlink(new WebHyperlink("https://en.wikipedia.org/wiki/" + fragment.getText()));
        }

        document.save(inputFile.toString().replace("in.pdf", "out.pdf"));
    }
}
```

## Поиск текста по характеристикам стиля

Используйте этот пример, когда нужно проверять фрагменты на основе форматирования, например жирного или скрытого текста.

1. Откройте исходный документ PDF.
1. Запустите `TextFragmentAbsorber` на целевой странице.
1. Проверьте стиль каждого фрагмента и выведите соответствующие записи.

```java
public static void textFragmentAbsorberSearchStyledText(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.setTextSearchOptions(new TextSearchOptions(true));
        absorber.visit(document.getPages().get_Item(1));

        for (TextFragment fragment : absorber.getTextFragments()) {
            if (fragment.getTextState().getFontStyle() == FontStyles.Bold) {
                System.out.println("Bold: " + fragment.getText());
            }
            if (fragment.getTextState().isInvisible()) {
                System.out.println("Invisible: " + fragment.getText());
            }
        }
    }
}
```

## Подсвечивайте результаты поиска в отрисованных превью страниц

Используйте этот пример, когда совпадения текста следует сопоставлять с визуализированными изображениями страниц для визуального осмотра.

1. Создайте PNG-устройство с требуемым разрешением.
1. Ищите каждую страницу с `TextFragmentAbsorber` и отобразить страницу в поток изображения.
1. Запишите изображения предварительного просмотра страниц и выведите координаты фрагментов для проверки.

```java
public static void textFragmentAbsorberSearchAndHighlight(Path inputFile) throws Exception {
    int resolution = 150;
    PngDevice pngDevice = new PngDevice(new Resolution(resolution, resolution));

    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(Pattern.compile("[\\S]+"));
        absorber.setTextSearchOptions(new TextSearchOptions(true));

        for (int pageNumber = 1; pageNumber <= document.getPages().size(); pageNumber++) {
            Page page = document.getPages().get_Item(pageNumber);
            page.accept(absorber);

            try (ByteArrayOutputStream stream = new ByteArrayOutputStream()) {
                pngDevice.process(page, stream);
                Path output = Path.of(inputFile.toString().replace("_in.pdf", page.getNumber() + "_out.png"));
                Files.write(output, stream.toByteArray());
            }

            for (TextFragment textFragment : absorber.getTextFragments()) {
                Rectangle pageRect = page.getPageRect(true);
                System.out.println("TextFragment = " + textFragment.getText()
                        + " Page URY = " + pageRect.getURY()
                        + " TextFragment URY = " + textFragment.getRectangle().getURY());
            }
        }
    }
}
```


