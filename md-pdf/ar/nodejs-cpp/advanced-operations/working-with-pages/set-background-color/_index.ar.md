---
title: ضبط لون الخلفية لملف PDF في Node.js
linktitle: ضبط لون الخلفية
type: docs
weight: 80
url: /nodejs-cpp/set-background-color/
description: ضبط لون الخلفية لملف PDF الخاص بك باستخدام Node.js عبر C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

في حالة رغبتك في ضبط لون خلفية ملف PDF، يمكنك استخدام وظيفة [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/).

يرجى التحقق من مقتطف الشيفرة التالي من أجل ضبط لون خلفية ملف PDF في بيئة Node.js.

**CommonJS:**

1. استدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
2. تحديد اسم ملف PDF الذي ترغب في ضبط لون خلفيته.
3. استدعاء `AsposePdf` كـ Promise والقيام بعملية ضبط لون الخلفية. استقبال الكائن إذا تم بنجاح.

1. استدعاء الدالة [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/).  
1. تعيين لون الخلفية لملف الـ PDF. تحتاج إلى تمرير 3 معطيات لهذه الدالة: اسم ملف الإدخال، اللون المطلوب بصيغة الألوان الست عشرية، واسم ملف الإخراج. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultRotation.pdf". إذا كانت قيمة المعامل json.errorCode ليست 0 وبالتالي تظهر خطأ في ملفك، ستكون معلومات الخطأ موجودة في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*تعيين لون الخلفية لملف الـ PDF وحفظ "ResultPdfSetBackgroundColor.pdf"*/
      const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
      console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. استيراد الوحدة `asposepdfnodejs`.
1. تحديد اسم ملف PDF الذي ترغب في تعيين لون الخلفية له.
1. تهيئة وحدة AsposePdf. استقبال الكائن إذا كان ناجحًا.
1. استدعاء الدالة [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/).
1. تعيين لون الخلفية لملف PDF. يتم تعيين لون الخلفية إلى "#426bf4"، وهو رمز لون سداسي عشري يمثل درجة من اللون الأزرق. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultRotation.pdf". إذا كان معامل json.errorCode ليس 0 ومن ثم يظهر خطأ في ملفك، ستكون معلومات الخطأ موجودة في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*تعيين لون الخلفية لملف PDF وحفظ "ResultPdfSetBackgroundColor.pdf"*/
  const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
  console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```