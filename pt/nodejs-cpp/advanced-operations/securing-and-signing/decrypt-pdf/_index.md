---
title: Decrypt PDF em Node.js
linktitle: Decrypt PDF File
type: docs
weight: 40
url: /pt/nodejs-cpp/decrypt-pdf/
description: Decrypt PDF File com Aspose.PDF para Node.js via C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Decrypt PDF File usando Senha do Proprietário

Recentemente, mais e mais usuários trocam documentos criptografados para não se tornarem vítimas de fraudes na Internet e proteger seus documentos. 
Nesse sentido, torna-se necessário acessar o arquivo PDF criptografado, já que tal acesso só pode ser obtido por um usuário autorizado. Além disso, as pessoas estão procurando várias soluções para descriptografar arquivos PDF.

Caso você queira descriptografar um arquivo PDF, você pode usar a função [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/). 
Se você deseja descriptografar um arquivo PDF, experimente o próximo trecho de código:

**CommonJS:**

1. Chame `require` e importe o módulo `asposepdfnodejs` como variável `AsposePdf`.
1. Especifique o nome do arquivo PDF que será alterado para descriptografado.

1. Chame `AsposePdf` como Promise e execute a operação para descriptografar o arquivo. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/).
1. Descriptografar arquivo PDF com a senha "owner".
1. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultDecrypt.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Descriptografar um arquivo PDF com a senha "owner" e salvar como "ResultDecrypt.pdf"*/
      const json = AsposePdfModule.AsposePdfDecrypt(pdf_encrypt_file, "owner", "ResultDecrypt.pdf");
      console.log("AsposePdfDecrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importe o módulo `asposepdfnodejs`.
1. Especifique o nome do arquivo PDF que será alterado para descriptografado.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/).
1. Descriptografe o arquivo PDF com a senha "owner".
1. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultDecrypt.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer em seu arquivo, as informações do erro serão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /*Descriptografe um arquivo PDF com a senha "owner" e salve como "ResultDecrypt.pdf"*/
  const json = AsposePdfModule.AsposePdfDecrypt(pdf_encrypt_file, "owner", "ResultDecrypt.pdf");
  console.log("AsposePdfDecrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```