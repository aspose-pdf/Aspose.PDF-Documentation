---
title: Adicionar assinatura digital em PDF no Node.js
linktitle: Assinar PDF digitalmente
type: docs
weight: 70
url: /pt/nodejs-cpp/sign-pdf/
description: Assinar documentos PDF digitalmente no ambiente Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---


Uma assinatura digital em um documento PDF é uma forma de verificar a autenticidade e integridade do documento. Este é o processo de assinatura eletrônica de um documento PDF usando uma chave privada e certificado digital. Esta assinatura garante ao titular que o documento não foi alterado ou modificado desde a assinatura e que o signatário é quem o aprova. Para assinar PDF com Node.js, use a ferramenta Aspose.PDF.

Caso queira assinar um arquivo PDF, você pode usar [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/) função.

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
- location
- isVisible
- signatureAppearance
- fileNameResult 

Este trecho de código utiliza o módulo AsposePDFforNode.js em um ambiente Node.js para assinar digitalmente um arquivo PDF usando a assinatura PKCS7.

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome do arquivo PDF a ser assinado, o arquivo de chave PKCS7 e o arquivo de imagem da aparência da assinatura. O certificado e a imagem podem ser colocados em qualquer lugar no seu sistema de arquivos de onde você os envia para a assinatura de PDF.
1. Chamada `AsposePdf` como Promise e execute a operação de assinatura do arquivo. Receba o objeto se for bem-sucedido.
1. Chame o [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/) função. 
1. Assine um arquivo PDF com assinaturas digitais. Parâmetros relacionados à assinatura (como o arquivo de chave, senha, coordenadas, motivo, contato, local, etc). 
1. Portanto, se ‘json.errorCode’ for 0, o resultado da operação será salvo em “ResultSignPKCS7.pdf”. Se o parâmetro json.errorCode não for 0 e, consequentemente, ocorrer um erro no seu arquivo, as informações do erro estarão contidas em ‘json.errorText’.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Key PKCS7*/
      const test_pfx_file = 'test.pfx';
      /*Signature appearance*/
      const sign_img_file = 'Aspose.jpg';
      /*Sign a PDF-file with digital signatures and save the "ResultSignPKCS7.pdf"*/
      const json = AsposePdfModule.AsposePdfSignPKCS7(pdf_file, 1, test_pfx_file, "Pa$$w0rd2023", 100, 100, 200, 100, "Reason", "Contact", "Location", 1, sign_img_file, "ResultSignPKCS7.pdf");
      console.log("AsposePdfSignPKCS7 => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome do arquivo PDF a ser assinado, o arquivo de chave PKCS7 e o arquivo de imagem de aparência da assinatura.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame o [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/) função. 
1. Assine um arquivo PDF com assinaturas digitais. Parâmetros relacionados à assinatura (como o arquivo de chave, senha, coordenadas, motivo, contato, local, etc). 
1. Portanto, se ‘json.errorCode’ for 0, o resultado da operação será salvo em “ResultSignPKCS7.pdf”. Se o parâmetro json.errorCode não for 0 e, consequentemente, ocorrer um erro no seu arquivo, as informações do erro estarão contidas em ‘json.errorText’.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Key PKCS7*/
  const test_pfx_file = 'test.pfx';
  /*Signature appearance*/
  const sign_img_file = 'Aspose.jpg';
  /*Sign a PDF-file with digital signatures and save the "ResultSignPKCS7.pdf"*/
  const json = AsposePdfModule.AsposePdfSignPKCS7(pdf_file, 1, test_pfx_file, "Pa$$w0rd2023", 100, 100, 200, 100, "Reason", "Contact", "Location", 1, sign_img_file, "ResultSignPKCS7.pdf");
  console.log("AsposePdfSignPKCS7 => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```