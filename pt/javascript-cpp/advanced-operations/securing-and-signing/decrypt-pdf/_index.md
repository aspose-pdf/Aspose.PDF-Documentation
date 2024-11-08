---
title: Descriptografar PDF usando JavaScript
linktitle: Descriptografar Arquivo PDF
type: docs
weight: 40
url: /pt/javascript-cpp/decrypt-pdf/
description: Descriptografar Arquivo PDF com Aspose.PDF para JavaScript via C++.
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Descriptografar Arquivo PDF usando Senha de Proprietário

Recentemente, mais e mais usuários trocam documentos criptografados para não se tornarem vítimas de fraudes na Internet e proteger seus documentos. 
Nesse sentido, torna-se necessário acessar o arquivo PDF criptografado, já que tal acesso só pode ser obtido por um usuário autorizado. Além disso, as pessoas estão procurando várias soluções para descriptografar arquivos PDF.

É melhor resolver esse problema de uma vez usando o Aspose.PDF para JavaScript via C++ diretamente no seu navegador. O seguinte trecho de código mostra como descriptografar arquivos PDF.

1. Selecione um arquivo PDF para descriptografar.
1. Crie um 'FileReader'.
1. A função [AsposePdfDecrypt](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfdecrypt/) é executada.

1. O nome do arquivo resultante é definido, neste exemplo "ResultDecrypt.pdf".
1. Em seguida, se o 'json.errorCode' for 0, então seu DownloadFile recebe o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro em seu arquivo, então informações sobre tal erro estarão contidas no arquivo 'json.errorText'.
1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante para o sistema operacional do usuário.

```js

    var ffileDecrypt = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Descriptografar um arquivo PDF com a senha "owner" e salvar como "ResultDecrypt.pdf"*/
        const json = AsposePdfDecrypt(event.target.result, e.target.files[0].name, "owner", "ResultDecrypt.pdf");
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
        (evt.data.json.errorCode == 0) ?
          `Resultado:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Erro: ${evt.data.json.errorText}`;

    /*Manipulador de evento*/
    const ffileDecrypt = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const password = 'owner';
        /*Descriptografar um arquivo PDF com a senha "owner" e salvar como "ResultDecrypt.pdf" - Solicitar ao Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfDecrypt',
            "params": [event.target.result, e.target.files[0].name, password, "ResultDecrypt.pdf"] }, 
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Criar um link para baixar o arquivo de resultado*/
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