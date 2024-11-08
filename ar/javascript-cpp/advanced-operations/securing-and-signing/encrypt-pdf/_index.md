---
title: تشفير PDF باستخدام JavaScript
linktitle: تشفير ملف PDF
type: docs
weight: 50
url: /ar/javascript-cpp/encrypt-pdf/
description: تشفير ملف PDF باستخدام Aspose.PDF لـ JavaScript عبر C++.
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## تشفير ملف PDF باستخدام كلمة مرور للمستخدم أو المالك

إذا كنت ترسل بريدًا إلكترونيًا إلى شخص ما مع مرفق PDF يحتوي على معلومات سرية، قد ترغب في إضافة بعض الأمان إليه أولًا لمنعه من الوقوع في الأيدي الخطأ. أفضل طريقة للحد من الوصول غير المصرح به إلى مستند PDF هي حمايته بكلمة مرور. لتشفير المستندات بسهولة وأمان، يمكنك استخدام Aspose.PDF لـ JavaScript عبر C++.

>يرجى تحديد كلمات مرور مختلفة للمستخدم والمالك أثناء تشفير ملف PDF.

- **كلمة مرور المستخدم**، إذا تم تعيينها، هي ما تحتاج إلى تقديمه لفتح ملف PDF. سيطلب Acrobat/Reader من المستخدم إدخال كلمة مرور المستخدم. إذا لم تكن صحيحة، لن يفتح المستند.
- **كلمة مرور المالك**، إذا تم تعيينها، تتحكم في الأذونات، مثل الطباعة، التحرير، الاستخراج، التعليق، إلخ.
 Acrobat/Reader سيمنع هذه الأشياء بناءً على إعدادات الأذونات. سيتطلب Acrobat كلمة المرور هذه إذا كنت ترغب في تعيين/تغيير الأذونات.

يظهر لك كود البرمجة التالي كيفية تشفير ملفات PDF.

1. اختر ملف PDF للتشفير.
1. أنشئ 'FileReader'.
1. يتم تنفيذ وظيفة [AsposePdfEncrypt](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfencrypt/).
1. يتم تحديد اسم الملف الناتج، وفي هذا المثال "ResultEncrypt.pdf".
1. بعد ذلك، إذا كان 'json.errorCode' يساوي 0، فسيتم إعطاء DownloadFile الاسم الذي حددته سابقًا. إذا كان معطى 'json.errorCode' لا يساوي 0 وبالتالي سيكون هناك خطأ في ملفك، فإن المعلومات حول هذا الخطأ ستكون موجودة في ملف 'json.errorText'.
1. كنتيجة لذلك، فإن وظيفة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) تقوم بإنشاء رابط وتسمح لك بتنزيل الملف الناتج إلى نظام التشغيل الخاص بالمستخدم.

```js

  var ffileEncrypt = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*تشفير ملف PDF بكلمات مرور "user" و "owner"، وحفظ "ResultDecrypt.pdf"*/
      const json = AsposePdfEncrypt(event.target.result, e.target.files[0].name, "user", "owner", Module.Permissions.PrintDocument, Module.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
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
      (evt.data == 'ready') ? 'تم التحميل!' :
        (evt.data.json.errorCode == 0) ?
          `النتيجة:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `خطأ: ${evt.data.json.errorText}`;

    /*معالج الحدث*/
    const ffileEncrypt = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const password_user = 'user';
        const password_owner = 'owner';
        const permissions = 'Module.Permissions.PrintDocument';
        const algorithm = 'Module.CryptoAlgorithm.RC4x40';
        /*تشفير ملف PDF بكلمات مرور "user" و "owner"، وحفظ "ResultEncrypt.pdf" - طلب من عامل الويب*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfEncrypt',
            "params": [event.target.result, e.target.files[0].name, password_user, password_owner,
                      permissions, algorithm, "ResultEncrypt.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*إنشاء رابط لتحميل ملف النتيجة*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "انقر هنا لتحميل الملف " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```