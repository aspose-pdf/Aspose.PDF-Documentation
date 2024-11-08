---
title: تحويل PDF إلى Excel
linktitle: تحويل PDF إلى Excel
type: docs
weight: 20
url: /ar/java/convert-pdf-to-excel/
lastmod: "2021-11-19"
keywords: تحويل PDF إلى Excel باستخدام Java, تحويل PDF إلى XLS باستخدام Java, تحويل PDF إلى XLSX باستخدام Java, تصدير جدول من PDF إلى Excel في Java
description: يسمح لك Aspose.PDF for Java بتحويل PDF إلى صيغة Excel باستخدام جافا. خلال ذلك، يتم تحويل الصفحات الفردية من ملف PDF إلى أوراق عمل Excel.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

تتيح لك Aspose.PDF for Java API تحويل ملفات PDF الخاصة بك إلى صيغ ملفات Excel [XLS](https://docs.fileformat.com/spreadsheet/xls/) و[XLSX](https://docs.fileformat.com/spreadsheet/xlsx/). لدينا بالفعل واجهة برمجة تطبيقات أخرى، معروفة باسم [Aspose.Cells for Java](https://products.aspose.com/cells/java)، التي توفر القدرة على إنشاء وتعديل دفاتر عمل Excel الموجودة. كما أنها توفر القدرة على تحويل دفاتر عمل Excel إلى صيغة PDF.

{{% alert color="primary" %}}

**حاول تحويل PDF إلى Excel عبر الإنترنت**

Aspose.PDF for Java يقدم لك تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى Excel باستخدام التطبيق المجاني](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## تحويل PDF إلى Excel XLS

لتحويل ملفات PDF إلى تنسيق XLS، يحتوي Aspose.PDF على فئة تسمى [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions). يتم تمرير كائن من الفئة [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) كوسيطة ثانية إلى طريقة Document.Save(..).

تحويل ملف PDF إلى تنسيق XLSX هو جزء من المكتبة من إصدار Aspose.PDF for Java 18.6. لتحويل ملفات PDF إلى تنسيق XLSX، تحتاج إلى تعيين التنسيق كـ XLSX باستخدام طريقة setFormat() لفئة [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions).

يظهر مقتطف الشيفرة التالي كيفية تحويل ملف PDF إلى تنسيق xls و .xlsx:

```java
package com.aspose.pdf.examples;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPDFtoXLSX {

    private ConvertPDFtoXLSX() {

    }

    // المسار إلى دليل المستندات.
    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {

        ConvertPDFtoExcelSimple();
        ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst();
        ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets();
        ConvertPDFtoExcelAdvanced_SaveXLSX();
    }

    public static void ConvertPDFtoExcelSimple() {
        // تحميل مستند PDF
        Document pdfDocument = new Document(_dataDir + "input.pdf");

        // إنشاء كائن خيار ExcelSave
        ExcelSaveOptions excelsave = new ExcelSaveOptions();

        // حفظ الناتج بتنسيق XLS
        pdfDocument.save("PDFToXLS_out.xls", excelsave);
    }
}
```


## تحويل PDF إلى XLS مع التحكم في العمود

عند تحويل ملف PDF إلى تنسيق XLS، يتم إضافة عمود فارغ إلى ملف الإخراج كأول عمود. يتم استخدام خيار InsertBlankColumnAtFirst في فئة [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) للتحكم في هذا العمود. القيمة الافتراضية له هي true.

```java
    public static void ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst() {
        // تحميل مستند PDF
        Document pdfDocument = new Document(_dataDir + "input.pdf");
        // إنشاء كائن خيار ExcelSave
        ExcelSaveOptions excelsave = new ExcelSaveOptions();
        excelsave.setInsertBlankColumnAtFirst(false);
        // حفظ الإخراج بتنسيق XLS
        pdfDocument.save("PDFToXLS_out.xls", excelsave);
    }
```

## تحويل PDF إلى ورقة عمل Excel واحدة

عند تصدير ملف PDF يحتوي على العديد من الصفحات إلى XLS، يتم تصدير كل صفحة إلى ورقة مختلفة في ملف Excel.
 هذا لأن خاصية MinimizeTheNumberOfWorksheets مضبوطة على false بشكل افتراضي. للتأكد من تصدير جميع الصفحات إلى ورقة واحدة في ملف Excel الناتج، اضبط خاصية MinimizeTheNumberOfWorksheets على true.

```java
    public static void ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets() {
        // تحميل مستند PDF
        Document pdfDocument = new Document(_dataDir + "input.pdf");

        // إنشاء كائن خيار حفظ Excel
        ExcelSaveOptions excelsave = new ExcelSaveOptions();
        excelsave.setMinimizeTheNumberOfWorksheets(true);

        // احفظ الناتج بتنسيق XLS
        pdfDocument.save("PDFToXLS_out.xls", excelsave);
    }
```

## التحويل إلى تنسيق XLSX

بشكل افتراضي، تستخدم Aspose.PDF تنسيق XML Spreadsheet 2003 لتخزين البيانات. من أجل تحويل ملفات PDF إلى تنسيق XLSX، تحتوي Aspose.PDF على فئة تسمى ExcelSaveOptions مع Format. يتم تمرير كائن من فئة [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) كمعامل ثانٍ إلى طريقة Document.Save(..).

```java
    public static void ConvertPDFtoExcelAdvanced_SaveXLSX() {
        // تحميل مستند PDF
        Document pdfDocument = new Document(_dataDir + "input.pdf");

        // إنشاء كائن خيار ExcelSave
        ExcelSaveOptions excelSave = new ExcelSaveOptions();
        excelSave.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);

        // حفظ النتيجة بتنسيق XLS
        pdfDocument.save("PDFToXLS_out.xlsx", excelSave);
    }
```