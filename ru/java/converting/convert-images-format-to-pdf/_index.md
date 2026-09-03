---
title: Конвертировать форматы изображений в PDF на Java
linktitle: Конвертировать изображения в PDF
type: docs
weight: 60
url: /ru/java/convert-images-format-to-pdf/
lastmod: "2026-08-19"
description: Узнайте, как конвертировать BMP, CGM, DICOM, PNG, TIFF, EMF, SVG, CDR и другие форматы изображений в PDF на Java с помощью Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Как конвертировать изображения в PDF на Java
Abstract: В этой статье объясняется, как конвертировать несколько форматов изображений в PDF с помощью Aspose.PDF for Java. Описывается непосредственное размещение изображения на новой странице PDF, а также параметры загрузки, специфичные для типов файлов CGM, SVG и CDR.
---
Aspose.PDF for Java может конвертировать множество растровых и векторных форматов изображений в PDF‑документы.

## Преобразуйте BMP в PDF

Используйте этот пример, когда BMP‑изображение должно быть вставлено в PDF‑документ.

1. Создайте пустой [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) для хранения выходного PDF.
1. Добавьте [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и разместить BMP с `page.addImage(...)`.
1. Определите целевой прямоугольник изображения с [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) поэтому растровый контент заполняет область страницы PDF.
1. Сохраните выходной PDF‑файл.

```java
public static void convertBmpToPdf(Path inputFile, Path outputFile) {
        try (Document document = new Document()) {
            try (Page page = document.getPages().add()) {
                page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
            }
            document.save(outputFile.toString());
        }
        System.out.println(inputFile + " converted into " + outputFile);
    }
```

## Преобразуйте CGM в PDF

Используйте этот пример, когда файл графики CGM должен быть преобразован в PDF.

1. Откройте источник CGM, передав путь к файлу и [`CgmLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/cgmloadoptions/) в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) конструктор.
1. Позвольте Aspose.PDF интерпретировать поток графики CGM при загрузке документа.
1. Сохраните преобразованный PDF в целевой путь вывода.

```java
public static void convertCgmToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new CgmLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Конвертируйте DICOM в PDF

Используйте этот пример, когда медицинское изображение DICOM следует обернуть в документ PDF.

1. Создайте пустой [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) для вывода PDF.
1. Создайте [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) объект, установить его [`ImageFileType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagefiletype/) к `Dicom`, и назначьте путь к исходному файлу.
1. Добавьте [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и добавить изображение DICOM в коллекцию абзацев страницы.
1. Сохраните результат как PDF.

```java
public static void convertDicomToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        Image image = new Image();
        image.setFileType(ImageFileType.Dicom);
        image.setFile(inputFile.toString());

        try (Page page = document.getPages().add()) {
            page.getParagraphs().add(image);
        }

        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Конвертируйте EMF в PDF с прямой загрузкой документа

Используйте этот пример, когда файл EMF должен быть преобразован в PDF через основной путь загрузки EMF.

1. Создайте пустой [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и откройте источник EMF как бинарный поток.
1. Добавьте [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и очистить его поля, чтобы графика EMF могла занимать всю площадь страницы.
1. Создайте [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/), привяжите к нему поток EMF и добавьте его в коллекцию абзацев страницы.
1. Сохраните выходной PDF‑файл.

```java
public static void convertEmfToPdf01(Path inputFile, Path outputFile) throws IOException {
    try (Document document = new Document();
         FileInputStream imageStream = new FileInputStream(inputFile.toFile())) {
        try (Page page = document.getPages().add()) {
            page.getPageInfo().getMargin().setBottom(0);
            page.getPageInfo().getMargin().setTop(0);
            page.getPageInfo().getMargin().setLeft(0);
            page.getPageInfo().getMargin().setRight(0);

            Image image = new Image();
            image.setFileType(ImageFileType.Unknown);
            image.setImageStream(imageStream);
            page.getParagraphs().add(image);
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Конвертируйте EMF в PDF с альтернативным рабочим процессом

Используйте этот пример, когда содержимое EMF должно быть преобразовано с использованием альтернативной настройки или потока композиции страниц.

1. Загрузите источник EMF с помощью Aspose.Imaging и отрендерите его в поток PNG в памяти перед размещением в PDF.
1. Создайте пустой [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавить [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Создайте [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) из промежуточного потока байтов и добавить его на страницу.
1. Сохраните преобразованный PDF.

```java
public static void convertEmfToPdf02(Path inputFile, Path outputFile) throws IOException {
    try (Document document = new Document();
         com.aspose.imaging.Image emfImage = com.aspose.imaging.Image.load(inputFile.toString());
         ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream()) {
        emfImage.save(byteArrayOutputStream, new PngOptions());

        try (Page page = document.getPages().add()) {
            Image image = new Image();
            image.setImageStream(new ByteArrayInputStream(byteArrayOutputStream.toByteArray()));
            page.getParagraphs().add(image);
        }

        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразуйте GIF в PDF

Используйте этот пример, когда нужно добавить GIF‑изображение на страницу PDF.

1. Создайте пустой [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) для вывода PDF.
1. Добавьте [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и разместите GIF с `page.addImage(...)`.
1. Определите границы размещения с помощью [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) поэтому изображение заполняет область страницы.
1. Сохраните выходной PDF.

```java
public static void convertGifToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразуйте JPEG в PDF

Используйте этот пример, когда JPEG‑изображение должно быть преобразовано в одностраничный PDF.

1. Создайте пустой [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) для выходного PDF.
1. Добавьте [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и вставьте JPEG‑изображение с `page.addImage(...)`.
1. Используйте [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) чтобы контролировать, как растровое изображение сопоставляется с координатами страницы.
1. Сохраните сгенерированный файл PDF.

```java
public static void convertJpegToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Конвертируйте PNG в PDF

Используйте этот пример, когда PNG‑изображение должно быть упаковано в документ PDF.

1. Создайте пустой [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) для вывода преобразования.
1. Добавьте [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и разместите PNG‑изображение на нём с `page.addImage(...)`.
1. Используйте [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) изменить размер изображения относительно холста страницы.
1. Сохраните выходной файл.

```java
public static void convertPngToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразуйте SVG в PDF

Используйте этот пример, когда графику SVG необходимо отобразить внутри PDF‑документа.

1. Откройте исходный SVG, передав путь к файлу и [`SvgLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgloadoptions/) в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) конструктор.
1. Позвольте Aspose.PDF разбирать разметку SVG и создавать соответствующую графическую модель PDF при загрузке.
1. Сохраните вывод PDF в целевой путь файла.

```java
public static void convertSvgToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new SvgLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Конвертируйте TIFF в PDF

Используйте этот пример, когда TIFF‑изображение должно быть преобразовано в PDF.

1. Создайте пустой [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) для вывода PDF.
1. Добавьте [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и разместите изображение TIFF с `page.addImage(...)`.
1. Определите область размещения с помощью [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) поэтому содержимое TIFF отображается в координатах страницы.
1. Сохраните результат как PDF.

```java
public static void convertTiffToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Конвертируйте CDR в PDF

Используйте этот пример, когда файл CorelDRAW CDR должен быть преобразован в PDF.

1. Откройте источник CDR, передав путь к файлу и [`CdrLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/cdrloadoptions/) в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) конструктор.
1. Позвольте Aspose.PDF загрузить содержимое CorelDRAW в модель PDF‑документа.
1. Сохраните преобразованный PDF-файл в указанный путь вывода.

```java
public static void convertCdrToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new CdrLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```


