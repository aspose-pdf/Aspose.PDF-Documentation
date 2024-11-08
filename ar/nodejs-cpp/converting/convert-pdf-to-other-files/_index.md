---
title: تحويل PDF إلى EPUB، TeX، نص، XPS في Node.js
linktitle: تحويل PDF إلى تنسيقات أخرى
type: docs
weight: 90
url: /ar/nodejs-cpp/convert-pdf-to-other-files/
lastmod: "2023-11-16"
keywords: تحويل، PDF، EPUB، TeX، نص، XPS، Node.js
description: يعرض هذا الموضوع كيفية تحويل ملف PDF إلى تنسيقات ملفات أخرى مثل EPUB، LaTeX، نص، XPS وغيرها في بيئة Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

{{% alert color="success" %}}
**حاول تحويل PDF إلى EPUB عبر الإنترنت**

تقدم Aspose.PDF لـ Node.js تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF لتحويل PDF إلى EPUB باستخدام تطبيق مجاني](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## تحويل PDF إلى EPUB

**<abbr title="Electronic Publication">EPUB</abbr>** هو معيار كتاب إلكتروني مجاني ومفتوح من المنتدى الدولي للنشر الرقمي (IDPF).
 الملفات لها الامتداد .epub. تم تصميم EPUB للمحتوى القابل لإعادة التدفق، مما يعني أن قارئ EPUB يمكنه تحسين النص لجهاز عرض معين. كما يدعم EPUB المحتوى ذو التخطيط الثابت. يهدف التنسيق ليكون تنسيقًا واحدًا يمكن للناشرين وبيوت التحويل استخدامه داخليًا، وكذلك للتوزيع والبيع. يحل محل معيار الكتاب الإلكتروني المفتوح.

في حالة رغبتك في تحويل مستند PDF، يمكنك استخدام دالة [AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/). يرجى التحقق من الشيفرة التالية لتحويل في بيئة Node.js.

**CommonJS:**

1. استدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
2. حدد اسم ملف PDF الذي سيتم تحويله.
3. استدعاء `AsposePdf` كـ Promise وأداء العملية لتحويل الملف. استلم الكائن إذا نجح.
4. استدعاء الدالة [AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPDFtoEPUB.epub". إذا لم يكن معامل json.errorCode يساوي 0، وظهر خطأ في ملفك، فإن معلومات الخطأ ستكون موجودة في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*تحويل ملف PDF إلى ePub وحفظ "ResultPDFtoEPUB.epub"*/
      const json = AsposePdfModule.AsposePdfToEPUB(pdf_file, "ResultPDFtoEPUB.epub");
      console.log("AsposePdfToEPUB => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
2. تحديد اسم ملف PDF الذي سيتم تحويله.
3. تهيئة وحدة AsposePdf. استلم الكائن إذا كان ناجحًا.
4. استدعاء الدالة [AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/).

1. تحويل ملف PDF. لذلك، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPDFtoEPUB.epub". إذا كانت قيمة معامل json.errorCode ليست 0 وبالتالي ظهرت خطأ في ملفك، فإن معلومات الخطأ ستكون موجودة في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*تحويل ملف PDF إلى ePub وحفظ "ResultPDFtoEPUB.epub"*/
  const json = AsposePdfModule.AsposePdfToEPUB(pdf_file, "ResultPDFtoEPUB.epub");
  console.log("AsposePdfToEPUB => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى LaTeX/TeX عبر الإنترنت**

يقدم لك Aspose.PDF لـ Node.js تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)، حيث يمكنك تجربة استكشاف الوظائف والجودة التي يعمل بها.


[![Aspose.PDF تحويل PDF إلى LaTeX/TeX مع التطبيق المجاني](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## تحويل PDF إلى TeX

**Aspose.PDF لـ Node.js** يدعم تحويل PDF إلى TeX. في حال كنت ترغب في تحويل مستند PDF، يمكنك استخدام دالة [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/). يرجى مراجعة مقتطف الكود التالي من أجل التحويل في بيئة Node.js.

**CommonJS:**

1. استدعاء `require` واستيراد الوحدة `asposepdfnodejs` كمتغير `AsposePdf`.
2. حدد اسم ملف PDF الذي سيتم تحويله.
3. استدعاء `AsposePdf` كـ Promise وتنفيذ العملية لتحويل الملف. استلم الكائن إذا نجحت العملية.
4. استدعاء الدالة [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/).
5. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' هو 0، يتم حفظ نتيجة العملية في "ResultPDFtoTeX.tex". إذا لم يكن معامل json.errorCode هو 0 وظهرت خطأ في ملفك، فستكون معلومات الخطأ موجودة في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*تحويل ملف PDF إلى TeX وحفظ "ResultPDFtoTeX.tex"*/
      const json = AsposePdfModule.AsposePdfToTeX(pdf_file, "ResultPDFtoTeX.tex");
      console.log("AsposePdfToTeX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
1. حدد اسم ملف PDF الذي سيتم تحويله
1. تهيئة وحدة AsposePdf. استلام الكائن في حالة النجاح.
1. استدعاء الدالة [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPDFtoTeX.tex". إذا لم يكن معامل json.errorCode يساوي 0، وظهرت بالتالي خطأ في ملفك، فإن معلومات الخطأ ستكون موجودة في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*تحويل ملف PDF إلى TeX وحفظ "ResultPDFtoTeX.tex"*/
  const json = AsposePdfModule.AsposePdfToTeX(pdf_file, "ResultPDFtoTeX.tex");
  console.log("AsposePdfToTeX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**جرب تحويل PDF إلى نص عبر الإنترنت**


يقدم لك Aspose.PDF for Node.js تطبيقًا مجانيًا عبر الإنترنت ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى نص باستخدام تطبيق مجاني](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## تحويل PDF إلى TXT

في حال كنت ترغب في تحويل مستند PDF، يمكنك استخدام وظيفة [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/). 
يرجى مراجعة المثال التالي من الشيفرة لتحويل في بيئة Node.js.

**CommonJS:**

1. استدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
1. تحديد اسم ملف PDF الذي سيتم تحويله.
1. استدعاء `AsposePdf` كـ Promise وتنفيذ العملية لتحويل الملف. استلام الكائن إذا كان ناجحًا.
1. استدعاء الدالة [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/).

1. تحويل ملف PDF. وبالتالي، إذا كانت 'json.errorCode' تساوي 0، يتم حفظ نتيجة العملية في "ResultPDFtoTxt.txt". إذا كانت قيمة json.errorCode ليست 0 وظهرت بالتالي خطأ في ملفك، فسيتم تضمين معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*تحويل ملف PDF إلى نص وحفظ "ResultPDFtoTxt.txt"*/
      const json = AsposePdfModule.AsposePdfToTxt(pdf_file, "ResultPDFtoTxt.txt");
      console.log("AsposePdfToTxt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
1. تحديد اسم ملف PDF الذي سيتم تحويله
1. تهيئة وحدة AsposePdf. استلم الكائن إذا كانت العملية ناجحة.
1. استدعاء الوظيفة [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/).

1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' هو 0، يتم حفظ نتيجة العملية في "ResultPDFtoTxt.txt". إذا لم يكن معامل json.errorCode يساوي 0 وظهرت بالتالي خطأ في ملفك، ستحتوي 'json.errorText' على معلومات الخطأ.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*تحويل ملف PDF إلى نص وحفظ "ResultPDFtoTxt.txt"*/
  const json = AsposePdfModule.AsposePdfToTxt(pdf_file, "ResultPDFtoTxt.txt");
  console.log("AsposePdfToTxt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى XPS عبر الإنترنت**

يقدم لك Aspose.PDF لـ Node.js تطبيق مجاني عبر الإنترنت ["PDF إلى XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps)، حيث يمكنك تجربة التحقيق في الوظيفة والجودة التي يعمل بها.


[![Aspose.PDF تحويل PDF إلى XPS باستخدام تطبيق مجاني](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## تحويل PDF إلى XPS

نوع ملف XPS مرتبط بشكل رئيسي بمواصفات الورق XML بواسطة شركة مايكروسوفت. مواصفات الورق XML (XPS)، التي كانت تُعرف سابقًا بالاسم الرمزي Metro وتشمل مفهوم التسويق Next Generation Print Path (NGPP)، هي مبادرة من مايكروسوفت لدمج إنشاء وعرض المستندات في نظام تشغيل ويندوز.

**Aspose.PDF لـ Node.js** يوفر إمكانية تحويل ملفات PDF إلى تنسيق <abbr title="XML Paper Specification">XPS</abbr>. دعنا نحاول استخدام مقتطف الكود المقدم لتحويل ملفات PDF إلى تنسيق XPS باستخدام Node.js.

في حال كنت ترغب في تحويل مستند PDF، يمكنك استخدام وظيفة [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/).
يرجى الاطلاع على مقتطف الكود التالي من أجل التحويل في بيئة Node.js.

**CommonJS:**

1. قم باستدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
2. حدد اسم ملف PDF الذي سيتم تحويله.

1. استدعاء `AsposePdf` كـ Promise وأداء العملية لتحويل الملف. استلم الكائن إذا نجحت العملية.
1. استدعاء الدالة [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، فإن نتيجة العملية تُحفظ في "ResultPDFtoXps.xps". إذا لم يكن معامل json.errorCode يساوي 0، وبالتالي ظهرت خطأ في ملفك، سيتم احتواء معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*تحويل ملف PDF إلى Xps وحفظ "ResultPDFtoXps.xps"*/
      const json = AsposePdfModule.AsposePdfToXps(pdf_file, "ResultPDFtoXps.xps");
      console.log("AsposePdfToXps => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد الوحدة `asposepdfnodejs`.
1. تحديد اسم ملف PDF الذي سيتم تحويله.

1. قم بتهيئة وحدة AsposePdf. استلم الكائن إذا تم بنجاح.
1. استدعِ الدالة [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/).
1. حوّل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، سيتم حفظ نتيجة العملية في "ResultPDFtoXps.xps". إذا لم تكن قيمة json.errorCode تساوي 0 وبالتالي ظهرت خطأ في ملفك، ستحتوي معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*حوّل ملف PDF إلى Xps واحفظ "ResultPDFtoXps.xps"*/
  const json = AsposePdfModule.AsposePdfToXps(pdf_file, "ResultPDFtoXps.xps");
  console.log("AsposePdfToXps => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

## تحويل PDF إلى PDF بتدرج الرمادي

حوّل ملف PDF إلى أبيض وأسود باستخدام Aspose.PDF لـ Node.js عبر مجموعة أدوات C++.  
لماذا يجب أن أحول PDF إلى تدرج الرمادي؟
 إذا كان ملف PDF يحتوي على العديد من الصور الملونة وحجم الملف مهم بدلاً من اللون، فإن التحويل يوفر المساحة. إذا قمت بطباعة ملف PDF بالأبيض والأسود، فإن تحويله سيمكنك من التحقق بصريًا مما يبدو عليه الناتج النهائي.

في حال كنت ترغب في تحويل مستند PDF، يمكنك استخدام [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/) الدالة.
يرجى التحقق من الكود التالي لتحويل في بيئة Node.js.

**CommonJS:**

1. استدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
2. تحديد اسم ملف PDF الذي سيتم تحويله.
3. استدعاء `AsposePdf` كـ Promise وتنفيذ العملية لتحويل الملف. استلام الكائن إذا نجحت العملية.
4. استدعاء الدالة [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultConvertToGrayscale.pdf". إذا كان معامل json.errorCode لا يساوي 0، وظهرت خطأ في ملفك، ستكون معلومات الخطأ موجودة في 'json.errorText'.

```js

const AsposePdf = require('asposepdfnodejs');
const pdf_file = 'Aspose.pdf';
AsposePdf().then(AsposePdfModule => {
    /*تحويل ملف PDF إلى تدرج الرمادي وحفظه في "ResultConvertToGrayscale.pdf"*/
    const json = AsposePdfModule.AsposePdfConvertToGrayscale(pdf_file, "ResultConvertToGrayscale.pdf");
    console.log("AsposePdfConvertToGrayscale => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
});
```

**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
1. تحديد اسم ملف PDF الذي سيتم تحويله.
1. تهيئة وحدة AsposePdf. استلام الكائن إذا كان ناجحًا.

1. استدعاء الدالة [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultConvertToGrayscale.pdf". إذا كانت قيمة json.errorCode ليست 0 وظهرت بالتالي خطأ في ملفك، سيتم تضمين معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*تحويل ملف PDF إلى تدرج الرمادي وحفظه كـ "ResultConvertToGrayscale.pdf"*/
  const json = AsposePdfModule.AsposePdfConvertToGrayscale(pdf_file, "ResultConvertToGrayscale.pdf");
  console.log("AsposePdfConvertToGrayscale => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```