---
title: استيراد وتصدير بيانات النموذج (Form)
linktitle: استيراد وتصدير بيانات النموذج (Form)
type: docs
weight: 80
url: /ar/java/import-export-form-data/
description: استيراد وتصدير بيانات حقول AcroForm بصيغة XML و FDF و XFDF و JSON باستخدام Aspose.PDF for Java.
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: استيراد وتصدير بيانات نموذج PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية تبادل بيانات AcroForm مع الصيغ الخارجية باستخدام Aspose.PDF for Java. تغطي استيراد وتصدير بيانات XML و FDF و XFDF من خلال واجهة Form واستخراج قيم حقول النموذج إلى JSON.
---
يدعم Aspose.PDF for Java عدة تنسيقات تبادل بيانات شائعة للنماذج التفاعلية.

## استيراد بيانات النموذج من XML

استخدم هذا المثال عندما يتم تخزين قيم النموذج في ملف XML ويجب تطبيقها على نموذج PDF.

1. أنشئ كائنًا من الفئة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) الواجهة وربط ملف PDF المصدر.
1. افتح تدفق الإدخال XML واستورد البيانات إلى النموذج.
1. احفظ مستند PDF المحدث.

```java
public static void importDataFromXml(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream stream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXml(stream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## تصدير بيانات النموذج إلى XML

استخدم هذا المثال عندما تحتاج إلى تخزين قيم AcroForm الحالية بتنسيق XML.

1. أنشئ كائنًا من الفئة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) الواجهة وربط ملف PDF المصدر.
1. افتح تدفق الإخراج لملف XML..
1. صدّر بيانات النموذج إلى XML..

```java
public static void exportDataToXml(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXml(stream);
    } finally {
        form.close();
    }
}
```

## استيراد بيانات النموذج من FDF

استخدم هذا المثال عندما تصل قيم النموذج بتنسيق التبادل FDF.

1. أنشئ كائنًا من الفئة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) الواجهة وربط ملف PDF المصدر.
1. افتح تدفق الإدخال FDF واستورد البيانات.
1. احفظ مستند PDF المملأ.

```java
public static void importDataFromFdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream stream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importFdf(stream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## تصدير بيانات النموذج إلى FDF

استخدم هذا المثال عندما يجب مشاركة قيم نموذج PDF كملف FDF.

1. أنشئ كائنًا من الفئة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) الواجهة وربط ملف PDF المصدر.
1. افتح تدفق الإخراج لملف FDF..
1. صدّر بيانات النموذج بتنسيق FDF..

```java
public static void exportDataToFdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportFdf(stream);
    } finally {
        form.close();
    }
}
```

## استيراد بيانات النموذج من XFDF

استخدم هذا المثال عندما يتم توفير بيانات النموذج بتنسيق XFDF ويجب دمجها في ملف PDF.

1. أنشئ كائنًا من الفئة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) الواجهة وربط ملف PDF المصدر.
1. افتح تدفق الإدخال XFDF واستورد القيم.
1. احفظ مستند PDF المحدث.

```java
public static void importDataFromXfdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream stream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXfdf(stream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## تصدير بيانات النموذج إلى XFDF

استخدم هذا المثال عندما تحتاج إلى ملف تبادل مبني على XML لقيم AcroForm.

1. أنشئ كائنًا من الفئة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) الواجهة وربط ملف PDF المصدر.
1. افتح تدفق الإخراج لملف XFDF..
1. صدّر قيم النموذج الحالية إلى XFDF..

```java
public static void exportDataToXfdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXfdf(stream);
    } finally {
        form.close();
    }
}
```

## استخراج حقول النموذج إلى JSON

استخدم هذا المثال عندما يجب تصدير قيم النموذج إلى تمثيل JSON خفيف الوزن.

1. افتح ملف PDF باستخدام واجهة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/).
1. مرّ على أسماء الحقول وتسلسل قيمها إلى نص JSON..
1. اكتب محتوى JSON إلى الملف الهدف.

```java
public static void extractFormFieldsToJson(Path inputFile, Path outputFile) throws Exception {
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

## إعادة استخدام أداة استخراج JSON

استخدم هذا المثال عندما تريد طريقة تغليف مخصصة تُفوض إلى الروتين الرئيسي لتصدير JSON.

1. استدعِ المساعد الحالي لاستخراج JSON باستخدام ملف PDF المصدر ومسار الإخراج.
1. أعد استخدام نفس منطق الاستخراج دون تكرار رمز التسلسل.

```java
public static void extractFormFieldsToJsonDoc(Path inputFile, Path outputFile) throws Exception {
    extractFormFieldsToJson(inputFile, outputFile);
}
```
