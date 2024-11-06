---
title: Adicionar assinatura digital em PDF no Node.js
linktitle: Assinar PDF digitalmente
type: docs
weight: 70
url: pt/nodejs-cpp/sign-pdf/
description: Assinar digitalmente documentos PDF no ambiente Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Uma assinatura digital em um documento PDF é uma forma de verificar a autenticidade e integridade do documento. Este é o processo de assinatura eletrônica de um documento PDF usando uma chave privada e um certificado digital. Esta assinatura garante ao titular que o documento não foi alterado ou modificado desde a assinatura e que o assinante é quem ele aprova. Para assinar PDF com Node.js, use a ferramenta Aspose.PDF.

Caso você queira assinar um arquivo PDF, pode usar a função [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/).

É possível usar **parâmetros** relacionados à assinatura:

- fileName
- pageNum
- fileSign
- pswSign
- setXIndent
- setYIndent
- setHeight
- setWidth
- reason

- contact
- localização
- estáVisível
- aparênciaDaAssinatura
- nomeDoArquivoResultado

Este trecho de código utiliza o módulo AsposePDFforNode.js em um ambiente Node.js para assinar digitalmente um arquivo PDF usando a assinatura PKCS7.

**CommonJS:**

1. Chame `require` e importe o módulo `asposepdfnodejs` como variável `AsposePdf`.
1. Especifique o nome do arquivo PDF a ser assinado, o arquivo de chave PKCS7 e o arquivo de imagem de aparência da assinatura. O certificado e a imagem podem ser colocados em qualquer lugar no seu sistema de arquivos de onde você os envia para assinatura de PDF.
1. Chame `AsposePdf` como Promise e execute a operação para assinar o arquivo. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/).
1. Assine um arquivo PDF com assinaturas digitais. Parâmetros relacionados à assinatura (como o arquivo de chave, senha, coordenadas, motivo, contato, localização, etc).

1. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultSignPKCS7.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, a informação do erro estará contida em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Chave PKCS7*/
      const test_pfx_file = 'test.pfx';
      /*Aparência da assinatura*/
      const sign_img_file = 'Aspose.jpg';
      /*Assinar um arquivo PDF com assinaturas digitais e salvar o "ResultSignPKCS7.pdf"*/
      const json = AsposePdfModule.AsposePdfSignPKCS7(pdf_file, 1, test_pfx_file, "Pa$$w0rd2023", 100, 100, 200, 100, "Reason", "Contact", "Location", 1, sign_img_file, "ResultSignPKCS7.pdf");
      console.log("AsposePdfSignPKCS7 => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importe o módulo `asposepdfnodejs`.

1. Especifique o nome do arquivo PDF a ser assinado, o arquivo de chave PKCS7 e o arquivo de imagem de aparência da assinatura.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/).
1. Assine um arquivo PDF com assinaturas digitais. Parâmetros relacionados à assinatura (como o arquivo de chave, senha, coordenadas, motivo, contato, localização, etc).
1. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultSignPKCS7.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, a informação do erro será contida em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Chave PKCS7*/
  const test_pfx_file = 'test.pfx';
  /*Aparência da assinatura*/
  const sign_img_file = 'Aspose.jpg';
  /*Assine um arquivo PDF com assinaturas digitais e salve o "ResultSignPKCS7.pdf"*/
  const json = AsposePdfModule.AsposePdfSignPKCS7(pdf_file, 1, test_pfx_file, "Pa$$w0rd2023", 100, 100, 200, 100, "Reason", "Contact", "Location", 1, sign_img_file, "ResultSignPKCS7.pdf");
  console.log("AsposePdfSignPKCS7 => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```