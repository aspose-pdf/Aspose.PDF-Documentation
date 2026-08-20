---
title: Класс PdfViewer
linktitle: Класс PdfViewer
type: docs
weight: 135
url: /ru/java/pdfviewer-class/
description: Узнайте, как использовать фасад PdfViewer в Java для декодирования страниц PDF и проверки настроек, связанных с просмотрщиком.
lastmod: "2026-08-19"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Декодируйте страницы PDF и проверяйте данные просмотрщика в Java с помощью PdfViewer
Abstract: В этом разделе объясняется, как использовать фасад PdfViewer в Aspose.PDF for Java для задач декодирования страниц и проверки связанных с просмотрщиком параметров. Текущие примеры на Java охватывают рендеринг всех страниц в изображения, декодирование конкретной страницы и проверку количества страниц, типа координат, разрешения и привязанных настроек просмотрщика.
---
Джава `PdfViewerExamples` Класс демонстрирует основные рабочие процессы просмотра, доступные через Facades API.

## Декодировать все страницы PDF

Используйте этот рабочий процесс, когда каждая страница исходного PDF должна быть отрисована как изображение.

### Шаги

1. Создайте и настроить `PdfViewer` экземпляр.
2. Привяжите исходный PDF к `bindPdf`.
3. Вызовите `decodeAllPages()` отобразить документ в `BufferedImage` массив.
4. Сохраните каждую декодированную страницу в выходной файл изображения.
5. Закройте связанный PDF‑файл.

### Пример Java

```java
public static void decodeAllPages(Path inputFile, Path outputDir) throws Exception {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        BufferedImage[] pages = viewer.decodeAllPages();
        for (int index = 0; index < pages.length; index++) {
            ImageIO.write(pages[index], "png", outputDir.resolve("decode_all_pages_" + (index + 1) + ".png").toFile());
        }
    } finally {
        viewer.closePdfFile();
    }
}
```

## Декодировать конкретную страницу PDF

Используйте этот рабочий процесс, если нужно отобразить только одну страницу в виде изображения.

### Шаги

1. Создайте и настроить `PdfViewer` экземпляр.
2. Привяжите исходный PDF.
3. Вызовите `decodePage()` для страницы, которую вы хотите отобразить.
4. Сохраните декодированную страницу в выходной файл изображения.
5. Закройте просмотрщик.

### Пример Java

```java
public static void decodeSpecificPage(Path inputFile, Path outputFile) throws Exception {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        ImageIO.write(viewer.decodePage(1), "png", outputFile.toFile());
    } finally {
        viewer.close();
    }
}
```

## Просмотреть метаданные PDF

Используйте этот рабочий процесс, когда вам нужна информация о документе, связанная с просмотрщиком, перед рендерингом или печатью.

### Шаги

1. Создайте и настроить `PdfViewer` экземпляр.
2. Привяжите исходный PDF.
3. Прочитайте количество страниц, тип координат и разрешение рендеринга.
4. Используйте или выведите полученные значения.
5. Закройте связанный PDF‑файл.

### Пример Java

```java
public static void inspectPdfMetadata(Path inputFile) {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        System.out.println("Page count: " + viewer.getPageCount());
        System.out.println("Coordinate type: " + viewer.getCoordinateType());
        System.out.println("Resolution: " + viewer.getResolution());
    } finally {
        viewer.closePdfFile();
    }
}
```

## Проверьте привязанные настройки просмотрщика

Используйте этот рабочий процесс, когда необходимо подтвердить или скорректировать поведение просмотрщика после привязки PDF.

### Шаги

1. Создайте и настроить `PdfViewer` экземпляр.
2. Привяжите исходный PDF.
3. Установите параметры просмотрщика, такие как автоизменение размера, автоповорот и видимость диалогового окна печати.
4. Прочитайте активные настройки просмотрщика и количество страниц.
5. Закройте просмотрщик.

### Пример Java

```java
public static void inspectBoundViewerSettings(Path inputFile) {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        viewer.setAutoResize(true);
        viewer.setAutoRotate(true);
        viewer.setPrintPageDialog(false);
        System.out.println("Page count: " + viewer.getPageCount());
        System.out.println("Print as image: " + viewer.getPrintAsImage());
        System.out.println("Auto resize: " + viewer.getAutoResize());
        System.out.println("Auto rotate: " + viewer.getAutoRotate());
    } finally {
        viewer.close();
    }
}
```


