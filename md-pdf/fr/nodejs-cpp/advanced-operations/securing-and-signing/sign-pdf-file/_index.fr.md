---
title: Ajouter une signature numérique dans un PDF en Node.js
linktitle: Signer numériquement un PDF
type: docs
weight: 70
url: /nodejs-cpp/sign-pdf/
description: Signer numériquement des documents PDF dans l'environnement Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Une signature numérique dans un document PDF est un moyen de vérifier l'authenticité et l'intégrité du document. C'est le processus de signature électronique d'un document PDF en utilisant une clé privée et un certificat numérique. Cette signature garantit au détenteur que le document n'a pas été modifié depuis la signature et que le signataire est bien celui qu'il approuve. Pour signer un PDF avec Node.js, utilisez l'outil Aspose.PDF.

Dans le cas où vous souhaitez signer un fichier PDF, vous pouvez utiliser la fonction [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/).

Il est possible d'utiliser des **paramètres** liés à la signature :

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

Ce snippet de code utilise le module AsposePDFforNode.js dans un environnement Node.js pour signer numériquement un fichier PDF en utilisant la signature PKCS7.

**CommonJS :**

1. Appelez `require` et importez le module `asposepdfnodejs` en tant que variable `AsposePdf`.
1. Spécifiez le nom du fichier PDF à signer, le fichier de clé PKCS7 et le fichier d'image d'apparence de la signature. Le certificat et l'image peuvent être placés n'importe où sur votre système de fichiers à partir duquel vous les téléchargez pour la signature PDF.
1. Appelez `AsposePdf` en tant que Promise et effectuez l'opération de signature du fichier. Recevez l'objet si l'opération réussit.
1. Appelez la fonction [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/).
1. Signez un fichier PDF avec des signatures numériques. Paramètres liés à la signature (comme le fichier de clé, le mot de passe, les coordonnées, la raison, le contact, l'emplacement, etc.).

1. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultSignPKCS7.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Clé PKCS7*/
      const test_pfx_file = 'test.pfx';
      /*Apparence de la signature*/
      const sign_img_file = 'Aspose.jpg';
      /*Signer un fichier PDF avec des signatures numériques et enregistrer le "ResultSignPKCS7.pdf"*/
      const json = AsposePdfModule.AsposePdfSignPKCS7(pdf_file, 1, test_pfx_file, "Pa$$w0rd2023", 100, 100, 200, 100, "Reason", "Contact", "Location", 1, sign_img_file, "ResultSignPKCS7.pdf");
      console.log("AsposePdfSignPKCS7 => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6 :**

1. Importer le module `asposepdfnodejs`.

1. Spécifiez le nom du fichier PDF à signer, le fichier clé PKCS7 et le fichier image d'apparence de la signature.
1. Initialisez le module AsposePdf. Recevez l'objet si l'initialisation est réussie.
1. Appelez la fonction [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/).
1. Signez un fichier PDF avec des signatures numériques. Paramètres liés à la signature (comme le fichier clé, le mot de passe, les coordonnées, la raison, le contact, l'emplacement, etc.).
1. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultSignPKCS7.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Clé PKCS7*/
  const test_pfx_file = 'test.pfx';
  /*Apparence de la signature*/
  const sign_img_file = 'Aspose.jpg';
  /*Signer un fichier PDF avec des signatures numériques et enregistrer le "ResultSignPKCS7.pdf"*/
  const json = AsposePdfModule.AsposePdfSignPKCS7(pdf_file, 1, test_pfx_file, "Pa$$w0rd2023", 100, 100, 200, 100, "Reason", "Contact", "Location", 1, sign_img_file, "ResultSignPKCS7.pdf");
  console.log("AsposePdfSignPKCS7 => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```