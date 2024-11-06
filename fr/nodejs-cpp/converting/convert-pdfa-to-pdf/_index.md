---
title: Convertir PDF/A en format PDF dans Node.js
linktitle: Convertir PDF/A en format PDF
type: docs
weight: 110
url: fr/nodejs-cpp/convert-pdfa-to-pdf/
lastmod: "2023-11-16"
description: Ce sujet vous montre comment Aspose.PDF permet de convertir un fichier PDF/A en document PDF dans l'environnement Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Convertir PDF/A en format PDF

Si vous souhaitez convertir un document PDF, vous pouvez utiliser la fonction [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/). 
Veuillez vérifier l'extrait de code suivant afin de convertir dans l'environnement Node.js.

**CommonJS :**

1. Appelez `require` et importez le module `asposepdfnodejs` en tant que variable `AsposePdf`.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Appelez `AsposePdf` en tant que Promise et effectuez l'opération pour convertir le fichier. Recevez l'objet si c'est réussi.

1. Appelez la fonction [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/).
1. Convertir le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultConvertToPDF.pdf". Si le paramètre json.errorCode n'est pas 0 et qu'une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_PDFA_file = 'ResultConvertToPDFA.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convertir un fichier PDF/A en PDF et enregistrer le "ResultConvertToPDF.pdf"*/
      const json = AsposePdfModule.AsposePdfAConvertToPDF(pdf_PDFA_file, "ResultConvertToPDF.pdf");
      console.log("AsposePdfAConvertToPDF => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6 :**

1. Importez le module `asposepdfnodejs`.
1. Spécifiez le nom du fichier PDF/A qui sera converti.

1. Initialiser le module AsposePdf. Recevez l'objet si réussi.
1. Appelez la fonction [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/).
1. Convertir le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultConvertToPDF.pdf". Si le paramètre json.errorCode n'est pas 0 et qu'une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js
  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_PDFA_file = 'ResultConvertToPDFA.pdf';
  /*Convertir un fichier PDF/A en PDF et enregistrer le "ResultConvertToPDF.pdf"*/
  const json = AsposePdfModule.AsposePdfAConvertToPDF(pdf_PDFA_file, "ResultConvertToPDF.pdf");
  console.log("AsposePdfAConvertToPDF => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```