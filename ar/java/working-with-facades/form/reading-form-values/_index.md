---
title: قيم نموذج القراءة
linktitle: قيم نموذج القراءة
type: docs
weight: 60
url: /java/reading-form-values/
description: تعرف على كيفية فحص أسماء حقول نموذج PDF وقيمها في Java باستخدام واجهة النموذج في Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: اقرأ أسماء حقول نموذج PDF وقيمها في Java
Abstract: يغطي هذا القسم مسارات عمل قراءة نماذج Java التي تم تنفيذها في مثال واجهة النموذج الحالية المعينة لـ Aspose.PDF لـ Java. يوفر المستودع مثالاً عامًا للفحص الميداني ويستخدم ملاحظات نطاق واضحة للصفحات المتخصصة التي لا تحتوي حتى الآن على عينات Java مطابقة.
---
توضح فئة Java `FormExamples` مسارات عمل معالجة النماذج الرئيسية التي كشفت عنها واجهة برمجة التطبيقات Facades.

## الحصول على قيم الحقل

استخدم `FormExamples.inspectFormFields(...)` لفحص أسماء الحقول وقيمها الحالية.

```java
public static void inspectFormFields(Path inputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        System.out.println("Field names: " + Arrays.toString(form.getFieldNames()));
        for (String fieldName : form.getFieldNames()) {
            System.out.println(fieldName + " = " + form.getField(fieldName));
        }
    } finally {
        form.close();
    }
}
```
