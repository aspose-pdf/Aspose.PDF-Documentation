---
title: Конвертация PDF в Excel на JavaScript
linktitle: Конвертация PDF в Excel
type: docs
weight: 20
url: /javascript-cpp/convert-pdf-to-xlsx/
lastmod: "2023-11-01"
keywords: конвертация PDF в Excel с использованием javascript, конвертация PDF в XLSX, конвертация PDF в CSV.
description: Aspose.PDF для JavaScript позволяет конвертировать PDF в XLSX и форматы CSV.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Создание электронных таблиц из PDF с использованием JavaScript

**Aspose.PDF для JavaScript** поддерживает функцию конвертации PDF-файлов в форматы Excel и CSV.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в Excel онлайн**

Aspose.PDF для JavaScript предлагает вам бесплатное онлайн-приложение ["PDF в XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), где вы можете попробовать исследовать функционал и качество его работы.

[![Aspose.PDF Конвертация PDF в Excel с бесплатным приложением](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

Процесс конвертации зависит от количества страниц в документе и может быть очень трудоемким.
 Поэтому мы настоятельно рекомендуем использовать Web Workers.

Этот код демонстрирует способ переноса ресурсоемких задач по конвертации PDF-файлов в веб-воркер, чтобы предотвратить блокировку основного потока пользовательского интерфейса. Он также предлагает удобный способ загрузки преобразованного файла.

## Конвертация PDF в XLSX

```js

  /*Создать Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Ошибка от Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'загружено!' :
        (evt.data.json.errorCode == 0) ? `Результат:\n${DownloadFile(evt.data.json.fileNameResult, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", evt.data.params[0])}` : `Ошибка: ${evt.data.json.errorText}`;

    /*Обработчик события*/
    const ffileToXlsX = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*конвертировать PDF-файл в XlsX и сохранить как "ResultPDFtoXlsX.xlsx" - спросить у Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToXlsX', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoXlsX.xlsx"] }, [event.target.result]);
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

Следующий пример кода на JavaScript демонстрирует простой пример преобразования страниц PDF в файлы XlsX:

1. Выберите PDF файл для конвертации.
1. Создайте 'FileReader'.
1. Выполняется функция [AsposePdfToXlsX](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdftoxlsx/).
1. Устанавливается имя результирующего файла, в этом примере "ResultPDFtoXlsX.xlsx".
1. Далее, если 'json.errorCode' равно 0, то вашему результирующему файлу присваивается имя, которое вы указали ранее. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация о такой ошибке будет содержаться в файле 'json.errorText'.
1. В результате функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) генерирует ссылку и позволяет загрузить результирующий файл на операционную систему пользователя.

```js

  var ffileToXlsX = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*преобразовать PDF-файл в XlsX и сохранить как "ResultPDFtoXlsX.xlsx"*/
      const json = AsposePdfToXlsX(event.target.result, e.target.files[0].name, "ResultPDFtoXlsX.xlsx");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*создать ссылку для скачивания результирующего файла*/
      DownloadFile(json.fileNameResult, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```


## Преобразование PDF в CSV

```js

    /*Создать Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Ошибка от Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'загружено!' :
        (evt.data.json.errorCode == 0) ? 
          `Количество файлов (таблиц): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "text/csv", element) ) ?? ""}` : 
          `Ошибка: ${evt.data.json.errorText}`;

    /*Обработчик события*/
    const ffileToCSV = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Преобразовать PDF-файл в CSV (извлечь таблицы) с шаблоном "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... формат номера страницы), TAB в качестве разделителя и сохранить - Запрос к Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfTablesToCSV', "params": [event.target.result, e.target.files[0].name, "ResultPdfTablesToCSV{0:D2}.csv", "\t"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Создать ссылку для скачивания результирующего файла*/
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


Следующий фрагмент кода JavaScript показывает простой пример преобразования PDF в CSV:

1. Выберите PDF файл для конвертации.
1. Создайте 'FileReader'.
1. Выполняется функция [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftablestocsv/).
1. Устанавливается имя результирующего файла, в этом примере "ResultPdfTablesToCSV{0:D2}.csv".
1. Далее, если 'json.errorCode' равен 0, то вашему результирующему файлу присваивается ранее указанное имя. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация о такой ошибке будет содержаться в файле 'json.errorText'.
1. В результате функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) генерирует ссылку и позволяет загрузить результирующий файл в операционную систему пользователя.

```js

  var ffileToCSV = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Преобразовать PDF-файл в CSV (извлечь таблицы) с шаблоном "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... формат номера страницы), TAB в качестве разделителя*/
        const json = AsposePdfTablesToCSV(event.target.result, e.target.files[0].name, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
        if (json.errorCode == 0) {
          document.getElementById('output').textContent = "Количество файлов (таблиц): " + json.filesCount.toString();
          /*Создать ссылки на результирующие файлы*/
          for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "text/csv");
        }
        else document.getElementById('output').textContent = json.errorText;
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```