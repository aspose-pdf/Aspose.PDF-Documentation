---
title: العمل مع طبقات PDF باستخدام Java
linktitle: العمل مع طبقات PDF
type: docs
weight: 50
url: /ar/java/working-with-pdf-layers/
description: تعلم كيفية إضافة، وقفل، واستخراج، وتسطيح، ودمج طبقات PDF في Java.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إدارة طبقات PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية العمل مع طبقات PDF، المعروفة أيضًا بمجموعات المحتوى الاختياري، باستخدام Aspose.PDF for Java. تعلم كيفية إضافة طبقات إلى صفحة، قفل طبقة موجودة، استخراج محتوى الطبقة إلى ملفات أو تدفقات، تسطيح المحتوى المتعدد الطبقات، ودمج الطبقات في واحدة.
---
Aspose.PDF for Java تعرض طبقات PDF من خلال الـ `Layer` API على كل صفحة. يمكنك إنشاء مجموعات محتوى اختيارية، تعديل سلوكها، وتصدير محتواها أو تسطيحه عند الحاجة.

## إضافة طبقات إلى صفحة PDF

1. إنشاء PDF جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إضافة [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) إلى المستند.
1. إنشاء وتكوين المطلوب [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/) الكائنات على الصفحة.
1. حفظ ملف PDF الناتج [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

المثال الكامل يُنشئ ثلاث طبقات منفصلة بمحتوى خطوط أحمر وأخضر وأزرق.

## قفل طبقة

1. فتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. الوصول إلى الهدف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) واحصل على [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/) مجموعة.
1. قفل الهدف [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/).
1. احفظ ملف PDF المحدث [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
