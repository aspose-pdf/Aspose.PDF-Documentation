---
title: Diviser un PDF dans Node.js
linktitle: Diviser des fichiers PDF
type: docs
weight: 30
url: /fr/nodejs-cpp/split-pdf/
description: Ce sujet montre comment diviser les pages PDF en fichiers PDF individuels avec Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Diviser le PDF en deux fichiers en utilisant Node.js

Au cas où vous voudriez diviser un PDF unique en parties, vous pouvez utiliser [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/) fonction. 
Veuillez vérifier le fragment de code suivant afin de diviser deux PDF dans un environnement Node.js.

**CommonJS:**

1. Appel `require` et importer `asposepdfnodejs` module en tant que `AsposePdf` variable.
1. Spécifiez le nom des fichiers PDF qui seront divisés.
1. Appel `AsposePdf` en tant que Promise et exécuter l'opération de division du fichier. Recevoir l'objet en cas de succès.
1. Appeler la fonction [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/).
1. Diviser deux fichiers PDF. Il définit la variable pageToSplit à 1, indiquant que le fichier PDF sera divisé à la page 1. 
1. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultSplit1.pdf" et "ResultSplit2.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Set number a page to split*/
      const pageToSplit = 1;
      /*Split to two PDF-files and save the "ResultSplit1.pdf", "ResultSplit2.pdf"*/
      const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
      console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
  });
```

**ECMAScript/ES6 :**

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom des fichiers PDF qui seront divisés.
1. Initialisez le module AsposePdf. Recevez l'objet si l'opération réussit.
1. Appeler la fonction [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/).
1. Diviser deux fichiers PDF. Il définit la variable pageToSplit à 1, indiquant que le fichier PDF sera divisé à la page 1. 
1. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultSplit1.pdf" et "ResultSplit2.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Set number a page to split*/
  const pageToSplit = 1;
  /*Split to two PDF-files and save the "ResultSplit1.pdf", "ResultSplit2.pdf"*/
  const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
  console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
```