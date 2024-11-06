---
title: Извлечение изображений из PDF на JavaScript
linktitle: Извлечение изображений из PDF
type: docs
weight: 20
url: ru/javascript-cpp/extract-images-from-the-pdf-file/
description: Как извлечь часть изображения из PDF с использованием инструментария Aspose.PDF для JavaScript.
lastmod: "2023-09-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Веб-инструментарий от Aspose.PDF позволяет легко извлекать изображения из PDF-файлов.

Если вы хотите извлечь изображения из PDF-документа, вы можете использовать функцию [AsposePdfExtractImage](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextractimage/). Пожалуйста, ознакомьтесь с следующим примером кода, чтобы извлечь изображения из PDF-файла с использованием JavaScript через C++.

1. Создайте 'FileReader'.
1. Выполняется функция [AsposePdfExtractImage](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextractimage/).
1. Устанавливается имя результирующего файла, в этом примере "ResultPdfExtractImage{0:D2}.jpg".

1. Далее, если 'json.errorCode' равен 0, то вы можете получить ссылки на файлы с результатами. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация о такой ошибке будет содержаться в файле 'json.errorText'.
1. В результате функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) генерирует ссылку и позволяет скачать полученный файл в операционную систему пользователя.

```js

    var ffileExtractImage = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
    /*Извлечение изображения из PDF-файла с шаблоном "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... формат номера страницы), разрешение 150 DPI и сохранение*/
    const json = AsposePdfExtractImage(event.target.result, e.target.files[0].name, "ResultPdfExtractImage{0:D2}.jpg", 150);
    if (json.errorCode == 0) {
        document.getElementById('output').textContent = "Количество файлов(изображений): " + json.filesCount.toString();
        /*Создать ссылки на файлы с результатами*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/jpeg");
    }
    else document.getElementById('output').textContent = json.errorText;
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


## Использование Web Workers

```js

  /*Создать Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Ошибка от Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'загружено!' :
        (evt.data.json.errorCode == 0) ? 
          `Количество файлов(изображений): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/jpeg", element) ) ?? ""}` : 
          `Ошибка: ${evt.data.json.errorText}`;

    /*Обработчик событий*/
    const ffileExtractImage = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Извлечь изображение из PDF-файла с шаблоном "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... формат номера страницы), разрешение 150 DPI и сохранить*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfExtractImage', "params": [event.target.result, e.target.files[0].name, "ResultPdfExtractImage{0:D2}.jpg", 150] }, [event.target.result]);
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