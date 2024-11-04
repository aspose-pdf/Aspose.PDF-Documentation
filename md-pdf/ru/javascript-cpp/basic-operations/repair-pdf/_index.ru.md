---
title: Восстановление PDF с помощью JavaScript через C++ 
linktitle: Восстановление PDF
type: docs
weight: 10
url: /javascript-cpp/repair-pdf/
description: Эта тема описывает, как восстановить PDF через JavaScript через C++
lastmod: "2023-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF для JavaScript позволяет выполнять высококачественное восстановление PDF. PDF файл может не открываться по любой причине, независимо от программы или браузера. В некоторых случаях документ можно восстановить, попробуйте следующий код и убедитесь сами.

1. Создайте 'FileReader'.
1. Выполняется функция [AsposePdfRepair](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfrepair/).
1. Устанавливается имя результирующего файла, в этом примере "ResultPdfRepair.pdf".
1. Далее, если 'json.errorCode' равен 0, то вы можете получить ссылки на результирующие файлы. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация о такой ошибке будет содержаться в файле 'json.errorText'.

1. В результате функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) генерирует ссылку и позволяет скачать полученный файл в операционную систему пользователя.

```js

    var ffilePdfRepair = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Восстановить PDF-файл и сохранить как "ResultPdfRepair.pdf"*/
        const json = AsposePdfRepair(event.target.result, e.target.files[0].name, "ResultPdfRepair.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Создать ссылку для скачивания полученного файла*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

## Использование Web Workers

```js

    /*Создать Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Ошибка от Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'загружено!' :
        (evt.data.json.errorCode == 0) ? `Результат:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `Ошибка: ${evt.data.json.errorText}`;

    /*Обработчик события*/
    const ffilePdfRepair = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Восстановить PDF-файл и сохранить как "ResultPdfRepair.pdf" - Запрос к Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfRepair', "params": [event.target.result, e.target.files[0].name, "ResultPdfRepair.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Фрагмент кода]

    /*Создать ссылку для скачивания полученного файла*/
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