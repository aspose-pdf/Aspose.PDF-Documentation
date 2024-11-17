---
title: تحويل PDF إلى Microsoft Excel
linktitle: تحويل PDF إلى Excel
type: docs
weight: 20
url: /ar/php-java/convert-pdf-to-excel/
lastmod: "2024-05-20"
description: يتيح لك Aspose.PDF for PHP تحويل PDF إلى تنسيق Excel باستخدام PHP. خلال هذه العملية، يتم تحويل الصفحات الفردية من ملف PDF إلى أوراق عمل Excel.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

تتيح لك Aspose.PDF for PHP API تحويل ملفات PDF الخاصة بك إلى تنسيقات ملفات Excel [XLS](https://docs.fileformat.com/spreadsheet/xls/) و [XLSX](https://docs.fileformat.com/spreadsheet/xlsx/). لدينا بالفعل واجهة برمجة تطبيقات أخرى، تُعرف باسم [Aspose.Cells for PHP عبر Java](https://products.aspose.com/cells/php-java)، التي توفر القدرة على إنشاء وتعديل دفاتر عمل Excel الموجودة. كما أنها توفر القدرة على تحويل دفاتر عمل Excel إلى تنسيق PDF.

{{% alert color="primary" %}}

**حاول تحويل PDF إلى Excel عبر الإنترنت**

Aspose.PDF لـ PHP يقدم لك تطبيقًا مجانيًا على الإنترنت ["PDF إلى XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى Excel باستخدام التطبيق المجاني](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## تحويل PDF إلى Excel XLS

لتحويل ملفات PDF إلى تنسيق XLS، يحتوي Aspose.PDF على فئة تسمى [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions). يتم تمرير كائن من فئة [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) كوسيطة ثانية إلى طريقة Document.Save(..).

تحويل ملف PDF إلى تنسيق XLSX هو جزء من المكتبة من Aspose.PDF لإصدار PHP 18.6. لكي تقوم بتحويل ملفات PDF إلى تنسيق XLSX، تحتاج إلى تعيين التنسيق كـ XLSX باستخدام طريقة setFormat() لفئة [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions).

توضح الشفرات التالية كيفية تحويل ملف PDF إلى تنسيق XLS و XLSX:

```php
// تحميل مستند PDF المدخل باستخدام فئة Document.
$document = new Document($inputFile);

// إنشاء مثيل لفئة ExcelSaveOptions لتحديد خيارات الحفظ.
$saveOption = new ExcelSaveOptions();

// تعيين التنسيق الناتج إلى XLS.
// $saveOption->setFormat(ExcelSaveOptions_ExcelFormat::$XMLSpreadSheet2003);

// تعيين التنسيق الناتج إلى XLSX.
    $excelSaveOptions_ExcelFormat = new ExcelSaveOptions_ExcelFormat();
    $saveOption->setFormat($excelSaveOptions_ExcelFormat->XLSX);

// حفظ مستند PDF كملف Excel باستخدام خيارات الحفظ المحددة.
$document->save($outputFile, $saveOption);
```