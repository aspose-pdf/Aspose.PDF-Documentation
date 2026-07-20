---
title: Modifier le mot de passe d'un fichier PDF dans Node.js
linktitle: Modifier le mot de passe
type: docs
weight: 50
url: /fr/nodejs-cpp/change-password-pdf/
description: Modifier le mot de passe d'un fichier PDF avec Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Modifier le mot de passe d'un fichier PDF

Dans le cas où vous souhaitez modifier le mot de passe d'un PDF, vous pouvez utiliser [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/) fonction. Elle modifie le mot de passe utilisateur et le mot de passe propriétaire par le mot de passe propriétaire, tout en conservant les paramètres de sécurité d'origine.
Si vous souhaitez changer le mot de passe d'un fichier PDF de "owner" à "newowner" ou "newuser", essayez le fragment de code suivant :

**CommonJS:**

1. Appel `require` et importer `asposepdfnodejs` module comme `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF dont le mot de passe sera modifié.
1. Appel `AsposePdf` en tant que Promise et exécuter l'opération de changement de mot de passe. Recevoir l'objet en cas de succès.
1. Appeler la fonction [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/).
1. Modifier le mot de passe. Le mot de passe propriétaire existant est défini sur "owner," et il est changé en "newowner" avec le nouveau mot de passe utilisateur "newuser".
1. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfChangePassword.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Change passwords of the PDF-file from "owner" to "newowner" and save the "ResultPdfChangePassword.pdf"*/
      const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
      console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

Veuillez noter que si le mot de passe est une chaîne vide :

1. Si le mot de passe de l'utilisateur est vide, le PDF s'ouvre sans demander de mot de passe (mais il reste chiffré).
1. Si le mot de passe du propriétaire est vide, le PDF s'ouvre avec une demande de mot de passe utilisateur.
1. Si les deux sont vides  - le PDF s'ouvre sans demander de mot de passe (mais il reste chiffré).


**ECMAScript/ES6 :**

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF dont le mot de passe sera modifié.
1. Initialisez le module AsposePdf. Recevez l'objet si l'opération réussit.
1. Appeler la fonction [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/).
1. Modifier le mot de passe. Le mot de passe propriétaire existant est défini sur "owner," et il est changé en "newowner" avec le nouveau mot de passe utilisateur "newuser".
1. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfChangePassword.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /*Change passwords of the PDF-file from "owner" to "newowner" and save the "ResultPdfChangePassword.pdf"*/
  const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
  console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```