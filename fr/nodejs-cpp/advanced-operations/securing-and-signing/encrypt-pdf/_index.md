---
title:  Chiffrer PDF dans Node.js
linktitle: Chiffrer le fichier PDF
type: docs
weight: 50
url: /fr/nodejs-cpp/encrypt-pdf/
description: Chiffrer le fichier PDF avec Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Chiffrer le fichier PDF en utilisant en utilisant le mot de passe Utilisateur ou Propriétaire

Si vous envoyez un courriel à quelqu’un avec une pièce jointe PDF contenant des informations confidentielles  vous pourriez souhaiter ajouter une sécurité au préalable afin d’empêcher qu’elle tombe entre de mauvaises mains. La meilleure façon de limiter l’accès non autorisé à un document PDF est de le protéger avec un mot de passe. Pour chiffrer facilement et en toute sécurité les documents, vous pouvez utiliser Aspose.PDF for Node.js via C++.

>Veuillez spécifier des mots de passe utilisateur et propriétaire différents lors du chiffrement du fichier PDF.

- Le **mot de passe utilisateur**, s'il est défini, est ce que vous devez fournir pour ouvrir un PDF. Acrobat/Reader invite l'utilisateur à entrer le mot de passe utilisateur. Si ce n’est pas correct, le document ne s'ouvrira pas.
- Le **mot de passe propriétaire**, s'il est défini, contrôle les autorisations, telles que l'impression, la modification, l'extraction, les commentaires, etc. Acrobat/Reader interdira ces actions en fonction des paramètres d'autorisation. Acrobat exigera ce mot de passe si vous voulez définir/modifier les autorisations.

Dans le cas où vous souhaitez chiffrer un fichier PDF, vous pouvez utiliser [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/) fonction. 
Si vous voulez chiffrer un fichier PDF, essayez le fragment de code suivant :

**CommonJS :**

1. Appel `require` et importer `asposepdfnodejs` module en tant que `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF qui sera chiffré.
1. Appel `AsposePdf` en tant que Promise et effectuez l'opération de chiffrement du fichier. Recevez l'objet en cas de succès.
1. Appelez le [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/) fonction. 
1. Chiffrez le fichier PDF avec les mots de passe “user” et “owner”.
1. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultEncrypt.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Encrypt a PDF-file with passwords "user" and "owner", and save the "ResultEncrypt.pdf"*/
      const json = AsposePdfModule.AsposePdfEncrypt(pdf_file, "user", "owner", AsposePdfModule.Permissions.PrintDocument, AsposePdfModule.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
      console.log("AsposePdfEncrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

Il y a différents [autorisations de chiffrement](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#acbb404dc8d3b328891faa5fba341ce0c):

- Module.Permissions.PrintDocument
- Module.Permissions.ModifyContent
- Module.Permissions.ExtraireContenu
- Module.Permissions.ModifierAnnotationsDeTexte
- Module.Permissions.RemplirFormulaire
- Module.Permissions.ExtraireContenuAvecDesHandicaps
- Module.Permissions.AssemblerDocument
- Module.Permissions.QualitéImpression

Il existe plusieurs [algorithmes de chiffrement](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#ae15d4d8afe86aae14972a6e493d19f66):

- Module.CryptoAlgorithm.RC4x40
- Module.CryptoAlgorithm.RC4x128
- Module.CryptoAlgorithm.AESx128
- Module.CryptoAlgorithm.AESx256

**ECMAScript/ES6:**

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF dont le chiffrement sera modifié.
1. Initialisez le module AsposePdf. Recevez l'objet en cas de succès.
1. Appelez le [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/) fonction. 
1. Déchiffrez le fichier PDF avec les mots de passe "user" et "owner".
1. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultEncrypt.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Encrypt a PDF-file with passwords "user" and "owner", and save the "ResultEncrypt.pdf"*/
  const json = AsposePdfModule.AsposePdfEncrypt(pdf_file, "user", "owner", AsposePdfModule.Permissions.PrintDocument, AsposePdfModule.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
  console.log("AsposePdfEncrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```