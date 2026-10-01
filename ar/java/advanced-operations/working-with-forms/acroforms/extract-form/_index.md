---
title: استخراج AcroForm - استخراج بيانات النموذج (Form) من PDF في Java
linktitle: استخراج AcroForm
type: docs
weight: 30
url: /ar/java/extract-form/
description: استخراج القيم من حقول AcroForm في مستندات PDF باستخدام Aspose.PDF for Java.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استخراج قيم حقول النموذج من ملفات PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية استخراج البيانات من حقول AcroForm باستخدام Aspose.PDF for Java. يمرّ المثال عبر أسماء الحقول باستخدام واجهة Form، يقرأ كل قيمة حالية، ويخزن النتيجة في خريطة للمعالجة اللاحقة.
---
استخدم `Form` واجهة عندما تحتاج إلى تدفق استخراج بسيط من اسم الحقل إلى قيمة الحقل.

## استخراج القيم من جميع حقول AcroForm

1. افتح مستند نموذج PDF باستخدام [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) واجهة.
1. التكرار عبر أسماء الحقول من [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) واجهة وقراءة كل قيمة حقل حالية في خريطة.

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
