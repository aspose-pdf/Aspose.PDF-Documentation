---
title: استخراج النص الخام من ملف PDF
linktitle: استخراج النص من PDF
type: docs
weight: 10
url: /ar/androidjava/extract-text-from-all-pdf/
description: تصفّح هذه المقالة الطرق المختلفة لاستخراج النص من مستندات PDF باستخدام Aspose.PDF for Android عبر Java. من الصفحات الكاملة، من جزء محدد، بناءً على الأعمدة، إلخ.
lastmod: "2026-06-30"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## استخراج النص من جميع صفحات مستند PDF

استخراج النص من مستند PDF هو طلب شائع. في هذا المثال، سترى كيف يتيح Aspose.PDF for Java استخراج النص من جميع صفحات مستند PDF.
لاستخراج النص من جميع صفحات PDF:

1. إنشاء كائن من [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) فئة.
1. افتح ملف PDF باستخدام [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) فئة واستدعِ [قبول](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) طريقة الـ [صفحات](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) مجموعة.
1. ال [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) الفئة تمتص النص من المستند وتعيده في **Text** خاصية.

يعرض لك مقطع الشيفرة التالي كيفية استخراج النص من جميع صفحات مستند PDF.

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

## استخراج النص المبرز من مستند PDF

في سيناريوهات مختلفة لاستخراج النص من مستند PDF، قد تحتاج إلى استخراج النص المبرز فقط من مستند PDF. لتنفيذ هذه الوظيفة، قمنا بإضافة طريقتي TextMarkupAnnotation.GetMarkedText() و TextMarkupAnnotation.GetMarkedTextFragments() في الـ API. يمكنك استخراج النص المبرز من مستند PDF عن طريق تصفية TextMarkupAnnotation واستخدام الطريقتين المذكورتين. يوضح مقطع الشيفرة التالي كيفية استخراج النص المبرز من مستند PDF.

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

## الوصول إلى مقطع النص وعناصر الجزء من XML

في بعض الأحيان نحتاج إلى الوصول إلى عناصر TextFragement أو TextSegment عند معالجة مستندات PDF التي تم إنشاؤها من XML. يوفر Aspose.PDF for Android via Java إمكانية الوصول إلى هذه العناصر بالاسم. يوضح مقتطف الشيفرة أدناه كيفية استخدام هذه الوظيفة.

  public static void AccessTextFragmentAndSegmentElements() {
        String inXml = \u002240014.xml\u0022;
        Document doc = new Document();
        doc.bindXml(_dataDir \u002B inXml);

        TextSegment segment = (TextSegment) doc.getObjectById(\u0022boldHtml\u0022);
        segment = (TextSegment) doc.getObjectById("strongHtml");

        System.out.println(segment.getText());
        
    }
```

