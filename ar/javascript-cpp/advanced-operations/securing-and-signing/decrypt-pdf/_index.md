---
title: فك تشفير PDF باستخدام JavaScript
linktitle: فك تشفير ملف PDF
type: docs
weight: 40
url: /ar/javascript-cpp/decrypt-pdf/
description: فك تشفير ملف PDF باستخدام Aspose.PDF لـ JavaScript عبر C++.
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## فك تشفير ملف PDF باستخدام كلمة مرور المالك

في الآونة الأخيرة، يتبادل المزيد والمزيد من المستخدمين المستندات المشفرة لتجنب الوقوع ضحية للاحتيال عبر الإنترنت وحماية مستنداتهم.
وبهذا الصدد، يصبح من الضروري الوصول إلى ملف PDF المشفر، حيث يمكن الحصول على هذا الوصول فقط بواسطة مستخدم معتمد. كما يبحث الأشخاص عن حلول مختلفة لفك تشفير ملفات PDF.

من الأفضل حل هذه المشكلة مرة واحدة باستخدام Aspose.PDF لـ JavaScript عبر C++ مباشرة في متصفح الويب الخاص بك. يوضح لك مقتطف الشفرة التالي كيفية فك تشفير ملفات PDF.

1. اختر ملف PDF لفك تشفيره.
1. أنشئ 'FileReader'.
1. يتم تنفيذ وظيفة [AsposePdfDecrypt](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfdecrypt/).

1. يتم تعيين اسم الملف الناتج، في هذا المثال "ResultDecrypt.pdf".
1. بعد ذلك، إذا كان 'json.errorCode' يساوي 0، فإن DownloadFile الخاص بك يُعطى الاسم الذي قمت بتحديده سابقًا. إذا لم تكن قيمة 'json.errorCode' تساوي 0، وبالتالي سيكون هناك خطأ في ملفك، فستحتوي المعلومات حول هذا الخطأ في ملف 'json.errorText'.
1. كنتيجة لذلك، تقوم دالة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) بإنشاء رابط وتسمح لك بتنزيل الملف الناتج إلى نظام تشغيل المستخدم.

```js

    var ffileDecrypt = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*فك تشفير ملف PDF بكلمة سر هي "owner" واحفظه كـ "ResultDecrypt.pdf"*/
        const json = AsposePdfDecrypt(event.target.result, e.target.files[0].name, "owner", "ResultDecrypt.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*إنشاء رابط لتحميل ملف النتيجة*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```


## استخدام عمال الويب

```js

    /*إنشاء عامل ويب*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`خطأ من عامل الويب: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'محمل!' :
        (evt.data.json.errorCode == 0) ?
          `نتيجة:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `خطأ: ${evt.data.json.errorText}`;

    /*معالج الحدث*/
    const ffileDecrypt = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const password = 'owner';
        /*فك تشفير ملف PDF بكلمة المرور "owner" واحفظ "ResultDecrypt.pdf" - اطلب من عامل الويب*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfDecrypt',
            "params": [event.target.result, e.target.files[0].name, password, "ResultDecrypt.pdf"] }, 
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*إنشاء رابط لتنزيل ملف النتيجة*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "انقر هنا لتنزيل الملف " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```