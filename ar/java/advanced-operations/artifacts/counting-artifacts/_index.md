---
title: عد القطع الأثرية PDF في جافا
linktitle: عد التحف
type: docs
weight: 40
url: /java/counting-artifacts/
description: تعرف على كيفية فحص وحساب عناصر ترقيم الصفحات في مستندات PDF باستخدام Java مع Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: عد القطع الأثرية في PDF باستخدام جافا
Abstract: تشرح هذه المقالة كيفية فحص وحساب عناصر ترقيم الصفحات في مستندات PDF باستخدام Aspose.PDF لـ Java. فهو يوضح كيفية التكرار من خلال عناصر الصفحة وحساب الأنواع الفرعية للعلامة المائية والخلفية والرأس والتذييل.
---
## عد عناصر ترقيم الصفحات على الصفحة

استخدم هذا المثال عندما تحتاج إلى إحصاء سريع للأنواع الفرعية لعناصر ترقيم الصفحات الرئيسية على الصفحة.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اقرأ مجموعة [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) من [الصفحة] المستهدفة(https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. قم بالتكرار من خلال مجموعة الصفحة [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) وقم بحساب كل نوع فرعي لترقيم الصفحات الذي تحتاج إلى الإبلاغ عنه.

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
