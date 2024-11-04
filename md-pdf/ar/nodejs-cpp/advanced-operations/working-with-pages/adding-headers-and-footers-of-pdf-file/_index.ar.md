---
title: إضافة رأس وتذييل إلى PDF في Node.js
linktitle: إضافة رأس وتذييل إلى PDF
type: docs
weight: 70
url: /nodejs-cpp/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF لـ Node.js عبر C++ يسمح لك بإضافة رؤوس وتذييلات إلى ملف PDF الخاص بك باستخدام AsposePdfAddTextHeaderFooter.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF لـ Node.js عبر C++** يسمح لك بإضافة رأس وتذييل في ملف PDF الحالي الخاص بك.

في حالة رغبتك في إضافة رأس وتذييل، يمكنك استخدام دالة [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/).

يرجى مراجعة مقتطف الكود التالي من أجل إضافة رأس وتذييل إلى ملف PDF في بيئة Node.js.

**CommonJS:**

1. قم باستدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
2. حدد اسم ملف PDF الذي سيتم إضافة الرأس والتذييل إليه.

1. استدعِ `AsposePdf` كـ Promise وقم بإجراء العملية لإضافة الرأس والتذييل. استلم الكائن إذا نجحت العملية.
1. استدعِ الدالة [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/).
1. أضف نصًا في رأس وتذييل ملف PDF. وهكذا، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultAddHeaderFooter.pdf". إذا لم يكن معامل json.errorCode يساوي 0، وظهرت خطأ في ملفك، ستكون معلومات الخطأ موجودة في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*أضف نصًا في رأس/تذييل ملف PDF واحفظ "ResultAddHeaderFooter.pdf"*/
      const json = AsposePdfModule.AsposePdfAddTextHeaderFooter(pdf_file, "Aspose.PDF for Node.js via C++", "ASPOSE", "ResultAddHeaderFooter.pdf");
      console.log("AsposePdfAddTextHeaderFooter => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
2. تحديد اسم ملف PDF الذي سيتم إضافة الرأس والتذييل إليه.
3. تهيئة وحدة AsposePdf. استلام الكائن إذا نجح.
4. استدعاء الدالة [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/).
5. إضافة نص في رأس وتذييل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultAddHeaderFooter.pdf". إذا لم يكن معامل json.errorCode يساوي 0، وبالتالي يظهر خطأ في ملفك، فسيتم احتواء معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*إضافة نص في رأس/تذييل ملف PDF وحفظ "ResultAddHeaderFooter.pdf"*/
  const json = AsposePdfModule.AsposePdfAddTextHeaderFooter(pdf_file, "Aspose.PDF for Node.js via C++ via C++", "ASPOSE", "ResultAddHeaderFooter.pdf");
  console.log("AsposePdfAddTextHeaderFooter => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```