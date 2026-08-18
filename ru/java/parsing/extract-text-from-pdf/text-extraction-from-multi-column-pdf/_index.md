---
title: Улучшение извлечения текста из многоколоночных PDF-файлов
linktitle: Извлечение текста из многоколоночных PDF-файлов
type: docs
weight: 30
url: /java/text-extraction-from-multi-column-pdf/
description: Изучите методы улучшения извлечения текста из многоколоночных макетов PDF с помощью Aspose.PDF для Java.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
Макеты с несколькими столбцами часто требуют дополнительной обработки для улучшения порядка чтения и качества извлечения.

## Извлеките текст после уменьшения размера шрифта

Этот метод обновляет размеры шрифта текстового фрагмента, сохраняет скорректированный документ в памяти, а затем извлекает текст из преобразованного результата.

1. Откройте исходный PDF-файл в экземпляре [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [TextFragmentAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragmentabsorber/) и посетите все страницы документа, чтобы собрать объекты [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. Выполните итерацию по фрагментам и уменьшите размер каждого шрифта на запрошенное соотношение, чтобы перед извлечением можно было нормализовать плотную компоновку столбцов.
1. Сохраните измененный [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) в потоке байтов в памяти.
1. Снова откройте второй [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) из этого буфера памяти.
1. Создайте [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/), посетите все страницы преобразованного документа и запишите извлеченный текст в выходной файл.

```java
public static void extractTextReduceFont(Path inputFile, Path outputFile, double reduceRatio) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber fragmentAbsorber = new TextFragmentAbsorber();
        document.getPages().accept(fragmentAbsorber);
        for (TextFragment fragment : fragmentAbsorber.getTextFragments()) {
            fragment.getTextState().setFontSize((float) (fragment.getTextState().getFontSize() * reduceRatio));
        }

        ByteArrayOutputStream stream = new ByteArrayOutputStream();
        document.save(stream);
        try (Document document2 = new Document(new ByteArrayInputStream(stream.toByteArray()))) {
            TextAbsorber textAbsorber = new TextAbsorber();
            document2.getPages().accept(textAbsorber);
            Files.writeString(outputFile, textAbsorber.getText());
        }
    }
}
```

## Извлечение текста с масштабным коэффициентом

Используйте `TextExtractionOptions` в режиме чистого форматирования и настройте коэффициент масштабирования для макетов с большим количеством столбцов.

1. Откройте исходный PDF-файл в экземпляре [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) для извлечения всего документа.
1. Создайте [TextExtractionOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/textextractionoptions/) в режиме чистого форматирования, чтобы использовать поведение извлечения с учетом макета.
1. Перед посещением страниц задайте масштабный коэффициент и примените параметры экстракции к поглотителю.
1. Посетите все страницы документа и запишите извлеченный текст в выходной файл.

```java
public static void extractTextScaleFactor(Path inputFile, Path outputFile, double scaleFactor) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber textAbsorber = new TextAbsorber();
        TextExtractionOptions extractionOptions =
                new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
        extractionOptions.setScaleFactor(scaleFactor);
        textAbsorber.setExtractionOptions(extractionOptions);
        document.getPages().accept(textAbsorber);
        Files.writeString(outputFile, textAbsorber.getText());
    }
}
```
