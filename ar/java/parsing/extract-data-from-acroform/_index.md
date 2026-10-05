---
title: استخراج البيانات من AcroForm باستخدام Java
linktitle: استخراج البيانات من AcroForm
type: docs
weight: 50
url: /ar/java/extract-data-from-acroform/
description: يجعل Aspose.PDF من السهل استخراج بيانات حقول النموذج من ملفات PDF. تعلّم كيفية استخراج البيانات من AcroForms وحفظها بصيغة JSON أو XML أو FDF.
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية استخراج البيانات من AcroForm عبر Java
Abstract: تشرح هذه المقالة كيفية استخراج وتصدير بيانات AcroForm من ملفات PDF باستخدام Aspose.PDF for Java. وتغطي قراءة جميع حقول النموذج، استرداد قيمة حقل بالاسم، تصدير بيانات الحقول إلى JSON، وكتابة بيانات النموذج إلى صيغ XML وFDF وXFDF.
---

## استخراج حقول النموذج من مستند PDF

استخدم `com.aspose.pdf.facades.Form` لقراءة أسماء الحقول والقيم دون المرور عبر نموذج كائن المستند الكامل.

1. افتح نموذج PDF المصدر باستخدام واجهة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) بحيث يمكن قراءة حقول AcroForm دون عبور نموذج كائن المستند الكامل.
1. استدعِ `getFieldNames()` لتجميع كافة معرفات الحقول الموجودة في النموذج.
1. مرّ على أسماء الحقول تلك واستدعائها `getField(fieldName)` لقراءة قيمة كل حقل.
1. أنشئ سلسلة الإخراج من أزواج المفاتيح والقيم المستخرجة واطبع بيانات النموذج المجمعة.
1. أغلق واجهة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) في ال كتلة `finally`.

```java
public static void extractFormFields(Path inputFile) {
    Form form = new Form(inputFile.toString());
    try {
        StringBuilder formValues = new StringBuilder("{");
        String[] fieldNames = form.getFieldNames();
        for (int i = 0; i < fieldNames.length; i++) {
            if (i > 0) {
                formValues.append(", ");
            }
            formValues.append(fieldNames[i]).append("=").append(form.getField(fieldNames[i]));
        }
        formValues.append("}");
        System.out.println(formValues);
    } finally {
        form.close();
    }
}
```

## استرجاع قيمة حقل النموذج بالاسم

عندما تعرف الاسم الدقيق للحقل المحدد في نموذج PDF، يمكنك استرداد قيمته مباشرةً باستخدام `getField(fieldName)`
دون التكرار عبر مجموعة الحقول بأكملها.

1. افتح نموذج PDF المصدر باستخدام واجهة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/).
1. استدعِ `getField(fieldName)` مع اسم الحقل المطلوب لقراءة قيمته الحالية من بيانات AcroForm..
1. اطبع قيمة الحقل المستخرجة.
1. أغلق واجهة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) في ال كتلة `finally`.

```java
public static void extractFormFieldByTitle(Path inputFile, String fieldName) {
    Form form = new Form(inputFile.toString());
    try {
        String formValue = form.getField(fieldName);
        System.out.println(formValue);
    } finally {
        form.close();
    }
}
```

## استخراج حقول النموذج من مستند PDF إلى JSON

يمكن أيضًا استخراج قيم حقل Form وتخزينها كـ JSON. هذا مفيد عندما يحتاج بيانات نموذج PDF إلى الاستهلاك بواسطة
تطبيقات الويب، وواجهات برمجة التطبيقات (APIs)، أو الأنظمة الأخرى التي تعمل مع JSON.

1. افتح نموذج PDF المصدر باستخدام واجهة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/).
1. استدعِ `getFieldNames()` لجمع جميع معرّفات الحقول المتاحة من AcroForm..
1. مرّ على تلك الحقول، تشفير الأسماء والقيم، وأنشئ سلسلة كائن JSON..
1. اكتب نتيجة JSON إلى ملف الإخراج.
1. أغلق واجهة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) في ال كتلة `finally`.

```java
public static void extractFormFieldsJson(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form(inputFile.toString());
    try {
        StringBuilder json = new StringBuilder();
        json.append("{\n");
        String[] fieldNames = form.getFieldNames();
        for (int i = 0; i < fieldNames.length; i++) {
            String fieldName = fieldNames[i];
            json.append("    \"").append(escapeJson(fieldName)).append("\": \"")
                    .append(escapeJson(form.getField(fieldName))).append("\"");
            if (i < fieldNames.length - 1) {
                json.append(",");
            }
            json.append("\n");
        }
        json.append("}\n");
        Files.writeString(outputFile, json.toString());
    } finally {
        form.close();
    }
}
```

## تصدير بيانات النموذج إلى XML من ملف PDF

تصدير XML مفيد عندما تحتاج بيانات نموذج PDF إلى أن تُستهلك من قبل الأنظمة التي تعمل مع بيانات XML مُهيكلة.

1. أنشئ واجهة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) دون ربط مستند بعد.
1. افتح تدفق إخراج لملف XML واربط ملف PDF المصدر بالواجهة باستخدام `bindPdf(...)`.
1. استدعِ `exportXml(stream)` لذلك يتم تسلسل بيانات حقل النموذج الحالية كـ XML..
1. أغلق واجهة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) بعد إكمال التصدير.

```java
public static void extractDataToXml(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXml(stream);
    } finally {
        form.close();
    }
}
```

## تصدير البيانات إلى FDF من ملف PDF

يُستخدم FDF (صيغة بيانات النماذج) عادةً لتبادل بيانات حقول AcroForm بشكل مستقل عن مستند PDF.

1. أنشئ واجهة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) دون ربط مستند بعد.
1. افتح تدفق إخراج لملف FDF وربط ملف PDF المصدر بالواجهة باستخدام `bindPdf(...)`.
1. استدعِ `exportFdf(stream)` لذا يتم تسلسل بيانات حقل النموذج بتنسيق FDF..
1. أغلق واجهة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) بعد إكمال التصدير.

```java
public static void extractDataToFdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportFdf(stream);
    } finally {
        form.close();
    }
}
```

## تصدير البيانات إلى XFDF من ملف PDF

XFDF هو تمثيل قائم على XML لتنسيق بيانات النماذج وهو مناسب لتبادل بيانات النماذج مع الأنظمة التي تعمل مع XML.

1. أنشئ واجهة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) دون ربط مستند بعد.
1. افتح تدفق إخراج لملف XFDF واربط ملف PDF المصدر بالواجهة باستخدام `bindPdf(...)`.
1. استدعِ `exportXfdf(stream)` لذلك يتم تسلسل بيانات حقل النموذج بتنسيق XFDF..
1. أغلق واجهة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) بعد إكمال التصدير.

```java
public static void extractDataToXfdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXfdf(stream);
    } finally {
        form.close();
    }
}
```
