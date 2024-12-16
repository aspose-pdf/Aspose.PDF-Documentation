---
title: إضافة صورة إلى PDF باستخدام JavaScript عبر C++
linktitle: إضافة صورة
type: docs
weight: 10
url: /ar/javascript-cpp/add-image-to-pdf/
description: يصف هذا القسم كيفية إضافة صورة إلى ملف PDF موجود باستخدام Aspose.PDF لـ JavaScript عبر C++.
lastmod: "2023-12-15"
---

## إضافة صورة في ملف PDF موجود

هل تحتاج إلى إرفاق صورة بملف PDF؟ هل تريد تحسين قابلية القراءة لملف PDF الخاص بك؟ أضف الصور إلى ملف PDF الخاص بك وسيبدو عرضك التقديمي أو سيرتك الذاتية أكثر جاذبية.

يُعتقد عمومًا أن إضافة الصور إلى ملفات PDF يتطلب أداة خاصة معقدة. ومع ذلك، باستخدام Aspose.PDF لـ JavaScript يمكنك بسرعة وسهولة إضافة الصور التي تحتاجها إلى ملف PDF باستخدام JavaScript مباشرة في متصفحك.

لإضافة صورة إلى ملف PDF موجود:

1. قم بتعيين اسم الملف الافتراضي للصورة.
2. أنشئ 'FileReader'.
3. قم بتعيين اسم ملف الصورة.
4. قم بتحضير ملف الصورة من BLOB.
5. يتم تنفيذ وظيفة [AsposePdfAddImage](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddimage/).

1. أضف ملف الصورة إلى نهاية ملف PDF واحفظ "ResultImage.pdf".
1. بعد ذلك، إذا كان 'json.errorCode' يساوي 0، فسيتم إعطاء ملفك القابل للتنزيل الاسم الذي حددته سابقاً. إذا لم يكن معامل 'json.errorCode' يساوي 0، وبالتالي سيكون هناك خطأ في ملفك، فسيتم تضمين معلومات عن هذا الخطأ في ملف 'json.errorText'.
1. كنتيجة لذلك، تقوم وظيفة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) بإنشاء رابط وتسمح لك بتنزيل الملف الناتج إلى نظام تشغيل المستخدم.

يوضح مقتطف الشيفرة التالي كيفية إضافة الصورة في مستند PDF.

```js

  /*تعيين اسم الملف الافتراضي للصورة*/
  var fileImage = "/Aspose.jpg";

  var ffileImage = function (e) {
    const file_reader = new FileReader();
    /*تعيين اسم ملف الصورة*/
    fileImage = e.target.files[0].name;
    file_reader.onload = (event) => {
      /*تحضير(حفظ) ملف الصورة من BLOB*/
      AsposePdfPrepare(event.target.result, fileImage);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```

في المثال التالي، نختار الصورة للتعامل معها:

```js

  var ffileAddImage = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*إضافة ملف الصورة إلى نهاية ملف PDF وحفظ "ResultImage.pdf"*/
      const json = AsposePdfAddImage(event.target.result, e.target.files[0].name, fileImage, "ResultImage.pdf");
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
        (evt.data.json.errorCode == 0) ?
          `النتيجة:\n${(evt.data.operation == 'AsposePdfPrepare') ?
            'تم تجهيز الصورة!':
            DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `خطأ: ${evt.data.json.errorText}`;

    /*تعيين اسم الملف الافتراضي للصورة: 'Aspose.jpg' تم تحميله بالفعل، انظر الإعدادات في 'settings.json'*/
    var fileImage = "Aspose.jpg";

    /*معالج الحدث*/
    const ffileAddImage = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*إضافة الصورة إلى نهاية ملف PDF وحفظ "ResultImage.pdf" - طلب من Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddImage',
            "params": [event.target.result, e.target.files[0].name, fileImage, "ResultImage.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileImage = e => {
      const file_reader = new FileReader();
      /*تعيين اسم ملف الصورة*/
      fileImage = e.target.files[0].name;
      file_reader.onload = event => {
        /*حفظ BLOB في الذاكرة للمعالجة*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfPrepare', "params": [event.target.result, e.target.files[0].name] },
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