---
title: إزالة رؤوس الصفحات وتذييلاتها من PDF باستخدام Java
linktitle: إزالة الرؤوس والتذييلات
type: docs
weight: 110
url: /ar/java/remove-headers-footers/
description: إزالة عناصر الرؤوس والتذييلات من الصفحة الأولى من ملف PDF باستخدام Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إزالة رؤوس الصفحات وتذييلاتها من PDF في Java
Abstract: إزالة عناصر الرؤوس والتذييلات من الصفحة الأولى من ملف PDF.
---

إزالة عناصر الرؤوس والتذييلات من الصفحة الأولى من ملف PDF.

## إزالة عناصر الرؤوس والتذييلات

يحذف المثال عناصر الرؤوس والتذييلات الموجودة في الصفحة الأولى.

1. افتح ملف PDF المصدر باستخدام الفئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. مرّ على عناصر الصفحة بترتيب عكسي.
1. احذف عناصر الترقيم التي يمثّل نوعها الفرعي رأسًا أو تذييلًا، ثم احفظ المستند.

```java
public static void deleteHeaderFooterArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && (artifact.getSubtype() == Artifact.ArtifactSubtype.Header
                    || artifact.getSubtype() == Artifact.ArtifactSubtype.Footer)) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```

## مواضيع ذات صلة

- [إضافة الرؤوس والتذييلات](/pdf/ar/java/artifacts-header-footer/)
- [العمل مع عناصر PDF](/pdf/ar/java/artifacts/)
