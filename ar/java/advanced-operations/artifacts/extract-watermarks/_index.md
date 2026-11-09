---
title: استخراج تفاصيل العلامات المائية من PDF باستخدام Java
linktitle: استخراج تفاصيل العلامات المائية
type: docs
weight: 50
url: /ar/java/extract-watermarks/
description: قراءة النص والمستطيل المحيط بكل عنصر علامة مائية في الصفحة الأولى من ملف PDF باستخدام Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استخراج تفاصيل العلامات المائية من PDF في Java
Abstract: قراءة النص والمستطيل المحيط بكل عنصر علامة مائية في الصفحة الأولى من ملف PDF.
---

قراءة النص والمستطيل المحيط بكل عنصر علامة مائية في الصفحة الأولى من ملف PDF.

## استخراج نص العلامات المائية وحدودها

يفحص المثال عناصر العلامات المائية في الصفحة الأولى ويعرض نصوصها وحدودها.

1. افتح ملف PDF المصدر باستخدام الفئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. مرّ على مجموعة عناصر الصفحة المستهدفة.
1. رشّح عناصر الترقيم من النوع الفرعي Watermark واطبع نص كل عنصر ومستطيله المحيط.

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

## مواضيع ذات صلة

- [إضافة العلامات المائية](/pdf/ar/java/add-watermarks/)
- [إزالة العلامات المائية](/pdf/ar/java/remove-watermarks/)
- [العمل مع عناصر PDF](/pdf/ar/java/artifacts/)
