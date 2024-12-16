---
title: حذف صفحة في PDF في Node.js
linktitle: حذف صفحات PDF
type: docs
weight: 30
url: /ar/nodejs-cpp/delete-pages/
description: يمكنك حذف الصفحات من ملف PDF الخاص بك باستخدام Aspose.PDF for Node.js عبر C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

في حال كنت تريد حذف صفحات PDF، يمكنك استخدام وظيفة [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/).

ميزة هذه الوظيفة هي أنها يمكن أن تقبل عدة أنواع كمعامل numPages:

- string: في هذه الحالة، يمكننا ذكر مجموعة من الصفحات باستخدام صفحات معينة أو فترات. على سبيل المثال، السلسلة "7, 20, 30-32, 34" تعني أننا نريد إزالة الصفحات 7، 20، من 30 إلى 32 و34.
- array: في هذه الحالة، يمكننا ذكر الصفحات فقط. المصفوفة [3,7] تعني أننا نريد إزالة الصفحات 3 و7.
- int: رقم صفحة واحد.

يرجى التحقق من مقطع التعليمات البرمجية التالي من أجل حذف صفحات PDF في بيئة Node.js.

**CommonJS:**

1. قم باستدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
1. حدد اسم ملف PDF الذي سيتم حذف الصفحات منه.
1. قم باستدعاء `AsposePdf` كـ Promise وقم بتنفيذ العملية لإزالة الصفحات. استلم الكائن إذا نجحت العملية.
1. قم باستدعاء الدالة [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/).
1. يزيل الصفحات المحددة من ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultDeletePages.pdf". إذا لم يكن معامل json.errorCode يساوي 0 وظهرت بالتالي خطأ في ملفك، سيتم احتواء معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*string, تشمل أرقام الصفحات مع الفاصل: "7, 20, 22, 30-32, 33, 36-40, 46"*/
      /*const numPages = "1-3";*/
      /*array, مصفوفة من أرقام الصفحات*/
      /*const numPages = [1,3];*/
      /*number, رقم الصفحة*/
      const numPages = 1;
      /*احذف الصفحات من ملف PDF واحفظه كـ "ResultDeletePages.pdf"*/
      const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
      console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
1. تحديد اسم ملف PDF الذي سيتم حذف الصفحات منه.
1. تهيئة وحدة AsposePdf. استلام الكائن إذا تم بنجاح.
1. استدعاء الدالة [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/). هذه الدالة تساعد في إزالة الصفحات المحددة من ملف PDF. يتم تحديد العملية بواسطة متغير numPages، الذي يمكن أن يكون سلسلة مع فواصل صفح (مثل "7, 20, 22, 30-32, 33, 36-40, 46")، أو مصفوفة من أرقام الصفحات، أو رقم صفحة واحد.
1. إزالة الصفحات المحددة من ملف PDF. وبالتالي، إذا كان 'json.errorCode' هو 0، يتم حفظ نتيجة العملية في "ResultDeletePages.pdf". إذا لم يكن معلمة json.errorCode تساوي 0 وظهرت بالتالي خطأ في ملفك، سيتم احتواء معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*string, تتضمن أرقام الصفحات بفواصل: "7, 20, 22, 30-32, 33, 36-40, 46"*/
  /*const numPages = "1-3";*/
  /*array, مصفوفة من أرقام الصفحات*/
  /*const numPages = [1,3];*/
  /*number, رقم الصفحة*/
  const numPages = 1;
  /*حذف الصفحات من ملف PDF وحفظ النتيجة في "ResultDeletePages.pdf"*/
  const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
  console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```