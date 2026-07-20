---
title: Convertir le PDF en documents Word dans Node.js
linktitle: Convertir le PDF en Word
type: docs
weight: 10
url: /fr/nodejs-cpp/convert-pdf-to-doc/
lastmod: "2026-07-18"
description: Apprenez comment convertir le PDF en DOC(DOCX) dans l'environnement Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Pour modifier le contenu d'un fichier PDF dans Microsoft Word ou d'autres traitements de texte qui prennent en charge les formats DOC et DOCX. Les fichiers PDF sont éditables, mais les fichiers DOC et DOCX sont plus souples et personnalisables.

{{% alert color="success" %}}
**Essayez de convertir PDF en DOC en ligne**

Aspose.PDF for Node.js vous propose une application en ligne gratuite ["PDF en DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), où vous pouvez essayer d'examiner la fonctionnalité et la qualité avec lesquelles il fonctionne.

[![Convertir PDF en DOC](/pdf/fr/nodejs-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Convertir PDF en DOC

Dans le cas où vous souhaitez convertir un document PDF, vous pouvez utiliser [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/) fonction. 
Veuillez vérifier le fragment de code suivant afin de convertir dans un environnement Node.js.

**CommonJS:**

1. Appeler `require` et importer `asposepdfnodejs` module comme `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Appeler `AsposePdf` en tant que Promise et exécuter l'opération de conversion du fichier. Recevoir l'objet si succès.
1. Appelez la fonction [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/).
1. Convertir le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPDFtoDoc.doc". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to Doc and save the "ResultPDFtoDoc.doc"*/
      const json = AsposePdfModule.AsposePdfToDoc(pdf_file, "ResultPDFtoDoc.doc");
      console.log("AsposePdfToDoc => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF qui sera converti
1. Initialisez le module AsposePdf. Recevez l'objet si l'opération réussit.
1. Appelez la fonction [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/).
1. Convertir le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPDFtoDoc.doc". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to Doc and save the "ResultPDFtoDoc.doc"*/
  const json = AsposePdfModule.AsposePdfToDoc(pdf_file, "ResultPDFtoDoc.doc");
  console.log("AsposePdfToDoc => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="warning" %}}
**Essayez de convertir PDF en DOCX en ligne**

Aspose.PDF for Node.js vous propose une application en ligne gratuite ["PDF en Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), où vous pouvez essayer d'examiner la fonctionnalité et la qualité avec lesquelles il fonctionne.

[![Aspose.PDF Conversion PDF en Word Application gratuite](/pdf/fr/nodejs-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Convertir PDF en DOCX

Aspose.PDF for Node.js via C++ toolkit vous permet de lire et de convertir des documents PDF en DOCX. DOCX est un format bien connu pour les documents Microsoft Word dont la structure est passée du binaire simple à une combinaison de fichiers XML et binaires. Les fichiers Docx peuvent être ouverts avec Word 2007 et les versions ultérieures, mais pas avec les versions antérieures de MS Word qui prennent en charge les extensions de fichiers DOC.

Dans le cas où vous souhaitez convertir un document PDF, vous pouvez utiliser [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/) fonction. 
Veuillez vérifier le fragment de code suivant afin de convertir dans un environnement Node.js.

**CommonJS:**

1. Appeler `require` et importer `asposepdfnodejs` module comme `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Appeler `AsposePdf` en tant que Promise et exécuter l'opération de conversion du fichier. Recevoir l'objet si succès.
1. Appelez la fonction [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/).
1. Convertir le fichier PDF. Ainsi, si 'json.errorCode' vaut 0, le résultat de l'opération est enregistré dans "ResultPDFtoDocX.docx". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to DocX and save the "ResultPDFtoDocX.docx"*/
      const json = AsposePdfModule.AsposePdfToDocX(pdf_file, "ResultPDFtoDocX.docx");
      console.log("AsposePdfToDocX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF qui sera converti
1. Initialisez le module AsposePdf. Recevez l'objet si l'opération réussit.
1. Appelez la fonction [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/).
1. Convertir le fichier PDF. Ainsi, si 'json.errorCode' vaut 0, le résultat de l'opération est enregistré dans "ResultPDFtoDocX.docx". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to DocX and save the "ResultPDFtoDocX.docx"*/
  const json = AsposePdfModule.AsposePdfToDocX(pdf_file, "ResultPDFtoDocX.docx");
  console.log("AsposePdfToDocX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```


