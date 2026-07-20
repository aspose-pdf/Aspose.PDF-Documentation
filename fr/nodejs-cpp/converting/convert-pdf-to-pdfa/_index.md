---
title: Convertir le PDF en formats PDF/A dans Node.js
linktitle: Convertir le PDF en formats PDF/A
type: docs
weight: 100
url: /fr/nodejs-cpp/convert-pdf-to-pdfa/
lastmod: "2026-07-18"
description: Ce sujet vous montre comment Aspose.PDF permet de convertir un fichier PDF en un fichier PDF conforme à PDF/A dans l'environnement Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for Node.js** vous permet de convertir un fichier PDF en un <abbr title="Portable Document Format for Archiving of electronic documents">PDF/A</abbr> fichier PDF conforme. 

{{% alert color="success" %}}
**Essayez de convertir le PDF en PDF/A en ligne**

Aspose.PDF for Node.js vous présente une application en ligne gratuite ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF vers PDF/A avec Application gratuite](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}


## Convertir le PDF au format PDF/A

Dans le cas où vous souhaitez convertir un document PDF, vous pouvez utiliser [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/) fonction. 
Veuillez consulter l'extrait de code suivant afin de convertir dans un environnement Node.js.

**CommonJS:**

1. Appeler `require` et importer `asposepdfnodejs` module comme `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Appeler `AsposePdf` comme Promise et effectuer l'opération de conversion de fichier. Recevoir l'objet si succès.
1. Appelez la fonction [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/).
1. Réparez le fichier PDF. Ainsi, si ‘json.errorCode’ est 0, le résultat de l'opération est enregistré dans "ResultConvertToPDFA.pdf". Au cours du processus de conversion, une validation est effectuée, et les résultats de la validation sont enregistrés sous "ResultConvertToPDFALog.xml." Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans ‘json.errorText’.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to PDF/A(1A) and save the "ResultConvertToPDFA.pdf"*/
      /*During conversion process, the validation is also performed, "ResultConvertToPDFA.xml"*/
      const json = AsposePdfModule.AsposePdfConvertToPDFA(pdf_file, AsposePdfModule.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFALog.xml");
      console.log("AsposePdfConvertToPDFA => %O", json.errorCode == 0 ? [json.fileNameResult, json.fileNameLogResult] : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Initialisez le module AsposePdf. Recevez l'objet en cas de succès.
1. Appelez la fonction [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/).
1. Réparez le fichier PDF. Ainsi, si ‘json.errorCode’ est 0, le résultat de l'opération est enregistré dans "ResultConvertToPDFA.pdf". Au cours du processus de conversion, une validation est effectuée, et les résultats de la validation sont enregistrés sous "ResultConvertToPDFALog.xml." Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans ‘json.errorText’.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to PDF/A(1A) and save the "ResultConvertToPDFA.pdf"*/
  /*During conversion process, the validation is also performed, "ResultConvertToPDFA.xml"*/
  const json = AsposePdfModule.AsposePdfConvertToPDFA(pdf_file, AsposePdfModule.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFALog.xml");
  console.log("AsposePdfConvertToPDFA => %O", json.errorCode == 0 ? [json.fileNameResult, json.fileNameLogResult] : json.errorText);
```





