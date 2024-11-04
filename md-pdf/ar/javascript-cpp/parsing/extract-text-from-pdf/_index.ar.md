---
title: استخراج النص من PDF باستخدام JavaScript
linktitle: استخراج النص من PDF
type: docs
weight: 30
url: /javascript-cpp/extract-text-from-pdf/
description: يصف هذا المقال طرقًا مختلفة لاستخراج النص من مستندات PDF باستخدام Aspose.PDF لـ JavaScript.
lastmod: "2023-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## استخراج النص من مستند PDF

استخراج النص من مستند PDF هو مهمة شائعة ومفيدة للغاية. 
يخدم استخراج النص من ملفات PDF مجموعة متنوعة من الأغراض، من تحسين البحث والتوافر إلى تمكين التحليل وأتمتة البيانات في مجالات مختلفة مثل الأعمال والبحث وإدارة المعلومات.

في حال كنت تريد استخراج النص من مستند PDF، يمكنك استخدام وظيفة [AsposePdfExtractText](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextracttext/).
يرجى مراجعة الكود التالي لاستخراج النص من ملف PDF باستخدام JavaScript عبر C++.

1. إنشاء 'FileReader'.

1. يتم تنفيذ وظيفة [AsposePdfExtractText](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextracttext/).
1. بعد ذلك، إذا كان 'json.errorCode' يساوي 0، يمكنك الحصول على روابط لملفات النتيجة. إذا كانت قيمة 'json.errorCode' لا تساوي 0 و، بالتالي، سيكون هناك خطأ في ملفك، فسيتم احتواء معلومات حول هذا الخطأ في ملف 'json.errorText'.

```js

    var ffileExtract = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*استخراج النص من ملف PDF*/
        const json = AsposePdfExtractText(event.target.result, e.target.files[0].name);
        if (json.errorCode == 0) document.getElementById('output').textContent = json.extractText;
        else document.getElementById('output').textContent = json.errorText;
        };
        file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

## استخدام Web Workers

```js

    /*إنشاء Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`خطأ من Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
        (evt.data == 'ready') ? 'محمل!' :
        (evt.data.json.errorCode == 0) ?
            evt.data.json.extractText :
            `خطأ: ${evt.data.json.errorText}`; 

    /*معالج الحدث*/
    const ffileExtract = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*استخراج النص من ملف PDF - طلب من Web Worker*/
        AsposePDFWebWorker.postMessage(
            { "operation": 'AsposePdfExtractText', "params": [event.target.result, e.target.files[0].name] },
            [event.target.result]
        );
        };
        file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```