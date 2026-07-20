---
title: تعيين لون الخلفية لملف PDF في Node.js
linktitle: تعيين لون الخلفية
type: docs
weight: 80
url: /ar/nodejs-cpp/set-background-color/
description: تعيين لون الخلفية لملف PDF الخاص بك باستخدام Node.js عبر C++.
lastmod: "2026-07-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

في حالة رغبتك في تعيين لون الخلفية لملف PDF، يمكنك استخدام [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/) دالة. 

يرجى مراجعة مقتطف الشيفرة التالي لتعيين لون خلفية ملف PDF في بيئة Node.js.

**CommonJS:**

1. اتصال `require` و استيراد `asposepdfnodejs` الوحدة كـ `AsposePdf` متغير.
1. حدّد اسم ملف PDF الذي تريد تعيين لون خلفيته.
1. اتصال `AsposePdf` كـ Promise وأداء العملية لتعيين لون الخلفية. استلم الكائن إذا نجح.
1. استدعِ الدالة [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/). 
1. تعيين لون الخلفية لملف PDF. تحتاج إلى تمرير 3 معلمات إلى هذه الدالة: اسم ملف الإدخال، اللون المطلوب بصيغة سداسي عشرية، واسم ملف الإخراج. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultRotation.pdf". إذا لم يكن معامل json.errorCode يساوي 0، وبالتالي ظهر خطأ في ملفك، ستحتوي معلومات الخطأ على 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Set the background color for the PDF-file and save the "ResultPdfSetBackgroundColor.pdf"*/
      const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
      console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد `asposepdfnodejs` وحدة.
1. حدّد اسم ملف PDF الذي تريد تعيين لون خلفيته.
1. ابدأ وحدة AsposePdf. استلم الكائن إذا نجح.
1. استدعِ الدالة [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/). 
1. قم بتعيين لون الخلفية لملف PDF. تم تعيين لون الخلفية إلى "#426bf4,"، وهو رمز لون سداسي عشري يمثل درجة من اللون الأزرق. وبالتالي، إذا كانت قيمة 'json.errorCode' هي 0، يتم حفظ نتيجة العملية في "ResultRotation.pdf". إذا لم يكن معلمة json.errorCode مساوية لـ 0، وبناءً عليه ظهر خطأ في ملفك، ستحتوي معلومات الخطأ على 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Set the background color for the PDF-file and save the "ResultPdfSetBackgroundColor.pdf"*/
  const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
  console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```