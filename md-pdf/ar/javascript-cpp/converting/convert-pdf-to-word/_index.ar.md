---
title: تحويل ملفات PDF إلى مستندات Word في JavaScript
linktitle: تحويل PDF إلى Word
type: docs
weight: 10
url: /javascript-cpp/convert-pdf-to-doc/
lastmod: "2023-08-04"
description: تعلم كيفية كتابة كود JavaScript لتحويل PDF إلى DOC (DOCX) مباشرة على الويب.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

تعتمد عملية التحويل على عدد الصفحات في المستند ويمكن أن تكون مستهلكة للوقت بشكل كبير. لذلك، نوصي بشدة باستخدام عمال الويب.

يوضح هذا الكود طريقة لنقل مهام تحويل ملفات PDF المكثفة للموارد إلى عامل ويب لمنع حظر خيط واجهة المستخدم الرئيسية. كما يقدم طريقة سهلة الاستخدام لتنزيل الملف المحول.

لتحرير محتوى ملف PDF في Microsoft Word أو معالجات النصوص الأخرى التي تدعم تنسيقات DOC وDOCX. ملفات PDF قابلة للتحرير، لكن ملفات DOC وDOCX أكثر مرونة وقابلية للتخصيص.

{{% alert color="success" %}}
**حاول تحويل PDF إلى DOC عبر الإنترنت**

يقدم لك Aspose.PDF لـ JavaScript تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل PDF إلى DOC](/pdf/javascript-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## تحويل PDF إلى DOC

```js

  /*إنشاء عامل ويب*/
  const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
  AsposePDFWebWorker.onerror = evt => console.log(`خطأ من عامل الويب: ${evt.message}`);
  AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
    (evt.data == 'ready') ? 'تم التحميل!' :
      (evt.data.json.errorCode == 0) ? `النتيجة:\n${DownloadFile(evt.data.json.fileNameResult, "application/msword", evt.data.params[0])}` : `خطأ: ${evt.data.json.errorText}`;

  /*معالج الحدث*/
  const ffileToDoc = e => {
    const file_reader = new FileReader();
    file_reader.onload = event => {
      /*تحويل ملف PDF إلى Doc وحفظ "ResultPDFtoDoc.doc" - طلب من عامل الويب*/
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToDoc', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoDoc.doc"] }, [event.target.result]);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

  /*إنشاء رابط لتنزيل ملف النتيجة*/
  const DownloadFile = (filename, mime, content) => {
      mime = mime || "application/octet-stream";
      var link = document.createElement("a"); 
      link.href = URL.createObjectURL(new Blob([content], {type: mime}));
      link.download = filename;
      link.innerHTML = "اضغط هنا لتنزيل الملف " + filename;
      document.body.appendChild(link); 
      document.body.appendChild(document.createElement("br"));
      return filename;
    }
```


يوضح مقتطف الشيفرة البرمجية التالي بلغة JavaScript مثالًا بسيطًا لتحويل صفحات PDF إلى ملفات DOC:

1. اختر ملف PDF للتحويل.
2. أنشئ 'FileReader'.
3. يتم تنفيذ وظيفة [AsposePdfToDoc](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftodoc/).
4. يتم تعيين اسم الملف الناتج، في هذا المثال "ResultPDFtoDoc.doc".
5. بعد ذلك، إذا كان 'json.errorCode' يساوي 0، يتم إعطاء ملف النتيجة الاسم الذي حددته سابقًا. إذا كان معامل 'json.errorCode' لا يساوي 0، ووفقًا لذلك، سيكون هناك خطأ في ملفك، فسيتم احتواء معلومات حول هذا الخطأ في ملف 'json.errorText'.
6. كنتيجة، تقوم وظيفة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) بإنشاء رابط وتسمح لك بتنزيل الملف الناتج إلى نظام التشغيل الخاص بالمستخدم.

```js

  var ffileToDoc = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*حوّل ملف PDF إلى Doc واحفظ "ResultPDFtoDoc.doc"*/
      const json = AsposePdfToDoc(event.target.result, e.target.files[0].name, "ResultPDFtoDoc.doc");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*أنشئ رابطًا لتنزيل ملف النتيجة*/
      DownloadFile(json.fileNameResult, "application/msword");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```


{{% alert color="warning" %}}
**حاول تحويل PDF إلى DOCX عبر الإنترنت**

تقدم Aspose.PDF for JavaScript تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تطبيق Aspose.PDF لتحويل PDF إلى Word مجاناً](/pdf/javascript-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## تحويل PDF إلى DOCX

يسمح لك Aspose.PDF for JavaScript API بقراءة وتحويل مستندات PDF إلى DOCX. DOCX هو تنسيق معروف لمستندات Microsoft Word حيث تم تغيير هيكله من ثنائي بسيط إلى مزيج من ملفات XML وملفات ثنائية. يمكن فتح ملفات Docx باستخدام Word 2007 والإصدارات اللاحقة ولكن ليس مع الإصدارات السابقة من MS Word التي تدعم ملحقات ملفات DOC.

```js

  /*إنشاء Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`خطأ من Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'محمل!' :
        (evt.data.json.errorCode == 0) ? `النتيجة:\n${DownloadFile(evt.data.json.fileNameResult, "application/vnd.openxmlformats-officedocument.wordprocessingml.document", evt.data.params[0])}` : `خطأ: ${evt.data.json.errorText}`;

    /*معالج الحدث*/
    const ffileToDocX = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*تحويل ملف PDF إلى DocX وحفظ "ResultPDFtoDocX.docx" - اسأل Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToDocX', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoDocX.docx"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [مقتطف الشيفرة]

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


الشفرة التالية بلغة JavaScript تعرض مثالًا بسيطًا لتحويل صفحات PDF إلى ملفات DOCX:

1. اختر ملف PDF للتحويل.
1. أنشئ 'FileReader'.
1. يتم تنفيذ وظيفة [AsposePdfToDocX](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdftodocx/).
1. يتم تعيين اسم الملف الناتج، في هذا المثال "ResultPDFtoDocX.docx".
1. بعد ذلك، إذا كان 'json.errorCode' يساوي 0، فإن ملف النتيجة يُعطى الاسم الذي حددته سابقًا. إذا كان معامل 'json.errorCode' لا يساوي 0 وبالتالي سيكون هناك خطأ في الملف، فسيتم احتواء معلومات حول هذا الخطأ في ملف 'json.errorText'.
1. كنتيجة لذلك، تقوم وظيفة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) بإنشاء رابط وتسمح لك بتنزيل الملف الناتج إلى نظام التشغيل الخاص بالمستخدم.

```js

  var ffileToDocX = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*تحويل ملف PDF إلى DocX وحفظه باسم "ResultPDFtoDocX.docx"*/
      const json = AsposePdfToDocX(event.target.result, e.target.files[0].name, "ResultPDFtoDocX.docx");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*إنشاء رابط لتنزيل ملف النتيجة*/
      DownloadFile(json.fileNameResult, "application/vnd.openxmlformats-officedocument.wordprocessingml.document");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```