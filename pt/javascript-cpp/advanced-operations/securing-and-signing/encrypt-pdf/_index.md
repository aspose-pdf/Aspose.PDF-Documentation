---
title:  Criptografar PDF usando JavaScript
linktitle: Criptografar Arquivo PDF
type: docs
weight: 50
url: /pt/javascript-cpp/encrypt-pdf/
description: Criptografar Arquivo PDF com Aspose.PDF para JavaScript via C++.
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Criptografar Arquivo PDF usando Senha de Usuário ou Proprietário

Se você estiver enviando um e-mail para alguém com um anexo PDF que contém informações confidenciais, pode desejar adicionar alguma segurança a ele primeiro para evitar que caia em mãos erradas. A melhor maneira de limitar o acesso não autorizado a um documento PDF é protegê-lo com uma senha. Para criptografar documentos de forma fácil e segura, você pode usar Aspose.PDF para JavaScript via C++.

>Especifique senhas de usuário e proprietário diferentes ao criptografar o arquivo PDF.

- A **senha do usuário**, se definida, é o que você precisa fornecer para abrir um PDF. O Acrobat/Reader solicitará que um usuário insira a senha do usuário. Se não estiver correta, o documento não será aberto.
- A **senha do proprietário**, se definida, controla permissões, como impressão, edição, extração, comentários, etc.
 Acrobat/Reader desativará essas coisas com base nas configurações de permissão. O Acrobat exigirá essa senha se você quiser definir/alterar permissões.

O trecho de código a seguir mostra como criptografar arquivos PDF.

1. Selecione um arquivo PDF para criptografar.
1. Crie um 'FileReader'.
1. A função [AsposePdfEncrypt](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfencrypt/) é executada.
1. O nome do arquivo resultante é definido, neste exemplo "ResultEncrypt.pdf".
1. Em seguida, se o 'json.errorCode' for 0, então o seu DownloadFile recebe o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro no seu arquivo, então as informações sobre tal erro estarão contidas no arquivo 'json.errorText'.
1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante para o sistema operacional do usuário.

```js

  var ffileEncrypt = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*criptografar um arquivo PDF com as senhas "user" e "owner", e salvar como "ResultDecrypt.pdf"*/
      const json = AsposePdfEncrypt(event.target.result, e.target.files[0].name, "user", "owner", Module.Permissions.PrintDocument, Module.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*criar um link para baixar o arquivo resultante*/
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

    /*Manipulador de eventos*/
    const ffileEncrypt = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const password_user = 'user';
        const password_owner = 'owner';
        const permissions = 'Module.Permissions.PrintDocument';
        const algorithm = 'Module.CryptoAlgorithm.RC4x40';
        /*Criptografar um arquivo PDF com senhas "user" e "owner", e salvar o "ResultEncrypt.pdf" - Pedir ao Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfEncrypt',
            "params": [event.target.result, e.target.files[0].name, password_user, password_owner,
                      permissions, algorithm, "ResultEncrypt.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Fazer um link para baixar o arquivo resultante*/
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