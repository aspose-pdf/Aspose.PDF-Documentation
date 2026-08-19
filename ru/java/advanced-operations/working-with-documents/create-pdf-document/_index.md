---
title: Создать PDF-файлы на Java
linktitle: Создать PDF документ
type: docs
weight: 10
url: /ru/java/create-pdf-document/
description: Узнайте, как создавать PDF‑файлы и создавать поисковые PDF‑документы в Java с использованием Aspose.PDF.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Создавайте PDF‑файлы и поисковые PDF‑документы с помощью Java
Abstract: В этой статье показано, как создавать PDF‑документы с помощью Aspose.PDF for Java. Описывается создание нового PDF с нуля и преобразование документа, основанного на изображении, в поисковый PDF путем предоставления вывода HOCR от внешнего OCR‑движка.
---
Aspose.PDF for Java поддерживает как простое создание документов, так и рабочие процессы создания поисковых PDF с поддержкой OCR.

## Создайте новый документ PDF

Используйте этот подход, когда вам нужно создать простой PDF‑файл с нуля.

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в документ.
1. Создайте [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) и добавить его на страницу.
1. Сохраните выходной PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void createNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment("Hello World!"));
        document.save(outputFile.toString());
    }
}
```

## Создайте PDF с возможностью поиска

{"translatedText":""} `createSearchablePdf` примеры использования `Document.convert(...)` с `CallBackGetHocr` реализация. Обратный вызов записывает исходное изображение во временный файл, вызывает Tesseract с `hocr` опция, читает сгенерированную разметку HOCR и возвращает её в Aspose.PDF.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте `CallBackGetHocr` обратный вызов и преобразовать исходный документ в PDF‑контент, доступный для поиска.
1. Сохраните обновлённый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void createSearchablePdf(Path inputFile, Path outputFile) {
    Path tempDir = outputFile.getParent().resolve("ocr-temp");
    CallBackGetHocr cbgh = new CallBackGetHocr() {
        @Override
        public String invoke(java.awt.image.BufferedImage img) {
            // save the image, run Tesseract with "hocr", and return the HOCR text
            return fileContents.toString();
        }
    };
    try (Document document = new Document(inputFile.toString())) {
        document.convert(cbgh);
        document.save(outputFile.toString());
    }
}
```

## Получите настройки окна документа

Используйте этот пример, чтобы проверить текущие настройки просмотра, хранящиеся в существующем PDF‑документе.

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

## Установите параметры окна документа

Этот пример обновляет то, как PDF должен отображаться при открытии в совместимом просмотрщике.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Установите необходимые параметры окна, макета и режима страниц.
1. Сохраните обновлённый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
1. Включить стандартное встраивание шрифтов и пройтись по шрифтам, используемым каждым [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Отметьте любые не встроенные [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) объекты для встраивания.
1. Сохраните обновлённый документ.

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

## Встраивать шрифты при создании нового PDF

Этот пример создает новый PDF и присваивает встроенный шрифт текстовому содержимому с самого начала.

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавить [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Создайте требуемое [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/), [Текстовый сегмент](https://reference.aspose.com/pdf/java/com.aspose.pdf/textsegment/), и [Состояние текста](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/).
1. Разрешить цель [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) из репозитория и пометить его как встроенный.
1. Добавьте текстовое содержание на страницу и сохраните результирующий документ.

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

## Установите Font по умолчанию для вывода PDF

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

## Получите все шрифты, используемые в PDF

Этот пример выводит список всех шрифтов, обнаруженных в документе, чтобы вы могли проверить их использование перед экспортом или обновлением файла.

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

## Улучшить встраивание шрифтов с помощью субсетирования шрифтов

Используйте этот метод, когда хотите уменьшить нагрузку шрифтов, одновременно сохраняя встроенные данные шрифта согласованными с использованием документа.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Запустите подмножество шрифтов через утилиты шрифтов документа с требуемым [Стратегия подмножества шрифтов](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontsubsetstrategy/) значения.
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

Этот пример настраивает начальный уровень масштабирования, который должен применяться при открытии PDF.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) с [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/).
1. Назначьте действие как действие при открытии документа и сохраните результат.

```java
public static void setZoomFactor(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GoToAction action = new GoToAction(new XYZExplicitDestination(1, 0.0, 0.0, 0.5));
        document.setOpenAction(action);
        document.save(outputFile.toString());
    }
}
```

## Получите коэффициент увеличения при открытии документа

Используйте этот пример, чтобы проверить, задаёт ли PDF уже явный уровень масштабирования для своей операции открытия.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Проверьте, является ли действие открытия [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) с [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/).
1. Выведите настроенное значение масштаба или сообщите, что масштаб не установлен.

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

