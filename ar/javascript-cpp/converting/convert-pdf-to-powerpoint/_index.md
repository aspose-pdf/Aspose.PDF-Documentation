---
title: تحويل PDF إلى PPTX في JavaScript
linktitle: تحويل PDF إلى PowerPoint
type: docs
weight: 30
url: /ar/javascript-cpp/convert-pdf-to-powerpoint/
lastmod: "2023-11-01"
description: يتيح لك Aspose.PDF تحويل PDF إلى تنسيق PPTX باستخدام JavaScript مباشرة على الويب.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

تعتمد عملية التحويل على عدد الصفحات في المستند ويمكن أن تكون مستهلكة للوقت بشكل كبير. لذلك، نوصي بشدة باستخدام Web Workers.

يوضح هذا الكود طريقة لنقل مهام تحويل ملفات PDF المكثفة للموارد إلى web worker لمنع حظر الخيوط الرئيسية لواجهة المستخدم. كما يوفر طريقة سهلة الاستخدام لتنزيل الملف المحول.

{{% alert color="success" %}}
**حاول تحويل PDF إلى PowerPoint عبر الإنترنت**

يقدم لك Aspose.PDF لـ JavaScript تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)، حيث يمكنك محاولة التحقق من الوظيفة والجودة التي يعمل بها.

[![تحويل PDF إلى PPTX باستخدام التطبيق المجاني Aspose.PDF](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

## تحويل PDF إلى PPTX

```js

  /*إنشاء عامل ويب*/
  const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
  AsposePDFWebWorker.onerror = evt => console.log(`خطأ من عامل الويب: ${evt.message}`);
  AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
    (evt.data == 'ready') ? 'تم التحميل!' :
      (evt.data.json.errorCode == 0) ? `النتيجة:\n${DownloadFile(evt.data.json.fileNameResult, "application/vnd.openxmlformats-officedocument.presentationml.presentation", evt.data.params[0])}` : `خطأ: ${evt.data.json.errorText}`;

  /*معالج الحدث*/
  const ffileToPptX = e => {
    const file_reader = new FileReader();
    file_reader.onload = event => {
      /*تحويل ملف PDF إلى PptX وحفظ "ResultPDFtoPptX.pptx" - اطلب من عامل الويب*/
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToPptX', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoPptX.pptx"] }, [event.target.result]);
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


The following JavaScript code snippet shows simple example of coverting PDF to PPTX files:

يوضح مقتطف الكود JavaScript التالي مثالًا بسيطًا لتحويل ملفات PDF إلى ملفات PPTX:

1. Select a PDF file for converting.
1. Create a 'FileReader'.
1. The [AsposePdfToPptX](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftopptx/) function is executed.
1. The name of the resulting file is set, in this example "ResultPDFtoPptX.pptx".
1. Next, if the 'json.errorCode' is 0, then your result File is given the name you specified earlier. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.
1. As a result, the [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) function generates a link and allows you to download the resulting file to the user's operating system.

1. قم باختيار ملف PDF للتحويل.
2. قم بإنشاء 'FileReader'.
3. يتم تنفيذ الدالة [AsposePdfToPptX](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftopptx/).
4. يتم تعيين اسم الملف الناتج، في هذا المثال "ResultPDFtoPptX.pptx".
5. بعد ذلك، إذا كان 'json.errorCode' يساوي 0، فإنه يتم إعطاء ملف النتيجة الاسم الذي حددته سابقًا. إذا كانت قيمة 'json.errorCode' لا تساوي 0، وبناءً عليه، سيكون هناك خطأ في ملفك، فسيتم احتواء معلومات حول هذا الخطأ في ملف 'json.errorText'.
6. كنتيجة لذلك، تقوم الدالة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) بتوليد رابط وتسمح لك بتنزيل الملف الناتج إلى نظام تشغيل المستخدم.

```js

  var ffileToPptX = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*Convert a PDF-file to PptX and save the "ResultPDFtoPptX.pptx"*/
      const json = AsposePdfToPptX(event.target.result, e.target.files[0].name, "ResultPDFtoPptX.pptx");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*Make a link to download the result file*/
      DownloadFile(json.fileNameResult, "application/vnd.openxmlformats-officedocument.presentationml.presentation");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```