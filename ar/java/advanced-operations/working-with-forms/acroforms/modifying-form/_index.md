---
title: تعديل AcroForm
linktitle: تعديل AcroForm
type: docs
weight: 45
url: /ar/java/modifying-form/
description: قم بتعديل حقول AcroForm في مستندات PDF باستخدام Aspose.PDF for Java، بما في ذلك مسح النص، وتحديد الحدود، وتنسيق الحقول، وإزالة الحقول.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تعديل وتخصيص حقول نموذج PDF باستخدام Java
Abstract: توضح هذه المقالة كيفية تعديل محتوى AcroForm باستخدام Aspose.PDF for Java. وتشمل مسح النص من موارد نموذج Typewriter، وتحديد وقراءة حدود طول حقول النص، وتغيير مظهر خط حقل النموذج، وحذف حقول محددة بالاسم.
---
غالبًا ما تتضمن صيانة النموذج (Form) كلًا من تحرير الحقول على مستوى الحقل وتنظيف موارد الصفحة المتعلقة بالنموذج.

## مسح النص في موارد النموذج المدمجة

استخدم هذا المثال عندما يجب إفراغ محتوى نموذج آلة الكتابة دون إزالة كائنات النموذج نفسها.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. مرّ على موارد نموذج الصفحة وحدّد نماذج الآلة الكاتبة.
1. امسح مقاطع النص المستخرجة واحفظ المستند.

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

## تعيين حد طول حقل النص

استخدم هذا المثال عندما يجب أن يقبل حقل النص عددًا محدودًا فقط من الأحرف.

1. أنشئ واجهة [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/) وربط ملف PDF المصدر.
1. عيّن الحد الأقصى للطول لحقل الهدف.
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

## احصل على حد طول حقل النص

استخدم هذا المثال عندما تحتاج إلى فحص الحد الأقصى الحالي لطول حقل النص.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. انتقل إلى الحقل المستهدف من مجموعة النماذج.
1. اقرأ الحد من [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/) وإخراجها.

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

استخدام هذا المثال عندما يجب على حقل نص موجود أن يستخدم خطًا أو مظهرًا مختلفًا.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. انتقل إلى الهدف [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/) وعيّن مظهر افتراضي جديد.
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

## حذف حقل النموذج حسب الاسم

استخدم هذا المثال عندما يجب إزالة حقل محدد من AcroForm.

1. افتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. احذف الحقل المستهدف من النموذج باستخدام اسمه.
1. احفظ المستند المحدث.

```java
public static void deleteFormField(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getForm().delete("First Name");
        document.save(outputFile.toString());
    }
}
```
