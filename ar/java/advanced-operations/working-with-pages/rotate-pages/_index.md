---
title: تدوير صفحات PDF في Java
linktitle: تدوير صفحات PDF
type: docs
weight: 110
url: /ar/java/rotate-pages/
description: تعرف على كيفية تدوير صفحات PDF وتغيير اتجاه الصفحات في Java.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تدوير صفحات PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية تدوير صفحات PDF باستخدام Aspose.PDF for Java. تقوم العينة بالتنقل عبر جميع الصفحات في المستند، وتطبيق تدوير بزاوية 90 درجة، وحفظ ملف PDF المحدث.
---
استخدم واجهة برمجة تطبيقات تدوير الصفحات عندما تحتاج إلى تغيير الاتجاه عبر صفحة واحدة أو أكثر.

## قم بتدوير جميع الصفحات بزاوية 90 درجة

استخدم هذا المثال عندما يجب تدوير كل صفحة في المستند باتجاه عقارب الساعة.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. التكرار عبر جميع [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) الكائنات وتعيين قيمة التدوير.
1. احفظ ملف PDF المحدث.

```java
public static void rotatePage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            page.setRotate(Rotation.on90);
        }
        document.save(outputFile.toString());
    }
}
```
