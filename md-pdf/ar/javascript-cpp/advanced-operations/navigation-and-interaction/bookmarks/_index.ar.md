---
title: العلامات المرجعية في PDF باستخدام JavaScript
linktitle: العلامات المرجعية في PDF
type: docs
weight: 10
url: /javascript-cpp/bookmark/
description: يمكنك إضافة أو حذف العلامات المرجعية في مستند PDF باستخدام JavaScript.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## حذف علامة مرجعية معينة من مستند PDF

يمكنك حذف العلامات المرجعية من ملف PDF باستخدام Aspose.PDF لـ JavaScript عبر C++. يمكنك الحصول على النتيجة مباشرة في متصفحك.

1. إنشاء 'FileReader'.
1. يتم تنفيذ وظيفة [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfdeletebookmarks/).
1. يتم تعيين اسم الملف الناتج، في هذا المثال "ResultPdfDeleteBookmarks.pdf".
1. بعد ذلك، إذا كان 'json.errorCode' يعادل 0، فإن DownloadFile الخاص بك يُعطى الاسم الذي حددته سابقًا. إذا لم يكن معامل 'json.errorCode' يعادل 0 وبالتالي سيكون هناك خطأ في ملفك، فإن معلومات حول هذا الخطأ ستحتوي عليها ملف 'json.errorText'.

1. نتيجة لذلك، تقوم وظيفة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) بإنشاء رابط وتسمح لك بتنزيل الملف الناتج إلى نظام تشغيل المستخدم.

```js

    var ffilePdfDeleteBookmarks = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*حذف العلامات المرجعية من ملف PDF وحفظ "ResultPdfDeleteBookmarks.pdf"*/
        const json = AsposePdfDeleteBookmarks(event.target.result, e.target.files[0].name, "ResultPdfDeleteBookmarks.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*إنشاء رابط لتنزيل الملف الناتج*/
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
    const ffilePdfDeleteBookmarks = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*حذف العلامات المرجعية من ملف PDF وحفظ "ResultPdfDeleteBookmarks.pdf" - اطلب من Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfDeleteBookmarks', "params": [event.target.result, e.target.files[0].name, "ResultPdfDeleteBookmarks.pdf"] }, [event.target.result]);
        };
        file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*إنشاء رابط لتنزيل الملف الناتج*/
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