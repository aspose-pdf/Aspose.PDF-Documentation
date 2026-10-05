---
title: استخراج الخطوط من PDF باستخدام Java
linktitle: استخراج الخطوط من PDF
type: docs
weight: 30
url: /ar/java/extract-fonts-from-pdf/
description: استخدم Aspose.PDF for Java لفحص واستخراج الخطوط المستخدمة في مستند PDF.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية استخراج الخطوط من PDF باستخدام Java
Abstract: يوضح هذا المقال كيفية فحص الخطوط المستخدمة في مستند PDF باستخدام Aspose.PDF for Java. يوضح كيفية فتح PDF، واستدعاء `getFontUtilities().getAllFonts()`، والتجول عبر كائنات الخط الناتجة لقراءة أسمائها.
---
استخدم استخراج الخطوط عندما تحتاج إلى تدقيق طباعية المستند، فحص الموارد المدمجة، أو التحقق من استخدام الخط قبل عمليات التحويل أو سير عمل الأرشفة.

1. افتح ملف PDF المصدر في مثيل [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. استدعِ `document.getFontUtilities().getAllFonts()` لجمع كل [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) المورد المشار إليه من قبل المستند.
1. مرّ على المستخرج الكائنات [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) واقرأ اسم كل خط من البيانات الوصفية للخط.
1. اطبع أسماء الخطوط حتى يمكن تدقيق أو تصدير تنسيق المستند.

```java
public static void extractFonts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Font[] fonts = document.getFontUtilities().getAllFonts();
        for (Font font : fonts) {
            System.out.println(font.getFontName());
        }
    }
}
```
