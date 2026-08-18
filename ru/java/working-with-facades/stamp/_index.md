---
title: Класс штампа
linktitle: Класс штампа
type: docs
weight: 150
url: /java/stamp-class/
description: Узнайте, как работать с классом Stamp в Java, чтобы добавлять штампы изображений, PDF и текста в PDF-документы.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавление изображений, PDF-файлов и текстовых штампов в PDF-документы в Java
Abstract: В этом разделе объясняется, как использовать класс Stamp вместе с PdfFileStamp в Aspose.PDF для Java для добавления многократно используемого содержимого штампа в PDF-документы. Текущие примеры Java охватывают штампы изображений, штампы страниц PDF, текстовые штампы с пользовательским TextState, штампы для конкретных страниц и штампы фоновых изображений с настройками непрозрачности, размера и поворота.
---
Класс Java `StampExamples` демонстрирует основные рабочие процессы создания штампов, доступные через API фасадов.

## Добавьте штамп изображения

Используйте этот рабочий процесс, если файл изображения необходимо поместить в PDF-файл в качестве штампа.

### Шаги

1. Создайте экземпляр `PdfFileStamp` и привяжите исходный PDF-файл.
2. Создайте объект `Stamp` и привяжите его к файлу изображения.
3. Установите идентификатор штампа и начало размещения.
4. Добавьте штамп в документ.
5. Сохраните результат и закройте объект фасада.

### Пример Java

```java
public static void addImageStamp(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        stamp.setStampId(1);
        stamp.setOrigin(36, 520);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## Добавьте страницу PDF в качестве штампа

Используйте этот рабочий процесс, если содержимое другой страницы PDF необходимо повторно использовать в качестве содержимого штампа.

### Шаги

1. Создайте экземпляр `PdfFileStamp` и привяжите целевой PDF-файл.
2. Создайте объект `Stamp`.
3. Привяжите штамп к определенной странице из другого PDF-файла.
4. Установите номер целевой страницы и источник для размещения.
5. Добавьте штамп, сохраните результат и закройте объект фасада.

### Пример Java

```java
public static void addPdfPageAsStamp(Path inputFile, Path stampPdf, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindPdf(stampPdf.toString(), 1);
        stamp.setPageNumber(1);
        stamp.setOrigin(36, 250);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## Добавьте текстовый штамп с помощью TextState

Используйте этот рабочий процесс, если штамп должен содержать стилизованный текст, а не изображение.

### Шаги

1. Создайте экземпляр `PdfFileStamp` и привяжите исходный PDF-файл.
2. Создайте объект `Stamp`.
3. Привяжите к штампу логотип `FormattedText` и собственный `TextState`.
4. Установите начало координат и поворот штампа.
5. Добавьте штамп, сохраните результат и закройте объект фасада.

### Пример Java

```java
public static void addTextStampWithTextState(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindLogo(createTextLogo("Approved by signing workflow"));
        stamp.bindTextState(createTextState());
        stamp.setOrigin(36, 700);
        stamp.setRotation(15.0f);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## Добавьте штамп на определенные страницы

Используйте этот рабочий процесс, если штамп должен отображаться только на выбранных страницах, а не во всем документе.

### Шаги

1. Создайте экземпляр `PdfFileStamp` и привяжите исходный PDF-файл.
2. Создайте объект `Stamp` и привяжите его к файлу изображения.
3. Установите список целевых страниц, источник и размер изображения.
4. Добавьте штамп в документ.
5. Сохраните результат и закройте объект фасада.

### Пример Java

```java
public static void addStampToSpecificPages(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        stamp.setPages(new int[] {1});
        stamp.setOrigin(400, 40);
        stamp.setImageSize(120, 60);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```

## Добавьте штамп фонового изображения

Используйте этот рабочий процесс, когда штамп должен появиться позади содержимого страницы с контролируемой непрозрачностью и поворотом.

### Шаги

1. Создайте экземпляр `PdfFileStamp` и привяжите исходный PDF-файл.
2. Создайте объект `Stamp` и привяжите его к файлу изображения.
3. Отметьте штамп как фоновое содержимое.
4. Настройте непрозрачность, качество, поворот, размер и начало координат.
5. Добавьте штамп, сохраните результат и закройте объект фасада.

### Пример Java

```java
public static void addBackgroundImageStamp(Path inputFile, Path imageFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        Stamp stamp = new Stamp();
        stamp.bindImage(imageFile.toString());
        stamp.setBackground(true);
        stamp.setOpacity(0.35f);
        stamp.setQuality(90);
        stamp.setRotation(45.0f);
        stamp.setImageSize(160, 80);
        stamp.setOrigin(200, 300);
        pdfStamper.addStamp(stamp);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
