---
title: Alterar senha de um arquivo PDF em Node.js
linktitle: Alterar senha
type: docs
weight: 50
url: /pt/nodejs-cpp/change-password-pdf/
description: Alterar senha de um arquivo PDF com Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Alterar senha de um arquivo PDF

Caso você queira alterar a senha do PDF, pode usar [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/) função. altera a senha do usuário e a senha do proprietário usando a senha do proprietário, mantendo as configurações de segurança originais.
Se você quiser mudar a senha de um arquivo PDF de “owner” para “newowner” ou “newuser”, experimente o próximo trecho de código:

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome do arquivo PDF que terá a senha alterada.
1. Chamada `AsposePdf` como Promise e execute a operação de alteração de senha. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/).
1. Alterar senha. A senha do proprietário existente é definida como “owner”, e é alterada para “newowner” com a nova senha de usuário “newuser”.
1. Assim, se ‘json.errorCode’ for 0, o resultado da operação será salvo em “ResultPdfChangePassword.pdf”. Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, as informações do erro estarão contidas em ‘json.errorText’.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Change passwords of the PDF-file from "owner" to "newowner" and save the "ResultPdfChangePassword.pdf"*/
      const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
      console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

Observe que se a senha for uma string vazia:

1. Se a senha do usuário estiver vazia - o PDF abre sem solicitar uma senha (mas ainda está criptografado).
1. Se a senha do proprietário estiver vazia, o PDF abrirá solicitando uma senha de usuário.
1. Se ambas estiverem vazias  - o PDF abrirá sem solicitar uma senha (mas ainda está criptografado).


**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome do arquivo PDF que terá a senha alterada.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/).
1. Alterar senha. A senha do proprietário existente é definida como “owner”, e é alterada para “newowner” com a nova senha de usuário “newuser”.
1. Assim, se ‘json.errorCode’ for 0, o resultado da operação será salvo em “ResultPdfChangePassword.pdf”. Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, as informações do erro estarão contidas em ‘json.errorText’.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /*Change passwords of the PDF-file from "owner" to "newowner" and save the "ResultPdfChangePassword.pdf"*/
  const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
  console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```