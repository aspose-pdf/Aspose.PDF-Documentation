---
title: إزالة الخلفيات من PDF باستخدام Java
linktitle: إزالة الخلفيات
type: docs
weight: 80
url: /ar/java/remove-backgrounds/
description: إزالة عناصر الخلفية من الصفحة الأولى من ملف PDF باستخدام Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إزالة الخلفيات من PDF في Java
Abstract: إزالة عناصر الخلفية من الصفحة الأولى من ملف PDF.
---

إزالة عناصر الخلفية من الصفحة الأولى من ملف PDF.

## إزالة عناصر الخلفية

يحذف المثال عناصر الخلفية الموجودة في الصفحة الأولى.

1. افتح ملف PDF المصدر باستخدام الفئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. مرّ على عناصر الصفحة بترتيب عكسي.
1. احذف العناصر من النوع pagination والنوع الفرعي background، ثم احفظ المستند.

```java
public static void removeBackground(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && artifact.getSubtype() == Artifact.ArtifactSubtype.Background) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```

## مواضيع ذات صلة

- [إضافة الخلفيات](/pdf/ar/java/add-backgrounds/)
- [العمل مع عناصر PDF](/pdf/ar/java/artifacts/)
