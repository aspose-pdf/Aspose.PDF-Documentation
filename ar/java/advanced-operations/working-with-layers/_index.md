---
title: العمل مع طبقات PDF باستخدام Java
linktitle: العمل مع طبقات PDF
type: docs
weight: 50
url: /java/working-with-pdf-layers/
description: تعرف على كيفية إضافة طبقات PDF وقفلها واستخراجها وتسويتها ودمجها في Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إدارة طبقات PDF باستخدام Java
Abstract: يشرح هذا المقال كيفية العمل مع طبقات PDF، المعروفة أيضًا بمجموعات المحتوى الاختيارية، باستخدام Aspose.PDF لـ Java. تعرف على كيفية إضافة طبقات إلى الصفحة، وقفل طبقة موجودة، واستخراج محتوى الطبقة إلى ملفات أو تدفقات، وتسوية محتوى الطبقات، ودمج الطبقات في طبقة واحدة.
---
يعرض Aspose.PDF for Java طبقات PDF من خلال `Layer` API في كل صفحة. يمكنك إنشاء مجموعات محتوى اختيارية، وتعديل سلوكها، وتصدير محتواها أو تعديله عند الحاجة.

## إضافة طبقات إلى صفحة PDF

1. قم بإنشاء ملف PDF جديد [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أضف [صفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى المستند.
1. قم بإنشاء وتكوين كائنات [الطبقة](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/) المطلوبة على الصفحة.
1. احفظ ملف PDF الناتج [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addLayers(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Layer layer = new Layer("oc1", "Red Line");
        layer.getContents().add(new SetRGBColorStroke(1, 0, 0));
        layer.getContents().add(new MoveTo(500, 700));
        layer.getContents().add(new LineTo(400, 700));
        layer.getContents().add(new Stroke());
        page.getLayers().add(layer);

        document.save(outputFile.toString());
    }
}
```

يقوم المثال الكامل بإنشاء ثلاث طبقات منفصلة بمحتوى خط أحمر وأخضر وأزرق.

## قفل طبقة

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بالوصول إلى [الصفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) المستهدفة واحصل على مجموعة [الطبقة](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/) الخاصة بها.
1. قفل الهدف [الطبقة](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/).
1. احفظ ملف PDF المحدث [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void lockLayer(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        if (!page.getLayers().isEmpty()) {
            Layer layer = page.getLayers().getFirst();
            layer.lock();
            document.save(outputFile.toString());
        }
    }
}
```
