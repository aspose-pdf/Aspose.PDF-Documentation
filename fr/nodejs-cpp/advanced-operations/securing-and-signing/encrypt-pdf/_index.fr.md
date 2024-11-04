---
title: Chiffrer un PDF en Node.js
linktitle: Chiffrer un fichier PDF
type: docs
weight: 50
url: /nodejs-cpp/encrypt-pdf/
description: Chiffrer un fichier PDF avec Aspose.PDF pour Node.js via C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Chiffrer un fichier PDF en utilisant un mot de passe utilisateur ou propriétaire

Si vous envoyez un email à quelqu'un avec une pièce jointe PDF contenant des informations confidentielles, vous pourriez souhaiter y ajouter d'abord une certaine sécurité pour éviter qu'elle ne tombe entre de mauvaises mains. La meilleure façon de limiter l'accès non autorisé à un document PDF est de le protéger avec un mot de passe. Pour chiffrer des documents facilement et en toute sécurité, vous pouvez utiliser Aspose.PDF pour Node.js via C++.

> Veuillez spécifier des mots de passe utilisateur et propriétaire différents lors du chiffrement du fichier PDF.

- Le **mot de passe utilisateur**, s'il est défini, est ce que vous devez fournir pour ouvrir un PDF. Acrobat/Reader demandera à un utilisateur de saisir le mot de passe utilisateur. S'il n'est pas correct, le document ne s'ouvrira pas.
- Le **mot de passe propriétaire**, s'il est défini, contrôle les permissions, telles que l'impression, l'édition, l'extraction, les commentaires, etc.
 Acrobat/Reader interdira ces actions en fonction des paramètres d'autorisation. Acrobat nécessitera ce mot de passe si vous souhaitez définir/modifier les autorisations.

Si vous souhaitez chiffrer un fichier PDF, vous pouvez utiliser la fonction [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/). Si vous voulez chiffrer un fichier PDF, essayez l'extrait de code suivant :

**CommonJS :**

1. Appelez `require` et importez le module `asposepdfnodejs` comme variable `AsposePdf`.
1. Spécifiez le nom du fichier PDF qui sera chiffré.
1. Appelez `AsposePdf` en tant que Promise et effectuez l'opération de chiffrement du fichier. Recevez l'objet en cas de succès.
1. Appelez la fonction [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/).
1. Chiffrez le fichier PDF avec les mots de passe "user" et "owner".
1. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultEncrypt.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Crypter un fichier PDF avec les mots de passe "user" et "owner", et enregistrer le "ResultEncrypt.pdf"*/
      const json = AsposePdfModule.AsposePdfEncrypt(pdf_file, "user", "owner", AsposePdfModule.Permissions.PrintDocument, AsposePdfModule.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
      console.log("AsposePdfEncrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

Il existe différentes [autorisations de cryptage](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#acbb404dc8d3b328891faa5fba341ce0c):

- Module.Permissions.PrintDocument
- Module.Permissions.ModifyContent
- Module.Permissions.ExtractContent

- Module.Permissions.ModifyTextAnnotations
- Module.Permissions.FillForm
- Module.Permissions.ExtractContentWithDisabilities
- Module.Permissions.AssembleDocument
- Module.Permissions.PrintingQuality

Il existe divers [algorithmes de chiffrement](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#ae15d4d8afe86aae14972a6e493d19f66) :

- Module.CryptoAlgorithm.RC4x40
- Module.CryptoAlgorithm.RC4x128
- Module.CryptoAlgorithm.AESx128
- Module.CryptoAlgorithm.AESx256

**ECMAScript/ES6 :**

1. Importez le module `asposepdfnodejs`.
1. Spécifiez le nom du fichier PDF qui changera le crypté.
1. Initialisez le module AsposePdf. Recevez l'objet si réussi.
1. Appelez la fonction [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/).
1. Déchiffrez le fichier PDF avec les mots de passe "user" et "owner".

1. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultEncrypt.pdf". Si le paramètre json.errorCode n'est pas 0 et, par conséquent, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Crypter un fichier PDF avec les mots de passe "user" et "owner", et sauvegarder dans "ResultEncrypt.pdf"*/
  const json = AsposePdfModule.AsposePdfEncrypt(pdf_file, "user", "owner", AsposePdfModule.Permissions.PrintDocument, AsposePdfModule.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
  console.log("AsposePdfEncrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```