---
title: كيفية دمج PDF في Node.js
linktitle: دمج ملفات PDF
type: docs
weight: 20
url: /ar/nodejs-cpp/merge-pdf/
description: تشرح هذه الصفحة كيفية دمج مستندات PDF في ملف PDF واحد باستخدام Aspose.PDF for Node.js via C++.
lastmod: "2026-07-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## دمج أو جمع ملفي PDF في ملف PDF واحد في Node.js

إن دمج وتجميع الملفات هو مهمة شائعة جداً أثناء العمل مع عدد كبير من المستندات. أحيانًا، عند العمل مع المستندات والصور، عندما يتم مسحها ضوئياً، معالجتها، وتنظيمها، يتم إنشاء عدة ملفات.
لكن ماذا لو كنت بحاجة لتخزين كل شيء في ملف واحد؟ أو هل لا تريد طباعة عدة مستندات؟ ربط ملفي PDF معًا باستخدام Aspose.PDF for Node.js via C++.

في حال رغبتك في دمج ملفين PDF، يمكنك استخدام [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/) دالة. 
يرجى مراجعة المقتطف البرمجي التالي لدمج ملفي PDF في بيئة Node.js.

**CommonJS:**

1. اتصال `require` و استيراد `asposepdfnodejs` الوحدة كـ `AsposePdf` متغيّر.
1. حدد اسم ملفات PDF التي سيتم دمجها.
1. اتصال `AsposePdf` كـ Promise وتنفيذ العملية للدمج. استقبل الكائن إذا نجح.
1. استدعِ الدالة [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/).
1. دمج ملفي PDF. وبالتالي، إذا كان ‘json.errorCode’ يساوي 0، يتم حفظ نتيجة العملية في “ResultMerge.pdf”. إذا لم يكن معلمة json.errorCode تساوي 0 وبالتالي ظهر خطأ في ملفك، ستتضمن معلومات الخطأ في ‘json.errorText’.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Merge two PDF-files and save the "ResultMerge.pdf"*/
      const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
      console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد `asposepdfnodejs` وحدة.
1. حدد اسم ملفات PDF التي سيتم دمجها.
1. تهيئة وحدة AsposePdf. استلم الكائن إذا نجح.
1. استدعِ الدالة [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/).
1. دمج ملفي PDF. وبالتالي، إذا كان ‘json.errorCode’ يساوي 0، يتم حفظ نتيجة العملية في “ResultMerge.pdf”. إذا لم يكن معلمة json.errorCode تساوي 0 وبالتالي ظهر خطأ في ملفك، ستتضمن معلومات الخطأ في ‘json.errorText’.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Merge two PDF-files and save the "ResultMerge.pdf"*/
  const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
  console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```