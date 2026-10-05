---
title: تحقق من حدود الشكل في الرسوم البيانية PDF باستخدام Java
linktitle: تحقق من حدود الشكل
type: docs
weight: 70
url: /ar/java/checking-shape-bounds/
description: تعلم كيفية التحقق من صحة حدود الشكل في مجموعات الرسوم البيانية PDF باستخدام Java.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تحقق من صحة حدود شكل الرسم البياني في ملفات PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية التحقق من صحة حدود الشكل في مجموعات Graph باستخدام Aspose.PDF for Java. تغطي تمكين فحص الحدود الصارم، ومحاولة إضافة شكل خارج النطاق، ومعالجة الاستثناء الناتج مع الاستمرار في حفظ المستند.
---
استخدم `BoundsCheckMode` عندما تحتاج إلى التأكد من أن الأشكال تتناسب داخل حاوية الرسم البياني.

## تحقق من حدود شكل الرسم البياني

1. أنشئ PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أضف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى المستند.
1. أنشئ كائنًا من الفئة [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) حاوية وأضفها إلى الصفحة.
1. أنشئ شكل [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) واضبط هندسته.
1. فعّل التحقق الصارم من الحدود ومحاولة إضافة الشكل إلى مجموعة الرسوم البيانية باستخدام `BoundsCheckMode`.
1. تعامل مع الاستثناء إذا لم يتناسب الشكل.
1. احفظ ملف PDF الناتج [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void checkShapeBounds(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(100.0, 100.0);
        graph.setTop(10);
        graph.setLeft(15);
        graph.setBorder(new BorderInfo(BorderSide.Box, 1, Color.getBlack()));
        page.getParagraphs().add(graph);

        Rectangle rectangle = new Rectangle(-1, 0, 50, 50);
        rectangle.getGraphInfo().setFillColor(Color.getTomato());
        try {
            graph.getShapes().updateBoundsCheckMode(BoundsCheckMode.ThrowExceptionIfDoesNotFit);
            graph.getShapes().addItem(rectangle);
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }

        document.save(outputFile.toString());
    }
}
```
