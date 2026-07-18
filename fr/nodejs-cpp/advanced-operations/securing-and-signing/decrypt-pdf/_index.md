---
title: Décrypter un PDF en Node.js
linktitle: Décrypter le fichier PDF
type: docs
weight: 40
url: /fr/nodejs-cpp/decrypt-pdf/
description: Décrypter le fichier PDF avec Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Décrypter le fichier PDF en utilisant le mot de passe propriétaire

Récemment, de plus en plus d'utilisateurs échangent des documents chiffrés afin de ne pas devenir victimes de fraudes sur Internet et de protéger leurs documents.
À cet égard, il devient nécessaire d'accéder au fichier PDF chiffré, car cet accès ne peut être obtenu que par un utilisateur autorisé. De plus, les gens recherchent diverses solutions pour décrypter les fichiers PDF. 

Dans le cas où vous voulez déchiffrer un fichier PDF, vous pouvez utiliser [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/) fonction. 
Si vous voulez déchiffrer un fichier PDF, essayez le fragment de code suivant :

**CommonJS:**

1. Appel `require` et importer `asposepdfnodejs` module comme `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF qui sera déchiffré.
1. Appel `AsposePdf` comme Promise et exécuter l'opération de décryptage du fichier. Recevez l'objet si l'opération réussit.
1. Appelez le [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/) fonction.
1. Déchiffrer le fichier PDF avec le mot de passe "owner".
1. Ainsi, si 'json.errorCode' vaut 0, le résultat de l'opération est enregistré dans "ResultDecrypt.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Decrypt a PDF-file with password is "owner" and save the "ResultDecrypt.pdf"*/
      const json = AsposePdfModule.AsposePdfDecrypt(pdf_encrypt_file, "owner", "ResultDecrypt.pdf");
      console.log("AsposePdfDecrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6 :**

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF qui sera déchiffré.
1. Initialisez le module AsposePdf. Recevez l'objet si le processus réussit.
1. Appelez le [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/) fonction.
1. Déchiffrer le fichier PDF avec le mot de passe "owner".
1. Ainsi, si 'json.errorCode' vaut 0, le résultat de l'opération est enregistré dans "ResultDecrypt.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /*Decrypt a PDF-file with password is "owner" and save the "ResultDecrypt.pdf"*/
  const json = AsposePdfModule.AsposePdfDecrypt(pdf_encrypt_file, "owner", "ResultDecrypt.pdf");
  console.log("AsposePdfDecrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```