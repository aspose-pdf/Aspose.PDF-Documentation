---
title: Descriptografar PDF em Node.js
linktitle: Descriptografar arquivo PDF
type: docs
weight: 40
url: /pt/nodejs-cpp/decrypt-pdf/
description: Descriptografar arquivo PDF com Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Descriptografar arquivo PDF usando senha de proprietário

Recentemente, cada vez mais usuários trocam documentos criptografados para não se tornar vítimas de fraudes na Internet e proteger seus documentos.
Nesse sentido, torna-se necessário acessar o arquivo PDF criptografado, já que esse acesso só pode ser obtido por um usuário autorizado. Além disso, as pessoas buscam várias soluções para descriptografar arquivos PDF. 

Caso você queira descriptografar um arquivo PDF, você pode usar [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/) função. 
Se você quiser descriptografar um arquivo PDF, tente o próximo trecho de código:

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome do arquivo PDF que será alterado após a descriptografia.
1. Chamada `AsposePdf` como Promise e execute a operação de descriptografia do arquivo. Receba o objeto se for bem-sucedido.
1. Chame o [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/) função.
1. Descriptografar arquivo PDF com a senha "owner".
1. Portanto, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultDecrypt.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Decrypt a PDF-file with password is "owner" and save the "ResultDecrypt.pdf"*/
      const json = AsposePdfModule.AsposePdfDecrypt(pdf_encrypt_file, "owner", "ResultDecrypt.pdf");
      console.log("AsposePdfDecrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome do arquivo PDF que será alterado após a descriptografia.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame o [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/) função.
1. Descriptografar arquivo PDF com a senha "owner".
1. Portanto, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultDecrypt.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /*Decrypt a PDF-file with password is "owner" and save the "ResultDecrypt.pdf"*/
  const json = AsposePdfModule.AsposePdfDecrypt(pdf_encrypt_file, "owner", "ResultDecrypt.pdf");
  console.log("AsposePdfDecrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```