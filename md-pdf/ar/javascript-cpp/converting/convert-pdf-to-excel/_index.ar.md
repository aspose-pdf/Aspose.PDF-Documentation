---

title: تحويل PDF إلى Excel في JavaScript  
linktitle: تحويل PDF إلى Excel  
type: docs  
weight: 20  
url: /javascript-cpp/convert-pdf-to-xlsx/  
lastmod: "2023-11-01"  
keywords: تحويل PDF إلى Excel باستخدام javascript، تحويل PDF إلى XLSX، تحويل PDF إلى CSV.  
description: Aspose.PDF لـ JavaScript يسمح لك بتحويل PDF إلى XLSX، وصيغ CSV.  
sitemap:  
    changefreq: "monthly"  
    priority: 0.7  
---
## إنشاء جداول بيانات من PDF باستخدام JavaScript

**Aspose.PDF لـ JavaScript** يدعم ميزة تحويل ملفات PDF إلى صيغ Excel وCSV.

{{% alert color="success" %}}  
**جرّب تحويل PDF إلى Excel عبر الإنترنت**

Aspose.PDF لـ JavaScript يقدم لك تطبيقًا مجانيًا عبر الإنترنت ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx) حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى Excel بتطبيق مجاني](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)  
{{% /alert %}}

تعتمد عملية التحويل على عدد الصفحات في المستند ويمكن أن تكون مستهلكة للوقت.
 لذلك، نوصي بشدة باستخدام Web Workers.

يوضح هذا الكود طريقة لتحميل مهام تحويل ملفات PDF المستهلكة للموارد إلى web worker لمنع حجب خيط واجهة المستخدم الرئيسية. كما يقدم طريقة سهلة الاستخدام لتنزيل الملف المحول.

## تحويل PDF إلى XLSX

```js

  /*إنشاء Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`خطأ من Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'تم التحميل!' :
        (evt.data.json.errorCode == 0) ? `النتيجة:\n${DownloadFile(evt.data.json.fileNameResult, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", evt.data.params[0])}` : `خطأ: ${evt.data.json.errorText}`;

    /*معالج الحدث*/
    const ffileToXlsX = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*تحويل ملف PDF إلى XlsX وحفظ "ResultPDFtoXlsX.xlsx" - طلب من Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToXlsX', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoXlsX.xlsx"] }, [event.target.result]);
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

يظهر مقطع الشفرة JavaScript التالي مثالاً بسيطًا لتحويل صفحات PDF إلى ملفات XlsX:

1. اختر ملف PDF للتحويل.
2. قم بإنشاء 'FileReader'.
3. يتم تنفيذ دالة [AsposePdfToXlsX](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdftoxlsx/).
4. يتم تعيين اسم الملف الناتج، في هذا المثال "ResultPDFtoXlsX.xlsx".
5. بعد ذلك، إذا كان 'json.errorCode' هو 0، فسيتم إعطاء ملف النتيجة الاسم الذي حددته سابقًا. إذا لم يكن معامل 'json.errorCode' مساويًا لـ 0 وبالتالي سيكون هناك خطأ في ملفك، فستكون معلومات حول هذا الخطأ موجودة في ملف 'json.errorText'.
6. ونتيجة لذلك، تقوم دالة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) بإنشاء رابط وتسمح لك بتحميل الملف الناتج إلى نظام تشغيل المستخدم.

```js

  var ffileToXlsX = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*تحويل ملف PDF إلى XlsX وحفظ "ResultPDFtoXlsX.xlsx"*/
      const json = AsposePdfToXlsX(event.target.result, e.target.files[0].name, "ResultPDFtoXlsX.xlsx");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*إنشاء رابط لتحميل ملف النتيجة*/
      DownloadFile(json.fileNameResult, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```


## تحويل PDF إلى CSV

```js

    /*إنشاء عامل ويب*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`خطأ من عامل الويب: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'تم التحميل!' :
        (evt.data.json.errorCode == 0) ? 
          `عدد الملفات (الجداول): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "text/csv", element) ) ?? ""}` : 
          `خطأ: ${evt.data.json.errorText}`;

    /*معالج الحدث*/
    const ffileToCSV = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*تحويل ملف PDF إلى CSV (استخراج الجداول) مع قالب "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... رقم الصفحة بصيغة)، TAB كمحدد وحفظ - اسأل عامل الويب*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfTablesToCSV', "params": [event.target.result, e.target.files[0].name, "ResultPdfTablesToCSV{0:D2}.csv", "\t"] }, [event.target.result]);
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


The following JavaScript code snippet shows simple example of coverting PDF into CSV:

يوضح مقتطف الشيفرة البرمجية التالي بلغة جافا سكريبت مثالاً بسيطًا لتحويل ملف PDF إلى CSV:

1. Select a PDF file for converting.
   
   اختر ملف PDF للتحويل.
   
2. Create a 'FileReader'.

   أنشئ 'FileReader'.

3. The [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftablestocsv/) function is executed.

   يتم تنفيذ وظيفة [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftablestocsv/).

4. The name of the resulting file is set, in this example "ResultPdfTablesToCSV{0:D2}.csv".

   يتم تعيين اسم الملف الناتج، في هذا المثال "ResultPdfTablesToCSV{0:D2}.csv".

5. Next, if the 'json.errorCode' is 0, then your result File is given the name you specified earlier. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.

   بعد ذلك، إذا كان 'json.errorCode' يساوي 0، فسيتم إعطاء ملف النتيجة الاسم الذي حددته سابقًا. إذا لم يكن معامل 'json.errorCode' يساوي 0، وبناءً على ذلك، سيكون هناك خطأ في ملفك، فستحتوي المعلومات حول هذا الخطأ في ملف 'json.errorText'.

6. As a result, the [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) function generates a link and allows you to download the resulting file to the user's operating system.

   وكنتيجة لذلك، تقوم وظيفة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) بإنشاء رابط وتتيح لك تنزيل الملف الناتج إلى نظام تشغيل المستخدم.

```js

  var ffileToCSV = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Convert a PDF-file to CSV (extract tables) with template "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... format page number), TAB as delimiter*/
        const json = AsposePdfTablesToCSV(event.target.result, e.target.files[0].name, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
        if (json.errorCode == 0) {
          document.getElementById('output').textContent = "Files(tables) count: " + json.filesCount.toString();
          /*Make links to result files*/
          for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "text/csv");
        }
        else document.getElementById('output').textContent = json.errorText;
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```