---
title: استخراج النص من PDF باستخدام JavaScript
linktitle: استخراج النص من PDF
type: docs
weight: 10
url: ar/javascript-cpp/extract-text/
description: يصف هذا القسم كيفية استخراج النص من مستند PDF باستخدام أدوات JavaScript.
lastmod: "2022-12-14"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## استخراج النص من جميع صفحات مستند PDF

استخراج النص من PDF ليس بالأمر السهل. لا يمكن للعديد من قارئي PDF استخراج النص من صور PDF أو ملفات PDF الممسوحة ضوئيًا. ولكن أداة **Aspose.PDF for JavaScript عبر C++** تتيح لك بسهولة استخراج النص من جميع ملفات PDF.

افحص مقتطف الكود واتبع الخطوات لاستخراج النص من ملف PDF الخاص بك:

1. اختر ملف PDF لاستخراج النص منه.
2. قم بإنشاء 'FileReader' لقراءة النص.
3. يتم تنفيذ وظيفة [AsposePdfExtractText](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfextracttext/).

1. بعد ذلك، إذا كان 'json.errorCode' يساوي 0، فسيحتوي 'json.extractText' على المحتوى المستخرج. إذا لم يكن معامل 'json.errorCode' يساوي 0، وبالتالي سيكون ملفك يحتوي على خطأ، فسيتم احتواء معلومات حول هذا الخطأ في 'json.errorText'.
1. كنتيجة، ستحصل على سلسلة نصية تحتوي على النص المستخرج من ملف PDF الخاص بك.

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
      (evt.data == 'ready') ? 'تم التحميل!' :
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