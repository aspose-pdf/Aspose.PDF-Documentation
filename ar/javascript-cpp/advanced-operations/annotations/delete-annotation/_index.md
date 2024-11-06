---
title: حذف التعليق التوضيحي باستخدام JavaScript
linktitle: حذف التعليق التوضيحي
type: docs
weight: 10
url: ar/javascript-cpp/delete-annotation/
description: باستخدام Aspose.PDF لـ JavaScript يمكنك حذف التعليق التوضيحي من ملف PDF الخاص بك.
lastmod: "2023-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

يمكنك حذف التعليقات التوضيحية من ملف PDF باستخدام Aspose.PDF لـ JavaScript عبر C++. يمكنك الحصول على النتيجة مباشرة في متصفحك.

1. قم بإنشاء 'FileReader'.
2. يتم تنفيذ وظيفة [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfdeleteannotations/).
3. يتم تعيين اسم الملف الناتج، في هذا المثال "ResultPdfDeleteAnnotations.pdf".
4. بعد ذلك، إذا كان 'json.errorCode' يساوي 0، فسيتم إعطاء ملف التنزيل الخاص بك الاسم الذي حددته سابقًا. إذا لم يكن معامل 'json.errorCode' يساوي 0، وبالتالي سيكون هناك خطأ في ملفك، فسيتم احتواء معلومات عن هذا الخطأ في ملف 'json.errorText'.

1. ونتيجة لذلك، تقوم وظيفة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) بإنشاء رابط وتسمح لك بتنزيل الملف الناتج إلى نظام التشغيل الخاص بالمستخدم.

```js

    var ffilePdfDeleteAnnotations = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*حذف التعليقات التوضيحية من ملف PDF وحفظ "ResultPdfDeleteAnnotations.pdf"*/
        const json = AsposePdfDeleteAnnotations(event.target.result, e.target.files[0].name, "ResultPdfDeleteAnnotations.pdf");
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
    const ffilePdfDeleteAnnotations = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*حذف التعليقات التوضيحية من ملف PDF وحفظ "ResultPdfDeleteAnnotations.pdf" - اطلب من عامل الويب*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfDeleteAnnotations', "params": [event.target.result, e.target.files[0].name, "ResultPdfDeleteAnnotations.pdf"] }, [event.target.result]);
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