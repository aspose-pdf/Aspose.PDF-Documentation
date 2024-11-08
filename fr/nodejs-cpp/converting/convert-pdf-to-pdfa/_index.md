---
title: Convertir des PDF aux formats PDF/A dans Node.js
linktitle: Convertir des PDF aux formats PDF/A
type: docs
weight: 100
url: /fr/nodejs-cpp/convert-pdf-to-pdfa/
lastmod: "2023-11-16"
description: Ce sujet vous montre comment Aspose.PDF permet de convertir un fichier PDF en un fichier PDF conforme à la norme PDF/A dans l'environnement Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF pour Node.js** vous permet de convertir un fichier PDF en un fichier PDF conforme à la norme <abbr title="Format de Document Portable pour l'Archivage de documents électroniques">PDF/A</abbr>.

{{% alert color="success" %}}
**Essayez de convertir un PDF en PDF/A en ligne**

Aspose.PDF pour Node.js vous présente une application en ligne gratuite ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Conversion Aspose.PDF de PDF en PDF/A avec une application gratuite](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}


## Convertir un PDF au format PDF/A

Si vous souhaitez convertir un document PDF, vous pouvez utiliser la fonction [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/).
 
Veuillez vérifier l'extrait de code suivant afin de le convertir dans l'environnement Node.js.

**CommonJS :**

1. Appelez `require` et importez le module `asposepdfnodejs` en tant que variable `AsposePdf`.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Appelez `AsposePdf` en tant que Promise et effectuez l'opération de conversion du fichier. Recevez l'objet si réussi.
1. Appelez la fonction [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/).
1. Réparez le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultConvertToPDFA.pdf". Pendant le processus de conversion, une validation est effectuée, et les résultats de la validation sont enregistrés sous "ResultConvertToPDFALog.xml". Si le paramètre json.errorCode n'est pas 0 et qu'une erreur apparaît dans votre fichier en conséquence, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convertir un fichier PDF en PDF/A(1A) et enregistrer le "ResultConvertToPDFA.pdf"*/
      /*Pendant le processus de conversion, la validation est également effectuée, "ResultConvertToPDFA.xml"*/
      const json = AsposePdfModule.AsposePdfConvertToPDFA(pdf_file, AsposePdfModule.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFALog.xml");
      console.log("AsposePdfConvertToPDFA => %O", json.errorCode == 0 ? [json.fileNameResult, json.fileNameLogResult] : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importez le module `asposepdfnodejs`.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Initialisez le module AsposePdf. Recevez l'objet en cas de succès.
1. Appelez la fonction [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/).
1. Réparez le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultConvertToPDFA.pdf". Pendant le processus de conversion, une validation est effectuée, et les résultats de la validation sont enregistrés sous "ResultConvertToPDFALog.xml." Si le paramètre json.errorCode n'est pas 0 et, en conséquence, qu'une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convertir un fichier PDF en PDF/A(1A) et enregistrer le "ResultConvertToPDFA.pdf"*/
  /*Pendant le processus de conversion, la validation est également effectuée, "ResultConvertToPDFA.xml"*/
  const json = AsposePdfModule.AsposePdfConvertToPDFA(pdf_file, AsposePdfModule.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFALog.xml");
  console.log("AsposePdfConvertToPDFA => %O", json.errorCode == 0 ? [json.fileNameResult, json.fileNameLogResult] : json.errorText);
```