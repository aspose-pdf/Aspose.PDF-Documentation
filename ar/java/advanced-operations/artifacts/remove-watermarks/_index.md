---
title: إزالة العلامات المائية من PDF باستخدام Java
linktitle: إزالة العلامات المائية
type: docs
weight: 90
url: /ar/java/remove-watermarks/
description: إزالة عناصر العلامات المائية من الصفحة الأولى من ملف PDF باستخدام Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إزالة العلامات المائية من PDF في Java
Abstract: إزالة عناصر العلامات المائية من الصفحة الأولى من ملف PDF.
---

إزالة عناصر العلامات المائية من الصفحة الأولى من ملف PDF.

## إزالة عناصر العلامات المائية

يحذف المثال من الصفحة الأولى عناصر النوع `Pagination` والنوع الفرعي `Watermark` فقط. وتبقى في ملف PDF العلامات المائية المرئية المخزّنة كنص عادي في الصفحة أو كصور أو تعليقات توضيحية.

1. افتح ملف PDF المصدر باستخدام الفئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. مرّ على عناصر الصفحة بترتيب عكسي.
1. احذف عناصر الترقيم من النوع الفرعي Watermark، ثم احفظ المستند.

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

## مواضيع ذات صلة

- [إضافة العلامات المائية](/pdf/ar/java/add-watermarks/)
- [استخراج تفاصيل العلامات المائية](/pdf/ar/java/extract-watermarks/)
- [العمل مع عناصر PDF](/pdf/ar/java/artifacts/)
