---
title: Alterar Senha de um Arquivo PDF em Node.js
linktitle: Alterar Senha
type: docs
weight: 50
url: /nodejs-cpp/change-password-pdf/
description: Alterar a senha de um arquivo PDF com Aspose.PDF para Node.js via C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Alterar Senha de um Arquivo PDF

Caso você queira alterar a senha de um PDF, você pode usar a função [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/). Ela altera a senha do usuário e a senha do proprietário pela senha do proprietário, mantendo as configurações de segurança originais. Se você quiser alterar a senha de um arquivo PDF de "owner" para "newowner" ou "newuser", tente o seguinte trecho de código:

**CommonJS:**

1. Chame `require` e importe o módulo `asposepdfnodejs` como variável `AsposePdf`.
1. Especifique o nome do arquivo PDF que terá a senha alterada.
1. Chame `AsposePdf` como Promise e execute a operação para alterar a senha. Receba o objeto se bem-sucedido.

1. Chame a função [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/).
1. Alterar Senha. A senha do proprietário existente é definida como "owner" e é alterada para "newowner" com a nova senha de usuário "newuser".
1. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultPdfChangePassword.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, as informações de erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Altere as senhas do arquivo PDF de "owner" para "newowner" e salve o "ResultPdfChangePassword.pdf"*/
      const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
      console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


Observe que se a senha for uma string vazia:

1. Se a senha do usuário estiver vazia - o PDF abre sem pedir uma senha (mas ainda está criptografado).
1. Se a senha do proprietário estiver vazia, o PDF abre com uma solicitação de senha do usuário.
1. Se ambas estiverem vazias - o PDF abre sem pedir uma senha (mas ainda está criptografado).

**ECMAScript/ES6:**

1. Importe o módulo `asposepdfnodejs`.
1. Especifique o nome do arquivo PDF que terá a senha alterada.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/).
1. Altere a Senha. A senha do proprietário existente é definida como "owner" e é alterada para "newowner" com a nova senha de usuário "newuser".

1. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultPdfChangePassword.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer em seu arquivo, a informação do erro será contida em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /*Altera as senhas do arquivo PDF de "owner" para "newowner" e salva o "ResultPdfChangePassword.pdf"*/
  const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
  console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```