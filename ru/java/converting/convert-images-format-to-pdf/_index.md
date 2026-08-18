---
title: Преобразование форматов изображений в PDF в Java
linktitle: Конвертируйте изображения в PDF
type: docs
weight: 60
url: /java/convert-images-format-to-pdf/
lastmod: "2026-06-16"
description: Узнайте, как конвертировать BMP, CGM, DICOM, PNG, TIFF, EMF, SVG, CDR и другие форматы изображений в PDF на Java с помощью Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Как конвертировать изображения в PDF в Java
Abstract: В этой статье объясняется, как конвертировать несколько форматов изображений в PDF с помощью Aspose.PDF для Java. Он охватывает прямое размещение изображений на новой странице PDF, а также параметры загрузки для конкретных типов файлов для входных данных CGM, SVG и CDR.
---
Aspose.PDF для Java может конвертировать многие форматы растровых и векторных изображений в документы PDF.

## Конвертировать BMP в PDF

Используйте этот пример, когда изображение BMP необходимо поместить в документ PDF.

1. Создайте пустой [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) для хранения выходного PDF-файла.
1. Добавьте [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и поместите BMP с `page.addImage(...)`.
1. Определите прямоугольник целевого изображения с помощью [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/), чтобы растровое содержимое заполнило область страницы PDF.
1. Сохраните выходной PDF-файл.

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

## Конвертировать CGM в PDF

Используйте этот пример, когда графический файл CGM необходимо преобразовать в PDF.

1. Откройте исходный код CGM, передав путь к файлу и [`CgmLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/cgmloadoptions/) в конструктор [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Позвольте Aspose.PDF интерпретировать графический поток CGM во время загрузки документа.
1. Сохраните преобразованный PDF-файл в целевой путь вывода.

```java
public static void convertCgmToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new CgmLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Конвертировать DICOM в PDF

Используйте этот пример, когда медицинское изображение DICOM необходимо обернуть в документ PDF.

1. Создайте пустой [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) для вывода PDF.
1. Создайте объект [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/), установите для его [`ImageFileType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagefiletype/) значение `Dicom` и назначьте путь к исходному файлу.
1. Добавьте [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и добавьте изображение DICOM в коллекцию абзацев страницы.
1. Сохраните результат в формате PDF.

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

Используйте этот пример, когда файл EMF необходимо преобразовать в PDF с помощью основного пути загрузки EMF.

1. Создайте пустой [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и откройте источник EMF как двоичный поток.
1. Добавьте [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и очистите его поля, чтобы изображение EMF могло занимать всю площадь страницы.
1. Создайте [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/), привяжите к нему поток EMF и добавьте его в коллекцию абзацев страницы.
1. Сохраните выходной PDF-файл.

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

## Преобразование EMF в PDF с помощью альтернативного рабочего процесса

Используйте этот пример, когда содержимое EMF необходимо преобразовать с использованием альтернативной настройки или процесса составления страницы.

1. Загрузите источник EMF с помощью Aspose.Imaging и визуализируйте его в поток PNG в памяти перед размещением в PDF.
1. Создайте пустой [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавьте [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Создайте [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) из промежуточного потока байтов и добавьте его на страницу.
1. Сохраните преобразованный PDF-файл.

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

## Конвертировать GIF в PDF

Используйте этот пример, когда изображение GIF необходимо добавить на страницу PDF.

1. Создайте пустой [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) для вывода PDF.
1. Добавьте [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и поместите GIF с `page.addImage(...)`.
1. Определите границы размещения с помощью [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/), чтобы изображение заполнило всю область страницы.
1. Сохраните выходной PDF-файл.

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

## Конвертировать JPEG в PDF

Используйте этот пример, когда изображение JPEG необходимо преобразовать в одностраничный PDF-файл.

1. Создайте пустой [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) для выходного PDF-файла.
1. Добавьте [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и вставьте изображение JPEG с `page.addImage(...)`.
1. Используйте [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/), чтобы управлять тем, как растровое изображение сопоставляется с координатами страницы.
1. Сохраните созданный PDF-файл.

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

## Конвертировать PNG в PDF

Используйте этот пример, когда изображение PNG необходимо обернуть в документ PDF.

1. Создайте пустой [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) для вывода преобразования.
1. Добавьте [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и поместите на него изображение PNG с `page.addImage(...)`.
1. Используйте [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/), чтобы изменить размер изображения по размеру холста страницы.
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

## Конвертировать SVG в PDF

Используйте этот пример, когда изображение SVG должно отображаться внутри документа PDF.

1. Откройте исходный код SVG, передав путь к файлу и [`SvgLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgloadoptions/) в конструктор [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Позвольте Aspose.PDF проанализировать разметку SVG и создать соответствующую графическую модель PDF во время загрузки.
1. Сохраните вывод PDF по целевому пути к файлу.

```java
public static void convertSvgToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new SvgLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Конвертировать TIFF в PDF

Используйте этот пример, когда изображение TIFF необходимо преобразовать в PDF.

1. Создайте пустой [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) для вывода PDF.
1. Добавьте [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и поместите изображение TIFF с `page.addImage(...)`.
1. Определите область размещения с помощью [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/), чтобы содержимое TIFF сопоставлялось с координатами страницы.
1. Сохраните результат в формате PDF.

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

## Конвертировать CDR в PDF

Используйте этот пример, когда файл CorelDRAW CDR необходимо преобразовать в PDF.

1. Откройте исходный код CDR, передав путь к файлу и [`CdrLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/cdrloadoptions/) в конструктор [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Позвольте Aspose.PDF загрузить содержимое CorelDRAW в модель документа PDF.
1. Сохраните преобразованный PDF-файл в требуемом пути вывода.

```java
public static void convertCdrToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new CdrLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
