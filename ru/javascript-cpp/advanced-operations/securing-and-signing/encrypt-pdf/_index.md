---
title:  Шифрование PDF с использованием JavaScript
linktitle: Шифрование PDF файла
type: docs
weight: 50
url: /ru/javascript-cpp/encrypt-pdf/
description: Шифрование PDF файла с помощью Aspose.PDF для JavaScript через C++.
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Шифрование PDF файла с использованием пользовательского или владельческого пароля

Если вы отправляете кому-то по электронной почте PDF-файл, содержащий конфиденциальную информацию, вы можете захотеть добавить к нему защиту, чтобы он не попал в чужие руки. Лучший способ ограничить несанкционированный доступ к PDF-документу — защитить его паролем. Для простого и безопасного шифрования документов вы можете использовать Aspose.PDF для JavaScript через C++.

>Пожалуйста, указывайте разные пользовательский и владельческий пароли при шифровании PDF файла.

- **Пользовательский пароль**, если установлен, необходимо указать для открытия PDF. Acrobat/Reader предложит пользователю ввести пользовательский пароль. Если он не будет правильным, документ не откроется.
- **Владельческий пароль**, если установлен, контролирует разрешения, такие как печать, редактирование, извлечение, комментирование и т.д.
 Acrobat/Reader запретит эти действия в зависимости от настроек разрешений. Acrobat потребует этот пароль, если вы хотите установить/изменить разрешения.

Следующий фрагмент кода показывает, как зашифровать PDF-файлы.

1. Выберите PDF-файл для шифрования.
1. Создайте 'FileReader'.
1. Выполняется функция [AsposePdfEncrypt](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfencrypt/).
1. Устанавливается имя результирующего файла, в этом примере "ResultEncrypt.pdf".
1. Далее, если 'json.errorCode' равен 0, то вашему DownloadFile присваивается имя, указанное вами ранее. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация о такой ошибке будет содержаться в файле 'json.errorText'.
1. В результате функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) генерирует ссылку и позволяет загрузить результирующий файл на операционную систему пользователя.

```js

  var ffileEncrypt = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*зашифровать PDF-файл с паролями "user" и "owner" и сохранить как "ResultDecrypt.pdf"*/
      const json = AsposePdfEncrypt(event.target.result, e.target.files[0].name, "user", "owner", Module.Permissions.PrintDocument, Module.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*создать ссылку для загрузки результирующего файла*/
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
    const ffileEncrypt = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const password_user = 'user';
        const password_owner = 'owner';
        const permissions = 'Module.Permissions.PrintDocument';
        const algorithm = 'Module.CryptoAlgorithm.RC4x40';
        /*Зашифровать PDF-файл с паролями "user" и "owner", и сохранить "ResultEncrypt.pdf" - запросить Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfEncrypt',
            "params": [event.target.result, e.target.files[0].name, password_user, password_owner,
                      permissions, algorithm, "ResultEncrypt.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Создать ссылку для скачивания файла результата*/
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