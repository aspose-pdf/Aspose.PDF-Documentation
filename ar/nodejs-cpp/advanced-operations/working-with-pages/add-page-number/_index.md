---
title: إضافة ترقيم الصفحات إلى PDF في Node.js
linktitle: إضافة رقم الصفحة
type: docs
weight: 100
url: /ar/nodejs-cpp/add-page-number/
description: Aspose.PDF for Node.js via C++ يتيح لك إضافة ختم رقم الصفحة إلى ملف PDF الخاص بك باستخدام AsposePdfAddPageNum.
lastmod: "2026-07-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

رقم الصفحة يجعل من السهل على القارئ تحديد أجزاء مختلفة من المستند. يوضح مقاطع الشيفرة التالية كيفية إضافة أرقام الصفحات إلى صفحات PDF باستخدام [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/) دالة في Node.js.

يرجى فحص مقتطف الشيفرة التالي لإضافة أرقام الصفحات إلى ملف PDF في بيئة Node.js.

**CommonJS:**

1. اتصال `require` و استيراد `asposepdfnodejs` الوحدة كك `AsposePdf` متغير.
1. حدّد اسم ملف PDF الذي ستُضاف إليه أرقام الصفحات.
1. اتصال `AsposePdf` كـ Promise وتنفيذ العملية لإضافة أرقام الصفحات. استلم الكائن إذا نجح.
1. استدعِ الدالة [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/).
1. إضافة رقم الصفحة إلى ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultAddPageNum.pdf". إذا لم يكن معامل json.errorCode يساوي 0، وبناءً على ذلك يظهر خطأ في ملفك، فستتضمن معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Add page number to a PDF-file save the "ResultAddPageNum.pdf"*/
      const json = AsposePdfModule.AsposePdfAddPageNum(pdf_file, "ResultAddPageNum.pdf");
      console.log("AsposePdfAddPageNum => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد الـ `asposepdfnodejs` وحدة.
1. حدّد اسم ملف PDF الذي ستُضاف إليه أرقام الصفحات.
1. قم بتهيئة وحدة AsposePdf. احصل على الكائن إذا نجح.
1. استدعِ الدالة [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/).
1. إضافة رقم الصفحة إلى ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultAddPageNum.pdf". إذا لم يكن معامل json.errorCode يساوي 0، وبناءً على ذلك يظهر خطأ في ملفك، فستتضمن معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Add page number to a PDF-file and save the "ResultAddPageNum.pdf"*/
  const json = AsposePdfModule.AsposePdfAddPageNum(pdf_file, "ResultAddPageNum.pdf");
  console.log("AsposePdfAddPageNum => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```