---
title:  Criptografar PDF em Node.js
linktitle: Criptografar arquivo PDF
type: docs
weight: 50
url: /pt/nodejs-cpp/encrypt-pdf/
description: Criptografar arquivo PDF com Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Criptografar arquivo PDF usando usando senha de usuário ou de proprietário

Se você está enviando um e‑mail para alguém com um anexo PDF que contém informações confidenciais, pode desejar adicionar alguma segurança a ele primeiro para evitar que caia em mãos erradas. A melhor maneira de limitar o acesso não autorizado a um documento PDF é protegê-lo com uma senha. Para criptografar documentos de forma fácil e segura, você pode usar Aspose.PDF for Node.js via C++.

>Por favor, especifique senhas diferentes de usuário e de proprietário ao criptografar o arquivo PDF.

- A **senha de usuário**, se definida, é o que você precisa fornecer para abrir um PDF. Acrobat/Reader solicitará que o usuário insira a senha de usuário. Se não estiver correta, o documento não será aberto.
- A **senha de proprietário**, se definida, controla permissões, como impressão, edição, extração, comentários, etc. Acrobat/Reader impedirá essas ações com base nas configurações de permissão. Acrobat exigirá essa senha se você quiser definir/alterar permissões.

Caso você queira criptografar um arquivo PDF, pode usar [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/) função. 
Se você quiser criptografar um arquivo PDF, experimente o próximo trecho de código:

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome do arquivo PDF que será criptografado.
1. Chamada `AsposePdf` como Promise e execute a operação de criptografia do arquivo. Receba o objeto se for bem-sucedido.
1. Chame o [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/) função. 
1. Criptografe o arquivo PDF com as senhas "user" e "owner".
1. Assim, se ‘json.errorCode’ for 0, o resultado da operação será salvo em "ResultEncrypt.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, ocorrer um erro no seu arquivo, as informações do erro estarão contidas em ‘json.errorText’.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Encrypt a PDF-file with passwords "user" and "owner", and save the "ResultEncrypt.pdf"*/
      const json = AsposePdfModule.AsposePdfEncrypt(pdf_file, "user", "owner", AsposePdfModule.Permissions.PrintDocument, AsposePdfModule.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
      console.log("AsposePdfEncrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

Existem diferentes [permissões de criptografia](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#acbb404dc8d3b328891faa5fba341ce0c):

- Module.Permissions.PrintDocument
- Module.Permissions.ModifyContent
- Module.Permissions.ExtractContent
- Module.Permissions.ModifyTextAnnotations
- Module.Permissions.FillForm
- Module.Permissions.ExtractContentWithDisabilities
- Module.Permissions.AssembleDocument
- Module.Permissions.PrintingQuality

Existem vários [algoritmos de criptografia](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#ae15d4d8afe86aae14972a6e493d19f66):

- Module.CryptoAlgorithm.RC4x40
- Module.CryptoAlgorithm.RC4x128
- Module.CryptoAlgorithm.AESx128
- Module.CryptoAlgorithm.AESx256

**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome do arquivo PDF que será alterado (criptografado).
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame o [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/) função. 
1. Descriptografar o arquivo PDF com as senhas "user" e "owner".
1. Assim, se ‘json.errorCode’ for 0, o resultado da operação será salvo em "ResultEncrypt.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, ocorrer um erro no seu arquivo, as informações do erro estarão contidas em ‘json.errorText’.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Encrypt a PDF-file with passwords "user" and "owner", and save the "ResultEncrypt.pdf"*/
  const json = AsposePdfModule.AsposePdfEncrypt(pdf_file, "user", "owner", AsposePdfModule.Permissions.PrintDocument, AsposePdfModule.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
  console.log("AsposePdfEncrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```