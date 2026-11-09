---
title: عدّ عناصر الترقيم في PDF باستخدام Java
linktitle: عدّ عناصر الترقيم
type: docs
weight: 40
url: /ar/java/counting-artifacts/
description: عدّ عناصر الترقيم في صفحة PDF بحسب النوع الفرعي للعلامة المائية أو الخلفية أو الرأس أو التذييل باستخدام Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: عدّ عناصر الترقيم في PDF في Java
Abstract: عدّ عناصر الترقيم في صفحة PDF بحسب النوع الفرعي للعلامة المائية أو الخلفية أو الرأس أو التذييل. يوضّح المثال طريقة العدّ باستخدام Aspose.PDF for Java.
---
## عدّ عناصر الترقيم في الصفحة

يحسب المثال عدد عناصر الترقيم في الصفحة الأولى بحسب النوع الفرعي.

1. افتح ملف PDF المصدر باستخدام الفئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اقرأ مجموعة عناصر [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) من الصفحة [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) المستهدفة.
1. مرّ على مجموعة عناصر [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/artifact/) في الصفحة واحسب عدد العناصر من كل نوع فرعي مطلوب.

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

## مواضيع ذات صلة

- [العمل مع عناصر PDF](/pdf/ar/java/artifacts/)
- [استخراج تفاصيل العلامات المائية](/pdf/ar/java/extract-watermarks/)
- [إزالة الخلفيات](/pdf/ar/java/remove-backgrounds/)
- [إزالة العلامات المائية](/pdf/ar/java/remove-watermarks/)
- [إزالة ترقيم Bates](/pdf/ar/java/remove-bates-numbering/)
- [إزالة الرؤوس والتذييلات](/pdf/ar/java/remove-headers-footers/)
