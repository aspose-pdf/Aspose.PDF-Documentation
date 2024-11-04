---
title: Расшифровать PDF с использованием JavaScript
linktitle: Расшифровать PDF файл
type: docs
weight: 40
url: /javascript-cpp/decrypt-pdf/
description: Расшифровать PDF файл с помощью Aspose.PDF для JavaScript через C++.
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Расшифровать PDF файл с использованием пароля владельца

В последнее время все больше пользователей обмениваются зашифрованными документами, чтобы не стать жертвами интернет-мошенничества и защитить свои документы.
В связи с этим возникает необходимость доступа к зашифрованному PDF файлу, так как такой доступ может быть получен только авторизованным пользователем. Также люди ищут различные решения для расшифровки PDF файлов.

Лучше решить эту проблему один раз, используя Aspose.PDF для JavaScript через C++ напрямую в вашем веб-браузере. Следующий фрагмент кода показывает, как расшифровать PDF файлы.

1. Выберите PDF файл для расшифровки.
1. Создайте 'FileReader'.
1. Функция [AsposePdfDecrypt](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfdecrypt/) выполняется.

1. Имя результирующего файла установлено, в этом примере "ResultDecrypt.pdf".
1. Далее, если 'json.errorCode' равно 0, то вашему DownloadFile присваивается имя, указанное вами ранее. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация о такой ошибке будет содержаться в файле 'json.errorText'.
1. В результате функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) генерирует ссылку и позволяет скачать полученный файл на операционную систему пользователя.

```js
    var ffileDecrypt = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Расшифровать PDF-файл с паролем "owner" и сохранить как "ResultDecrypt.pdf"*/
        const json = AsposePdfDecrypt(event.target.result, e.target.files[0].name, "owner", "ResultDecrypt.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Создать ссылку для скачивания результирующего файла*/
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
        (evt.data.json.errorCode == 0) ?
          `Результат:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Ошибка: ${evt.data.json.errorText}`;

    /*Обработчик события*/
    const ffileDecrypt = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const password = 'owner';
        /*Расшифровать PDF-файл с паролем "owner" и сохранить как "ResultDecrypt.pdf" - Запрос в Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfDecrypt',
            "params": [event.target.result, e.target.files[0].name, password, "ResultDecrypt.pdf"] }, 
          [event.target.result]
        );
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