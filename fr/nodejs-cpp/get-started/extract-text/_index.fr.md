---
title: Extraire du Texte à partir d'un PDF en Node.js
linktitle: Extraire du Texte à partir d'un PDF
type: docs
weight: 10
url: /nodejs-cpp/extract-text/
description: Cette section décrit comment extraire du texte d'un document PDF en utilisant Aspose.PDF pour Node.js via l'outil C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraire du Texte de toutes les Pages d'un Document PDF

Extraire du texte d'un PDF n'est pas facile. Seuls quelques lecteurs PDF peuvent extraire du texte à partir d'images PDF ou de PDF scannés. Mais l'outil **Aspose.PDF pour Node.js via C++** vous permet d'extraire facilement du texte de tous les fichiers PDF dans l'environnement Node.js.

Ce code démontre comment utiliser le module AsposePDFforNode.js pour extraire du texte d'un fichier PDF spécifié et enregistrer soit le texte extrait soit les erreurs rencontrées.

Consultez les extraits de code et suivez les étapes pour extraire du texte de votre PDF :

**CommonJS :**

1. Appelez `require` et importez le module `asposepdfnodejs` en tant que variable `AsposePdf`.

1. Spécifiez le nom du fichier PDF à partir duquel le texte sera extrait.
1. Appelez `AsposePdf` comme une Promesse et effectuez l'opération d'extraction de texte. Recevez l'objet en cas de succès.
1. Appelez la fonction [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. Le texte extrait est stocké dans l'objet JSON. Ainsi, si 'json.errorCode' est 0, le texte extrait est affiché en utilisant console.log. Si le paramètre json.errorCode n'est pas 0 et qu'une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Extraire le texte d'un fichier PDF*/
      const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
      console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importez le module `asposepdfnodejs`.

1. Spécifiez le nom du fichier PDF à partir duquel le texte sera extrait.
1. Initialisez le module AsposePdf. Recevez l'objet en cas de succès.
1. Appelez la fonction [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. Le texte extrait est stocké dans l'objet JSON. Ainsi, si 'json.errorCode' est 0, le texte extrait est affiché en utilisant console.log. Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Extraire le texte d'un fichier PDF*/
  const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
  console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
```