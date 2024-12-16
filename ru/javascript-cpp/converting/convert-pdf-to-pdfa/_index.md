---
title: Конвертировать PDF в форматы PDF/A 
linktitle: Конвертировать PDF в форматы PDF/A
type: docs
weight: 100
url: /ru/javascript-cpp/convert-pdf-to-pdfa/
lastmod: "2023-11-01"
description: Эта тема показывает, как Aspose.PDF позволяет конвертировать файл PDF в файл PDF, соответствующий стандарту PDF/A. 
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for JavaScript** позволяет конвертировать файл PDF в файл PDF, соответствующий стандарту <abbr title="Portable Document Format / A">PDF/A</abbr>. 

Операция конвертации зависит от количества страниц в документе и может быть очень продолжительной. Поэтому мы настоятельно рекомендуем использовать Web Workers. 

Этот код демонстрирует способ разгрузки ресурсоемких задач по конвертации PDF файлов в web worker, чтобы предотвратить блокировку основного потока пользовательского интерфейса. Он также предлагает удобный способ загрузки конвертированного файла.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в PDF/A онлайн**


Aspose.PDF for JavaScript предлагает вам бесплатное онлайн-приложение ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в PDF/A с бесплатным приложением](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

## Конвертировать PDF в формат PDF/A

```js

  /*Создать Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Ошибка от Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'загружено!' :
        (evt.data.json.errorCode == 0) ? `Результат:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}\n${DownloadFile(evt.data.json.fileNameLogResult, "application/xml", evt.data.params[1])}` : `Ошибка: ${evt.data.json.errorText}`;

    /*Обработчик событий*/
    const ffilePdfConvertToPDFA = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const pdfFormat = 'Module.PdfFormat.PDF_A_1A';
        /*конвертировать PDF-файл в PDF/A(1A) и сохранить "ResultConvertToPDFA.pdf"*/
        /*во время процесса конвертации также проводится проверка, "ResultConvertToPDFA.xml" - спросить Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfConvertToPDFA', "params": [event.target.result, e.target.files[0].name, pdfFormat, "ResultConvertToPDFA.pdf", "ResultConvertToPDFA.xml"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Фрагмент кода]

    /*создать ссылку для скачивания результирующего файла*/
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


The following JavaScript code snippet shows simple example of coverting PDF to PDF/A files:

1. Выберите PDF файл для конвертации.
1. Создайте 'FileReader'.
1. Функция [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfconverttopdfa/) выполняется.
1. Устанавливается имя результирующего файла, в этом примере "ResultConvertToPDFA.pdf". Во время процесса конвертации также выполняется валидация, "ResultConvertToPDFA.xml".
1. Далее, если 'json.errorCode' равен 0, то ваш DownloadFile получает имя, которое вы указали ранее. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация о такой ошибке будет содержаться в файле 'json.errorText'.
1. В результате функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) генерирует ссылку и позволяет загрузить полученный файл, а также ссылку для загрузки файла журнала (xml) в операционную систему пользователя.

```js

  var ffilePdfConvertToPDFA = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*преобразовать PDF-файл в PDF/A(1A) и сохранить как "ResultConvertToPDFA.pdf"*/
      /*во время процесса конвертации также выполняется валидация, "ResultConvertToPDFA.xml"*/
      const json = AsposePdfConvertToPDFA(event.target.result, e.target.files[0].name, Module.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFA.xml");
      if (json.errorCode == 0)
      {
        document.getElementById('output').textContent = json.fileNameResult + "\nФайл журнала (формат xml): " + json.fileNameLogResult;
        /*создать ссылку для загрузки результирующего файла*/
        DownloadFile(json.fileNameResult, "application/pdf");
      }
      else document.getElementById('output').textContent = json.errorText + "\nФайл журнала (формат xml): " + json.fileNameLogResult;
      /*создать ссылку для загрузки журнала (xml)*/
      DownloadFile(json.fileNameLogResult, "application/xml");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```