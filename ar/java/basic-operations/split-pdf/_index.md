---
title: تقسيم ملفات PDF في جافا
linktitle: تقسيم ملفات PDF
type: docs
weight: 60
url: /java/split-pdf/
description: تعرف على كيفية تقسيم ملف PDF إلى ملفات PDF ذات صفحة واحدة في Java باستخدام Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تقسيم صفحات PDF باستخدام جافا
Abstract: توضح هذه المقالة كيفية تقسيم مستند PDF إلى ملفات PDF منفصلة ذات صفحة واحدة في Java باستخدام Aspose.PDF. يفتح المثال المستند المصدر، ويتكرر عبر صفحاته، وينشئ مستندًا جديدًا لكل صفحة، ويحفظ كل صفحة كملف PDF فردي.
---
يعد تقسيم ملف PDF إلى ملفات منفصلة مفيدًا عندما تحتاج إلى تصدير كل صفحة للمراجعة أو التخزين أو المعالجة النهائية.

## مثال حي

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) هو تطبيق مجاني عبر الإنترنت لاختبار تقسيم PDF في المتصفح.

[![تخصيص ملف PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

يستخدم هذا المثال فئة [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) لفتح ملف PDF والتنقل خلال صفحاته. لكل [صفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)، يتم إنشاء مستند جديد وإضافة الصفحة إليه وحفظ النتيجة كملف PDF منفصل.

لتقسيم ملف PDF إلى ملفات صفحات فردية في Java:

1. افتح ملف PDF المصدر باستخدام مُنشئ [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بالتكرار عبر كائنات [الصفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) التي يتم إرجاعها بواسطة `document.getPages()`.
1. قم بإنشاء [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) فارغ جديد لكل صفحة.
1. أضف [الصفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) الحالية إلى [المستند] الجديد(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. احفظ [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) الجديد باسم ملف فريد.
1. قم بإغلاق كلا الكائنين [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) عند اكتمال المعالجة.

## تقسيم PDF إلى ملفات من صفحة واحدة

يستند مثال Java التالي إلى `SplitDocumentExamples.java` ويحفظ الصفحات باسم `Page_1.pdf` و`Page_2.pdf` وما إلى ذلك.

```java
public static void splitDocument(Path inputFile, Path outputDir) {
    Document document = new Document(inputFile.toString());
    try {
        int pageCount = 1;
        for (Page page : document.getPages()) {
            Document newDocument = new Document();
            try {
                newDocument.getPages().add(page);
                newDocument.save(outputDir.resolve("Page_" + pageCount + ".pdf").toString());
            } finally {
                newDocument.close();
            }
            pageCount++;
        }
    } finally {
        document.close();
    }
}
```
