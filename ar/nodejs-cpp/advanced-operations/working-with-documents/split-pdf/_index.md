---
title: تقسيم PDF في Node.js
linktitle: تقسيم ملفات PDF
type: docs
weight: 30
url: /ar/nodejs-cpp/split-pdf/
description: يوضح هذا الموضوع كيفية تقسيم صفحات PDF إلى ملف PDF فردي باستخدام Aspose.PDF لـ Node.js عبر C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## تقسيم PDF إلى ملفين باستخدام Node.js

في حال كنت ترغب في تقسيم ملف PDF واحد إلى أجزاء، يمكنك استخدام دالة [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/).
يرجى الاطلاع على مقتطف الشيفرة التالي لتقسيم ملفي PDF في بيئة Node.js.

**CommonJS:**

1. استدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
2. تحديد اسم ملفات PDF التي سيتم تقسيمها.
3. استدعاء `AsposePdf` كـ Promise وتنفيذ العملية لتقسيم الملف. استلم الكائن إذا نجحت العملية.
4. استدعاء الدالة [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/).

1. تقسيم ملفي PDF. يتم تعيين المتغير pageToSplit إلى 1، مما يشير إلى أن ملف PDF سيتم تقسيمه عند الصفحة 1.  
1. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultSplit1.pdf"، و "ResultSplit2.pdf". إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي يظهر خطأ في ملفك، ستكون معلومات الخطأ موجودة في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*تعيين رقم الصفحة للتقسيم*/
      const pageToSplit = 1;
      /*تقسيم إلى ملفي PDF وحفظ "ResultSplit1.pdf"، "ResultSplit2.pdf"*/
      const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
      console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد الوحدة `asposepdfnodejs`.

1. حدد اسم ملفات PDF التي سيتم تقسيمها.
1. قم بتهيئة وحدة AsposePdf. استلم الكائن إذا نجح.
1. استدع الدالة [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/).
1. قسم ملفي PDF. يحدد المتغير pageToSplit إلى 1، مما يشير إلى أن ملف PDF سيتم تقسيمه عند الصفحة 1.
1. بالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultSplit1.pdf"، و "ResultSplit2.pdf". إذا لم يكن معلم json.errorCode يساوي 0 وظهرت بالتالي خطأ في ملفك، سيتم احتواء معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*حدد عدد الصفحات للتقسيم*/
  const pageToSplit = 1;
  /*قسّم إلى ملفي PDF واحفظ "ResultSplit1.pdf"، "ResultSplit2.pdf"*/
  const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
  console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
```