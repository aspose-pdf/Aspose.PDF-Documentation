---
title: Extraire des tableaux d'un PDF en Node.js
linktitle: Extraire des tableaux d'un PDF
type: docs
weight: 10
url: /fr/nodejs-cpp/extract-tables-from-the-pdf-file/
description: Comment convertir un PDF en CSV en utilisant Aspose.PDF pour Node.js via l'outil C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraire des tableaux lors de la conversion de PDF en fichiers CSV

### Convertir PDF en CSV

S'il y a des tableaux dans le PDF, ils sont enregistrés dans des fichiers CSV séparés. Si vous souhaitez convertir un document PDF, vous pouvez utiliser la fonction [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/). Veuillez consulter l'extrait de code suivant afin de convertir un fichier PDF dans l'environnement Node.js.

**CommonJS :**

1. Appelez `require` et importez le module `asposepdfnodejs` en tant que variable `AsposePdf`.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Appelez `AsposePdf` comme Promise et effectuez l'opération de conversion du fichier. Recevez l'objet en cas de succès.

1. Appelez la fonction [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/).
1. Convertissez le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPDFtoXlsX.xlsx". Si le paramètre json.errorCode n'est pas 0 et qu'une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convertir un fichier PDF en CSV (extraire les tableaux) avec le modèle "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... format numéro de page), TAB comme délimiteur et enregistrer*/
      const json = AsposePdfModule.AsposePdfTablesToCSV(pdf_file, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
      console.log("AsposePdfTablesToCSV => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6 :**

1. Importez le module `asposepdfnodejs`.

1. Spécifiez le nom du fichier PDF qui sera converti.
1. Initialisez le module AsposePdf. Recevez l'objet en cas de succès.
1. Appelez la fonction [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/).
1. Convertissez le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPDFtoXlsX.xlsx". Si le paramètre json.errorCode n'est pas 0 et, par conséquent, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convertir un fichier PDF en CSV (extraire les tableaux) avec le modèle "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... format numéro de page), TAB comme délimiteur et enregistrer*/
  const json = AsposePdfModule.AsposePdfTablesToCSV(pdf_file, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
  console.log("AsposePdfTablesToCSV => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```