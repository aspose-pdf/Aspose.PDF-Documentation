---
title: إضافة رأس وتذييل إلى PDF في Node.js
linktitle: إضافة رأس وتذييل إلى PDF
type: docs
weight: 70
url: /ar/nodejs-cpp/add-headers-and-footers-of-pdf-file/
description: تتيح لك Aspose.PDF for Node.js via C++ إضافة رؤوس وتذييلات إلى ملف PDF الخاص بك باستخدام AsposePdfAddTextHeaderFooter.
lastmod: "2026-07-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF for Node.js via C++** يتيح لك إضافة رأس وتذييل في ملف PDF الحالي الخاص بك. 

في حال رغبتك في إضافة رأس وتذييل، يمكنك استخدام [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/) دالة. 

يرجى مراجعة مقتطف الشيفرة التالي لإضافة رأس وتذييل إلى ملف PDF في بيئة Node.js.

**CommonJS:**

1. اتصال `require` و استيراد `asposepdfnodejs` وحدة كـ `AsposePdf` متغير.
1. حدّد اسم ملف PDF الذي ستُضاف إليه الرأس والتذييل.
1. اتصال `AsposePdf` كـ Promise ونفّذ العملية لإضافة رأس وتذييل. استلم الكائن إذا نجح.
1. استدع الدالة [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/).
1. أضف نصًا في رأس وتذييل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultAddHeaderFooter.pdf". إذا لم يكن معامل json.errorCode يساوي 0، وبالتالي ظهر خطأ في ملفك، ستتضمن معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Add text in Header/Footer of a PDF-file and save the "ResultAddHeaderFooter.pdf"*/
      const json = AsposePdfModule.AsposePdfAddTextHeaderFooter(pdf_file, "Aspose.PDF for Node.js via C++ via C++", "ASPOSE", "ResultAddHeaderFooter.pdf");
      console.log("AsposePdfAddTextHeaderFooter => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد الـ `asposepdfnodejs` وحدة.
1. حدّد اسم ملف PDF الذي ستُضاف إليه الرأس والتذييل.
1. قم بتهيئة وحدة AsposePdf. استقبل الكائن إذا نجحت العملية.
1. استدع الدالة [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/).
1. أضف نصًا في رأس وتذييل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultAddHeaderFooter.pdf". إذا لم يكن معامل json.errorCode يساوي 0، وبالتالي ظهر خطأ في ملفك، ستتضمن معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Add text in Header/Footer of a PDF-file and save the "ResultAddHeaderFooter.pdf"*/
  const json = AsposePdfModule.AsposePdfAddTextHeaderFooter(pdf_file, "Aspose.PDF for Node.js via C++ via C++", "ASPOSE", "ResultAddHeaderFooter.pdf");
  console.log("AsposePdfAddTextHeaderFooter => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```