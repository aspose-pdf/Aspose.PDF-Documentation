---
title: تحويل PDF إلى Excel في Java
linktitle: تحويل PDF إلى Excel
type: docs
weight: 20
url: /ar/java/convert-pdf-to-excel/
lastmod: "2026-10-01"
description: تعلم كيفية تحويل ملفات PDF إلى Excel في Java باستخدام Aspose.PDF، بما في ذلك مخرجات XML Spreadsheet 2003 و XLSX و XLSM و CSV و ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية تحويل PDF إلى Excel في Java
Abstract: تشرح هذه المقالة كيفية تحويل ملفات PDF إلى تنسيقات متوافقة مع Excel باستخدام Aspose.PDF for Java. تغطي إخراج XML Spreadsheet 2003 و XLSX و XLSM و CSV و ODS، بالإضافة إلى خيارات إدراج أعمدة فارغة وتقليل عدد الأوراق.
---
يمكن لـ Aspose.PDF for Java تصدير محتوى PDF إلى تنسيقات جداول بيانات متعددة مع خيارات تخطيط مختلفة. استخدم [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) لاختيار تنسيق مصنف الهدف والتحكم في كيفية تعيين محتوى الصفحة إلى أوراق العمل والأعمدة.

## تحويل PDF إلى Excel 2003 XML

استخدم هذا المثال عندما يجب تصدير محتوى PDF إلى تنسيق جدول بيانات XML لإكسل 2003.

1. افتح ملف PDF المصدر في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثال.
1. إنشاء [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) وضع تنسيقه إلى `XMLSpreadSheet2003`.
1. اتصال `document.save(outputFile.toString(), saveOptions)` لذلك يتم تسلسل ملف PDF المحمَّل وفق مخطط XML لإكسل 2003.
1. احفظ ملف الإخراج المحول.

```java
public static void convertPdfToExcelSpreadSheet2003(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل PDF إلى XLSX

استخدم هذا المثال عندما يجب تحويل محتوى PDF إلى تنسيق Excel 2007+ XLSX.

1. افتح ملف PDF المصدر في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثال.
1. إنشاء [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) وضع تنسيقه إلى `XLSX`.
1. اتصال `document.save(outputFile.toString(), saveOptions)` لذلك يتم تصدير تخطيط PDF كدفتر عمل Office Open XML.
1. احفظ ملف جدول البيانات الناتج.

```java
public static void convertPdfToExcel2007(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل PDF إلى XLSX مع التحكم في الأعمدة

استخدم هذا المثال عندما يجب تعديل معالجة الأعمدة أثناء تحويل PDF إلى Excel.

1. افتح ملف PDF المصدر في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثال.
1. إنشاء [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) من أجل `XLSX` الإخراج.
1. تمكين `setInsertBlankColumnAtFirst(true)` عندما تكون هناك حاجة إلى عمود بادئ إضافي لتحسين تخطيط ورقة العمل الناتجة من ملف PDF.
1. اتصال `document.save(outputFile.toString(), saveOptions)` واكتب الملف XLSX المحوّل.

```java
public static void convertPdfToExcel2007ControlColumn(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        saveOptions.setInsertBlankColumnAtFirst(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل PDF إلى ورقة عمل Excel واحدة

استخدم هذا المثال عندما يجب تصدير جميع صفحات PDF إلى ورقة عمل واحدة.

1. افتح ملف PDF المصدر في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثال.
1. إنشاء [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) من أجل `XLSX` تصدير.
1. تمكين `setMinimizeTheNumberOfWorksheets(true)` لذا يتم دمج صفحات PDF المتعددة في عدد أقل من أوراق العمل.
1. اتصال `document.save(outputFile.toString(), saveOptions)` وحفظ ملف الإخراج XLSX.

```java
public static void convertPdfToExcel2007SingleExcelWorksheet(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        saveOptions.setMinimizeTheNumberOfWorksheets(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل PDF إلى XLSM

استخدم هذا المثال عندما يجب حفظ مخرجات PDF كدفتر عمل Excel يدعم الماكرو.

1. افتح ملف PDF المصدر في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثال.
1. إنشاء [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) وحدد التنسيق إلى `XLSM`.
1. اتصال `document.save(outputFile.toString(), saveOptions)` لذا يتم تصدير محتوى PDF إلى حاوية دفتر عمل مدعوم بالماكرو.
1. احفظ ملف XLSM.

```java
public static void convertPdfToExcel2007Macro(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSM);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل PDF إلى CSV

استخدم هذا المثال عندما يجب تصدير محتوى الجداول في PDF كملف CSV.

1. افتح ملف PDF المصدر في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثال.
1. إنشاء [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) وحدد التنسيق إلى `CSV`.
1. اتصال `document.save(outputFile.toString(), saveOptions)` لذلك يتم تسوية محتوى PDF إلى إخراج نصي مفصول بفواصل.
1. احفظ ملف CSV المُولَّد.

```java
public static void convertPdfToExcel2007Csv(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.CSV);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## تحويل PDF إلى ODS

استخدم هذا المثال عندما يجب تصدير محتوى PDF إلى صيغة جدول بيانات OpenDocument.

1. افتح ملف PDF المصدر في [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثال.
1. إنشاء [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) وحدد التنسيق إلى `ODS`.
1. اتصال `document.save(outputFile.toString(), saveOptions)` لذلك يتم تصدير PDF بتنسيق جدول بيانات OpenDocument.
1. احفظ ملف ODS المحول.

```java
public static void convertPdfToOds(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.ODS);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
