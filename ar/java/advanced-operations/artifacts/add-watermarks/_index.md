---
title: إضافة علامات مائية إلى PDF باستخدام Java
linktitle: إضافة العلامات المائية
type: docs
weight: 30
url: /ar/java/add-watermarks/
description: إضافة علامات مائية نصية منسّقة إلى صفحات PDF باستخدام Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إضافة علامات مائية إلى PDF في Java
Abstract: إضافة علامات مائية نصية منسّقة إلى صفحات PDF.
---

تضيف عناصر العلامات المائية علامات مرئية إلى الصفحة بمعزل عن المحتوى الرئيسي للمستند.

## إضافة عنصر علامة مائية

يضع المثال علامة مائية نصية في وسط الصفحة مع ضبط زاوية الدوران والعتامة وموضعها في الخلفية.

1. افتح ملف PDF المصدر باستخدام الفئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أنشئ كائنًا من الفئة [WatermarkArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/watermarkartifact/) واضبط حالة النص وموضع العلامة المائية.
1. أضف العلامة المائية إلى الصفحة واحفظ ملف PDF الناتج.

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

## مواضيع ذات صلة

- [استخراج تفاصيل العلامات المائية](/pdf/ar/java/extract-watermarks/)
- [إزالة العلامات المائية](/pdf/ar/java/remove-watermarks/)
- [العمل مع عناصر PDF](/pdf/ar/java/artifacts/)
