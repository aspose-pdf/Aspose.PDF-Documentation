---
title: Ajouter une numérotation de page au PDF dans Node.js
linktitle: Ajouter un numéro de page
type: docs
weight: 100
url: /fr/nodejs-cpp/add-page-number/
description: Aspose.PDF pour Node.js via C++ vous permet d'ajouter un tampon de numéro de page à votre fichier PDF en utilisant AsposePdfAddPageNum.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Le numéro de page facilite la localisation des différentes parties du document pour le lecteur. Les extraits de code suivants montrent comment ajouter des numéros de page aux pages PDF en utilisant la fonction [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/) dans Node.js.

Veuillez vérifier l'extrait de code suivant afin d'ajouter des numéros de page dans un environnement Node.js.

**CommonJS :**

1. Appelez `require` et importez le module `asposepdfnodejs` en tant que variable `AsposePdf`.
1. Spécifiez le nom du fichier PDF dans lequel les numéros de page seront ajoutés.
1. Appelez `AsposePdf` comme Promise et effectuez l'opération pour ajouter des numéros de page. Recevez l'objet si réussi.

1. Appelez la fonction [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/).
1. Ajoutez un numéro de page à un fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultAddPageNum.pdf". Si le paramètre json.errorCode n'est pas 0 et, par conséquent, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Ajoutez un numéro de page à un fichier PDF, enregistrez le "ResultAddPageNum.pdf"*/
      const json = AsposePdfModule.AsposePdfAddPageNum(pdf_file, "ResultAddPageNum.pdf");
      console.log("AsposePdfAddPageNum => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6 :**

1. Importez le module `asposepdfnodejs`.
1. Spécifiez le nom du fichier PDF dans lequel les numéros de page seront ajoutés.
1. Initialisez le module AsposePdf. Recevez l'objet en cas de succès.

1. Appelez la fonction [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/).
1. Ajoutez un numéro de page à un fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultAddPageNum.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Ajoutez un numéro de page à un fichier PDF et enregistrez le "ResultAddPageNum.pdf"*/
  const json = AsposePdfModule.AsposePdfAddPageNum(pdf_file, "ResultAddPageNum.pdf");
  console.log("AsposePdfAddPageNum => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```