---
title: استخراج الجداول من PDF في Node.js
linktitle: استخراج الجداول من PDF
type: docs
weight: 10
url: /ar/nodejs-cpp/extract-tables-from-the-pdf-file/
description: يوضح هذا الموضوع كيفية استخراج الجداول من PDF وتحويلها إلى CSV باستخدام Aspose.PDF لـ Node.js عبر C++.
lastmod: "2026-07-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## استخراج الجداول أثناء تحويل PDF إلى ملفات CSV

### تحويل PDF إلى CSV

إذا كانت هناك جداول في ملف PDF، فسيتم حفظها في ملفات CSV منفصلة. وإذا كنت ترغب في تحويل مستند PDF، يمكنك استخدام الدالة [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/).
يرجى مراجعة مقتطف الشيفرة التالي من أجل تحويل ملف PDF في بيئة Node.js.

**CommonJS:**

1. استدعِ `require` واستورد الوحدة `asposepdfnodejs` في المتغير `AsposePdf`.
1. حدِّد اسم ملف PDF الذي سيتم تحويله.
1. استدعِ `AsposePdf` كـ Promise ونفّذ عملية تحويل الملف. استلم الكائن إذا نجحت العملية.
1. استدعِ الدالة [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/).
1. حوّل ملف PDF. إذا كانت القيمة `json.errorCode` تساوي `0`، فسيتم حفظ النتيجة في ملفات CSV بالتنسيق `"ResultPdfTablesToCSV{0:D2}.csv"`. وإذا لم تكن كذلك، فستتضمن `json.errorText` معلومات الخطأ.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to CSV (extract tables) with template "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... format page number), TAB as delimiter and save*/
      const json = AsposePdfModule.AsposePdfTablesToCSV(pdf_file, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
      console.log("AsposePdfTablesToCSV => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استورد الوحدة `asposepdfnodejs`.
1. حدِّد اسم ملف PDF الذي سيتم تحويله.
1. هيّئ الوحدة `AsposePdf`. استلم الكائن إذا نجحت العملية.
1. استدعِ الدالة [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/).
1. حوّل ملف PDF. إذا كانت القيمة `json.errorCode` تساوي `0`، فسيتم حفظ النتيجة في ملفات CSV بالتنسيق `"ResultPdfTablesToCSV{0:D2}.csv"`. وإذا لم تكن كذلك، فستتضمن `json.errorText` معلومات الخطأ.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to CSV (extract tables) with template "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... format page number), TAB as delimiter and save*/
  const json = AsposePdfModule.AsposePdfTablesToCSV(pdf_file, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
  console.log("AsposePdfTablesToCSV => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```
