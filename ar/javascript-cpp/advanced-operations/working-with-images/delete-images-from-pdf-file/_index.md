---
title: حذف الصور من ملف PDF عبر JavaScript
linktitle: حذف الصور
type: docs
weight: 20
url: ar/javascript-cpp/delete-images-from-pdf-file/
description: يشرح هذا القسم كيفية حذف الصور من ملف PDF باستخدام Aspose.PDF لـ JavaScript.
lastmod: "2022-02-17"
---

يمكنك حذف الصور من ملف PDF باستخدام Aspose.PDF لـ JavaScript عبر C++. يمكنك الحصول على النتيجة مباشرة في متصفحك.

1. قم بإنشاء 'FileReader'.
1. يتم تنفيذ وظيفة [AsposePdfDeleteImages](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfdeleteimages/).
1. يتم تعيين اسم الملف الناتج، في هذا المثال "ResultPdfDeleteImages.pdf".
1. بعد ذلك، إذا كان 'json.errorCode' يساوي 0، فسيتم إعطاء DownloadFile الاسم الذي قمت بتحديده سابقًا. إذا لم يكن معامل 'json.errorCode' يساوي 0 وبالتالي سيكون هناك خطأ في ملفك، فإن المعلومات حول هذا الخطأ ستكون موجودة في ملف 'json.errorText'.

1. كنتيجة لذلك، تقوم دالة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) بتوليد رابط وتسمح لك بتنزيل الملف الناتج إلى نظام تشغيل المستخدم.

```js

    var ffilePdfDeleteImages = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*حذف الصور من ملف PDF وحفظ "ResultPdfDeleteImages.pdf"*/
        const json = AsposePdfDeleteImages(event.target.result, e.target.files[0].name, "ResultPdfDeleteImages.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*إنشاء رابط لتنزيل ملف النتيجة*/
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
        (evt.data.json.errorCode == 0) ? `النتيجة:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `خطأ: ${evt.data.json.errorText}`;

    /*معالج الحدث*/
    const ffilePdfDeleteImages = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*حذف الصور من ملف PDF وحفظ "ResultPdfDeleteImages.pdf" - طلب عامل الويب*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfDeleteImages', "params": [event.target.result, e.target.files[0].name, "ResultPdfDeleteImages.pdf"] }, [event.target.result]);
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