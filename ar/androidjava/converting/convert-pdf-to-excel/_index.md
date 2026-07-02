---
title: تحويل PDF إلى Excel
linktitle: تحويل PDF إلى Excel
type: docs
weight: 90
url: /ar/androidjava/convert-pdf-to-excel/
lastmod: "2026-06-30"
description: يسمح لك Aspose.PDF for Android عبر Java بتحويل PDF إلى تنسيق Excel. أثناء ذلك، يتم تحويل الصفحات الفردية لملف PDF إلى أوراق عمل Excel.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

تمكنك Aspose.PDF for Android عبر Java API من تحويل ملفات PDF الخاصة بك إلى Excel [XLS](https://docs.fileformat.com/spreadsheet/xls/) و [XLSX](https://docs.fileformat.com/spreadsheet/xlsx/) تنسيقات الملفات. لدينا بالفعل واجهة برمجة تطبيقات أخرى معروفة باسم [Aspose.Cells for Java](https://products.aspose.com/cells/java), التي توفر القدرة على إنشاء ومعالجة كتب عمل Excel الحالية. كما توفر القدرة على تحويل كتب عمل Excel إلى صيغة PDF.

{{% alert color="primary" %}}

جرّب عبر الإنترنت. يمكنك التحقق من جودة تحويل Aspose.PDF وعرض النتائج عبر الإنترنت على هذا الرابط [products.aspose.app/pdf/conversion/pdf-to-xlsx](https://products.aspose.app/pdf/conversion/pdf-to-xlsx) 

{{% /alert %}}

## تحويل PDF إلى Excel XLS

لتحويل ملفات PDF إلى صيغة XLS، يحتوي Aspose.PDF على فئة تسمى [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions). كائن من الـ [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) يتم تمرير الفئة كوسيط ثانٍ إلى الـ Document.Save(..) المنشئ. 

تحويل ملف PDF إلى تنسيق XLSX هو جزء من المكتبة في Aspose.PDF for Java الإصدار 18.6. لتحويل ملفات PDF إلى تنسيق XLSX، تحتاج إلى تعيين التنسيق كـ XLSX باستخدام طريقة setFormat() من [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) الفئة.

يُظهر مقتطف الشيفرة التالي كيفية تحويل ملف PDF إلى صيغ xls و .xlsx:

```java
public void convertPDFtoExcelSimple() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Save the file into MS document format
            document.save(xlsFileName.toString(), SaveFormat.Excel);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## تحويل PDF إلى XLS مع عمود التحكم

عند تحويل PDF إلى صيغة XLS، يتم إضافة عمود فارغ إلى ملف الإخراج كأول عمود. الـ في [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) الخيار class InsertBlankColumnAtFirst يُستخدم للتحكم في هذا العمود. القيمة الافتراضية له هي true.

```java
public void convertPDFtoExcelAdvanced_InsertBlankColumnAtFirst() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setInsertBlankColumnAtFirst(false);

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Save the file into MS document format
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

عند تصدير ملف PDF يحتوي على عدد كبير من الصفحات إلى XLS، يتم تصدير كل صفحة إلى ورقة مختلفة في ملف Excel. يحدث هذا لأن الخاصية MinimizeTheNumberOfWorksheets مُعَدة على false بشكل افتراضي. لضمان تصدير جميع الصفحات إلى ورقة واحدة فقط في ملف Excel الناتج، قم بتعيين الخاصية MinimizeTheNumberOfWorksheets إلى true.

```java
 public void convertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setMinimizeTheNumberOfWorksheets(true);

        // Save the output in XLSX
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Save the file into MS Excel format
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```

## تحويل إلى تنسيق XLSX 

بشكل افتراضي، يستخدم Aspose.PDF تنسيق XML Spreadsheet 2003 لتخزين البيانات. لتحويل ملفات PDF إلى تنسيق XLSX، يحتوي Aspose.PDF على فئة تسمى ExcelSaveOptions مع Format. كائن من الـ [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) الفئة تُمرَّر كمعامل ثانٍ إلى طريقة Document.Save(..).

```java
 public void convertPDFtoExcelAdvanced_SaveCSV() {
        // Load PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setFormat(ExcelSaveOptions.ExcelFormat.CSV);

        // Save the output in CSV
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.csv");
        try {
            // Save the file into CSV format
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```
