---
title: قراءة قيم Form
linktitle: قراءة قيم Form
type: docs
weight: 60
url: /ar/java/reading-form-values/
description: تعلم كيفية فحص أسماء حقول نموذج PDF والقيم في Java باستخدام الواجهة Form في Aspose.PDF.
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: قراءة أسماء حقول نموذج PDF والقيم في Java
Abstract: يغطي هذا القسم تدفقات عمل قراءة النماذج بلغة Java التي تم تنفيذها في مجموعة أمثلة الواجهة Form الحالية لـ Aspose.PDF for Java. يوفر المستودع مثالًا عامًا لفحص الحقول ويستخدم ملاحظات نطاق صريحة للصفحات المتخصصة التي لا تمتلك بعد عينات Java مطابقة.
---
الجافا الفئة `FormExamples` تُظهر سير عمل معالجة النماذج الرئيسي الذي توفره واجهة برمجة التطبيقات Facades API.

## الحصول على قيم الحقول

استخدام `FormExamples.inspectFormFields(...)` لتفقد أسماء الحقول وقيمها الحالية.

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
