---
title: التحقق من حدود الأشكال في الرسوم البيانية بتنسيق PDF باستخدام Java
linktitle: التحقق من حدود الشكل
type: docs
weight: 70
url: /java/aspose-pdf-drawing-graph-shapes-bounds-check/
description: تعرف على كيفية التحقق من صحة حدود الأشكال في مجموعات الرسوم البيانية بتنسيق PDF في Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: التحقق من صحة حدود شكل الرسم البياني في ملفات PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية التحقق من صحة حدود الشكل في مجموعات الرسم البياني باستخدام Aspose.PDF لـ Java. وهو يغطي تمكين التحقق الصارم من الحدود، ومحاولة إضافة شكل خارج النطاق، ومعالجة الاستثناء الناتج مع الاستمرار في حفظ المستند.
---
استخدم `BoundsCheckMode` عندما تحتاج إلى التأكد من احتواء الأشكال داخل حاوية الرسم البياني.

## التحقق من صحة حدود شكل الرسم البياني

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أضف [صفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى المستند.
1. أنشئ حاوية [رسم بياني](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) وأضفها إلى الصفحة.
1. أنشئ الشكل [المستطيل](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) وقم بتكوين شكله الهندسي.
1. قم بتمكين التحقق الصارم من الحدود وحاول إضافة الشكل إلى مجموعة الرسم البياني باستخدام `BoundsCheckMode`.
1. تعامل مع الاستثناء إذا كان الشكل غير مناسب.
1. احفظ ملف PDF الناتج [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
