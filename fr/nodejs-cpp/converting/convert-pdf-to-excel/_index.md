---
title: Convertir PDF en Excel dans Node.js
linktitle: Convertir PDF en Excel
type: docs
weight: 20
url: /fr/nodejs-cpp/convert-pdf-to-xlsx/
lastmod: "2026-07-18"
description: Aspose.PDF for Node.js vous permet de convertir un PDF au format XLSX.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Créer des feuilles de calcul à partir de PDF en utilisant Node.js 

**Aspose.PDF for Node.js via C++** prend en charge la fonction de conversion des fichiers PDF en fichier Excel.

{{% alert color="success" %}}
**Essayez de convertir le PDF en Excel en ligne**

Aspose.PDF for Node.js vous propose une application en ligne gratuite ["PDF en XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), où vous pouvez essayer d'examiner la fonctionnalité et la qualité avec lesquelles il fonctionne.

[![Aspose.PDF Conversion PDF en Excel avec l'application gratuite](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## Convertir PDF en XLSX

Dans le cas où vous souhaitez convertir un document PDF, vous pouvez utiliser [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/) fonction. 
Veuillez vérifier le fragment de code suivant afin de convertir dans un environnement Node.js.

**CommonJS:**

1. Appel `require` et importer `asposepdfnodejs` module comme `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Appel `AsposePdf` en tant que Promise et effectuer l'opération de conversion du fichier. Recevoir l'objet si succès.
1. Appelez la fonction [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/).
1. Convertissez le fichier PDF. Ainsi, si ‘json.errorCode’ vaut 0, le résultat de l'opération est enregistré dans “ResultPDFtoXlsX.xlsx”. Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans ‘json.errorText’.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to XlsX and save the "ResultPDFtoXlsX.xlsx"*/
      const json = AsposePdfModule.AsposePdfToXlsX(pdf_file, "ResultPDFtoXlsX.xlsx");
      console.log("AsposePdfToXlsX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Initialisez le module AsposePdf. Recevez l'objet si la création réussit.
1. Appelez la fonction [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/).
1. Convertissez le fichier PDF. Ainsi, si ‘json.errorCode’ vaut 0, le résultat de l'opération est enregistré dans “ResultPDFtoXlsX.xlsx”. Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans ‘json.errorText’.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to XlsX and save the "ResultPDFtoXlsX.xlsx"*/
  const json = AsposePdfModule.AsposePdfToXlsX(pdf_file, "ResultPDFtoXlsX.xlsx");
  console.log("AsposePdfToXlsX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

