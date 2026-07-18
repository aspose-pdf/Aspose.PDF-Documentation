---
title: Конвертировать PDF в EPUB, TeX, Text, XPS в Node.js
linktitle: Конвертировать PDF в другие форматы
type: docs
weight: 90
url: /ru/nodejs-cpp/convert-pdf-to-other-files/
lastmod: "2026-07-18"
description: Эта тема показывает, как преобразовать файл PDF в другие форматы, такие как EPUB, LaTeX, Text, XPS и т.д., в среде Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в EPUB онлайн**

Aspose.PDF for Node.js представляет вам онлайн бесплатное приложение ["PDF в EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в EPUB с бесплатным приложением](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## Конвертировать PDF в EPUB

**<abbr title="Electronic Publication">EPUB</abbr>** — свободный и открытый стандарт электронных книг от International Digital Publishing Forum (IDPF). Файлы имеют расширение .epub.
EPUB разработан для текучего контента, что означает, что EPUB‑читатель может оптимизировать текст под конкретное устройство отображения. EPUB также поддерживает контент фиксированного макета. Формат предназначен как единый формат, который издатели и конверсионные компании могут использовать внутри компании, а также для распространения и продажи. Он заменяет стандарт Open eBook.

Если вы хотите конвертировать PDF-документ, вы можете использовать [AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/) функция. 
Пожалуйста, проверьте следующий фрагмент кода, чтобы выполнить конвертацию в среде Node.js.

**CommonJS:**

1. Вызов `require` и импортировать `asposepdfnodejs` модуль как `AsposePdf` переменная.
1. Укажите имя PDF‑файла, который будет конвертирован.
1. Вызов `AsposePdf` в виде Promise и выполнить операцию по конвертации файла. Получить объект при успешном выполнении.
1. Вызовите функцию [AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/).
1. Конвертировать PDF‑файл. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в \"ResultPDFtoEPUB.epub\". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

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

1. Импортировать `asposepdfnodejs` модуль.
1. Укажите имя PDF‑файла, который будет преобразован
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/).
1. Конвертировать PDF‑файл. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в \"ResultPDFtoEPUB.epub\". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to ePub and save the "ResultPDFtoEPUB.epub"*/
  const json = AsposePdfModule.AsposePdfToEPUB(pdf_file, "ResultPDFtoEPUB.epub");
  console.log("AsposePdfToEPUB => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в LaTeX/TeX онлайн**

Aspose.PDF for Node.js представляет вам онлайн бесплатное приложение ["PDF в LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Преобразование PDF в LaTeX/TeX с бесплатным приложением](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Преобразовать PDF в TeX

**Aspose.PDF for Node.js** поддерживает конвертацию PDF в TeX.
Если вы хотите конвертировать PDF-документ, вы можете использовать [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/) функция. 
Пожалуйста, проверьте следующий фрагмент кода, чтобы выполнить конвертацию в среде Node.js.

**CommonJS:**

1. Вызов `require` и импортировать `asposepdfnodejs` модуль как `AsposePdf` переменная.
1. Укажите имя PDF‑файла, который будет конвертирован.
1. Вызов `AsposePdf` в виде Promise и выполнить операцию по конвертации файла. Получить объект при успешном выполнении.
1. Вызовите функцию [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/).
1. Конвертировать PDF‑файл. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultPDFtoTeX.tex". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

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

1. Импортировать `asposepdfnodejs` модуль.
1. Укажите имя PDF‑файла, который будет преобразован
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/).
1. Конвертировать PDF‑файл. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultPDFtoTeX.tex". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to TeX and save the "ResultPDFtoTeX.tex"*/
  const json = AsposePdfModule.AsposePdfToTeX(pdf_file, "ResultPDFtoTeX.tex");
  console.log("AsposePdfToTeX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в текст онлайн**

Aspose.PDF for Node.js представляет вам онлайн бесплатное приложение ["PDF в текст"](https://products.aspose.app/pdf/conversion/pdf-to-txt), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в Текст с бесплатным приложением](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Конвертировать PDF в TXT

Если вы хотите конвертировать PDF-документ, вы можете использовать [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/) функция. 
Пожалуйста, проверьте следующий фрагмент кода, чтобы выполнить конвертацию в среде Node.js.

**CommonJS:**

1. Вызов `require` и импортировать `asposepdfnodejs` модуль как `AsposePdf` переменная.
1. Укажите имя PDF‑файла, который будет конвертирован.
1. Вызов `AsposePdf` в виде Promise и выполнить операцию по конвертации файла. Получить объект при успешном выполнении.
1. Вызовите функцию [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/).
1. Преобразовать PDF‑файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPDFtoTxt.txt". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

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

1. Импортировать `asposepdfnodejs` модуль.
1. Укажите имя PDF‑файла, который будет преобразован
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/).
1. Преобразовать PDF‑файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPDFtoTxt.txt". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to Txt and save the "ResultPDFtoTxt.txt"*/
  const json = AsposePdfModule.AsposePdfToTxt(pdf_file, "ResultPDFtoTxt.txt");
  console.log("AsposePdfToTxt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в XPS онлайн**

Aspose.PDF for Node.js представляет вам онлайн бесплатное приложение ["PDF в XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в XPS с бесплатным приложением](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## Конвертировать PDF в XPS

Тип файла XPS в первую очередь связан со спецификацией XML Paper Specification компании Microsoft. Спецификация XML Paper Specification (XPS), ранее имевшая кодовое название Metro и включающая в себя маркетинговую концепцию Next Generation Print Path (NGPP), является инициативой Microsoft по интеграции создания и просмотра документов в операционную систему Windows.

**Aspose.PDF for Node.js** предоставляет возможность конвертировать PDF-файлы в <abbr title="XML Paper Specification">XPS</abbr> формат. Давайте попробуем использовать представленный фрагмент кода для преобразования PDF‑файлов в формат XPS с помощью Node.js.

Если вы хотите конвертировать PDF-документ, вы можете использовать [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/) функция. 
Пожалуйста, проверьте следующий фрагмент кода, чтобы выполнить конвертацию в среде Node.js.

**CommonJS:**

1. Вызов `require` и импортировать `asposepdfnodejs` модуль как `AsposePdf` переменная.
1. Укажите имя PDF‑файла, который будет конвертирован.
1. Вызов `AsposePdf` в виде Promise и выполнить операцию по конвертации файла. Получить объект при успешном выполнении.
1. Вызовите функцию [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/).
1. Преобразовать PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPDFtoXps.xps". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

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

1. Импортировать `asposepdfnodejs` модуль.
1. Укажите имя PDF‑файла, который будет конвертирован.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/).
1. Преобразовать PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPDFtoXps.xps". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to Xps and save the "ResultPDFtoXps.xps"*/
  const json = AsposePdfModule.AsposePdfToXps(pdf_file, "ResultPDFtoXps.xps");
  console.log("AsposePdfToXps => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

## Преобразовать PDF в PDF в градациях серого

Конвертировать PDF в чёрно‑белый с помощью Aspose.PDF for Node.js via C++ toolkit. 
Зачем мне конвертировать PDF в градации серого? Если PDF‑файл содержит много цветных изображений и важен размер файла вместо цвета, конвертация экономит место. Если вы печатаете PDF‑файл чёрно‑белым, преобразование позволит визуально проверить, как будет выглядеть конечный результат. 

Если вы хотите конвертировать PDF-документ, вы можете использовать [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/) функция. 
Пожалуйста, проверьте следующий фрагмент кода, чтобы выполнить конвертацию в среде Node.js.

**CommonJS:**

1. Вызов `require` и импортировать `asposepdfnodejs` модуль как `AsposePdf` переменная.
1. Укажите имя PDF‑файла, который будет конвертирован.
1. Вызов `AsposePdf` в виде Promise и выполнить операцию по конвертации файла. Получить объект при успешном выполнении.
1. Вызовите функцию [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/).
1. Конвертировать PDF‑файл. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultConvertToGrayscale.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

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

1. Импортировать `asposepdfnodejs` модуль.
1. Укажите имя PDF‑файла, который будет конвертирован.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/).
1. Конвертировать PDF‑файл. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultConvertToGrayscale.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to grayscale and save the "ResultConvertToGrayscale.pdf"*/
  const json = AsposePdfModule.AsposePdfConvertToGrayscale(pdf_file, "ResultConvertToGrayscale.pdf");
  console.log("AsposePdfConvertToGrayscale => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```






