---
title: إزالة المرفقات من PDF باستخدام JavaScript
linktitle: إزالة المرفقات من ملف PDF موجود
type: docs
weight: 10
url: ar/javascript-cpp/removing-attachment-from-an-existing-pdf/
description: يمكن لـ Aspose.PDF إزالة المرفقات من مستندات PDF الخاصة بك. استخدم مجموعة أدوات الويب JavaScript لإزالة المرفقات في ملفات PDF باستخدام Aspose.PDF.
lastmod: "2023-09-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

يمكنك حذف المرفقات من ملف PDF باستخدام Aspose.PDF لـ JavaScript عبر C++. يمكنك الحصول على النتيجة مباشرة في متصفحك.

1. قم بإنشاء 'FileReader'.
1. يتم تنفيذ وظيفة [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfdeleteattachments/).
1. يتم تعيين اسم الملف الناتج، في هذا المثال "ResultPdfDeleteAttachments.pdf".

1. بعد ذلك، إذا كان 'json.errorCode' يساوي 0، فإن ملفك المحمل DownloadFile سيُعطى الاسم الذي حددته سابقًا. إذا كانت قيمة 'json.errorCode' لا تساوي 0، وبناءً على ذلك، سيكون هناك خطأ في ملفك، فإن معلومات عن هذا الخطأ سيتم تضمينها في ملف 'json.errorText'.  
1. كنتيجة لذلك، تقوم دالة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) بإنشاء رابط وتسمح لك بتحميل الملف الناتج إلى نظام تشغيل المستخدم.

```js

    var ffilePdfDeleteAttachments = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*حذف المرفقات من ملف PDF وحفظ الملف "ResultPdfDeleteAttachments.pdf"*/
        const json = AsposePdfDeleteAttachments(event.target.result, e.target.files[0].name, "ResultPdfDeleteAttachments.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*إنشاء رابط لتحميل الملف الناتج*/
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
        (evt.data == 'ready') ? 'تم التحميل!' :
        (evt.data.json.errorCode == 0) ? `النتيجة:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `خطأ: ${evt.data.json.errorText}`;

    /*معالج الحدث*/
    const ffilePdfDeleteAttachments = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*حذف المرفقات من ملف PDF وحفظ "ResultPdfDeleteAttachments.pdf" - استدعاء عامل الويب*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfDeleteAttachments', "params": [event.target.result, e.target.files[0].name, "ResultPdfDeleteAttachments.pdf"] }, [event.target.result]);
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