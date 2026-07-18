---
title: Ajouter une signature numérique dans un PDF avec Node.js
linktitle: Signer numériquement un PDF
type: docs
weight: 70
url: /fr/nodejs-cpp/sign-pdf/
description: Signer numériquement des documents PDF dans l’environnement Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---


Une signature numérique dans un document PDF est un moyen de vérifier l’authenticité et l’intégrité du document. Il s’agit du processus de signature électronique d’un document PDF à l’aide d’une clé privée et d’un certificat numérique. Cette signature garantit au détenteur que le document n’a pas été modifié ou altéré depuis la signature et que le signataire est bien celui qu’il approuve. Pour signer un PDF avec Node.js, utilisez l’outil Aspose.PDF.

Dans le cas où vous souhaitez signer un fichier PDF, vous pouvez utiliser [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/) fonction.

Il est possible d'utiliser **paramètres** liés à la signature:

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
- emplacement
- estVisible
- apparenceSignature
- résultatNomFichier 

Cet extrait de code utilise le module AsposePDFforNode.js dans un environnement Node.js pour signer numériquement un fichier PDF à l'aide de la signature PKCS7.

**CommonJS:**

1. Appel `require` et importer `asposepdfnodejs` module comme `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF à signer, le fichier de clé PKCS7 et le fichier image d'apparence de la signature. Le certificat et l'image peuvent être placés n'importe où sur votre système de fichiers depuis lequel vous les téléchargez pour la signature PDF.
1. Appel `AsposePdf` en tant que Promise et exécuter l'opération de signature du fichier. Recevoir l'objet si réussi.
1. Appelez le [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/) fonction. 
1. Signez un fichier PDF avec des signatures numériques. Paramètres liés à la signature (comme le fichier de clé, le mot de passe, les coordonnées, la raison, le contact, l'emplacement, etc.). 
1. Ainsi, si 'json.errorCode' vaut 0, le résultat de l'opération est enregistré dans "ResultSignPKCS7.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

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

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF à signer, le fichier de clé PKCS7 et le fichier image d'apparence de la signature.
1. Initialisez le module AsposePdf. Recevez l'objet si l'opération réussit.
1. Appelez le [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/) fonction. 
1. Signez un fichier PDF avec des signatures numériques. Paramètres liés à la signature (comme le fichier de clé, le mot de passe, les coordonnées, la raison, le contact, l'emplacement, etc.). 
1. Ainsi, si 'json.errorCode' vaut 0, le résultat de l'opération est enregistré dans "ResultSignPKCS7.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

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