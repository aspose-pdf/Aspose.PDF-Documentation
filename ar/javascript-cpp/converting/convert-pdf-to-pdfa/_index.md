---
title: تحويل PDF إلى تنسيقات PDF/A
linktitle: تحويل PDF إلى تنسيقات PDF/A
type: docs
weight: 100
url: /ar/javascript-cpp/convert-pdf-to-pdfa/
lastmod: "2023-11-01"
description: يوضح هذا الموضوع كيف يسمح Aspose.PDF بتحويل ملف PDF إلى ملف PDF متوافق مع PDF/A.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for JavaScript** يسمح لك بتحويل ملف PDF إلى ملف PDF متوافق مع <abbr title="Portable Document Format / A">PDF/A</abbr>.

تعتمد عملية التحويل على عدد الصفحات في المستند ويمكن أن تكون مستهلكة جدًا للوقت. لذلك، نوصي بشدة باستخدام عمال الويب.

يوضح هذا الكود طريقة لنقل المهام المرهقة لموارد تحويل ملفات PDF إلى عامل ويب لمنع حجب سلسلة واجهة المستخدم الرئيسية. كما يقدم طريقة سهلة للمستخدم لتنزيل الملف المحول.

{{% alert color="success" %}}
**حاول تحويل PDF إلى PDF/A عبر الإنترنت**

يقدم Aspose.PDF for JavaScript تطبيقًا مجانيًا عبر الإنترنت ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF Convertion PDF to PDF/A with Free App](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}


## تحويل PDF إلى تنسيق PDF/A

```js

  /*إنشاء عامل ويب*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`خطأ من عامل الويب: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'تم التحميل!' :
        (evt.data.json.errorCode == 0) ? `النتيجة:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}\n${DownloadFile(evt.data.json.fileNameLogResult, "application/xml", evt.data.params[1])}` : `خطأ: ${evt.data.json.errorText}`;

    /*معالج الحدث*/
    const ffilePdfConvertToPDFA = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const pdfFormat = 'Module.PdfFormat.PDF_A_1A';
        /*تحويل ملف PDF إلى PDF/A(1A) وحفظ "ResultConvertToPDFA.pdf"*/
        /*أثناء عملية التحويل، يتم أيضًا إجراء التحقق، "ResultConvertToPDFA.xml" - اسأل عامل الويب*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfConvertToPDFA', "params": [event.target.result, e.target.files[0].name, pdfFormat, "ResultConvertToPDFA.pdf", "ResultConvertToPDFA.xml"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [مقتطف الكود]

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


The following JavaScript code snippet shows simple example of coverting PDF to PDF/A files:

1. حدد ملف PDF للتحويل.
1. قم بإنشاء 'FileReader'.
1. يتم تنفيذ وظيفة [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfconverttopdfa/).
1. يتم تعيين اسم الملف الناتج، في هذا المثال "ResultConvertToPDFA.pdf". أثناء عملية التحويل، يتم أيضًا إجراء التحقق، "ResultConvertToPDFA.xml".
1. بعد ذلك، إذا كانت 'json.errorCode' تساوي 0، فسيتم إعطاء ملف التنزيل الخاص بك الاسم الذي حددته سابقًا. إذا لم يكن معامل 'json.errorCode' يساوي 0 وبالتالي سيكون هناك خطأ في ملفك، فسيتم احتواء معلومات حول هذا الخطأ في ملف 'json.errorText'.
1. كنتيجة لذلك، تقوم وظيفة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) بإنشاء رابط وتسمح لك بتنزيل الملف الناتج، ورابط لتنزيل ملف السجل (xml) إلى نظام تشغيل المستخدم.

```js

  var ffilePdfConvertToPDFA = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*تحويل ملف PDF إلى PDF/A(1A) وحفظ "ResultConvertToPDFA.pdf"*/
      /*أثناء عملية التحويل، يتم أيضًا إجراء التحقق، "ResultConvertToPDFA.xml"*/
      const json = AsposePdfConvertToPDFA(event.target.result, e.target.files[0].name, Module.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFA.xml");
      if (json.errorCode == 0)
      {
        document.getElementById('output').textContent = json.fileNameResult + "\nملف السجل (صيغة xml): " + json.fileNameLogResult;
        /*إنشاء رابط لتنزيل الملف الناتج*/
        DownloadFile(json.fileNameResult, "application/pdf");
      }
      else document.getElementById('output').textContent = json.errorText + "\nملف السجل (صيغة xml): " + json.fileNameLogResult;
      /*إنشاء رابط لتنزيل ملف السجل (xml)*/
      DownloadFile(json.fileNameLogResult, "application/xml");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```