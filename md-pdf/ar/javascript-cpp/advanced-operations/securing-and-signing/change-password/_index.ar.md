---
title: تغيير كلمة مرور ملف PDF
linktitle: تغيير كلمة المرور
type: docs
weight: 50
url: /javascript-cpp/change-password-pdf/
description: تغيير كلمة مرور ملف PDF باستخدام Aspose.PDF لـ JavaScript عبر C++.
lastmod: "2023-09-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## تغيير كلمة مرور ملف PDF

إذا كنت تريد تغيير كلمة مرور ملف PDF من "owner" إلى "newowner" جرب قطعة الكود التالية:

1. اختر ملف PDF.
2. أنشئ 'FileReader'.
3. يتم تنفيذ دالة [AsposePdfChangePassword](https://reference.aspose.com/pdf/javascript-cpp/security/asposepdfchangepassword/).
4. يتم تعيين اسم الملف الناتج، في هذا المثال "ResultPdfChangePassword.pdf".
5. بعد ذلك، إذا كان 'json.errorCode' يساوي 0، سيتم إعطاء DownloadFile الاسم الذي حددته سابقًا. إذا كانت قيمة 'json.errorCode' لا تساوي 0، وبالتالي، سيكون هناك خطأ في ملفك، فسيتم احتواء معلومات حول هذا الخطأ في ملف 'json.errorText'.

1. نتيجة لذلك، تقوم وظيفة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) بإنشاء رابط وتسمح لك بتنزيل الملف الناتج إلى نظام تشغيل المستخدم.

```js

    var ffilePdfChangePassword = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*تغيير كلمات المرور لملف PDF من "owner" إلى "newowner" وحفظ "ResultPdfChangePassword.pdf"*/
        const json = AsposePdfChangePassword(event.target.result, e.target.files[0].name, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*إنشاء رابط لتنزيل ملف النتيجة*/
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
    const ffilePdfChangePassword = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const ownerPassword = 'owner'; /*كلمة مرور المالك*/
        const newUserPassword = "newuser"; /*كلمة مرور المستخدم الجديد*/
        const newOwnerPassword = "newowner"; /*كلمة مرور المالك الجديد*/
        /*تغيير كلمات المرور لملف PDF من "owner" إلى "newowner" وحفظ "ResultPdfChangePassword.pdf" - اطلب من Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfChangePassword', "params": [event.target.result, e.target.files[0].name, ownerPassword, newUserPassword, newOwnerPassword, "ResultPdfChangePassword.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Code snippet]

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