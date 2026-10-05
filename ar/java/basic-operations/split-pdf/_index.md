---
title: تقسيم ملفات PDF في Java
linktitle: تقسيم ملفات PDF
type: docs
weight: 60
url: /ar/java/split-pdf/
description: تعلم كيفية تقسيم ملف PDF إلى ملفات PDF بصفحة واحدة في Java باستخدام Aspose.PDF.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تقسيم صفحات PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية تقسيم مستند PDF إلى ملفات PDF منفصلة بصفحة واحدة في Java باستخدام Aspose.PDF. يفتح المثال المستند المصدر، ويتنقل عبر صفحاته، وينشئ مستندًا جديدًا لكل صفحة، ويحفظ كل صفحة كملف PDF منفصل.
---
يكون تقسيم ملف PDF إلى ملفات منفصلة مفيدًا عندما تحتاج إلى تصدير كل صفحة للمراجعة أو التخزين أو المعالجة اللاحقة.

## مثال حي

[Aspose.PDF مقسم](https://products.aspose.app/pdf/splitter) هو تطبيق مجاني عبر الإنترنت لاختبار تقسيم PDF في المتصفح.

[![Aspose تقسيم PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

هذا المثال يستخدم فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) لفتح ملف PDF والتنقل عبر صفحاته. لكل [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)، ينشئ مستندًا جديدًا، يضيف الصفحة إليه، ويحفظ النتيجة كملف PDF منفصل.

لتقسيم ملف PDF إلى ملفات صفحات فردية في Java:

1. افتح ملف PDF المصدر باستخدام [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) المُنشئ.
1. مرّ على الكائنات [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) التي تم إرجاعها بواسطة `document.getPages()`.
1. أنشئ جديد فارغ [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) لكل صفحة.
1. أضف الحالي [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى الجديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. احفظ الجديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) باسم ملف فريد.
1. أغلق كليهما الكائنات [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) عندما تكتمل المعالجة.

## قسّم PDF إلى ملفات صفحة واحدة

المثال التالي بلغة Java مبني على `SplitDocumentExamples.java` ويحفظ الصفحات كـ `Page_1.pdf`, `Page_2.pdf`، وما إلى ذلك.

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
