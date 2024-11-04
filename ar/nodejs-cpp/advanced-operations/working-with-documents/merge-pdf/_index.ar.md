---
title: كيفية دمج PDF في Node.js
linktitle: دمج ملفات PDF
type: docs
weight: 20
url: /nodejs-cpp/merge-pdf/
description: توضح هذه الصفحة كيفية دمج مستندات PDF في ملف PDF واحد باستخدام Aspose.PDF لـ Node.js عبر C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## دمج أو جمع ملفين PDF في ملف PDF واحد في Node.js

يُعد الجمع والدمج بين الملفات مهمة شائعة جدًا عند العمل مع عدد كبير من المستندات. أحيانًا، عند العمل مع المستندات والصور، عندما يتم مسحها ضوئيًا ومعالجتها وتنظيمها، يتم إنشاء العديد من الملفات.
لكن ماذا لو كنت بحاجة إلى تخزين كل شيء في ملف واحد؟ أو لا تريد طباعة عدة مستندات؟ قم بدمج ملفين PDF مع Aspose.PDF لـ Node.js عبر C++.

في حالة كنت ترغب في دمج ملفين PDF، يمكنك استخدام دالة [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/). 
يرجى التحقق من الشفرة التالية لدمج ملفين PDF في بيئة Node.js.

**CommonJS:**

1. استدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
1. تحديد اسم ملفات PDF التي سيتم دمجها.
1. استدعاء `AsposePdf` كـ Promise وتنفيذ العملية للدمج. استلام الكائن إذا كانت ناجحة.
1. استدعاء الدالة [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/).
1. دمج ملفي PDF. وبالتالي، إذا كان 'json.errorCode' هو 0، يتم حفظ نتيجة العملية في "ResultMerge.pdf". إذا كان معامل json.errorCode ليس 0 وبالتالي ظهرت خطأ في ملفك، فإن معلومات الخطأ ستكون موجودة في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*دمج ملفي PDF وحفظ "ResultMerge.pdf"*/
      const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
      console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
1. تحديد أسماء ملفات الـPDF التي سيتم دمجها.
1. تهيئة وحدة AsposePdf. استلام الكائن إذا نجح.
1. استدعاء الدالة [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/).
1. دمج ملفين PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultMerge.pdf". إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي ظهرت خطأ في ملفك، ستكون معلومات الخطأ موجودة في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*دمج ملفي PDF وحفظ "ResultMerge.pdf"*/
  const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
  console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```