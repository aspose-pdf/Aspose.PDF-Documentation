---
title: Форматирование PDF-документов в Java
linktitle: Форматирование PDF-документа
type: docs
weight: 11
url: /java/formatting-pdf-document/
description: Узнайте, как форматировать PDF-документы, встраивать шрифты, управлять настройками средства просмотра и настраивать параметры отображения в Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Форматирование окна документа, шрифты и поведение масштабирования в файлах PDF с помощью Java
Abstract: В этой статье объясняется, как форматировать PDF-документы с помощью Aspose.PDF для Java. Он охватывает чтение и обновление настроек окна документа, встраивание шрифтов, установку шрифта по умолчанию, составление списка шрифтов, выделение подмножеств встроенных шрифтов и управление исходным коэффициентом масштабирования.
---
Форматирование в Aspose.PDF для Java включает поведение средства просмотра, встраивание шрифтов и настройки отображения.

## Получите настройки окна документа

Используйте этот пример, чтобы проверить текущие настройки средства просмотра, хранящиеся в существующем PDF-документе.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Прочитайте необходимое окно и отобразите свойства из документа.
1. Выведите текущие настройки для проверки или отладки.

```java
public static void getDocumentWindow(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("CenterWindow: " + document.isCenterWindow());
        System.out.println("Direction: " + document.getDirection());
        System.out.println("DisplayDocTitle: " + document.isDisplayDocTitle());
        System.out.println("FitWindow: " + document.isFitWindow());
        System.out.println("HideMenuBar: " + document.isHideMenubar());
        System.out.println("HideToolBar: " + document.isHideToolBar());
        System.out.println("HideWindowUI: " + document.isHideWindowUI());
        System.out.println("NonFullScreenPageMode: " + document.getNonFullScreenPageMode());
        System.out.println("PageLayout: " + document.getPageLayout());
        System.out.println("PageMode: " + document.getPageMode());
    }
}
```

## Установите настройки окна документа

В этом примере обновляется способ отображения PDF-файла при его открытии в совместимом средстве просмотра.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Установите необходимые параметры окна, макета и режима страницы.
1. Сохраните обновленный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void setDocumentWindow(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.setCenterWindow(true);
        document.setDirection(Direction.R2L);
        document.setDisplayDocTitle(true);
        document.setFitWindow(true);
        document.setHideMenubar(true);
        document.setHideToolBar(true);
        document.setHideWindowUI(true);
        document.setNonFullScreenPageMode(PageMode.UseOC);
        document.setPageLayout(PageLayout.TwoColumnLeft);
        document.setPageMode(PageMode.UseThumbs);
        document.save(outputFile.toString());
    }
}
```

## Встраивание шрифтов в существующий PDF-файл

Используйте этот подход, когда документ должен содержать необходимые шрифты для более надежного рендеринга в других системах.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Включите встраивание стандартных шрифтов и перебирайте шрифты, используемые каждой [Страницей](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Отметьте все невстроенные объекты [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) для встраивания.
1. Сохраните обновленный документ.

```java
public static void embeddedFonts(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.setEmbedStandardFonts(true);
        for (Page page : document.getPages()) {
            for (Font pageFont : page.getResources().getFonts()) {
                if (!pageFont.isEmbedded()) {
                    pageFont.setEmbedded(true);
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```

## Встраивание шрифтов при создании нового PDF-файла

В этом примере создается новый PDF-файл и с самого начала назначается встроенный шрифт текстовому содержимому.

1. Создайте новый PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавьте [Страницу](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Создайте необходимые [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/), [TextSegment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textsegment/) и [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/).
1. Разрешите целевой [Шрифт](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) из репозитория и отметьте его как встроенный.
1. Добавьте текстовое содержимое на страницу и сохраните выходной документ.

```java
public static void embeddedFontsInNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            TextFragment fragment = new TextFragment("");
            TextSegment segment = new TextSegment(" This is a sample text using Custom font.");
            TextState textState = new TextState();
            Font font = FontRepository.findFont("Arial");
            font.setEmbedded(true);
            textState.setFont(font);
            segment.setTextState(textState);
            fragment.getSegments().add(segment);
            page.getParagraphs().add(fragment);
        }
        document.save(outputFile.toString());
    }
}
```

## Установите шрифт по умолчанию для вывода PDF

Используйте этот шаблон, когда сохраненный документ должен использовать определенный шрифт во время создания вывода.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [PdfSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfsaveoptions/) и установите имя шрифта по умолчанию.
1. Сохраните документ с настроенными параметрами сохранения.

```java
public static void setDefaultFont(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PdfSaveOptions saveOptions = new PdfSaveOptions();
        saveOptions.setDefaultFontName("Arial");
        document.save(outputFile.toString(), saveOptions);
    }
}
```

## Получите все шрифты, используемые в PDF-файле

В этом примере перечислены все шрифты, обнаруженные в документе, поэтому вы можете проверить использование шрифтов перед экспортом или обновлением файла.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Перечислите шрифты, возвращаемые утилитами шрифтов документа.
1. Выведите имя каждого обнаруженного [Шрифта](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/).

```java
public static void getAllFonts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Font font : document.getFontUtilities().getAllFonts()) {
            System.out.println(font.getFontName());
        }
    }
}
```

## Улучшите встраивание шрифтов путем подмножества шрифтов.

Используйте этот подход, если вы хотите уменьшить полезную нагрузку шрифта, сохраняя при этом данные встроенных шрифтов в соответствии с использованием документа.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Запустите поднабор шрифтов с помощью утилит шрифтов документа с необходимыми значениями [FontSubsetStrategy](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontsubsetstrategy/).
1. Сохраните оптимизированный документ.

```java
public static void improveFontsEmbedding(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getFontUtilities().subsetFonts(FontSubsetStrategy.SubsetAllFonts);
        document.getFontUtilities().subsetFonts(FontSubsetStrategy.SubsetEmbeddedFontsOnly);
        document.save(outputFile.toString());
    }
}
```

## Установите коэффициент масштабирования при открытии документа

В этом примере настраивается начальный уровень масштабирования, который должен применяться при открытии PDF-файла.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) с [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/).
1. Назначьте действие как действие открытия документа и сохраните результат.

```java
public static void setZoomFactor(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GoToAction action = new GoToAction(new XYZExplicitDestination(1, 0.0, 0.0, 0.5));
        document.setOpenAction(action);
        document.save(outputFile.toString());
    }
}
```

## Получите коэффициент масштабирования открытого документа

Используйте этот пример, чтобы проверить, определяет ли PDF-файл явный уровень масштабирования для действия открытия.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Проверьте, является ли действие открытия [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) с [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/).
1. Выведите настроенное значение масштабирования или сообщите, что масштаб не установлен.

```java
public static void getZoomFactor(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getOpenAction() instanceof GoToAction action
                && action.getDestination() instanceof XYZExplicitDestination destination) {
            System.out.println("Zoom: " + destination.getZoom());
        } else {
            System.out.println("Zoom: not set");
        }
    }
}
```
