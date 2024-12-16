---
title: استخراج النص من PDF في Node.js
linktitle: استخراج النص من PDF
type: docs
weight: 30
url: /ar/nodejs-cpp/extract-text-from-pdf/
description: تصف هذه المقالة طرقًا مختلفة لاستخراج النص من مستندات PDF باستخدام Aspose.PDF لـ Node.js عبر C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## استخراج النص من مستند PDF

استخراج النص من مستند PDF هو مهمة شائعة ومفيدة للغاية. 
يخدم استخراج النص من ملفات PDF مجموعة متنوعة من الأغراض، بدءًا من تحسين البحث والتوافر إلى تمكين التحليل وأتمتة البيانات في مجالات مختلفة مثل الأعمال والبحث وإدارة المعلومات.

في حال كنت ترغب في استخراج النص من مستند PDF، يمكنك استخدام وظيفة [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/). 
يرجى الاطلاع على مقتطف الشفرة التالي لاستخراج النص من ملف PDF باستخدام Node.js عبر C++.

تحقق من مقتطفات الشفرة واتبع الخطوات لاستخراج النص من ملف PDF الخاص بك:

**CommonJS:**

1. استدعِ `require` واستورد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
1. حدد اسم ملف الـ PDF الذي سيتم استخراج النص منه.
1. استدعِ `AsposePdf` كـ Promise ونفذ العملية لاستخراج النص. احصل على الكائن إذا نجحت العملية.
1. استدعِ الدالة [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. يتم تخزين النص المستخرج في كائن JSON. لذلك، إذا كان 'json.errorCode' يساوي 0، يتم عرض النص المستخرج باستخدام console.log. إذا كان معامل json.errorCode لا يساوي 0 وبناءً على ذلك، يظهر خطأ في ملفك، ستكون معلومات الخطأ موجودة في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*استخراج النص من ملف PDF*/
      const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
      console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
  });
```


**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
1. تحديد اسم ملف PDF الذي سيتم استخراج النص منه.
1. تهيئة وحدة AsposePdf. استلام الكائن إذا تم بنجاح.
1. استدعاء الدالة [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. يتم تخزين النص المستخرج في كائن JSON. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم عرض النص المستخرج باستخدام console.log. إذا كانت قيمة json.errorCode لا تساوي 0 وظهرت بالتالي خطأ في ملفك، سيتم تضمين معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*استخراج النص من ملف PDF*/
  const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
  console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
```