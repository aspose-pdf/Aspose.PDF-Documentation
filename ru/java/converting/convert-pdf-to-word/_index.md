---
title: Конвертируйте PDF в Word на Java
linktitle: Конвертировать PDF в Word
type: docs
weight: 10
url: /java/convert-pdf-to-word/
lastmod: "2026-06-16"
description: Узнайте, как конвертировать PDF-файлы в DOC и DOCX на Java с помощью Aspose.PDF для упрощения редактирования и повторного использования документов.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как конвертировать PDF в Word на Java
Abstract: В этой статье объясняется, как конвертировать PDF-файлы в форматы Microsoft Word с помощью Aspose.PDF для Java. Он охватывает вывод DOC, вывод DOCX, преобразование DOCX с улучшенным потоком, сохранение разрывов строк, распознавание маркеров и управление разрешением изображения с помощью `DocSaveOptions`.
---
Aspose.PDF for Java может экспортировать PDF-документы в форматы Microsoft Word с различными вариантами распознавания и макета. Используйте [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/), чтобы управлять тем, как текст PDF, списки и изображения отображаются в выходные данные Word.

## Конвертировать PDF в DOC

Используйте этот пример, когда документ PDF необходимо экспортировать в устаревший формат DOC. Код создает `DocSaveOptions`, устанавливает формат `Doc` и передает параметры общему методу сохранения.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) и установите формат `Doc`.
1. Позвоните `document.save(outputFile.toString(), saveOptions)`, чтобы PDF-файл был экспортирован в двоичный формат документа Microsoft Word.
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

## Конвертировать PDF в DOCX

Используйте этот пример, когда документ PDF необходимо экспортировать как файл DOCX. DOCX является предпочтительным форматом для большинства новых рабочих процессов обработки текстов, поскольку он широко поддерживается и его легче редактировать.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) и установите формат `DocX`.
1. Вызовите `document.save(outputFile.toString(), saveOptions)`, чтобы содержимое PDF было экспортировано как документ Office Open XML Word.
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

## Преобразование PDF в DOCX с улучшенным распознаванием потока

Используйте этот пример, когда при экспорте Word следует отдавать предпочтение плавному редактируемому содержимому, а не фиксированному визуальному макету.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) для вывода `DocX`.
1. Включите `setMode(DocSaveOptions.RecognitionMode.EnhancedFlow)`, чтобы конвертер использовал расширенное распознавание потока во время генерации DOCX.
1. Вызовите `document.save(outputFile.toString(), saveOptions)` и сохраните преобразованный вывод DOCX.

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

## Конвертируйте PDF в DOCX с сохраненными разрывами строк.

Используйте этот пример, когда окончания строк из исходного PDF-файла должны быть сохранены в выходных данных Word.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) для экспорта `DocX`.
1. Включите `setAddReturnToLineEnd(true)`, чтобы во время преобразования сохранялись явные разрывы строк.
1. Позвоните `document.save(outputFile.toString(), saveOptions)` и сохраните файл DOCX.

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

## Конвертируйте PDF в DOCX с распознаванием маркеров

Используйте этот пример, когда маркеры списка из исходного PDF-файла должны быть распознаны и сохранены как структуры списка в Word.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) для экспорта `DocX`.
1. Включите `setRecognizeBullets(true)`, чтобы содержимое PDF в виде списка распознавалось как маркированные списки во время преобразования.
1. Позвоните `document.save(outputFile.toString(), saveOptions)` и сохраните файл DOCX.

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

## Конвертируйте PDF в DOCX с настраиваемым разрешением изображения

Используйте этот пример, когда во время преобразования необходимо контролировать точность изображения внутри сгенерированного DOCX.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) для экспорта `DocX`.
1. Установите `setImageResolutionX(300)` и `setImageResolutionY(300)`, чтобы растровый контент генерировался с запрошенным разрешением.
1. Вызовите `document.save(outputFile.toString(), saveOptions)` и сохраните вывод DOCX.

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
