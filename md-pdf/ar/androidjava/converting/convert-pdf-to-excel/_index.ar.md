---
title: تحويل PDF إلى Excel 
linktitle: تحويل PDF إلى Excel 
type: docs
weight: 90
url: /androidjava/convert-pdf-to-excel/
lastmod: "2021-06-05"
description: يسمح لك Aspose.PDF لنظام Android عبر Java بتحويل PDF إلى تنسيق Excel. أثناء ذلك، يتم تحويل الصفحات الفردية من ملف PDF إلى أوراق عمل Excel.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

تمكنك Aspose.PDF لنظام Android عبر Java API من عرض ملفات PDF الخاصة بك إلى تنسيقات ملفات Excel [XLS](https://docs.fileformat.com/spreadsheet/xls/) و [XLSX](https://docs.fileformat.com/spreadsheet/xlsx/). لدينا بالفعل واجهة برمجة تطبيقات أخرى، تعرف باسم [Aspose.Cells for Java](https://products.aspose.com/cells/java)، التي توفر القدرة على إنشاء ومعالجة دفاتر العمل الموجودة في Excel. كما توفر القدرة على تحويل دفاتر العمل في Excel إلى تنسيق PDF.

{{% alert color="primary" %}}

جرب عبر الإنترنت.
 يمكنك التحقق من جودة تحويل Aspose.PDF وعرض النتائج عبر الإنترنت على هذا الرابط [products.aspose.app/pdf/conversion/pdf-to-xlsx](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)

## تحويل PDF إلى Excel XLS

لتحويل ملفات PDF إلى صيغة XLS، يحتوي Aspose.PDF على فئة تسمى [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions). يتم تمرير كائن من فئة [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) كوسيطة ثانية إلى منشئ Document.Save(..).

تحويل ملف PDF إلى صيغة XLSX هو جزء من المكتبة من Aspose.PDF لإصدار Java 18.6. من أجل تحويل ملفات PDF إلى صيغة XLSX، تحتاج إلى تعيين الصيغة كـ XLSX باستخدام طريقة setFormat() لفئة [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions).

يظهر مقتطف الشيفرة التالي كيفية تحويل ملف PDF إلى صيغة xls و .xlsx:

```java
public void convertPDFtoExcelSimple() {
        // فتح مستند PDF المصدر
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // إنشاء كائن ExcelSave Option
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // حفظ الملف بتنسيق مستند MS
            document.save(xlsFileName.toString(), SaveFormat.Excel);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## تحويل PDF إلى XLS مع التحكم في العمود

عند تحويل ملف PDF إلى تنسيق XLS، يتم إضافة عمود فارغ إلى الملف الناتج كأول عمود. يتم استخدام الخيار InsertBlankColumnAtFirst في فئة [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) للتحكم في هذا العمود. القيمة الافتراضية لها هي true.

```java
public void convertPDFtoExcelAdvanced_InsertBlankColumnAtFirst() {
        // افتح مستند PDF المصدر
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // إنشاء كائن خيار ExcelSave
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setInsertBlankColumnAtFirst(false);

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // احفظ الملف في تنسيق مستند MS
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


## تحويل PDF إلى ورقة عمل Excel واحدة

عند تصدير ملف PDF يحتوي على الكثير من الصفحات إلى XLS، يتم تصدير كل صفحة إلى ورقة مختلفة في ملف Excel. هذا لأن خاصية MinimizeTheNumberOfWorksheets تم تعيينها على false افتراضيًا. لضمان تصدير جميع الصفحات إلى ورقة واحدة في ملف Excel الناتج، قم بتعيين خاصية MinimizeTheNumberOfWorksheets إلى true.

```java
 public void convertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets() {
        // فتح مستند PDF المصدر
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // إنشاء كائن ExcelSave Option
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setMinimizeTheNumberOfWorksheets(true);

        // حفظ الناتج في XLSX
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // حفظ الملف بتنسيق MS Excel
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```


## التحويل إلى تنسيق XLSX

افتراضيًا، تستخدم Aspose.PDF XML Spreadsheet 2003 لتخزين البيانات. من أجل تحويل ملفات PDF إلى تنسيق XLSX، تقدم Aspose.PDF فئة تسمى ExcelSaveOptions مع Format. يتم تمرير كائن من فئة [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) كمعامل ثانٍ لطريقة Document.Save(..).

```java
 public void convertPDFtoExcelAdvanced_SaveCSV() {
        // تحميل مستند PDF
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // إنشاء كائن ExcelSave Option
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setFormat(ExcelSaveOptions.ExcelFormat.CSV);

        // حفظ المخرج في CSV
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.csv");
        try {
            // حفظ الملف في تنسيق CSV
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```