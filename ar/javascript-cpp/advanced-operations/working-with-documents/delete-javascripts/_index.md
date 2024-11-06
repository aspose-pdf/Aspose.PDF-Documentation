---
title: مسح كود JavaScript من ملف PDF
linktitle: حذف JavaScripts
type: docs
weight: 50
url: ar/javascript-cpp/delete-javascripts/
description: مسح وحدات ماكرو JavaScript من ملف PDF مباشرة في الويب باستخدام Aspose.PDF.
lastmod: "2023-09-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

قد يكون من الضروري إزالة JavaScript في ملف PDF لأسباب أمنية وخصوصية. يمكن أن يُستخدم JavaScript في ملفات PDF أحيانًا بشكل ضار أو لوظائف غير مرغوب فيها. يمكنك الحصول على النتيجة مباشرة في متصفحك.

1. إنشاء 'FileReader'.
1. يتم تنفيذ وظيفة [AsposePdfDeleteJavaScripts](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfdeletejavascripts/).
1. يتم تعيين اسم الملف الناتج، في هذا المثال "ResultPdfDeleteJavaScripts.pdf".

1. بعد ذلك، إذا كانت 'json.errorCode' تساوي 0، فإن ملفك المحمل سُيعطى الاسم الذي قمت بتحديده مسبقًا. إذا كانت قيمة 'json.errorCode' لا تساوي 0 وبالتالي سيكون هناك خطأ في ملفك، فإن معلومات حول هذا الخطأ ستكون موجودة في ملف 'json.errorText'.
2. نتيجة لذلك، فإن وظيفة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) تقوم بتوليد رابط وتسمح لك بتحميل الملف الناتج إلى نظام تشغيل المستخدم.

```js

    var ffilePdfDeleteJavaScripts = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*حذف JavaScripts من ملف PDF وحفظ "ResultPdfDeleteJavaScripts.pdf"*/
        const json = AsposePdfDeleteJavaScripts(event.target.result, e.target.files[0].name, "ResultPdfDeleteJavaScripts.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*إنشاء رابط لتحميل ملف النتيجة*/
        DownloadFile(json.fileNameResult, "application/pdf");
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
        (evt.data.json.errorCode == 0) ? `النتيجة:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `خطأ: ${evt.data.json.errorText}`;

    /*معالج الحدث*/
    const ffilePdfDeleteJavaScripts = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*حذف JavaScripts من ملف PDF وحفظ "ResultPdfDeleteJavaScripts.pdf" - طلب من Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfDeleteJavaScripts', "params": [event.target.result, e.target.files[0].name, "ResultPdfDeleteJavaScripts.pdf"] }, [event.target.result]);
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