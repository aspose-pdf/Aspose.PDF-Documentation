---
title:  Criptografar PDF em Node.js
linktitle: Criptografar Arquivo PDF
type: docs
weight: 50
url: /pt/nodejs-cpp/encrypt-pdf/
description: Criptografar Arquivo PDF com Aspose.PDF para Node.js via C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Criptografar Arquivo PDF usando Senha de Usuário ou Proprietário

Se você estiver enviando um email para alguém com um anexo PDF que contém informações confidenciais, você pode querer adicionar alguma segurança a ele primeiro para evitar que caia em mãos erradas. A melhor maneira de limitar o acesso não autorizado a um documento PDF é protegê-lo com uma senha. Para criptografar documentos de forma fácil e segura, você pode usar o Aspose.PDF para Node.js via C++.

>Especifique senhas de usuário e proprietário diferentes ao criptografar o arquivo PDF.

- A **senha de usuário**, se definida, é o que você precisa fornecer para abrir um PDF. O Acrobat/Reader solicitará ao usuário que insira a senha de usuário. Se não estiver correta, o documento não abrirá.
- A **senha de proprietário**, se definida, controla permissões, como impressão, edição, extração, comentários, etc.
 Acrobat/Reader irá desabilitar essas coisas com base nas configurações de permissão. O Acrobat exigirá esta senha se você quiser definir/alterar permissões.

Caso você queira criptografar um arquivo PDF, você pode usar a função [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/). 
Se você quiser criptografar um arquivo PDF, tente o próximo trecho de código:

**CommonJS:**

1. Chame `require` e importe o módulo `asposepdfnodejs` como variável `AsposePdf`.
1. Especifique o nome do arquivo PDF que será criptografado.
1. Chame `AsposePdf` como Promise e execute a operação para criptografar o arquivo. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/).
1. Criptografe o arquivo PDF com as senhas "user" e "owner".
1. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultEncrypt.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer em seu arquivo, a informação do erro estará contida em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Criptografe um arquivo PDF com as senhas "user" e "owner", e salve como "ResultEncrypt.pdf"*/
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

1. Importe o módulo `asposepdfnodejs`.
1. Especifique o nome do arquivo PDF que terá a criptografia alterada.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/).
1. Descriptografe o arquivo PDF com as senhas "user" e "owner".

1. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultEncrypt.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer em seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Criptografar um arquivo PDF com as senhas "user" e "owner", e salvar como "ResultEncrypt.pdf"*/
  const json = AsposePdfModule.AsposePdfEncrypt(pdf_file, "user", "owner", AsposePdfModule.Permissions.PrintDocument, AsposePdfModule.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
  console.log("AsposePdfEncrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```