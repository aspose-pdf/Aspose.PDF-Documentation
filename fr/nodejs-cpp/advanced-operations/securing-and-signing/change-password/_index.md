---
title: Changer le mot de passe d'un fichier PDF en Node.js
linktitle: Changer le mot de passe
type: docs
weight: 50
url: fr/nodejs-cpp/change-password-pdf/
description: Changer le mot de passe d'un fichier PDF avec Aspose.PDF pour Node.js via C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Changer le mot de passe d'un fichier PDF

Dans le cas où vous souhaitez changer le mot de passe d'un PDF, vous pouvez utiliser la fonction [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/). Elle change le mot de passe utilisateur et le mot de passe propriétaire par le mot de passe propriétaire, en conservant les paramètres de sécurité d'origine.
Si vous souhaitez changer le mot de passe d'un fichier PDF de "owner" à "newowner" ou "newuser", essayez le code suivant :

**CommonJS :**

1. Appelez `require` et importez le module `asposepdfnodejs` en tant que variable `AsposePdf`.
1. Spécifiez le nom du fichier PDF dont le mot de passe sera modifié.
1. Appelez `AsposePdf` en tant que Promise et effectuez l'opération de changement de mot de passe. Recevez l'objet si réussi.

1. Appelez la fonction [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/).
1. Changer le mot de passe. Le mot de passe propriétaire existant est défini sur "owner", et il est changé en "newowner" avec le nouveau mot de passe utilisateur "newuser".
1. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfChangePassword.pdf". Si le paramètre json.errorCode n'est pas 0 et, par conséquent, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Changer les mots de passe du fichier PDF de "owner" à "newowner" et enregistrer le "ResultPdfChangePassword.pdf"*/
      const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
      console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


Veuillez noter que si le mot de passe est une chaîne vide :

1. Si le mot de passe utilisateur est vide - le PDF s'ouvre sans demander de mot de passe (mais il est toujours chiffré).
1. Si le mot de passe du propriétaire est vide, le PDF s'ouvre avec une demande de mot de passe utilisateur.
1. Si les deux sont vides - le PDF s'ouvre sans demander de mot de passe (mais il est toujours chiffré).


**ECMAScript/ES6 :**

1. Importez le module `asposepdfnodejs`.
1. Spécifiez le nom du fichier PDF qui changera le mot de passe.
1. Initialisez le module AsposePdf. Recevez l'objet en cas de succès.
1. Appelez la fonction [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/).
1. Changez le mot de passe. Le mot de passe du propriétaire existant est défini sur "owner", et il est changé en "newowner" avec le nouveau mot de passe utilisateur "newuser".

1. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfChangePassword.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /*Changer les mots de passe du fichier PDF de "owner" à "newowner" et enregistrer "ResultPdfChangePassword.pdf"*/
  const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
  console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```