---
title: Décrypter un PDF en Node.js
linktitle: Décrypter un fichier PDF
type: docs
weight: 40
url: /nodejs-cpp/decrypt-pdf/
description: Décrypter un fichier PDF avec Aspose.PDF pour Node.js via C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Décrypter un fichier PDF en utilisant le mot de passe propriétaire

Récemment, de plus en plus d'utilisateurs échangent des documents cryptés afin de ne pas devenir victimes de fraudes sur Internet et de protéger leurs documents.
À cet égard, il devient nécessaire d'accéder au fichier PDF crypté, car un tel accès ne peut être obtenu que par un utilisateur autorisé. De plus, les gens recherchent diverses solutions pour décrypter les fichiers PDF.

Si vous souhaitez décrypter un fichier PDF, vous pouvez utiliser la fonction [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/).
Si vous voulez décrypter un fichier PDF, essayez l'extrait de code suivant :

**CommonJS :**

1. Appelez `require` et importez le module `asposepdfnodejs` en tant que variable `AsposePdf`.
1. Spécifiez le nom du fichier PDF qui sera décrypté.

1. Appelez `AsposePdf` en tant que Promise et effectuez l'opération pour déchiffrer le fichier. Recevez l'objet en cas de succès.
1. Appelez la fonction [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/).
1. Déchiffrez le fichier PDF avec le mot de passe "owner".
1. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultDecrypt.pdf". Si le paramètre json.errorCode n'est pas 0 et, par conséquent, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Déchiffrer un fichier PDF avec le mot de passe "owner" et enregistrer dans "ResultDecrypt.pdf"*/
      const json = AsposePdfModule.AsposePdfDecrypt(pdf_encrypt_file, "owner", "ResultDecrypt.pdf");
      console.log("AsposePdfDecrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6 :**

1. Importer le module `asposepdfnodejs`.
1. Spécifiez le nom du fichier PDF qui sera décrypté.
1. Initialiser le module AsposePdf. Recevez l'objet si réussi.
1. Appelez la fonction [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/).
1. Décryptez le fichier PDF avec le mot de passe "owner".
1. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultDecrypt.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /*Décrypter un fichier PDF avec le mot de passe "owner" et enregistrer dans "ResultDecrypt.pdf"*/
  const json = AsposePdfModule.AsposePdfDecrypt(pdf_encrypt_file, "owner", "ResultDecrypt.pdf");
  console.log("AsposePdfDecrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```