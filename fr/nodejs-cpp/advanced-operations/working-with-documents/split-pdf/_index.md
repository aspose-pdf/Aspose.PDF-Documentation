---
title: Diviser un PDF en Node.js
linktitle: Diviser des fichiers PDF
type: docs
weight: 30
url: /fr/nodejs-cpp/split-pdf/
description: Ce sujet montre comment diviser les pages PDF en fichiers PDF individuels avec Aspose.PDF pour Node.js via C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Diviser un PDF en deux fichiers en utilisant Node.js

Dans le cas où vous souhaitez diviser un seul PDF en parties, vous pouvez utiliser la fonction [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/). Veuillez vérifier l'extrait de code suivant afin de diviser deux PDF dans un environnement Node.js.

**CommonJS :**

1. Appelez `require` et importez le module `asposepdfnodejs` en tant que variable `AsposePdf`.
1. Spécifiez le nom des fichiers PDF qui seront divisés.
1. Appelez `AsposePdf` en tant que Promise et effectuez l'opération de division de fichier. Recevez l'objet en cas de succès.
1. Appelez la fonction [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/).

1. Diviser deux fichiers PDF. Cela définit la variable pageToSplit à 1, indiquant que le fichier PDF sera divisé à la page 1.  
1. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultSplit1.pdf" et "ResultSplit2.pdf". Si le paramètre json.errorCode n'est pas 0 et qu'une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Définir le nombre de pages à diviser*/
      const pageToSplit = 1;
      /*Diviser en deux fichiers PDF et enregistrer les "ResultSplit1.pdf", "ResultSplit2.pdf"*/
      const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
      console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importer le module `asposepdfnodejs`.

1. Spécifiez le nom des fichiers PDF qui seront divisés.
1. Initialisez le module AsposePdf. Recevez l'objet en cas de succès.
1. Appelez la fonction [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/).
1. Divisez deux fichiers PDF. Il définit la variable pageToSplit à 1, indiquant que le fichier PDF sera divisé à la page 1.
1. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultSplit1.pdf" et "ResultSplit2.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Définir le nombre de pages à diviser*/
  const pageToSplit = 1;
  /*Diviser en deux fichiers PDF et enregistrer "ResultSplit1.pdf", "ResultSplit2.pdf"*/
  const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
  console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
```