---
title: استخراج الجداول من PDF في Node.js
linktitle: استخراج الجداول من PDF
type: docs
weight: 10
url: /nodejs-cpp/extract-tables-from-the-pdf-file/
description: كيفية تحويل PDF إلى CSV باستخدام Aspose.PDF لـ Node.js عبر مجموعة أدوات C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## استخراج الجداول أثناء تحويل PDF إلى ملفات CSV

### تحويل PDF إلى CSV

إذا كانت هناك جداول في PDF، فإنها تُحفظ في ملفات CSV منفصلة. في حالة رغبتك في تحويل مستند PDF، يمكنك استخدام دالة [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/). يرجى التحقق من مقتطف الشيفرة التالي من أجل تحويل ملف PDF في بيئة Node.js.

**CommonJS:**

1. استدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
2. تحديد اسم ملف PDF الذي سيتم تحويله.
3. استدعاء `AsposePdf` كـ Promise وتنفيذ العملية لتحويل الملف. استلام الكائن إذا كانت العملية ناجحة.

1. استدعاء الدالة [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPDFtoXlsX.xlsx". إذا لم يكن معامل json.errorCode يساوي 0، وظهر خطأ في ملفك، ستحتوي معلومات الخطأ على 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*تحويل ملف PDF إلى CSV (استخراج الجداول) باستخدام القالب "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... تنسيق رقم الصفحة)، TAB كفاصل وحفظ*/
      const json = AsposePdfModule.AsposePdfTablesToCSV(pdf_file, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
      console.log("AsposePdfTablesToCSV => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد الوحدة `asposepdfnodejs`.

1. حدد اسم ملف PDF الذي سيتم تحويله.
1. قم بتهيئة وحدة AsposePdf. استلم الكائن إذا تم بنجاح.
1. استدع الدالة [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/).
1. قم بتحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPDFtoXlsX.xlsx". إذا لم يكن معامل json.errorCode يساوي 0، وظهرت بالتالي خطأ في ملفك، فسيتم تضمين معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /* تحويل ملف PDF إلى CSV (استخراج الجداول) باستخدام القالب "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... صيغة رقم الصفحة)، TAB كفاصل وحفظ */
  const json = AsposePdfModule.AsposePdfTablesToCSV(pdf_file, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
  console.log("AsposePdfTablesToCSV => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```