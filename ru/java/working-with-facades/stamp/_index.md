---
title: Класс Stamp
linktitle: Класс Stamp
type: docs
weight: 150
url: /ru/java/stamp-class/
description: Узнайте, как работать с классом Stamp в Java, чтобы добавлять штампы изображений, PDF и текста в PDF‑документы.
lastmod: "2026-08-19"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавление штампов изображений, PDF и текста в PDF‑документы на Java
Abstract: В этом разделе объясняется, как использовать класс Stamp вместе с PdfFileStamp в Aspose.PDF for Java для добавления переиспользуемого содержания штампов в PDF‑документы. Текущие примеры на Java охватывают штампы изображений, штампы страниц PDF, текстовые штампы с пользовательским TextState, штампы, применяемые к отдельным страницам, а также фоновые штампы изображений с настройками прозрачности, размера и вращения.
---
Java `StampExamples` класс демонстрирует основные рабочие процессы создания штампов, доступные через API фасадов.

## Добавьте штамп изображения

Используйте этот рабочий процесс, когда файл изображения должен быть размещён в PDF в качестве штампа.

### Шаги

1. Создайте `PdfFileStamp` создать экземпляр и привязать исходный PDF.
2. Создайте `Stamp` объект и привяжите его к файлу изображения.
3. Установите идентификатор штампа и исходную точку размещения.
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

Используйте этот рабочий процесс, когда содержимое другой страницы PDF должно быть повторно использовано в качестве содержимого штампа.

### Шаги

1. Создайте `PdfFileStamp` экземпляр и привязать целевой PDF.
2. Создайте `Stamp` объект.
3. Привяжите штамп к определённой странице из другого PDF-файла.
4. Установите номер целевой страницы и исходную точку для размещения.
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

## Добавьте текстовую печать с TextState

Используйте этот рабочий процесс, когда печать должна содержать стилизованный текст, а не изображение.

### Шаги

1. Создайте `PdfFileStamp` создать экземпляр и привязать исходный PDF.
2. Создайте `Stamp` объект.
3. Привяжите `FormattedText` логотип и пользовательский `TextState` к штампу.
4. Установите исходную точку штампа и его вращение.
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

## Добавьте штамп на конкретные страницы

Используйте этот рабочий процесс, когда штамп должен появляться только на выбранных страницах, а не во всём документе.

### Шаги

1. Создайте `PdfFileStamp` создать экземпляр и привязать исходный PDF.
2. Создайте `Stamp` объект и привязать его к файлу изображения.
3. Установите список целевых страниц, исходную точку и размер изображения.
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

Используйте этот процесс, когда штамп должен отображаться за содержимым страницы с контролируемой непрозрачностью и поворотом.

### Шаги

1. Создайте `PdfFileStamp` создать экземпляр и привязать исходный PDF.
2. Создайте `Stamp` объект и привяжите его к файлу изображения.
3. Отметьте штамп как фон.
4. Настройте непрозрачность, качество, поворот, размер и исходную точку.
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


