---
title: إضافة علامات مائية إلى PDF في Java
linktitle: إضافة علامة مائية
type: docs
weight: 30
url: /ar/java/add-watermarks/
description: تعلم كيفية إضافة واستخراج وحذف عناصر العلامة المائية في ملفات PDF باستخدام Aspose.PDF for Java.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية إضافة علامة مائية إلى PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية إضافة وفحص وإزالة عناصر العلامة المائية في مستندات PDF باستخدام Aspose.PDF for Java. وتغطي إنشاء علامة مائية نصية مع إعدادات المحاذاة والدوران والشفافية والخلفية، وفحص عناصر العلامة المائية على صفحة، وحذفها.
---
تسمح لك عناصر العلامة المائية بوضع علامات بصرية دائمة على صفحة دون دمجها في محتوى المستند الرئيسي.

## استخراج عناصر العلامة المائية من PDF

استخدم هذا المثال عندما تحتاج إلى فحص عناصر العلامة المائية الموجودة وقراءة نصها أو موقعها.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. تكرار عبر مجموعة القطع الأثرية للصفحة المستهدفة.
1. تصفية قطع الأثر المتعلقة بالعلامة المائية للترقيم وطباعة نصها ومستطيلاتها.

```java
public static void extractWatermarkFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Artifact artifact : document.getPages().get_Item(1).getArtifacts()) {
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                System.out.println(artifact.getText() + " " + artifact.getRectangle());
            }
        }
    }
}
```

## إضافة عنصر علامة مائية

استخدم هذا المثال عندما يجب أن تعرض الصفحة علامة مائية نصية متمركزة مع دوران مخصص، وتعتيم، وتحديد موضع الخلفية.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. إنشاء [WatermarkArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/watermarkartifact/) وقم بتكوين حالة النص وإعدادات الموضع الخاصة به.
1. أضف العلامة المائية إلى الصفحة واحفظ ملف الإخراج.

```java
public static void addWatermarkArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextState textState = new TextState();
        textState.setFontSize(72);
        textState.setForegroundColor(Color.getBlueViolet());
        textState.setFontStyle(FontStyles.Bold);
        textState.setFont(FontRepository.findFont("Arial"));

        WatermarkArtifact watermark = new WatermarkArtifact();
        watermark.setTextAndState("WATERMARK", textState);
        watermark.setArtifactHorizontalAlignment(HorizontalAlignment.Center);
        watermark.setArtifactVerticalAlignment(VerticalAlignment.Center);
        watermark.setRotation(60);
        watermark.setOpacity(0.2);
        watermark.setBackground(true);

        document.getPages().get_Item(1).getArtifacts().add(watermark);
        document.save(outputFile.toString());
    }
}
```

## حذف عناصر العلامة المائية

استخدم هذا النهج عندما يجب إزالة عناصر العلامة المائية الموجودة من الصفحة.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. تكرار مجموعة عناصر الصفحة بترتيب عكسي.
1. احذف عناصر ترقيم الصفحات التي يكون النوع الفرعي لها هو العلامة المائية، ثم احفظ المستند.

```java
public static void deleteWatermarkArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```
