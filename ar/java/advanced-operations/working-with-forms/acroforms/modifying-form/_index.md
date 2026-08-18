---
title: تعديل الأكروفورم
linktitle: تعديل الأكروفورم
type: docs
weight: 45
url: /java/modifying-form/
description: قم بتعديل حقول AcroForm في مستندات PDF باستخدام Aspose.PDF لـ Java، بما في ذلك مسح النص وتعيين الحدود وحقول التصميم وإزالة الحقول.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تعديل وتخصيص حقول نموذج PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية تعديل محتوى AcroForm باستخدام Aspose.PDF لـ Java. ويغطي مسح النص من موارد نموذج الآلة الكاتبة، وإعداد حدود طول حقل النص وقراءتها، وتغيير مظهر خط حقل النموذج، وحذف حقول محددة بالاسم.
---
تتضمن صيانة النموذج غالبًا عمليات التحرير على مستوى الحقل وتنظيف موارد الصفحة ذات الصلة بالنموذج.

## مسح النص في موارد النموذج المضمنة

استخدم هذا المثال عندما يجب إفراغ محتوى نموذج الآلة الكاتبة دون إزالة كائنات النموذج نفسها.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بالتكرار من خلال موارد نموذج الصفحة وتحديد موقع نماذج الآلة الكاتبة.
1. امسح أجزاء النص الممتصة واحفظ المستند.

```java
public static void clearTextInForm(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (XForm form : document.getPages().get_Item(1).getResources().getForms()) {
            if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
                TextFragmentAbsorber absorber = new TextFragmentAbsorber();
                absorber.visit(form);

                for (TextFragment fragment : absorber.getTextFragments()) {
                    fragment.setText("");
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```

## تعيين حد لطول حقل النص

استخدم هذا المثال عندما يجب أن يقبل حقل النص عددًا محدودًا فقط من الأحرف.

1. قم بإنشاء واجهة [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/) واربط ملف PDF المصدر.
1. قم بتعيين الحد الأقصى لطول الحقل الهدف.
1. احفظ المستند المحدث.

```java
public static void setFieldLimit(Path inputFile, Path outputFile) {
    FormEditor form = new FormEditor();
    form.bindPdf(inputFile.toString());
    try {
        form.setFieldLimit("First Name", 15);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## احصل على حد لطول حقل النص

استخدم هذا المثال عندما تحتاج إلى فحص الحد الأقصى الحالي لطول حقل النص.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بالوصول إلى الحقل الهدف من مجموعة النماذج.
1. اقرأ الحد من [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/) وقم بإخراجه.

```java
public static void getFieldLimit(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Field field = document.getForm().getFields()[0];
        if (field instanceof TextBoxField textBoxField) {
            System.out.println("Limit: " + textBoxField.getMaxLen());
        }
    }
}
```

## تغيير خط حقل النموذج

استخدم هذا المثال عندما يجب أن يستخدم حقل نص موجود خطًا أو مظهرًا مختلفًا.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بالوصول إلى الهدف [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/) وقم بتعيين مظهر افتراضي جديد.
1. احفظ ملف PDF المحدث.

```java
public static void setFormFieldFont(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Field field = document.getForm().getFields()[0];
        if (field instanceof TextBoxField textBoxField) {
            textBoxField.setDefaultAppearance(new DefaultAppearance(
                    FontRepository.findFont("Calibri"), 10, com.aspose.pdf.Color.getBlack().toRgb()));
        }

        document.save(outputFile.toString());
    }
}
```

## حذف حقل النموذج بالاسم

استخدم هذا المثال عندما يجب إزالة حقل معين من AcroForm.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. حذف الحقل الهدف من النموذج حسب اسمه.
1. احفظ المستند المحدث.

```java
public static void deleteFormField(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getForm().delete("First Name");
        document.save(outputFile.toString());
    }
}
```
