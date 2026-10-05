---
title: عدد عناصر PDF في Java
linktitle: عد العناصر
type: docs
weight: 40
url: /ar/java/counting-artifacts/
description: تعلم كيفية فحص وعدّ عناصر الترقيم في مستندات PDF باستخدام Java مع Aspose.PDF.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: عد العناصر في PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية فحص وعدّ عناصر الترقيم في مستندات PDF باستخدام Aspose.PDF for Java. تُظهر كيفية التنقل عبر عناصر الصفحة وعدّ الأنواع الفرعية للعلامة المائية، الخلفية، الترويسة، وتذييل الصفحة.
---
## عد عناصر الترقيم على صفحة

استخدم هذا المثال عندما تحتاج إلى حساب سريع لأنواع التجسيمات الفرعية الرئيسية للترقيم في صفحة.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اقرأ الـ مجموعة [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) من الهدف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. مرّ على الصفحة [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) جمع وعدّ كل نوع من أنواع الترقيم الفرعية التي تحتاج إلى الإبلاغ عنها.

```java
public static void countPdfArtifacts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        int watermarks = 0;
        int backgrounds = 0;
        int headers = 0;
        int footers = 0;

        for (Artifact artifact : document.getPages().get_Item(1).getArtifacts()) {
            if (artifact.getType() == Artifact.ArtifactType.Pagination) {
                if (artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) {
                    watermarks++;
                }
                if (artifact.getSubtype() == Artifact.ArtifactSubtype.Background) {
                    backgrounds++;
                }
                if (artifact.getSubtype() == Artifact.ArtifactSubtype.Header) {
                    headers++;
                }
                if (artifact.getSubtype() == Artifact.ArtifactSubtype.Footer) {
                    footers++;
                }
            }
        }

        System.out.println("Watermarks: " + watermarks);
        System.out.println("Backgrounds: " + backgrounds);
        System.out.println("Headers: " + headers);
        System.out.println("Footers: " + footers);
    }
}
```
