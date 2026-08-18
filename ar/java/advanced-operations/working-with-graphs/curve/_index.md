---
title: إضافة أشكال منحنى إلى PDF في Java
linktitle: أضف منحنى
type: docs
weight: 30
url: /java/add-curve/
description: تعرف على كيفية رسم الأشكال المنحنية وتعبئتها في ملفات PDF بلغة Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: رسم الأشكال المنحنية في ملفات PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية إضافة أشكال منحنية إلى مستندات PDF باستخدام Aspose.PDF لـ Java. It covers creating a curve from coordinate arrays and applying either stroke color or fill color inside a Graph container.
---
يتم تعريف المنحنيات في Aspose.PDF لـ Java بواسطة مصفوفة إحداثيات عائمة تم تمريرها إلى `Curve`.

## إضافة مخطط منحنى

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أضف [صفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى المستند.
1. أنشئ حاوية [رسم بياني](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) وأضفها إلى الصفحة.
1. قم بإنشاء الشكل [المنحنى](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/curve/) وقم بتكوين نقاط التحكم الخاصة به.
1. أضف [المنحنى](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/curve/) إلى حاوية [الرسم البياني](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).
1. قم بتعيين خصائص الشكل التي يتطلبها المثال، بما في ذلك [اللون](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).
1. احفظ ملف PDF الناتج [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
