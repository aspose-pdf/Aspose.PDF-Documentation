---
title: Extract AcroForm - استخراج بيانات النموذج من PDF في Java
linktitle: استخراج اكروفورم
type: docs
weight: 30
url: /java/extract-form/
description: استخرج القيم من حقول AcroForm في مستندات PDF باستخدام Aspose.PDF لـ Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استخراج قيم حقول النموذج من ملفات PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية استخراج البيانات من حقول AcroForm باستخدام Aspose.PDF لـ Java. يتكرر المثال عبر أسماء الحقول باستخدام واجهة النموذج، ويقرأ كل قيمة حالية، ويخزن النتيجة في خريطة للمعالجة النهائية.
---
استخدم الواجهة `Form` عندما تحتاج إلى اسم حقل بسيط لتدفق استخراج قيمة الحقل.

## استخراج القيم من كافة حقول AcroForm

1. افتح مستند نموذج PDF بالواجهة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/).
1. قم بالمراجعة عبر أسماء الحقول من الواجهة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) واقرأ كل قيمة حقل حالية في الخريطة.

```java
public static Map<String, String> getValuesFromAllFields(Path inputFile) {
    Form form = new Form(inputFile.toString());
    try {
        Map<String, String> formValues = new LinkedHashMap<>();
        for (String fieldName : form.getFieldNames()) {
            formValues.put(fieldName, form.getField(fieldName));
        }

        System.out.println(formValues);
        return formValues;
    } finally {
        form.close();
    }
}
```
