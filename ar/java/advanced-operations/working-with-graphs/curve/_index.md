---
title: إضافة أشكال المنحنيات إلى PDF في Java
linktitle: إضافة منحنى
type: docs
weight: 30
url: /ar/java/add-curve/
description: تعلم كيفية رسم وتعبئة أشكال المنحنيات في ملفات PDF باستخدام Java.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: رسم أشكال المنحنيات في ملفات PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية إضافة أشكال المنحنيات إلى مستندات PDF باستخدام Aspose.PDF for Java. وتغطي إنشاء منحنى من مصفوفات الإحداثيات وتطبيق إما لون الخط أو لون التعبئة داخل حاوية Graph.
---
يتم تعريف المنحنيات في Aspose.PDF for Java بواسطة مصفوفة إحداثيات عائمة تُمرّر إلى `Curve`.

## إضافة مخطط منحنى

1. إنشاء ملف PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إضافة [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى المستند.
1. إنشاء [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) حاوية وأضفها إلى الصفحة.
1. إنشاء [Curve](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/curve/) شكل وقم بتكوين نقاط التحكم الخاصة به.
1. أضف الـ [Curve](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/curve/) إلى الـ [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) الحاوية.
1. قم بتعيين خصائص الشكل المطلوبة في المثال، بما في ذلك [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).
1. احفظ ملف PDF الناتج [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addCurve(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 200.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Curve curve1 = new Curve(new float[]{10, 10, 50, 60, 70, 10, 100, 120});
        curve1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().addItem(curve1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
