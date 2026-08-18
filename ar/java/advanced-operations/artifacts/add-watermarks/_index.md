---
title: إضافة علامات مائية إلى PDF في Java
linktitle: إضافة علامة مائية
type: docs
weight: 30
url: /java/add-watermarks/
description: تعرف على كيفية إضافة عناصر العلامة المائية واستخراجها وحذفها في ملفات PDF باستخدام Aspose.PDF لـ Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية إضافة علامة مائية إلى ملف PDF باستخدام جافا
Abstract: تشرح هذه المقالة كيفية إضافة عناصر العلامة المائية وفحصها وإزالتها في مستندات PDF باستخدام Aspose.PDF لـ Java. ويغطي إنشاء علامة مائية نصية مع إعدادات المحاذاة والتدوير والعتامة والخلفية وفحص عناصر العلامة المائية على الصفحة وحذفها.
---
تتيح لك عناصر العلامة المائية وضع علامات مرئية ثابتة على الصفحة دون مزجها مع محتوى المستند الرئيسي.

## استخراج آثار العلامة المائية من ملف PDF

استخدم هذا المثال عندما تحتاج إلى فحص عناصر العلامة المائية الموجودة وقراءة نصها أو موضعها.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بالتكرار من خلال مجموعة القطع الأثرية للصفحة المستهدفة.
1. قم بتصفية عناصر ترقيم الصفحات للعلامة المائية وطباعة نصوصها ومستطيلاتها.

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

## إضافة قطعة أثرية مائية

استخدم هذا المثال عندما يجب أن تعرض الصفحة علامة مائية نصية مركزية مع تدوير مخصص وعتامة وموضع في الخلفية.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [WatermarkArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/watermarkartifact/) وقم بتكوين حالة النص وإعدادات الموضع الخاصة به.
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

## حذف آثار العلامة المائية

استخدم هذا الأسلوب عندما يجب إزالة آثار العلامة المائية الموجودة من الصفحة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بالتكرار عبر مجموعة عناصر الصفحة بترتيب عكسي.
1. احذف عناصر ترقيم الصفحات التي يكون نوعها الفرعي علامة مائية، ثم احفظ المستند.

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
