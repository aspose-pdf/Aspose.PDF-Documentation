---
title: Извлечение необработанного текста из PDF файла
linktitle: Извлечение текста из PDF
type: docs
weight: 10
url: /ru/androidjava/extract-text-from-all-pdf/
description: В этой статье описаны различные способы извлечения текста из PDF документов с использованием Aspose.PDF для Android через Java. Из целых страниц, из конкретной части, на основе столбцов и т.д.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Извлечение текста со всех страниц PDF документа

Извлечение текста из PDF документа является распространенной задачей. В этом примере вы увидите, как Aspose.PDF для Java позволяет извлекать текст со всех страниц PDF документа.
Чтобы извлечь текст со всех страниц PDF:

1. Создайте объект класса [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber).

1. Откройте PDF, используя класс [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) и вызовите метод [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) коллекции [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
1. Класс [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) поглощает текст из документа и возвращает его в свойстве **Text**.

Следующий фрагмент кода показывает, как извлечь текст со всех страниц PDF-документа.

```java
public static void ExtractFromAllPages() {
        // Путь к каталогу документов.

        String filePath = _dataDir + "ExtractTextAll.pdf";

        // Открыть документ
        Document pdfDocument = new com.aspose.pdf.Document(filePath);

        // Создать объект TextAbsorber для извлечения текста
        TextAbsorber textAbsorber = new com.aspose.pdf.TextAbsorber();

        // Применить абсорбер для всех страниц
        pdfDocument.getPages().accept(textAbsorber);

        // Получить извлеченный текст
        String extractedText = textAbsorber.getText();
        try {
            java.io.FileWriter writer = new java.io.FileWriter(_dataDir + "extracted-text.txt", true);
            // Записать строку текста в файл
            writer.write(extractedText);
            // Закрыть поток
            writer.close();
        } catch (java.io.IOException e) {
            e.printStackTrace();
        }

    }
```


## Извлечение выделенного текста из PDF-документа

В различных сценариях извлечения текста из PDF-документа может возникнуть необходимость извлечь только выделенный текст. Для реализации этой функциональности мы добавили методы TextMarkupAnnotation.GetMarkedText() и TextMarkupAnnotation.GetMarkedTextFragments() в API. Вы можете извлечь выделенный текст из PDF-документа, отфильтровав TextMarkupAnnotation и используя упомянутые методы. Следующий фрагмент кода показывает, как можно извлечь выделенный текст из PDF-документа.

```java
public static void ExtractHighlightedText() {
        Document doc = new Document(_dataDir + "ExtractHighlightedText.pdf");
        // Перебрать все аннотации
        for (Annotation annotation : doc.getPages().get_Item(1).getAnnotations()) {
            // Отфильтровать TextMarkupAnnotation
            if (annotation.getAnnotationType() == AnnotationType.Highlight) {
                HighlightAnnotation highlightedAnnotation = (HighlightAnnotation) annotation;
                // Получить фрагменты выделенного текста
                TextFragmentCollection collection = highlightedAnnotation.getMarkedTextFragments();
                for (TextFragment tf : collection) {
                    // Показать выделенный текст
                    System.out.println(tf.getText());
                }
            }
        }
    }
```


## Доступ к элементам Text Fragment и Segment из XML

Иногда нам нужно получить доступ к элементам TextFragment или TextSegment при обработке PDF-документов, созданных из XML. Aspose.PDF for Android via Java предоставляет доступ к таким элементам по имени. Пример кода ниже показывает, как использовать эту функциональность.

```java
public static void AccessTextFragmentAndSegmentElements() {
    String inXml = "40014.xml";
    Document doc = new Document();
    doc.bindXml(_dataDir + inXml);

    TextSegment segment = (TextSegment) doc.getObjectById("boldHtml");
    segment = (TextSegment) doc.getObjectById("strongHtml");

    System.out.println(segment.getText());
}
```