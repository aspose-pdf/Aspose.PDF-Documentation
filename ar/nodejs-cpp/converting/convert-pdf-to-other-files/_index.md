---
title: تحويل PDF إلى EPUB و TeX و Text و XPS في Node.js
linktitle: تحويل PDF إلى صيغ أخرى
type: docs
weight: 90
url: /ar/nodejs-cpp/convert-pdf-to-other-files/
lastmod: "2026-07-16"
description: هذا الموضوع يوضح لك كيفية تحويل ملف PDF إلى صيغ ملفات أخرى مثل EPUB و LaTeX و Text و XPS وغيرها في بيئة Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

{{% alert color="success" %}}
**حاول تحويل PDF إلى EPUB عبر الإنترنت**

Aspose.PDF for Node.js يقدم لك تطبيقًا مجانيًا عبر الإنترنت [PDF إلى EPUB](https://products.aspose.app/pdf/conversion/pdf-to-epub), حيث يمكنك محاولة التحقيق في الوظيفة والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى EPUB مع تطبيق مجاني](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## تحويل PDF إلى EPUB

**<abbr title="Electronic Publication">EPUB</abbr>** هو معيار للكتب الإلكترونية مجاني ومفتوح المصدر من المنتدى الدولي للنشر الرقمي (IDPF). الملفات تحمل الامتداد .epub.
تم تصميم EPUB للمحتوى القابل لإعادة التدفق، مما يعني أن قارئ EPUB يمكنه تحسين النص لجهاز عرض معين. يدعم EPUB أيضًا المحتوى ذو التخطيط الثابت. يهدف التنسيق إلى أن يكون تنسيقًا موحدًا يمكن للناشرين ومنازل التحويل استخدامه داخليًا، وكذلك للتوزيع والبيع. وهو يحل محل معيار Open eBook.

في حال رغبتك في تحويل مستند PDF، يمكنك استخدام [AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/) دالة. 
يرجى التحقق من مقتطف الشيفرة التالي من أجل التحويل في بيئة Node.js.

**CommonJS:**

1. اتصال `require` واستيراد `asposepdfnodejs` الوحدة كـ `AsposePdf` متغيّر.
1. حدد اسم ملف PDF الذي سيتم تحويله.
1. اتصال `AsposePdf` كـ Promise وقم بأداء العملية لتحويل الملف. استقبل الكائن إذا كان ناجحًا.
1. استدع الدالة [AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPDFtoEPUB.epub". إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي ظهر خطأ في ملفك، ستتضمن معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to ePub and save the "ResultPDFtoEPUB.epub"*/
      const json = AsposePdfModule.AsposePdfToEPUB(pdf_file, "ResultPDFtoEPUB.epub");
      console.log("AsposePdfToEPUB => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد الـ `asposepdfnodejs` الوحدة.
1. حدد اسم ملف PDF الذي سيتم تحويله
1. ابدأ وحدة AsposePdf. استلم الكائن إذا نجح.
1. استدع الدالة [AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPDFtoEPUB.epub". إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي ظهر خطأ في ملفك، ستتضمن معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to ePub and save the "ResultPDFtoEPUB.epub"*/
  const json = AsposePdfModule.AsposePdfToEPUB(pdf_file, "ResultPDFtoEPUB.epub");
  console.log("AsposePdfToEPUB => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**جرّب تحويل PDF إلى LaTeX/TeX عبر الإنترنت**

Aspose.PDF for Node.js يقدم لك تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), حيث يمكنك محاولة التحقيق في الوظيفة والجودة التي يعمل بها.

[![تحويل Aspose.PDF PDF إلى LaTeX/TeX باستخدام تطبيق مجاني](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## تحويل PDF إلى TeX

**Aspose.PDF for Node.js** يدعم تحويل PDF إلى TeX.
في حال رغبتك في تحويل مستند PDF، يمكنك استخدام [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/) دالة. 
يرجى التحقق من مقتطف الشيفرة التالي من أجل التحويل في بيئة Node.js.

**CommonJS:**

1. اتصال `require` واستيراد `asposepdfnodejs` الوحدة كـ `AsposePdf` متغيّر.
1. حدد اسم ملف PDF الذي سيتم تحويله.
1. اتصال `AsposePdf` كـ Promise وقم بأداء العملية لتحويل الملف. استقبل الكائن إذا كان ناجحًا.
1. استدع الدالة [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPDFtoTeX.tex". إذا لم يكن معامل json.errorCode يساوي 0، وبالتالي ظهر خطأ في ملفك، سيتم تضمين معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to TeX and save the "ResultPDFtoTeX.tex"*/
      const json = AsposePdfModule.AsposePdfToTeX(pdf_file, "ResultPDFtoTeX.tex");
      console.log("AsposePdfToTeX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد الـ `asposepdfnodejs` الوحدة.
1. حدد اسم ملف PDF الذي سيتم تحويله
1. ابدأ وحدة AsposePdf. استلم الكائن إذا نجح.
1. استدع الدالة [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPDFtoTeX.tex". إذا لم يكن معامل json.errorCode يساوي 0، وبالتالي ظهر خطأ في ملفك، سيتم تضمين معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to TeX and save the "ResultPDFtoTeX.tex"*/
  const json = AsposePdfModule.AsposePdfToTeX(pdf_file, "ResultPDFtoTeX.tex");
  console.log("AsposePdfToTeX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى نص عبر الإنترنت**

Aspose.PDF for Node.js يقدم لك تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى نص"](https://products.aspose.app/pdf/conversion/pdf-to-txt), حيث يمكنك محاولة التحقيق في الوظيفة والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى نص باستخدام تطبيق مجاني](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## تحويل PDF إلى TXT

في حال رغبتك في تحويل مستند PDF، يمكنك استخدام [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/) دالة. 
يرجى التحقق من مقتطف الشيفرة التالي من أجل التحويل في بيئة Node.js.

**CommonJS:**

1. اتصال `require` واستيراد `asposepdfnodejs` الوحدة كـ `AsposePdf` متغيّر.
1. حدد اسم ملف PDF الذي سيتم تحويله.
1. اتصال `AsposePdf` كـ Promise وقم بأداء العملية لتحويل الملف. استقبل الكائن إذا كان ناجحًا.
1. استدع الدالة [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، فإن نتيجة العملية تُحفظ في "ResultPDFtoTxt.txt". إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي ظهر خطأ في ملفك، فستحتوي معلومات الخطأ على 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to Txt and save the "ResultPDFtoTxt.txt"*/
      const json = AsposePdfModule.AsposePdfToTxt(pdf_file, "ResultPDFtoTxt.txt");
      console.log("AsposePdfToTxt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد الـ `asposepdfnodejs` الوحدة.
1. حدد اسم ملف PDF الذي سيتم تحويله
1. ابدأ وحدة AsposePdf. استلم الكائن إذا نجح.
1. استدع الدالة [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، فإن نتيجة العملية تُحفظ في "ResultPDFtoTxt.txt". إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي ظهر خطأ في ملفك، فستحتوي معلومات الخطأ على 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to Txt and save the "ResultPDFtoTxt.txt"*/
  const json = AsposePdfModule.AsposePdfToTxt(pdf_file, "ResultPDFtoTxt.txt");
  console.log("AsposePdfToTxt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى XPS عبر الإنترنت**

Aspose.PDF for Node.js يقدم لك تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), حيث يمكنك محاولة التحقيق في الوظيفة والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى XPS باستخدام تطبيق مجاني](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## تحويل PDF إلى XPS

نوع ملف XPS مرتبط أساسًا بـ XML Paper Specification من شركة Microsoft Corporation. XML Paper Specification (XPS)، الذي كان يُطلق عليه سابقًا الاسم الرمزي Metro ويضم مفهوم التسويق Next Generation Print Path (NGPP)، هو مبادرة Microsoft لدمج إنشاء المستندات وعرضها في نظام تشغيل Windows.

**Aspose.PDF for Node.js** يتيح إمكانية تحويل ملفات PDF إلى <abbr title="XML Paper Specification">XPS</abbr> تنسيق. دعنا نجرب استخدام مقتطف الشيفرة المعروض لتحويل ملفات PDF إلى تنسيق XPS باستخدام Node.js.

في حال رغبتك في تحويل مستند PDF، يمكنك استخدام [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/) دالة. 
يرجى التحقق من مقتطف الشيفرة التالي من أجل التحويل في بيئة Node.js.

**CommonJS:**

1. اتصال `require` واستيراد `asposepdfnodejs` الوحدة كـ `AsposePdf` متغيّر.
1. حدد اسم ملف PDF الذي سيتم تحويله.
1. اتصال `AsposePdf` كـ Promise وقم بأداء العملية لتحويل الملف. استقبل الكائن إذا كان ناجحًا.
1. استدع الدالة [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPDFtoXps.xps". إذا لم يكن معامل json.errorCode يساوي 0 وبناءً عليه ظهر خطأ في ملفك، فإن معلومات الخطأ ستكون موجودة في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to Xps and save the "ResultPDFtoXps.xps"*/
      const json = AsposePdfModule.AsposePdfToXps(pdf_file, "ResultPDFtoXps.xps");
      console.log("AsposePdfToXps => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد الـ `asposepdfnodejs` الوحدة.
1. حدد اسم ملف PDF الذي سيتم تحويله.
1. ابدأ وحدة AsposePdf. استلم الكائن إذا نجح.
1. استدع الدالة [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPDFtoXps.xps". إذا لم يكن معامل json.errorCode يساوي 0 وبناءً عليه ظهر خطأ في ملفك، فإن معلومات الخطأ ستكون موجودة في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to Xps and save the "ResultPDFtoXps.xps"*/
  const json = AsposePdfModule.AsposePdfToXps(pdf_file, "ResultPDFtoXps.xps");
  console.log("AsposePdfToXps => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

## تحويل PDF إلى PDF بتدرج الرمادي

تحويل PDF إلى أبيض وأسود باستخدام Aspose.PDF for Node.js via C++ toolkit. 
لماذا يجب علي تحويل PDF إلى تدرج الرمادي؟ إذا كان ملف PDF يحتوي على العديد من الصور الملونة وكان حجم الملف مهمًا بدلاً من اللون، فإن التحويل يوفر مساحة. إذا قمت بطباعة ملف PDF بالأبيض والأسود، سيسمح لك التحويل بالتحقق بصريًا مما يبدو عليه النتيجة النهائية. 

في حال رغبتك في تحويل مستند PDF، يمكنك استخدام [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/) دالة. 
يرجى التحقق من مقتطف الشيفرة التالي من أجل التحويل في بيئة Node.js.

**CommonJS:**

1. اتصال `require` واستيراد `asposepdfnodejs` الوحدة كـ `AsposePdf` متغيّر.
1. حدد اسم ملف PDF الذي سيتم تحويله.
1. اتصال `AsposePdf` كـ Promise وقم بأداء العملية لتحويل الملف. استقبل الكائن إذا كان ناجحًا.
1. استدع الدالة [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultConvertToGrayscale.pdf". إذا لم يكن معلمة json.errorCode تساوي 0 وبالتالي ظهر خطأ في ملفك، ستتضمن معلومات الخطأ في 'json.errorText'.

```js

const AsposePdf = require('asposepdfnodejs');
const pdf_file = 'Aspose.pdf';
AsposePdf().then(AsposePdfModule => {
    /*Convert a PDF-file to grayscale and save the "ResultConvertToGrayscale.pdf"*/
    const json = AsposePdfModule.AsposePdfConvertToGrayscale(pdf_file, "ResultConvertToGrayscale.pdf");
    console.log("AsposePdfConvertToGrayscale => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
});
```

**ECMAScript/ES6:**

1. استيراد الـ `asposepdfnodejs` الوحدة.
1. حدد اسم ملف PDF الذي سيتم تحويله.
1. ابدأ وحدة AsposePdf. استلم الكائن إذا نجح.
1. استدع الدالة [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultConvertToGrayscale.pdf". إذا لم يكن معلمة json.errorCode تساوي 0 وبالتالي ظهر خطأ في ملفك، ستتضمن معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to grayscale and save the "ResultConvertToGrayscale.pdf"*/
  const json = AsposePdfModule.AsposePdfConvertToGrayscale(pdf_file, "ResultConvertToGrayscale.pdf");
  console.log("AsposePdfConvertToGrayscale => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```






