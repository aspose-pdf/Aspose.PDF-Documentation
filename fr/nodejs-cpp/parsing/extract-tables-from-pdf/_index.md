---
title: Extraire les tables du PDF en Node.js
linktitle: Extraire les tables du PDF
type: docs
weight: 10
url: /fr/nodejs-cpp/extract-tables-from-the-pdf-file/
description: Comment convertir le PDF en CSV en utilisant Aspose.PDF for Node.js via la boîte à outils C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraire les tables lors de la conversion du PDF en fichiers CSV

### Convertir le PDF en CSV

S'il y a des tables dans le PDF, elles sont enregistrées dans des fichiers CSV distincts. Au cas où vous souhaitez convertir le document PDF, vous pouvez utiliser [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/) fonction. 
Veuillez vérifier le fragment de code suivant afin de convertir un fichier PDF dans un environnement Node.js.

**CommonJS:**

1. Appel `require` et importer `asposepdfnodejs` module comme `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Appel `AsposePdf` en tant que Promise et exécuter l'opération pour convertir le fichier. Recevoir l'objet en cas de succès.
1. Appelez la fonction [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/).
1. Convertissez le fichier PDF. Ainsi, si 'json.errorCode' vaut 0, le résultat de l'opération est enregistré dans "ResultPDFtoXlsX.xlsx". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to CSV (extract tables) with template "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... format page number), TAB as delimiter and save*/
      const json = AsposePdfModule.AsposePdfTablesToCSV(pdf_file, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
      console.log("AsposePdfTablesToCSV => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Initialisez le module AsposePdf. Recevez l'objet si l'opération réussit.
1. Appelez la fonction [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/).
1. Convertissez le fichier PDF. Ainsi, si 'json.errorCode' vaut 0, le résultat de l'opération est enregistré dans "ResultPDFtoXlsX.xlsx". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to CSV (extract tables) with template "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... format page number), TAB as delimiter and save*/
  const json = AsposePdfModule.AsposePdfTablesToCSV(pdf_file, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
  console.log("AsposePdfTablesToCSV => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```