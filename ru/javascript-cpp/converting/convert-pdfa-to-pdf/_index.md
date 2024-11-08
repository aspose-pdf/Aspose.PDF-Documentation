---
title: Конвертировать PDF/A в формат PDF
linktitle: Конвертировать PDF/A в формат PDF
type: docs
weight: 110
url: /ru/javascript-cpp/convert-pdfa-to-pdf/
lastmod: "2023-11-01"
description: Эта тема показывает, как Aspose.PDF позволяет конвертировать файл PDF/A в PDF-документ с помощью JavaScript.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Конвертировать PDF/A в формат PDF

```js

  /*Создать Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Ошибка от Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'загружено!' :
        (evt.data.json.errorCode == 0) ? `Результат:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `Ошибка: ${evt.data.json.errorText}`;

    /*Обработчик события*/
    const ffilePdfAConvertToPDF = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*конвертировать файл PDF/A в PDF и сохранить как "ResultConvertToPDF.pdf" - Запросить у Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfAConvertToPDF', "params": [event.target.result, e.target.files[0].name, "ResultConvertToPDF.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Сниппет кода]

    /*создать ссылку для загрузки файла результата*/
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


Следующий фрагмент кода JavaScript показывает простой пример конвертации PDF/A в PDF:

1. Выберите PDF файл для конвертации.
1. Создайте 'FileReader'.
1. Выполняется функция [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaconverttopdf/).
1. Устанавливается имя результирующего файла, в этом примере "ResultConvertToPDFA.pdf".
1. Далее, если 'json.errorCode' равен 0, то вашему DownloadFile будет присвоено имя, указанное вами ранее. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация об этой ошибке будет содержаться в файле 'json.errorText'.
1. В результате функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) генерирует ссылку и позволяет скачать полученный файл на операционную систему пользователя.

```js

    var ffilePdfAConvertToPDF = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*конвертировать файл PDF/A в PDF и сохранить как "ResultConvertToPDF.pdf"*/
        const json = AsposePdfAConvertToPDF(event.target.result, e.target.files[0].name, "ResultConvertToPDF.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*создать ссылку для скачивания результирующего файла*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

```