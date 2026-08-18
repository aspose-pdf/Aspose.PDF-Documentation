---
title: ملء AcroForm - ملء نموذج PDF باستخدام جافا
linktitle: ملء اكروفورم
type: docs
weight: 20
url: /java/fill-form/
description: املأ حقول AcroForm في مستند PDF باستخدام Aspose.PDF لـ Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: املأ حقول AcroForm في ملفات PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية ملء حقول AcroForm باستخدام Aspose.PDF لـ Java. يقوم المثال بتحميل ملف PDF من خلال واجهة النموذج، ومطابقة أسماء الحقول مع خريطة القيمة، وتحديث الحقول المطابقة، وحفظ المستند المكتمل.
---
يمكن استخدام الواجهة `Form` لأتمتة محتوى الحقل في AcroForm موجود.

## املأ حقول AcroForm بقيم جديدة

1. افتح مستند نموذج PDF بالواجهة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/).
1. قم بالتكرار عبر حقول النموذج وقم بتحديث الإدخالات المطابقة بالقيم المقدمة.
1. احفظ مستند PDF المحدث.

```java
public static void fillForm(Path inputFile, Path outputFile) {
    Map<String, String> newFieldValues = Map.of(
            "First Name", "Alexander_New",
            "Last Name", "Greenfield_New",
            "City", "Yellowtown_New",
            "Country", "Redland_New");

    Form form = new Form(inputFile.toString());
    try {
        for (String fieldName : form.getFieldNames()) {
            if (newFieldValues.containsKey(fieldName)) {
                form.fillField(fieldName, newFieldValues.get(fieldName));
            }
        }
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
