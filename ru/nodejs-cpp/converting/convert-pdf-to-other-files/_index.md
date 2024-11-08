---
title: Конвертировать PDF в EPUB, TeX, текст, XPS в Node.js
linktitle: Конвертировать PDF в другие форматы 
type: docs
weight: 90
url: /ru/nodejs-cpp/convert-pdf-to-other-files/
lastmod: "2023-11-16"
keywords: конвертировать, PDF, EPUB, TeX, текст, XPS, Node.js
description: Эта тема показывает, как конвертировать PDF файл в другие форматы файлов, такие как EPUB, LaTeX, текст, XPS и т.д. в среде Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в EPUB онлайн**

Aspose.PDF для Node.js представляет вам бесплатное онлайн-приложение ["PDF в EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), где вы можете попробовать исследовать функциональность и качество работы.

[![Aspose.PDF Конвертация PDF в EPUB с помощью бесплатного приложения](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## Конвертировать PDF в EPUB

**<abbr title="Электронная публикация">EPUB</abbr>** — это бесплатный и открытый стандарт для электронных книг от Международного форума цифровых публикаций (IDPF).
 Файлы имеют расширение .epub.  
EPUB разработан для содержания с возможностью переформатирования, что означает, что EPUB-ридер может оптимизировать текст для конкретного устройства отображения. EPUB также поддерживает содержание с фиксированной компоновкой. Формат предназначен как единый формат, который издатели и конверсионные компании могут использовать внутри компании, а также для распространения и продажи. Он заменяет стандарт Open eBook.

Если вы хотите конвертировать PDF-документ, вы можете использовать функцию [AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/).  
Пожалуйста, ознакомьтесь со следующим фрагментом кода для конвертации в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF-файла, который будет конвертирован.
1. Вызовите `AsposePdf` как Promise и выполните операцию по конвертации файла. Получите объект в случае успеха.
1. Вызовите функцию [AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/).
1. Конвертировать PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPDFtoEPUB.epub". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Преобразовать PDF файл в ePub и сохранить в "ResultPDFtoEPUB.epub"*/
      const json = AsposePdfModule.AsposePdfToEPUB(pdf_file, "ResultPDFtoEPUB.epub");
      console.log("AsposePdfToEPUB => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортировать модуль `asposepdfnodejs`.
1. Указать имя PDF файла, который будет конвертирован.
1. Инициализировать модуль AsposePdf. Получить объект в случае успеха.
1. Вызвать функцию [AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/).

1. Конвертировать PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPDFtoEPUB.epub". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Преобразовать PDF-файл в ePub и сохранить как "ResultPDFtoEPUB.epub"*/
  const json = AsposePdfModule.AsposePdfToEPUB(pdf_file, "ResultPDFtoEPUB.epub");
  console.log("AsposePdfToEPUB => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в LaTeX/TeX онлайн**

Aspose.PDF для Node.js предлагает вам бесплатное онлайн-приложение ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), где вы можете попробовать изучить функциональность и качество его работы.


[![Aspose.PDF Конвертация PDF в LaTeX/TeX с бесплатным приложением](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Преобразование PDF в TeX

**Aspose.PDF для Node.js** поддерживает преобразование PDF в TeX.
Если вы хотите преобразовать PDF документ, вы можете использовать функцию [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/). 
Пожалуйста, ознакомьтесь с приведенным ниже кодом, чтобы выполнить преобразование в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF файла, который будет преобразован.
1. Вызовите `AsposePdf` как Promise и выполните операцию по преобразованию файла. Получите объект в случае успеха.
1. Вызовите функцию [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/).
1. Преобразуйте PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPDFtoTeX.tex". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Преобразование PDF-файла в TeX и сохранение "ResultPDFtoTeX.tex"*/
      const json = AsposePdfModule.AsposePdfToTeX(pdf_file, "ResultPDFtoTeX.tex");
      console.log("AsposePdfToTeX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF-файла, который будет преобразован.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/).
1. Преобразуйте PDF-файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPDFtoTeX.tex". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Преобразуйте PDF-файл в TeX и сохраните как "ResultPDFtoTeX.tex"*/
  const json = AsposePdfModule.AsposePdfToTeX(pdf_file, "ResultPDFtoTeX.tex");
  console.log("AsposePdfToTeX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в текст онлайн**


Aspose.PDF для Node.js предлагает вам бесплатное онлайн-приложение ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Преобразование PDF в текст с бесплатным приложением](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Преобразование PDF в TXT

Если вы хотите преобразовать PDF документ, вы можете использовать функцию [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/). 
Пожалуйста, ознакомьтесь с следующим фрагментом кода, чтобы выполнить преобразование в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF файла, который будет преобразован.
1. Вызовите `AsposePdf` как Promise и выполните операцию по преобразованию файла. Получите объект при успешном выполнении.
1. Вызовите функцию [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/).

1. Преобразовать PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPDFtoTxt.txt". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Преобразовать PDF-файл в Txt и сохранить в "ResultPDFtoTxt.txt"*/
      const json = AsposePdfModule.AsposePdfToTxt(pdf_file, "ResultPDFtoTxt.txt");
      console.log("AsposePdfToTxt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF файла, который будет преобразован.
1. Инициализируйте модуль AsposePdf. Получите объект в случае успеха.
1. Вызовите функцию [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/).

1. Конвертировать PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPDFtoTxt.txt". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле возникает ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Конвертировать PDF-файл в Txt и сохранить в "ResultPDFtoTxt.txt"*/
  const json = AsposePdfModule.AsposePdfToTxt(pdf_file, "ResultPDFtoTxt.txt");
  console.log("AsposePdfToTxt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в XPS онлайн**

Aspose.PDF для Node.js представляет вашему вниманию бесплатное онлайн-приложение ["PDF в XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), где вы можете попробовать изучить функциональность и качество его работы.


[![Конвертация Aspose.PDF из PDF в XPS с бесплатным приложением](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## Конвертация PDF в XPS

Тип файла XPS в первую очередь ассоциируется с XML Paper Specification от Microsoft Corporation. XML Paper Specification (XPS), ранее имевший кодовое имя Metro и включающий в себя маркетинговую концепцию Next Generation Print Path (NGPP), является инициативой Microsoft по интеграции создания и просмотра документов в операционную систему Windows.

**Aspose.PDF для Node.js** предоставляет возможность конвертировать PDF файлы в формат <abbr title="XML Paper Specification">XPS</abbr>. Попробуем использовать представленный фрагмент кода для конвертации PDF файлов в формат XPS с помощью Node.js.

Если вы хотите конвертировать PDF документ, вы можете использовать функцию [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/). Пожалуйста, ознакомьтесь со следующим фрагментом кода для конвертации в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF файла, который будет конвертирован.

1. Вызовите `AsposePdf` как Promise и выполните операцию для преобразования файла. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/).
1. Преобразуйте PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPDFtoXps.xps". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Преобразовать PDF-файл в Xps и сохранить как "ResultPDFtoXps.xps"*/
      const json = AsposePdfModule.AsposePdfToXps(pdf_file, "ResultPDFtoXps.xps");
      console.log("AsposePdfToXps => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF файла, который будет преобразован.

1. Инициализируйте модуль AsposePdf. Получите объект в случае успеха.
1. Вызовите функцию [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/).
1. Конвертируйте PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPDFtoXps.xps". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Преобразуйте PDF-файл в Xps и сохраните как "ResultPDFtoXps.xps"*/
  const json = AsposePdfModule.AsposePdfToXps(pdf_file, "ResultPDFtoXps.xps");
  console.log("AsposePdfToXps => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

## Конвертация PDF в градации серого

Конвертируйте PDF в черно-белый с помощью Aspose.PDF для Node.js через C++ toolkit. Почему я должен конвертировать PDF в градации серого?
 Если PDF файл содержит много цветных изображений и размер файла важнее, чем цвет, преобразование экономит место. Если вы печатаете PDF файл в черно-белом варианте, преобразование позволит вам визуально проверить, как выглядит конечный результат.

Если вы хотите конвертировать PDF документ, вы можете использовать функцию [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/). Пожалуйста, ознакомьтесь с приведенным ниже фрагментом кода для конвертации в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
2. Укажите имя PDF файла, который будет конвертирован.
3. Вызовите `AsposePdf` как Promise и выполните операцию для преобразования файла. Получите объект в случае успеха.
4. Вызовите функцию [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/).
1. Конвертировать PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultConvertToGrayscale.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

const AsposePdf = require('asposepdfnodejs');
const pdf_file = 'Aspose.pdf';
AsposePdf().then(AsposePdfModule => {
    /*Преобразовать PDF-файл в градации серого и сохранить как "ResultConvertToGrayscale.pdf"*/
    const json = AsposePdfModule.AsposePdfConvertToGrayscale(pdf_file, "ResultConvertToGrayscale.pdf");
    console.log("AsposePdfConvertToGrayscale => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
});
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF-файла, который будет конвертирован.
1. Инициализируйте модуль AsposePdf. Получите объект в случае успеха.

1. Вызовите функцию [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/).
1. Конвертируйте PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultConvertToGrayscale.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Преобразование PDF-файла в градации серого и сохранение в "ResultConvertToGrayscale.pdf"*/
  const json = AsposePdfModule.AsposePdfConvertToGrayscale(pdf_file, "ResultConvertToGrayscale.pdf");
  console.log("AsposePdfConvertToGrayscale => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```