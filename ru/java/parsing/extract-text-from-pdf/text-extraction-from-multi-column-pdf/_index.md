---
title: Улучшение извлечения текста из многоколоночных PDF
linktitle: Извлечение текста из многоколоночных PDF
type: docs
weight: 30
url: /ru/java/text-extraction-from-multi-column-pdf/
description: Изучите методы улучшения извлечения текста из многоколоночных макетов PDF с помощью Aspose.PDF for Java.
lastmod: "2026-09-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
Многоколоночные макеты часто требуют дополнительной обработки для улучшения порядка чтения и качества извлечения.

## Извлечение текста после уменьшения размера шрифта

Эта методика обновляет размеры шрифтов фрагментов текста, сохраняет скорректированный документ в память, а затем извлекает текст из преобразованного результата.

1. Откройте исходный PDF в экземпляре [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [TextFragmentAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragmentabsorber/) и посетите все страницы документа, чтобы собрать объекты [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. Переберите фрагменты и уменьшите размер шрифта каждого с заданным коэффициентом, чтобы нормализовать плотный многоколоночный макет перед извлечением.
1. Сохраните скорректированный [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) в поток байтов в памяти.
1. Откройте второй [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) из этого буфера памяти.
1. Создайте [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/), пройдите по всем страницам преобразованного документа и запишите извлеченный текст в выходной файл.

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

## Извлечение текста с коэффициентом масштабирования

Используйте `TextExtractionOptions` в режиме чистого форматирования и настройте коэффициент масштабирования для макетов с большим количеством столбцов.

1. Откройте исходный PDF в экземпляре [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) для извлечения текста из всего документа.
1. Создайте [TextExtractionOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/textextractionoptions/) в режиме чистого форматирования, чтобы использовалось извлечение с учётом макета.
1. Установите коэффициент масштабирования и примените параметры извлечения к абсорберу перед обходом страниц.
1. Обойдите все страницы документа и запишите извлечённый текст в выходной файл.

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


