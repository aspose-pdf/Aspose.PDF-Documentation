---
title: Alterar Senha de um Arquivo PDF
linktitle: Alterar Senha
type: docs
weight: 50
url: /javascript-cpp/change-password-pdf/
description: Alterar Senha de um Arquivo PDF com Aspose.PDF para JavaScript via C++.
lastmod: "2023-09-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Alterar Senha de um Arquivo PDF

Se você deseja alterar a senha de um arquivo PDF de "owner" para "newowner", tente o seguinte trecho de código:

1. Selecione um arquivo PDF.
1. Crie um 'FileReader'.
1. A função [AsposePdfChangePassword](https://reference.aspose.com/pdf/javascript-cpp/security/asposepdfchangepassword/) é executada.
1. O nome do arquivo resultante é definido, neste exemplo "ResultPdfChangePassword.pdf".
1. Em seguida, se o 'json.errorCode' for 0, então seu DownloadFile receberá o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro em seu arquivo, então informações sobre tal erro estarão contidas no arquivo 'json.errorText'.

1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante para o sistema operacional do usuário.

```js

    var ffilePdfChangePassword = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Alterar senhas de um arquivo PDF de "owner" para "newowner" e salvar como "ResultPdfChangePassword.pdf"*/
        const json = AsposePdfChangePassword(event.target.result, e.target.files[0].name, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Criar um link para baixar o arquivo resultante*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

## Usando Web Workers

```js

  /*Criar Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erro do Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'carregado!' :
        (evt.data.json.errorCode == 0) ? `Resultado:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `Erro: ${evt.data.json.errorText}`;

    /*Manipulador de eventos*/
    const ffilePdfChangePassword = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const ownerPassword = 'owner'; /*Senha do proprietário*/
        const newUserPassword = "newuser"; /*Nova senha do usuário*/
        const newOwnerPassword = "newowner"; /*Nova senha do proprietário*/
        /*Alterar senhas de um arquivo PDF de "owner" para "newowner" e salvar como "ResultPdfChangePassword.pdf" - Solicitar ao Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfChangePassword', "params": [event.target.result, e.target.files[0].name, ownerPassword, newUserPassword, newOwnerPassword, "ResultPdfChangePassword.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Trecho de código]

    /*Criar um link para baixar o arquivo resultante*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "Clique aqui para baixar o arquivo " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```