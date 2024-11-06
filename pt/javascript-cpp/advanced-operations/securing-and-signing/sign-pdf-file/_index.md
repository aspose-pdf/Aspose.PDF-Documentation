---
title: Adicionar assinatura digital ou assinar PDF digitalmente em JavaScript via C++
linktitle: Assinar PDF digitalmente
type: docs
weight: 70
url: pt/javascript-cpp/sign-pdf/
description: Assinar digitalmente documentos PDF usando JavaScript via C++.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Uma assinatura digital em um documento PDF é uma forma de verificar a autenticidade e a integridade do documento. Este é o processo de assinatura eletrônica de um documento PDF usando uma chave privada e um certificado digital. Esta assinatura garante ao titular que o documento não foi alterado ou modificado desde a assinatura e que o signatário é aquele que aprovou. Para assinar PDF com JavaScript, use a ferramenta Aspose.PDF.

Aspose.PDF para JavaScript via C++ suporta o recurso de assinar digitalmente os arquivos PDF usando o [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfsignpkcs7/).

## Assinar PDF com assinaturas digitais

```js

    /*Definir o nome do arquivo de chave PKCS7 padrão*/
    var fileSign = "/test.pfx";

    var ffileSign = function (e) {
      const file_reader = new FileReader();
      /*Definir o nome do arquivo de chave PKCS7*/
      fileImage = e.target.files[0].name;
      file_reader.onload = (event) => {
        /*Salvar o BLOB na memória FS para processamento*/
        AsposePdfPrepare(event.target.result, fileSign);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Definir o nome do arquivo de imagem (Aparência da Assinatura) padrão*/
    var signatureAppearance = "/Aspose.jpg";

    var ffileImage = function (e) {
      const file_reader = new FileReader();
      /*Definir o nome do arquivo de imagem*/
      signatureAppearance = e.target.files[0].name;
      file_reader.onload = (event) => {
        /*Salvar o BLOB na memória FS para processamento*/
        AsposePdfPrepare(event.target.result, signatureAppearance);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    var ffileSignPKCS7 = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        let pswSign = document.getElementById("passwordSign").value;
        /*Assinar um arquivo PDF com assinaturas digitais e salvar o "ResultSignPKCS7.pdf"*/
        const json = AsposePdfSignPKCS7(event.target.result, e.target.files[0].name, 1, fileSign, pswSign, 200, 200, 200, 100, "TEST", "test@test.com", "EU", 1, signatureAppearance,"ResultSignPKCS7.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Criar um link para baixar o arquivo de resultado*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```


### Usando Web Workers

```js

    /*Criar Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erro do Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'carregado!' :
        (evt.data.json.errorCode == 0) ?
          `Resultado:\n${(evt.data.operation == 'AsposePdfPrepare') ?
            'arquivo preparado!':
            DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Erro: ${evt.data.json.errorText}`;

    /*Definir o nome de arquivo padrão da chave PKCS7*/
    var fileSign = "test.pfx";
    /*Definir o nome de arquivo padrão da imagem (Aparência da Assinatura): 'Aspose.jpg' já carregado, veja as configurações em 'settings.json'*/
    var signatureAppearance = "Aspose.jpg";

    /*Manipulador de eventos*/
    const ffileSignPKCS7 = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const pageNum = 1;
        const pswSign = document.getElementById("passwordSign").value;
        const setXIndent = 100;
        const setYIndent = 100;
        const setHeight = 200;
        const setWidth = 100;
        const reason = 'Razão';
        const contact = 'contact@test.com';
        const location = 'Localização';
        const isVisible = 1;
        /*Assinar um arquivo PDF com assinaturas digitais e salvar como "ResultSignPKCS7.pdf" - Perguntar ao Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfSignPKCS7',
            "params": [event.target.result, e.target.files[0].name, pageNum, fileSign, pswSign, setXIndent, setYIndent,
                      setHeight, setWidth, reason, contact, location, isVisible, signatureAppearance, "ResultSignPKCS7.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileSign = e => {
      const file_reader = new FileReader();
      /*Definir o nome de arquivo da chave PKCS7*/
      fileSign = e.target.files[0].name;
      file_reader.onload = event => {
        /*Salvar o BLOB no FS de Memória para processamento*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfPrepare', "params": [event.target.result, fileSign] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileImage = e => {
      const file_reader = new FileReader();
      /*Definir o nome do arquivo de imagem*/
      signatureAppearance = e.target.files[0].name;
      file_reader.onload = event => {
        /*Salvar o BLOB no FS de Memória para processamento*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfPrepare', "params": [event.target.result, signatureAppearance] },
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