---
title: Конвертировать PDF в Word на Java
linktitle: Конвертировать PDF в Word
type: docs
weight: 10
url: /ru/java/convert-pdf-to-word/
lastmod: "2026-08-19"
description: Узнайте, как конвертировать PDF‑файлы в DOC и DOCX на Java с помощью Aspose.PDF для более простого редактирования и повторного использования документов.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как конвертировать PDF в Word на Java
Abstract: В этой статье объясняется, как конвертировать PDF-файлы в форматы Microsoft Word с использованием Aspose.PDF for Java. Описываются вывод в DOC, вывод в DOCX, улучшенное преобразование DOCX с сохранением потоков, сохранение разрывов строк, распознавание маркеров и контроль разрешения изображений с помощью `DocSaveOptions`.
---
Aspose.PDF for Java может экспортировать PDF‑документы в форматы Microsoft Word с различными вариантами распознавания и макета. Используйте [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) чтобы контролировать, как текст PDF, списки и изображения преобразуются в вывод Word.

## Конвертировать PDF в DOC

Используйте этот пример, когда PDF‑документ должен быть экспортирован в устаревший формат DOC. Код создает `DocSaveOptions`, устанавливает формат в `Doc`, и передает параметры общему методу сохранения.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) и установить формат `Doc`.
1. Вызовите `document.save(outputFile.toString(), saveOptions)` поэтому PDF экспортируется в двоичный формат документа Microsoft Word.
1. Сохраните преобразованный файл DOC.

```java
public static void convertPdfToDoc(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.Doc);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразуйте PDF в DOCX

Используйте этот пример, когда PDF‑документ должен быть экспортирован в файл DOCX. DOCX является предпочтительным форматом для большинства новых рабочих процессов обработки текста, потому что он широко поддерживается и проще в редактировании.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) и установить формат `DocX`.
1. Вызовите `document.save(outputFile.toString(), saveOptions)` поэтому содержимое PDF экспортируется как документ Word в формате Office Open XML.
1. Сохраните полученный файл DOCX.

```java
public static void convertPdfToDocx(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Конвертировать PDF в DOCX с улучшенным распознаванием потока

Используйте этот пример, когда экспорт в Word должен отдавать предпочтение редактируемому текучему содержимому вместо фиксированного визуального макета.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) для `DocX` вывод.
1. Включить `setMode(DocSaveOptions.RecognitionMode.EnhancedFlow)` поэтому конвертер использует улучшенное распознавание потока при генерации DOCX.
1. Вызовите `document.save(outputFile.toString(), saveOptions)` и сохранить преобразованный вывод DOCX.

```java
public static void convertPdfToDocxAdvanced(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setMode(DocSaveOptions.RecognitionMode.EnhancedFlow);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Конвертировать PDF в DOCX с сохранёнными переносами строк

Используйте этот пример, когда окончания строк из исходного PDF должны сохраняться в выводе Word.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) для `DocX` экспорт.
1. Включить `setAddReturnToLineEnd(true)` поэтому явные разрывы строк сохраняются при конвертации.
1. Вызовите `document.save(outputFile.toString(), saveOptions)` и сохраните файл DOCX.

```java
public static void convertPdfToDocxWithLineBreaks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setAddReturnToLineEnd(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Конвертировать PDF в DOCX с распознаванием маркеров

Используйте этот пример, когда маркеры списков из исходного PDF должны быть распознаны и сохранены как структуры списков в Word.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) для `DocX` экспорт.
1. Включить `setRecognizeBullets(true)` поэтому содержимое PDF, похожее на списки, распознаётся как маркированные списки при конвертации.
1. Вызовите `document.save(outputFile.toString(), saveOptions)` и сохраните файл DOCX.

```java
public static void convertPdfToDocxWithBulletRecognition(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setRecognizeBullets(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Конвертировать PDF в DOCX с пользовательским разрешением изображения

Используйте этот пример, когда необходимо контролировать точность изображения внутри генерируемого DOCX во время конвертации.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) для `DocX` экспорт.
1. Установите `setImageResolutionX(300)` и `setImageResolutionY(300)` поэтому растровый контент генерируется с запрошенным разрешением.
1. Вызовите `document.save(outputFile.toString(), saveOptions)` и сохранить вывод DOCX.

```java
public static void convertPdfToDocxWithImageResolution(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setImageResolutionX(300);
        saveOptions.setImageResolutionY(300);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```


