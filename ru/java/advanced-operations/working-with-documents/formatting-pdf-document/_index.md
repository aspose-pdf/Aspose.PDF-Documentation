---
title: Форматировать PDF-документы на Java
linktitle: Форматирование PDF-документа
type: docs
weight: 11
url: /ru/java/formatting-pdf-document/
description: Узнайте, как форматировать PDF‑документы, внедрять шрифты, управлять настройками просмотра и настраивать параметры отображения в Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Форматируйте окно документа, шрифты и поведение масштабирования в PDF‑файлах с помощью Java.
Abstract: В этой статье объясняется, как форматировать PDF‑документы с помощью Aspose.PDF for Java. Рассматриваются чтение и обновление настроек окна документа, встраивание шрифтов, установка шрифта по умолчанию, отображение списка шрифтов, создание подмножества встроенных шрифтов и управление начальным коэффициентом масштабирования.
---
Форматирование в Aspose.PDF for Java включает поведение просмотрщика, встраивание шрифтов и настройки отображения.

## Получите настройки окна документа

Используйте этот пример, чтобы просмотреть текущие настройки просмотра, сохранённые в существующем PDF‑документе.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Прочитайте необходимые свойства окна и отображения из документа.
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

## Установите предпочтения окна документа

Этот пример обновляет способ отображения PDF при открытии в совместимом просмотрщике.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Установите требуемые параметры окна, макета и режима страницы.
1. Сохраните обновленный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

## Встроить шрифты в существующий PDF

Используйте этот подход, когда документ должен включать необходимые шрифты для более надёжного отображения на других системах.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Включить стандартное встраивание шрифтов и перебрать шрифты, используемые каждым [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Отметьте любой не встроенный [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) объекты для встраивания.
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

## Встраивание шрифтов при создании нового PDF

Этот пример создает новый PDF и сразу назначает встроенный шрифт для текстового содержимого.

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавить [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Создайте необходимое [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/), [Текстовый сегмент](https://reference.aspose.com/pdf/java/com.aspose.pdf/textsegment/), и [СостояниеТекста](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/).
1. Разрешить цель [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) из репозитория и пометить его как встроенный.
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

Используйте этот шаблон, когда сохранённый документ должен переключаться на определённый шрифт при генерации вывода.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [PdfSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfsaveoptions/) и установить имя шрифта по умолчанию.
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

## Получите все шрифты, использованные в PDF

В этом примере перечисляются все шрифты, обнаруженные в документе, чтобы вы могли проверить их использование перед экспортом или обновлением файла.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Перечислите шрифты, возвращаемые утилитами шрифтов документа.
1. Выведите имя каждого обнаруженного [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/).

```java
public static void getAllFonts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Font font : document.getFontUtilities().getAllFonts()) {
            System.out.println(font.getFontName());
        }
    }
}
```

## Улучшить встраивание шрифтов с помощью подмножества шрифтов

Используйте этот подход, когда хотите снизить нагрузку шрифта, сохраняя встроенные данные шрифта согласованными с использованием документа.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Запустите субсеттинг шрифтов через утилиты шрифтов документа с требуемыми [Стратегия подмножества шрифтов](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontsubsetstrategy/) значения.
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

В этом примере настраивается начальный уровень масштабирования, который должен применяться при открытии PDF.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
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

## Получите коэффициент масштабирования при открытии документа

Используйте этот пример, чтобы проверить, задаёт ли PDF уже явный уровень масштабирования для своего действия открытия.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
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

