---
title: تحويل PDF إلى Excel في جافا
linktitle: تحويل قوات الدفاع الشعبي إلى Excel
type: docs
weight: 20
url: /java/convert-pdf-to-excel/
lastmod: "2026-06-16"
description: تعرف على كيفية تحويل ملفات PDF إلى Excel في Java باستخدام Aspose.PDF، بما في ذلك مخرجات XML Spreadsheet 2003 وXLSX وXLSM وCSV وODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية تحويل PDF إلى Excel في جافا
Abstract: يشرح هذا المقال كيفية تحويل ملفات PDF إلى تنسيقات متوافقة مع Excel باستخدام Aspose.PDF لـ Java. وهو يغطي مخرجات XML Spreadsheet 2003 وXLSX وXLSM وCSV وODS، بالإضافة إلى خيارات لإدراج الأعمدة الفارغة وتقليل عدد أوراق العمل.
---
يمكن لـ Aspose.PDF for Java تصدير محتوى PDF إلى تنسيقات جداول بيانات متعددة مع خيارات تخطيط مختلفة. استخدم [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) لاختيار تنسيق المصنف المستهدف والتحكم في كيفية تعيين محتوى الصفحة في أوراق العمل والأعمدة.

## تحويل PDF إلى Excel 2003 XML

استخدم هذا المثال عندما يجب تصدير محتوى PDF إلى تنسيق جدول بيانات Excel 2003 XML.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) وقم بتعيين تنسيقه على `XMLSpreadSheet2003`.
1. اتصل بـ `document.save(outputFile.toString(), saveOptions)` حتى يتم إجراء تسلسل لملف PDF الذي تم تحميله في مخطط Excel 2003 XML.
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

## تحويل قوات الدفاع الشعبي إلى XLSX

استخدم هذا المثال عندما يجب تحويل محتوى PDF إلى تنسيق Excel 2007+ XLSX.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) وقم بتعيين تنسيقه على `XLSX`.
1. اتصل بـ `document.save(outputFile.toString(), saveOptions)` حتى يتم تصدير تخطيط PDF كمصنف Office Open XML.
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

## تحويل PDF إلى XLSX مع التحكم في العمود

استخدم هذا المثال عندما يجب ضبط معالجة الأعمدة أثناء التحويل من PDF إلى Excel.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) للإخراج `XLSX`.
1. قم بتمكين `setInsertBlankColumnAtFirst(true)` عندما تكون هناك حاجة إلى عمود بادئ إضافي لتحسين تخطيط ورقة العمل المنتج من ملف PDF.
1. اتصل بـ `document.save(outputFile.toString(), saveOptions)` واكتب ملف XLSX المحول.

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

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) للتصدير `XLSX`.
1. قم بتمكين `setMinimizeTheNumberOfWorksheets(true)` بحيث يتم دمج صفحات PDF المتعددة في أوراق عمل أقل.
1. اتصل بـ `document.save(outputFile.toString(), saveOptions)` واحفظ ملف إخراج XLSX.

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

## تحويل قوات الدفاع الشعبي إلى XLSM

استخدم هذا المثال عندما يجب حفظ مخرجات PDF كمصنف Excel يدعم وحدات الماكرو.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) وقم بتعيين التنسيق على `XLSM`.
1. اتصل بـ `document.save(outputFile.toString(), saveOptions)` حتى يتم تصدير محتوى PDF إلى حاوية مصنف ممكّنة بماكرو.
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

## تحويل قوات الدفاع الشعبي إلى CSV

استخدم هذا المثال عندما يجب تصدير محتوى جدول PDF بتنسيق CSV.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) وقم بتعيين التنسيق على `CSV`.
1. اتصل بـ `document.save(outputFile.toString(), saveOptions)` حتى يتم تسوية محتوى PDF إلى إخراج نص مفصول بفواصل.
1. احفظ ملف CSV الذي تم إنشاؤه.

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

## تحويل قوات الدفاع الشعبي إلى المواد المستنفدة للأوزون

استخدم هذا المثال عندما يجب تصدير محتوى PDF إلى تنسيق جدول بيانات OpenDocument.

1. افتح ملف PDF المصدر في مثيل [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) وقم بتعيين التنسيق على `ODS`.
1. اتصل بـ `document.save(outputFile.toString(), saveOptions)` حتى يتم تصدير ملف PDF بتنسيق جدول بيانات OpenDocument.
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
