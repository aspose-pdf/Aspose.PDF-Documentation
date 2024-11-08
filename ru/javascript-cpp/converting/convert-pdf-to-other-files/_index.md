---
title: Конвертировать PDF в EPUB, TeX, Text, XPS на JavaScript
linktitle: Конвертировать PDF в другие форматы
type: docs
weight: 90
url: /ru/javascript-cpp/convert-pdf-to-other-files/
lastmod: "2023-11-01"
keywords: конвертировать, PDF, EPUB, TeX, Text, XPS, JavaScript
description: Эта тема показывает, как конвертировать PDF файл в другие форматы файлов, такие как EPUB, LaTeX, Text, XPS и т.д., используя JavaScript или JavaScript.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

Операция конвертации зависит от количества страниц в документе и может занять очень много времени. Поэтому мы настоятельно рекомендуем использовать Web Workers.

Этот код демонстрирует способ разгрузить ресурсоемкие задачи по конвертации PDF файлов в веб-воркер, чтобы предотвратить блокировку основного потока пользовательского интерфейса. Он также предлагает удобный способ скачать конвертированный файл.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в EPUB онлайн**

Aspose.PDF для JavaScript предлагает вам бесплатное онлайн-приложение ["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Преобразование PDF в EPUB с бесплатным приложением](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## Конвертировать PDF в EPUB

**<abbr title="Electronic Publication">EPUB</abbr>** — это бесплатный и открытый стандарт для электронных книг от Международного форума цифрового издательства (IDPF). Файлы имеют расширение .epub. EPUB предназначен для переформатируемого контента, что означает, что средство чтения EPUB может оптимизировать текст для конкретного устройства отображения. EPUB также поддерживает контент с фиксированной компоновкой. Формат предназначен как единый формат, который издатели и компании по конверсии могут использовать внутри компании, а также для распространения и продажи. Он заменяет стандарт Open eBook.

```js

    /*Создать Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Ошибка от Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'загружено!' :
        (evt.data.json.errorCode == 0) ? `Результат:\n${DownloadFile(evt.data.json.fileNameResult, "application/epub+zip", evt.data.params[0])}` : `Ошибка: ${evt.data.json.errorText}`;

    /*Обработчик событий*/
    const ffileToEPUB = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Преобразовать PDF-файл в ePub и сохранить как "ResultPDFtoEPUB.epub" - Запросить у Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToEPUB', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoEPUB.epub"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Создать ссылку для загрузки результирующего файла*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "Нажмите здесь, чтобы скачать файл " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


The following JavaScript code snippet shows simple example of coverting PDF pages into EPUB files:

1. Выберите PDF файл для преобразования.
1. Создайте 'FileReader'.
1. Выполняется функция [AsposePdfToEPUB](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftoepub/).
1. Устанавливается имя результирующего файла, в этом примере "ResultPDFtoEPUB.epub".
1. Далее, если 'json.errorCode' равен 0, то вашему результирующему файлу присваивается имя, указанное вами ранее. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация о такой ошибке будет содержаться в файле 'json.errorText'.
1. В результате функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) генерирует ссылку и позволяет скачать полученный файл на операционную систему пользователя.

```js

    var ffileToEPUB = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Преобразовать PDF-файл в EPUB и сохранить как "ResultPDFtoEPUB.epub"*/
        const json = AsposePdfToEPUB(event.target.result, e.target.files[0].name, "ResultPDFtoEPUB.epub");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Создать ссылку для скачивания результирующего файла*/
        DownloadFile(json.fileNameResult, "application/epub+zip");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


{{% alert color="success" %}}
**Попробуйте преобразовать PDF в LaTeX/TeX онлайн**

Aspose.PDF для JavaScript предоставляет вам бесплатное онлайн-приложение ["PDF в LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в LaTeX/TeX с бесплатным приложением](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Преобразование PDF в TeX

**Aspose.PDF для JavaScript** поддерживает преобразование PDF в TeX.
Формат файла LaTeX — это текстовый формат файла с специальной разметкой, используемый в системе подготовки документов на базе TeX для высококачественной верстки.

```js

  /*Создать Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Ошибка от Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'загружено!' :
        (evt.data.json.errorCode == 0) ? `Результат:\n${DownloadFile(evt.data.json.fileNameResult, "application/x-tex", evt.data.params[0])}` : `Ошибка: ${evt.data.json.errorText}`;

    /*Обработчик события*/
    const ffileToTeX = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Преобразовать PDF-файл в TeX и сохранить "ResultPDFtoTeX.tex" - Запросить Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToTeX', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoTeX.tex"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Создать ссылку для загрузки результата*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "Нажмите здесь, чтобы скачать файл " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


Следующий фрагмент кода на JavaScript демонстрирует простой пример преобразования страниц PDF в файлы TEX:

1. Выберите PDF файл для конвертации.
1. Создайте 'FileReader'.
1. Выполняется функция [AsposePdfToTeX](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftotex/).
1. Устанавливается имя результирующего файла, в этом примере "ResultPDFtoTeX.tex".
1. Далее, если 'json.errorCode' равен 0, то ваш результирующий файл получает ранее указанное вами имя. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация об этой ошибке будет содержаться в файле 'json.errorText'.
1. В результате функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) генерирует ссылку и позволяет загрузить результирующий файл на операционную систему пользователя.

```js

    var ffileToTeX = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Конвертировать PDF-файл в TeX и сохранить как "ResultPDFtoTeX.tex"*/
        const json = AsposePdfToTeX(event.target.result, e.target.files[0].name, "ResultPDFtoTeX.tex");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Создать ссылку для загрузки результирующего файла*/
        DownloadFile(json.fileNameResult, "application/x-tex");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


{{% alert color="success" %}}
**Попробуйте конвертировать PDF в текст онлайн**

Aspose.PDF для JavaScript представляет вам бесплатное онлайн-приложение ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в текст с бесплатным приложением](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Конвертация PDF в TXT

```js

    /*Создать Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Ошибка от Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'загружено!' :
        (evt.data.json.errorCode == 0) ? `Результат:\n${DownloadFile(evt.data.json.fileNameResult, "text/plain", evt.data.params[0])}` : `Ошибка: ${evt.data.json.errorText}`;

    /*Обработчик события*/
    const ffileToTxt = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Преобразовать PDF-файл в Txt и сохранить как "ResultPDFtoTxt.txt" - Запрос к Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToTxt', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoTxt.txt"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Создать ссылку для скачивания итогового файла*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "Нажмите здесь, чтобы скачать файл " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


Следующий фрагмент кода JavaScript показывает простой пример преобразования страниц PDF в файлы TXT:

1. Выберите PDF файл для конвертации.
1. Создайте 'FileReader'.
1. Выполняется функция [AsposePdfToTxt](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftotxt/).
1. Устанавливается имя результирующего файла, в этом примере "ResultPDFtoTxt.txt".
1. Далее, если 'json.errorCode' равен 0, ваш результирующий файл получает имя, которое вы указали ранее. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация о такой ошибке будет содержаться в файле 'json.errorText'.
1. В результате функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) генерирует ссылку и позволяет скачать результирующий файл в операционной системе пользователя.

```js

    var ffileToTxt = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Преобразовать PDF-файл в Txt и сохранить как "ResultPDFtoTxt.txt"*/
        const json = AsposePdfToTxt(event.target.result, e.target.files[0].name, "ResultPDFtoTxt.txt");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Создать ссылку для скачивания результирующего файла*/
        DownloadFile(json.fileNameResult, "text/plain");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


{{% alert color="success" %}}
**Попробуйте преобразовать PDF в XPS онлайн**

Aspose.PDF для JavaScript представляет вам бесплатное онлайн-приложение ["PDF в XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в XPS с помощью бесплатного приложения](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## Преобразование PDF в XPS

Тип файла XPS в первую очередь ассоциируется с XML Paper Specification от Microsoft Corporation. XML Paper Specification (XPS), ранее кодовое название Metro и включающий маркетинговую концепцию Next Generation Print Path (NGPP), является инициативой Microsoft по интеграции создания и просмотра документов в операционную систему Windows.

**Aspose.PDF для JavaScript** предоставляет возможность преобразования PDF-файлов в формат <abbr title="XML Paper Specification">XPS</abbr>. Давайте попробуем использовать представленный код для преобразования PDF-файлов в формат XPS с помощью JavaScript.

```js

    /*Создать Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Ошибка от Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'загружено!' :
        (evt.data.json.errorCode == 0) ? `Результат:\n${DownloadFile(evt.data.json.fileNameResult, "application/vnd.ms-xpsdocument", evt.data.params[0])}` : `Ошибка: ${evt.data.json.errorText}`;

    /*Обработчик событий*/
    const ffileToXps = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Преобразовать PDF-файл в Xps и сохранить "ResultPDFtoXps.xps" - запросить Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToXps', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoXps.xps"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Создать ссылку для загрузки файла с результатом*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "Нажмите здесь, чтобы скачать файл " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


The following JavaScript code snippet shows simple example of coverting PDF pages into XPS files:

1. Выберите PDF файл для конвертации.
1. Создайте 'FileReader'.
1. Выполняется функция [AsposePdfToXps](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftoxps/).
1. Устанавливается имя результирующего файла, в этом примере "ResultPDFtoXps.xps".
1. Далее, если 'json.errorCode' равен 0, то вашему результирующему файлу присваивается имя, указанное ранее. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация о такой ошибке будет содержаться в файле 'json.errorText'.
1. В результате функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) генерирует ссылку и позволяет загрузить результирующий файл в операционную систему пользователя.

```js

    var ffileToXps = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Конвертируйте PDF-файл в Xps и сохраните как "ResultPDFtoXps.xps"*/
        const json = AsposePdfToXps(event.target.result, e.target.files[0].name, "ResultPDFtoXps.xps");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Создайте ссылку для загрузки результирующего файла*/
        DownloadFile(json.fileNameResult, "application/vnd.ms-xpsdocument");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


## Преобразование PDF в черно-белый PDF

Преобразование PDF в черно-белый с использованием Aspose.PDF для JavaScript через C++ Web toolkit.  
Зачем мне преобразовывать PDF в оттенки серого? Если PDF-файл содержит много цветных изображений, и размер файла важен больше, чем цвет, преобразование позволяет сэкономить место. Если вы печатаете PDF-файл в черно-белом цвете, преобразование позволит вам визуально проверить, как будет выглядеть конечный результат. 

```js

  /*Создать Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Ошибка от Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'загружено!' :
        (evt.data.json.errorCode == 0) ? `Результат:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `Ошибка: ${evt.data.json.errorText}`;

    /*Обработчик событий*/
    const ffileConvertToGrayscale = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*преобразовать PDF-файл в оттенки серого и сохранить "ResultConvertToGrayscale.pdf" - Запросить Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfConvertToGrayscale', "params": [event.target.result, e.target.files[0].name, "ResultConvertToGrayscale.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Фрагмент кода]

    /*создать ссылку для загрузки результирующего файла*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "Нажмите здесь, чтобы скачать файл " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


The following JavaScript code snippet shows simple example of coverting PDF pages into Grayscale PDF:

Следующий фрагмент кода на JavaScript показывает простой пример преобразования страниц PDF в оттенки серого PDF:

1. Select a PDF file for converting.
1. Выберите PDF-файл для преобразования.
2. Create a 'FileReader'.
2. Создайте 'FileReader'.
3. The [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfconverttograyscale/) function is executed.
3. Выполняется функция [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfconverttograyscale/).
4. The name of the resulting file is set, in this example "ResultConvertToGrayscale.pdf".
4. Устанавливается имя результирующего файла, в этом примере "ResultConvertToGrayscale.pdf".
5. Next, if the 'json.errorCode' is 0, then your DownloadFile is given the name you specified earlier. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.
5. Далее, если 'json.errorCode' равен 0, то вашему DownloadFile присваивается ранее указанное имя. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация об этой ошибке будет содержаться в файле 'json.errorText'.
6. As a result, the [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) function generates a link and allows you to download the resulting file to the user's operating system.
6. В результате функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) генерирует ссылку и позволяет скачать результирующий файл на операционную систему пользователя.

```js

  var ffileConvertToGrayscale = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*convert a PDF-file to grayscale and save the "ResultConvertToGrayscale.pdf"*/
      /*преобразовать PDF-файл в оттенки серого и сохранить как "ResultConvertToGrayscale.pdf"*/
      const json = AsposePdfConvertToGrayscale(event.target.result, e.target.files[0].name, "ResultConvertToGrayscale.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*make a link to download the result file*/
      /*создать ссылку для скачивания результирующего файла*/
      DownloadFile(json.fileNameResult, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

```