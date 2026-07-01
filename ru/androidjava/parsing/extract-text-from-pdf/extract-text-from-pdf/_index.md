---
title: Извлечение сырого текста из PDF‑файла
linktitle: Извлечь текст из PDF
type: docs
weight: 10
url: /ru/androidjava/extract-text-from-all-pdf/
description: В этой статье описываются различные способы извлечения текста из PDF‑документов с использованием Aspose.PDF for Android via Java. Из целых страниц, из определённой части, на основе колонок и т.д.
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Извлечение текста со всех страниц PDF‑документа

Извлечение текста из PDF‑документа является распространённой задачей. В этом примере вы увидите, как Aspose.PDF for Java позволяет извлекать текст со всех страниц PDF‑документа.
Для извлечения текста со всех страниц PDF:

1. Создайте объект [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) класс.
1. Откройте PDF, используя [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) класс и вызовите [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) метод [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) коллекция.
1. Этот [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) класс извлекает текст из документа и возвращает его в свойстве **Text** .

В следующем фрагменте кода показано, как извлечь текст со всех страниц PDF‑документа.

```java
public static void ExtractFromAllPages() {
        // The path to the documents directory.

        String filePath = _dataDir + "ExtractTextAll.pdf";

        // Open document
        Document pdfDocument = new com.aspose.pdf.Document(filePath);

        // Create TextAbsorber object to extract text
        TextAbsorber textAbsorber = new com.aspose.pdf.TextAbsorber();

        // Accept the absorber for all the pages
        pdfDocument.getPages().accept(textAbsorber);

        // Get the extracted text
        String extractedText = textAbsorber.getText();
        try {
            java.io.FileWriter writer = new java.io.FileWriter(_dataDir + "extracted-text.txt", true);
            // Write a line of text to the file
            writer.write(extractedText);
            // Close the stream
            writer.close();
        } catch (java.io.IOException e) {
            e.printStackTrace();
        }

    }
```

## Извлечение выделенного текста из PDF Document

В различных сценариях извлечения текста из PDF‑документа может возникнуть требование извлекать только выделенный текст из PDF‑документа. Чтобы реализовать эту функцию, мы добавили методы TextMarkupAnnotation.GetMarkedText() и TextMarkupAnnotation.GetMarkedTextFragments() в API. Вы можете извлекать выделенный текст из PDF‑документа, фильтруя TextMarkupAnnotation и используя указанные методы. Следующий фрагмент кода показывает, как можно извлечь выделенный текст из PDF‑документа.

```java
public static void ExtractHighlightedText() {
        Document doc = new Document(_dataDir + "ExtractHighlightedText.pdf");
        // Loop through all the annotations
        for (Annotation annotation : doc.getPages().get_Item(1).getAnnotations()) {
            // Filter TextMarkupAnnotation
            if (annotation.getAnnotationType() == AnnotationType.Highlight) {
                HighlightAnnotation highlightedAnnotation = (HighlightAnnotation) annotation;
                // Retrieve highlighted text fragments
                TextFragmentCollection collection = highlightedAnnotation.getMarkedTextFragments();
                for (TextFragment tf : collection) {
                    // Display highlighted text
                    System.out.println(tf.getText());
                }
            }
        }
    }
```

## Получить доступ к элементам Text Fragment и Segment из XML

Иногда нам нужно получить доступ к элементам TextFragement или TextSegment при обработке PDF‑документов, сгенерированных из XML. Aspose.PDF for Android via Java предоставляет доступ к таким элементам по имени. Пример кода ниже показывает, как использовать эту функциональность.

  public static void AccessTextFragmentAndSegmentElements() {
        String inXml = \u002240014.xml\u0022;
        Document doc = new Document();
        doc.bindXml(_dataDir \u002B inXml);

        TextSegment segment = (TextSegment) doc.getObjectById(\u0022boldHtml\u0022);
        segment = (TextSegment) doc.getObjectById("strongHtml");

        System.out.println(segment.getText());
        
    }
```

