---
title: Класс PDFViewer
linktitle: Класс PDFViewer
type: docs
weight: 135
url: /java/pdfviewer-class/
description: Узнайте, как использовать фасад PdfViewer в Java для декодирования PDF-страниц и проверки настроек, связанных с средством просмотра.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Декодируйте PDF-страницы и проверяйте данные средства просмотра на Java с помощью PdfViewer
Abstract: В этом разделе объясняется, как использовать фасад PdfViewer в Aspose.PDF для Java для декодирования страниц и задач проверки, связанных с просмотрщиком. Текущие примеры Java охватывают преобразование всех страниц в изображения, декодирование конкретной страницы и проверку количества страниц, типа координат, разрешения и связанных настроек средства просмотра.
---
Класс Java `PdfViewerExamples` демонстрирует основные рабочие процессы средства просмотра, доступные через API фасадов.

## Декодировать все страницы PDF

Используйте этот рабочий процесс, когда каждая страница исходного PDF-файла должна быть отображена как изображение.

### Шаги

1. Создайте и настройте экземпляр `PdfViewer`.
2. Свяжите исходный PDF-файл с помощью `bindPdf`.
3. Вызовите `decodeAllPages()`, чтобы преобразовать документ в массив `BufferedImage`.
4. Сохраните каждую декодированную страницу в выходной файл изображения.
5. Закройте связанный PDF-файл.

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

Используйте этот рабочий процесс, когда в изображение необходимо преобразовать только одну страницу.

### Шаги

1. Создайте и настройте экземпляр `PdfViewer`.
2. Привяжите исходный PDF-файл.
3. Позвоните `decodePage()` для страницы, которую вы хотите отобразить.
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

## Проверка метаданных PDF

Используйте этот рабочий процесс, если вам нужна информация о документе, связанная с средством просмотра, перед рендерингом или печатью.

### Шаги

1. Создайте и настройте экземпляр `PdfViewer`.
2. Привяжите исходный PDF-файл.
3. Прочтите количество страниц, тип координат и разрешение рендеринга.
4. Используйте или распечатайте полученные значения.
5. Закройте связанный PDF-файл.

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

## Проверьте настройки связанного средства просмотра

Используйте этот рабочий процесс, если вам нужно подтвердить или настроить поведение средства просмотра после привязки PDF-файла.

### Шаги

1. Создайте и настройте экземпляр `PdfViewer`.
2. Привяжите исходный PDF-файл.
3. Установите такие параметры просмотра, как автоматическое изменение размера, автоматический поворот и видимость диалогового окна печати.
4. Прочтите активные настройки просмотра и количество страниц.
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
