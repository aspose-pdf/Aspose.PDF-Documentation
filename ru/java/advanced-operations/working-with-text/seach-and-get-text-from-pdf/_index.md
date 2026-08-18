---
title: Поиск и извлечение текста PDF в Java
linktitle: Поиск и получение текста
type: docs
weight: 60
url: /java/search-and-get-text-from-pdf/
description: Узнайте, как искать, проверять и извлекать текст из PDF-документов на Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Поиск текста PDF и проверка извлеченных фрагментов в Java
Abstract: В этой статье объясняется, как искать и извлекать текст из PDF-документов с помощью Aspose.PDF для Java. Он охватывает TextAbsorber и TextFragmentAbsorber, включая извлечение на основе региона, поиск по конкретным страницам, сопоставление регулярных выражений и фраз, вставку гиперссылок, проверку стилизованного текста и выделение фрагментов.
---
Aspose.PDF для Java поддерживает извлечение необработанного текста и поиск на уровне фрагментов с координатами, стилями и сопоставлением регулярных выражений.

## Извлекайте текст со всех страниц с помощью TextAbsorber

Используйте этот пример, если вам нужен простой извлеченный текст из выбранной области документа на всех страницах.

1. Откройте исходный PDF-документ.
1. Создайте `TextExtractionOptions` и `TextSearchOptions` на основе региона.
1. Запустите `TextAbsorber` на всех страницах и выведите извлеченный текст.

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

## Извлекайте текст с одной страницы с помощью TextAbsorber

Используйте этот пример, когда извлечение простого текста должно быть ограничено одной страницей.

1. Откройте исходный PDF-документ.
1. Настройте параметры извлечения текста и поиска для целевого региона.
1. Запустите `TextAbsorber` на выбранной странице и выведите результат.

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

Используйте этот пример, если вам нужно текстовое содержимое вместе с метаданными шрифта, положения и цвета.

1. Откройте исходный PDF-документ.
1. Запустите `TextFragmentAbsorber` на всех страницах.
1. Переберите фрагменты и выведите их метаданные.

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

## Поиск одной фразы на конкретной странице

Используйте этот пример, когда целевое слово должно быть найдено только на выбранной странице.

1. Откройте исходный PDF-документ.
1. Создайте `TextFragmentAbsorber` с целевой фразой.
1. Посетите выбранную страницу и выведите соответствующие позиции фрагментов.

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

## Продолжить последовательный поиск по страницам

Используйте этот пример, если вы хотите повторно использовать один поглотитель при переходе от одной страницы поиска к другой.

1. Откройте исходный PDF-документ и создайте многоразовый поглотитель.
1. Найдите первую страницу и проверьте результаты.
1. Продолжайте поиск на дополнительных страницах и просмотрите обновленные совпадения.

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

## Поиск фразы внутри выделенного прямоугольника

Используйте этот пример, когда фразовое соответствие должно быть ограничено областью на одной странице.

1. Откройте исходный PDF-документ.
1. Создайте `TextFragmentAbsorber` с целевой фразой и прямоугольником `TextSearchOptions`.
1. Посетите страницу и выведите совпадающие позиции фрагментов.

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

Используйте этот пример, когда совпадения необходимо найти по шаблону регулярного выражения, а не по фиксированной фразе.

1. Откройте исходный PDF-документ.
1. Создайте `TextFragmentAbsorber` с поддержкой регулярных выражений.
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

## Поиск по списку фраз по шаблонам регулярных выражений

Используйте этот пример, когда необходимо найти несколько целевых фраз за один проход.

1. Откройте исходный PDF-документ.
1. Создайте массив шаблонов регулярных выражений и передайте его `TextFragmentAbsorber`.
1. Посетите документ и проверьте сгруппированные результаты регулярных выражений.

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

Используйте этот пример, когда совпадающие слова необходимо выделить и преобразовать в интерактивные ссылки.

1. Откройте исходный PDF-документ.
1. Найдите целевые слова с включенным поиском по регулярным выражениям.
1. Обновите стиль текста, прикрепите гиперссылки и сохраните измененный PDF-файл.

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

Используйте этот пример, когда вам нужно проверить фрагменты на основе форматирования, например жирного или невидимого текста.

1. Откройте исходный PDF-документ.
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

## Выделение результатов поиска в предварительном просмотре страниц

Используйте этот пример, когда текстовые совпадения необходимо сопоставить с визуализированными изображениями страниц для визуальной проверки.

1. Создайте PNG-устройство с необходимым разрешением.
1. Найдите каждую страницу с помощью `TextFragmentAbsorber` и преобразуйте страницу в поток изображений.
1. Запишите изображения предварительного просмотра страницы и координаты выходного фрагмента для проверки.

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
