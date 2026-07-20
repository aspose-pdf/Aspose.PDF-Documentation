---
title: Convertir PDF/A au format PDF dans Node.js
linktitle: Convertir PDF/A au format PDF
type: docs
weight: 110
url: /fr/nodejs-cpp/convert-pdfa-to-pdf/
lastmod: "2026-07-18"
description: Ce sujet vous montre comment Aspose.PDF permet de convertir un fichier PDF/A en document PDF dans l'environnement Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Convertir PDF/A au format PDF

Dans le cas où vous souhaitez convertir un document PDF, vous pouvez utiliser [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/) fonction. 
Veuillez vérifier le fragment de code suivant afin de convertir dans un environnement Node.js.

**CommonJS:**

1. Appel `require` et importer `asposepdfnodejs` module en tant que `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Appel `AsposePdf` en tant que Promise et exécuter l'opération de conversion du fichier. Recevoir l'objet si succès.
1. Appelez la fonction [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/).
1. Convertir le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultConvertToPDF.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_PDFA_file = 'ResultConvertToPDFA.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF/A-file to PDF and save the "ResultConvertToPDF.pdf"*/
      const json = AsposePdfModule.AsposePdfAConvertToPDF(pdf_PDFA_file, "ResultConvertToPDF.pdf");
      console.log("AsposePdfAConvertToPDF => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF/A qui sera converti
1. Initialisez le module AsposePdf. Recevez l'objet en cas de succès.
1. Appelez la fonction [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/).
1. Convertir le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultConvertToPDF.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_PDFA_file = 'ResultConvertToPDFA.pdf';
  /*Convert a PDF/A-file to PDF and save the "ResultConvertToPDF.pdf"*/
  const json = AsposePdfModule.AsposePdfAConvertToPDF(pdf_PDFA_file, "ResultConvertToPDF.pdf");
  console.log("AsposePdfAConvertToPDF => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```