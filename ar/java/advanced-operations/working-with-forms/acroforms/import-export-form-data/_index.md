---
title: استيراد وتصدير بيانات النموذج
linktitle: استيراد وتصدير بيانات النموذج
type: docs
weight: 80
url: /java/import-export-form-data/
description: قم باستيراد وتصدير بيانات حقل AcroForm بتنسيقات XML وFDF وXFDF وJSON باستخدام Aspose.PDF لـ Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: استيراد وتصدير بيانات نموذج PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية تبادل بيانات AcroForm مع التنسيقات الخارجية باستخدام Aspose.PDF لـ Java. ويغطي استيراد وتصدير بيانات XML وFDF وXFDF من خلال واجهة النموذج واستخراج قيم حقل النموذج إلى JSON.
---
يدعم Aspose.PDF for Java العديد من تنسيقات تبادل البيانات الشائعة للنماذج التفاعلية.

## استيراد بيانات النموذج من XML

استخدم هذا المثال عندما يتم تخزين قيم النموذج في ملف XML ويجب تطبيقها على نموذج PDF.

1. قم بإنشاء واجهة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) واربط ملف PDF المصدر.
1. افتح دفق إدخال XML واستورد البيانات إلى النموذج.
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

1. قم بإنشاء واجهة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) واربط ملف PDF المصدر.
1. افتح دفق الإخراج لملف XML.
1. تصدير بيانات النموذج إلى XML.

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

استخدم هذا المثال عندما تصل قيم النموذج إلى تنسيق تبادل FDF.

1. قم بإنشاء واجهة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) واربط ملف PDF المصدر.
1. افتح دفق إدخال FDF واستورد البيانات.
1. احفظ مستند PDF المملوء.

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

1. قم بإنشاء واجهة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) واربط ملف PDF المصدر.
1. افتح دفق الإخراج لملف FDF.
1. تصدير بيانات النموذج بتنسيق FDF.

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

1. قم بإنشاء واجهة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) واربط ملف PDF المصدر.
1. افتح دفق إدخال XFDF واستورد القيم.
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

استخدم هذا المثال عندما تحتاج إلى ملف تبادل يستند إلى XML لقيم AcroForm.

1. قم بإنشاء واجهة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) واربط ملف PDF المصدر.
1. افتح دفق الإخراج لملف XFDF.
1. تصدير قيم النموذج الحالي إلى XFDF.

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

1. افتح ملف PDF باستخدام الواجهة [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/).
1. قم بالتكرار عبر أسماء الحقول وإجراء تسلسل لقيمها في نص JSON.
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

## أعد استخدام مساعد استخراج JSON

Use this example when you want a dedicated wrapper method that delegates to the main JSON export routine.

1. اتصل بمساعد استخراج JSON الحالي باستخدام ملف PDF المصدر ومسار الإخراج.
1. أعد استخدام نفس منطق الاستخراج دون تكرار رمز التسلسل.

```java
public static void extractFormFieldsToJsonDoc(Path inputFile, Path outputFile) throws Exception {
    extractFormFieldsToJson(inputFile, outputFile);
}
```
