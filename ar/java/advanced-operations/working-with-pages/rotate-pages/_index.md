---
title: تدوير صفحات PDF في جافا
linktitle: تدوير صفحات PDF
type: docs
weight: 110
url: /java/rotate-pages/
description: تعرف على كيفية تدوير صفحات PDF وتغيير اتجاه الصفحة في Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تدوير صفحات PDF مع جافا
Abstract: تشرح هذه المقالة كيفية تدوير صفحات PDF باستخدام Aspose.PDF لـ Java. يتكرر المثال عبر كل الصفحات في المستند، ويطبق تدويرًا بمقدار 90 درجة، ويحفظ ملف PDF المحدث.
---
استخدم واجهة برمجة تطبيقات تدوير الصفحة عندما تحتاج إلى تغيير الاتجاه عبر صفحة واحدة أو أكثر.

## قم بتدوير كافة الصفحات بمقدار 90 درجة

استخدم هذا المثال عندما يجب تدوير كل صفحة في المستند في اتجاه عقارب الساعة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بالتكرار عبر كافة كائنات [الصفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) وقم بتعيين قيمة التدوير.
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
