---
title: حذف صفحة في PDF في Node.js
linktitle: حذف صفحات PDF
type: docs
weight: 30
url: /ar/nodejs-cpp/delete-pages/
description: يمكنك حذف الصفحات من ملف PDF الخاص بك باستخدام Aspose.PDF for Node.js عبر C++.
lastmod: "2026-07-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

في حال رغبتك في حذف صفحات PDF، يمكنك استخدام [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/) دالة. 

إحدى ميزات هذه الدالة هي أنها يمكنها قبول عدة أنواع كمعامل numPages:

- سلسلة نصية: في هذه الحالة، يمكننا ذكر مجموعة من الصفحات باستخدام صفحات محددة أو فواصل. على سبيل المثال، السلسلة "7, 20, 30-32, 34" تعني أننا نريد حذف الصفحات 7 و20 ومن 30 إلى 32 و34.
- مصفوفة: في هذه الحالة، يمكننا ذكر الصفحات فقط. المصفوفة [3,7] تعني أننا نريد حذف الصفحات 3 و7.
- عدد صحيح: رقم صفحة واحد.

يرجى مراجعة مقطع الشيفرة التالي لحذف صفحات PDF في بيئة Node.js.

**CommonJS:**

1. اتصال `require` و استيراد `asposepdfnodejs` الوحدة كـ `AsposePdf` متغير.
1. حدّد اسم ملف PDF الذي سيتم حذف الصفحات منه.
1. اتصال `AsposePdf` كـ Promise وتنفيذ العملية لإزالة الصفحات. استلم الكائن إذا نجح.
1. استدعِ الدالة [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/). 
1. يزيل الصفحات المحددة من ملف PDF. وبالتالي، إذا كان `json.errorCode` يساوي 0، يتم حفظ نتيجة العملية في "ResultDeletePages.pdf". إذا كان معامل `json.errorCode` ليس 0، وبالتالي يظهر خطأ في ملفك، ستتضمن معلومات الخطأ في `json.errorText`.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*string, include number pages with interval: "7, 20, 22, 30-32, 33, 36-40, 46"*/
      /*const numPages = "1-3";*/
      /*array, array of number pages*/
      /*const numPages = [1,3];*/
      /*number, number page*/
      const numPages = 1;
      /*Delete pages from a PDF-file and save the "ResultDeletePages.pdf"*/
      const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
      console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد `asposepdfnodejs` وحدة.
1. حدّد اسم ملف PDF الذي سيتم حذف الصفحات منه.
1. تهيئة وحدة AsposePdf. استلم الكائن إذا نجح.
1. استدعِ الدالة [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/). تساعد هذه الدالة على إزالة الصفحات المحددة من ملف PDF. يتم تحديد العملية بواسطة المتغير numPages، والذي يمكن أن يكون سلسلة بفواصل الصفحات (على سبيل المثال "7, 20, 22, 30-32, 33, 36-40, 46")، أو مصفوفة من أرقام الصفحات، أو رقم صفحة واحد.
1. يزيل الصفحات المحددة من ملف PDF. وبالتالي، إذا كان `json.errorCode` يساوي 0، يتم حفظ نتيجة العملية في "ResultDeletePages.pdf". إذا كان معامل `json.errorCode` ليس 0، وبالتالي يظهر خطأ في ملفك، ستتضمن معلومات الخطأ في `json.errorText`.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*string, include number pages with interval: "7, 20, 22, 30-32, 33, 36-40, 46"*/
  /*const numPages = "1-3";*/
  /*array, array of number pages*/
  /*const numPages = [1,3];*/
  /*number, number page*/
  const numPages = 1;
  /*Delete pages from a PDF-file and save the "ResultDeletePages.pdf"*/
  const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
  console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```