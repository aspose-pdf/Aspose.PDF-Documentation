---
title: استخراج النص الخام من ملف PDF
linktitle: استخراج النص من PDF
type: docs
weight: 10
url: ar/androidjava/extract-text-from-all-pdf/
description: تصف هذه المقالة طرقًا مختلفة لاستخراج النصوص من مستندات PDF باستخدام Aspose.PDF لنظام Android عبر Java. من صفحات كاملة، من جزء محدد، بناءً على الأعمدة، إلخ.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## استخراج النص من جميع صفحات مستند PDF

يُعد استخراج النص من مستند PDF مطلبًا شائعًا. في هذا المثال، سترى كيف يسمح Aspose.PDF لـ Java باستخراج النص من جميع صفحات مستند PDF. لاستخراج النص من جميع صفحات PDF:

1. قم بإنشاء كائن من فئة [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber).

1. افتح ملف PDF باستخدام فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) واستدعِ طريقة [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) من مجموعة [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
2. تقوم فئة [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) بامتصاص النص من المستند وإرجاعه في خاصية **Text**.

يوضح لك مقطع الكود التالي كيفية استخراج النص من جميع صفحات مستند PDF.

```java
public static void ExtractFromAllPages() {
        // المسار إلى دليل المستندات.

        String filePath = _dataDir + "ExtractTextAll.pdf";

        // افتح المستند
        Document pdfDocument = new com.aspose.pdf.Document(filePath);

        // إنشاء كائن TextAbsorber لاستخراج النص
        TextAbsorber textAbsorber = new com.aspose.pdf.TextAbsorber();

        // قبول المستخلص لجميع الصفحات
        pdfDocument.getPages().accept(textAbsorber);

        // الحصول على النص المستخرج
        String extractedText = textAbsorber.getText();
        try {
            java.io.FileWriter writer = new java.io.FileWriter(_dataDir + "extracted-text.txt", true);
            // كتابة سطر من النص إلى الملف
            writer.write(extractedText);
            // إغلاق التدفق
            writer.close();
        } catch (java.io.IOException e) {
            e.printStackTrace();
        }

    }
```


## استخراج النص المميز من مستند PDF

في مختلف السيناريوهات لاستخراج النص من مستند PDF، قد تواجه متطلبًا لاستخراج النص المميز فقط من مستند PDF. من أجل تنفيذ هذه الوظيفة، قمنا بإضافة طريقتي TextMarkupAnnotation.GetMarkedText() و TextMarkupAnnotation.GetMarkedTextFragments() في API. يمكنك استخراج النص المميز من مستند PDF عن طريق تصفية TextMarkupAnnotation واستخدام الطرق المذكورة. يوضح مقطع الشيفرة التالي كيفية استخراج النص المميز من مستند PDF.

```java
public static void ExtractHighlightedText() {
        Document doc = new Document(_dataDir + "ExtractHighlightedText.pdf");
        // قم بالتكرار عبر جميع التعليقات التوضيحية
        for (Annotation annotation : doc.getPages().get_Item(1).getAnnotations()) {
            // قم بتصفية TextMarkupAnnotation
            if (annotation.getAnnotationType() == AnnotationType.Highlight) {
                HighlightAnnotation highlightedAnnotation = (HighlightAnnotation) annotation;
                // استرجاع أجزاء النص المميز
                TextFragmentCollection collection = highlightedAnnotation.getMarkedTextFragments();
                for (TextFragment tf : collection) {
                    // عرض النص المميز
                    System.out.println(tf.getText());
                }
            }
        }
    }
```


## الوصول إلى عناصر Text Fragment و Segment من XML

أحيانًا نحتاج إلى الوصول إلى عناصر TextFragment أو TextSegment عند معالجة مستندات PDF المولدة من XML. يوفر Aspose.PDF for Android عبر Java إمكانية الوصول إلى هذه العناصر بالاسم. يُظهر مقتطف الكود أدناه كيفية استخدام هذه الوظيفة.

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