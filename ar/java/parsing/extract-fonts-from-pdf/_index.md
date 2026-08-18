---
title: استخراج الخطوط من PDF عبر جافا
linktitle: استخراج الخطوط من PDF
type: docs
weight: 30
url: /java/extract-fonts-from-pdf/
description: استخدم Aspose.PDF لـ Java لفحص الخطوط المستخدمة في مستند PDF واستخراجها.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية استخراج الخطوط من PDF باستخدام جافا
Abstract: تشرح هذه المقالة كيفية فحص الخطوط المستخدمة في مستند PDF باستخدام Aspose.PDF لـ Java. فهو يوضح كيفية فتح ملف PDF، والاتصال بـ `getFontUtilities().getAllFonts()`، والتكرار عبر كائنات الخطوط الناتجة لقراءة أسمائها.
---
استخدم استخراج الخطوط عندما تحتاج إلى تدقيق طباعة المستندات، أو فحص الموارد المضمنة، أو التحقق من استخدام الخط قبل سير عمل التحويل أو الأرشفة.

1. افتح ملف PDF المصدر في مثيل [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. اتصل بـ`document.getFontUtilities().getAllFonts()` لجمع كل مورد [الخط](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) المشار إليه في المستند.
1. قم بالمراجعة عبر كائنات [الخط](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) المستخرجة واقرأ اسم كل خط من البيانات التعريفية للخط.
1. اطبع أسماء الخطوط حتى يمكن تدقيق طباعة المستند أو تصديرها.

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
