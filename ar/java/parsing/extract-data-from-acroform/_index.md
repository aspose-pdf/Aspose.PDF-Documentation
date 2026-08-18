---
title: استخراج البيانات من AcroForm باستخدام Java
linktitle: استخراج البيانات من AcroForm
type: docs
weight: 50
url: /java/extract-data-from-acroform/
description: يسهل Aspose.PDF استخراج بيانات حقل النموذج من ملفات PDF. تعرف على كيفية استخراج البيانات من AcroForms وحفظها بتنسيق JSON أو XML أو FDF.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية استخراج البيانات من AcroForm عبر جافا
Abstract: تشرح هذه المقالة كيفية استخراج بيانات AcroForm وتصديرها من ملفات PDF باستخدام Aspose.PDF لـ Java. ويغطي قراءة جميع حقول النموذج، واسترداد قيمة الحقل بالاسم، وتصدير بيانات الحقل إلى JSON، وكتابة بيانات النموذج إلى تنسيقات XML وFDF وXFDF.
---
## استخراج كافة حقول النموذج

استخدم `com.aspose.pdf.facades.Form` لقراءة أسماء الحقول وقيمها دون العمل على نموذج كائن المستند الكامل.

1. افتح نموذج PDF المصدر باستخدام الواجهة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) حتى يمكن قراءة حقول AcroForm دون اجتياز نموذج كائن المستند بالكامل.
1. اتصل بـ `getFieldNames()` لتجميع كافة معرفات الحقول الموجودة في النموذج.
1. كرر أسماء الحقول هذه واتصل بـ`getField(fieldName)` لقراءة كل قيمة حقل.
1. قم ببناء سلسلة الإخراج من أزواج القيمة الرئيسية المستخرجة وطباعة بيانات النموذج المجمعة.
1. أغلق الواجهة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) في الكتلة `finally`.

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

## استرداد قيمة الحقل بالاسم

1. افتح نموذج PDF المصدر باستخدام الواجهة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/).
1. اتصل `getField(fieldName)` باسم الحقل المطلوب لقراءة قيمته الحالية من بيانات AcroForm.
1. طباعة قيمة الحقل المستخرج.
1. أغلق الواجهة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) في الكتلة `finally`.

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

## تصدير حقول النموذج إلى JSON

1. افتح نموذج PDF المصدر باستخدام الواجهة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/).
1. اتصل بـ `getFieldNames()` لجمع كافة معرفات الحقول المتاحة من AcroForm.
1. قم بالتكرار عبر هذه الحقول، والتخلص من الأسماء والقيم، وإنشاء سلسلة كائنات JSON.
1. اكتب نتيجة JSON إلى ملف الإخراج.
1. أغلق الواجهة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) في الكتلة `finally`.

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

## تصدير بيانات النموذج إلى XML، وFDF، وXFDF

1. قم بإنشاء الواجهة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) بدون ربط مستند حتى الآن.
1. افتح دفق الإخراج لملف XML واربط ملف PDF المصدر بالواجهة باستخدام `bindPdf(...)`.
1. اتصل بـ`exportXml(stream)` حتى يتم إجراء تسلسل لبيانات حقل النموذج الحالي بتنسيق XML.
1. أغلق واجهة [النموذج](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) بعد اكتمال التصدير.

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

1. قم بإنشاء الواجهة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) بدون ربط مستند حتى الآن.
1. افتح دفق الإخراج لملف FDF واربط ملف PDF المصدر بالواجهة باستخدام `bindPdf(...)`.
1. اتصل بـ `exportFdf(stream)` حتى يتم إجراء تسلسل لبيانات حقل النموذج بتنسيق FDF.
1. أغلق واجهة [النموذج](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) بعد اكتمال التصدير.

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

1. قم بإنشاء الواجهة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) بدون ربط مستند حتى الآن.
1. افتح دفق الإخراج لملف XFDF واربط ملف PDF المصدر بالواجهة باستخدام `bindPdf(...)`.
1. اتصل بـ `exportXfdf(stream)` حتى يتم إجراء تسلسل لبيانات حقل النموذج بتنسيق XFDF.
1. أغلق واجهة [النموذج](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) بعد اكتمال التصدير.

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
