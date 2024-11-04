---
title: استخراج الصور من ملف PDF باستخدام JavaScript
linktitle: استخراج الصور من PDF
type: docs
weight: 20
url: /javascript-cpp/extract-images-from-the-pdf-file/
description: كيفية استخراج جزء من الصورة من PDF باستخدام مجموعة أدوات Aspose.PDF لـ JavaScript.
lastmod: "2023-09-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

تتيح لك مجموعة أدوات الويب من Aspose.PDF استخراج الصور بسهولة من ملفات PDF.

في حال كنت تريد استخراج الصور من مستند PDF، يمكنك استخدام وظيفة [AsposePdfExtractImage](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextractimage/). 
يرجى الاطلاع على مقتطف الكود التالي لاستخراج الصور من ملف PDF باستخدام JavaScript عبر C++.

1. إنشاء 'FileReader'.
1. يتم تنفيذ وظيفة [AsposePdfExtractImage](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextractimage/).
1. يتم تعيين اسم الملف الناتج، في هذا المثال "ResultPdfExtractImage{0:D2}.jpg".

1. بعد ذلك، إذا كانت قيمة 'json.errorCode' تساوي 0، يمكنك الحصول على روابط لملفات النتيجة. إذا كانت قيمة 'json.errorCode' لا تساوي 0، وبالتالي، سيكون هناك خطأ في ملفك، فسيتم احتواء معلومات حول هذا الخطأ في ملف 'json.errorText'.
1. وكنتيجة لذلك، تقوم وظيفة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) بتوليد رابط وتسمح لك بتنزيل الملف الناتج على نظام تشغيل المستخدم.

```js

    var ffileExtractImage = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
    /*استخراج الصورة من ملف PDF باستخدام قالب "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... تنسيق رقم الصفحة)، بدقة 150 DPI وحفظها*/
    const json = AsposePdfExtractImage(event.target.result, e.target.files[0].name, "ResultPdfExtractImage{0:D2}.jpg", 150);
    if (json.errorCode == 0) {
        document.getElementById('output').textContent = "عدد الملفات (الصور): " + json.filesCount.toString();
        /*إنشاء روابط لملفات النتيجة*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/jpeg");
    }
    else document.getElementById('output').textContent = json.errorText;
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


## استخدام عمال الويب

```js

  /*إنشاء عامل ويب*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`خطأ من عامل الويب: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'تم التحميل!' :
        (evt.data.json.errorCode == 0) ? 
          `عدد الملفات (الصور): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/jpeg", element) ) ?? ""}` : 
          `خطأ: ${evt.data.json.errorText}`;

    /*معالج الحدث*/
    const ffileExtractImage = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*استخراج الصورة من ملف PDF باستخدام القالب "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... رقم الصفحة بتنسيق)، دقة 150 DPI وحفظ*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfExtractImage', "params": [event.target.result, e.target.files[0].name, "ResultPdfExtractImage{0:D2}.jpg", 150] }, [event.target.result]);
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