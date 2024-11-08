---
title: Convertir des fichiers PDF en documents Word dans Node.js
linktitle: Convertir PDF en Word
type: docs
weight: 10
url: /fr/nodejs-cpp/convert-pdf-to-doc/
lastmod: "2023-11-16"
description: Apprenez à convertir des PDF en DOC(DOCX) dans l'environnement Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Pour éditer le contenu d'un fichier PDF dans Microsoft Word ou d'autres traitements de texte qui supportent les formats DOC et DOCX. Les fichiers PDF sont modifiables, mais les fichiers DOC et DOCX sont plus flexibles et personnalisables.

{{% alert color="success" %}}
**Essayez de convertir un PDF en DOC en ligne**

Aspose.PDF pour Node.js vous propose une application en ligne gratuite ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), où vous pouvez essayer de vérifier la fonctionnalité et la qualité avec lesquelles elle fonctionne.

[![Convertir PDF en DOC](/pdf/fr/nodejs-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Convertir PDF en DOC

Dans le cas où vous souhaitez convertir un document PDF, vous pouvez utiliser la fonction [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/).
 
Veuillez vérifier l'extrait de code suivant pour le convertir dans un environnement Node.js.

**CommonJS :**

1. Appelez `require` et importez le module `asposepdfnodejs` en tant que variable `AsposePdf`.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Appelez `AsposePdf` comme Promise et effectuez l'opération pour convertir le fichier. Recevez l'objet en cas de succès.
1. Appelez la fonction [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/).
1. Convertissez le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPDFtoDoc.doc". Si le paramètre json.errorCode n'est pas 0 et qu'une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convertir un fichier PDF en Doc et enregistrer le "ResultPDFtoDoc.doc"*/
      const json = AsposePdfModule.AsposePdfToDoc(pdf_file, "ResultPDFtoDoc.doc");
      console.log("AsposePdfToDoc => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importez le module `asposepdfnodejs`.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Initialisez le module AsposePdf. Recevez l'objet si réussi.
1. Appelez la fonction [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/).
1. Convertissez le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPDFtoDoc.doc". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convertir un fichier PDF en Doc et enregistrer le "ResultPDFtoDoc.doc"*/
  const json = AsposePdfModule.AsposePdfToDoc(pdf_file, "ResultPDFtoDoc.doc");
  console.log("AsposePdfToDoc => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="warning" %}}
**Essayez de convertir PDF en DOCX en ligne**

Aspose.PDF pour Node.js vous présente l'application en ligne gratuite ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF to Word Free App](/pdf/fr/nodejs-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Convertir PDF en DOCX

Aspose.PDF pour Node.js via l'outil C++ vous permet de lire et de convertir des documents PDF en DOCX. DOCX est un format bien connu pour les documents Microsoft Word dont la structure a été modifiée d'un binaire simple à une combinaison de fichiers XML et binaires. Les fichiers Docx peuvent être ouverts avec Word 2007 et les versions ultérieures mais pas avec les versions antérieures de MS Word qui prennent en charge les extensions de fichiers DOC.

Si vous souhaitez convertir un document PDF, vous pouvez utiliser la fonction [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/). 
Veuillez consulter l'extrait de code suivant afin de convertir dans l'environnement Node.js.

**CommonJS :**

1. Appelez `require` et importez le module `asposepdfnodejs` en tant que variable `AsposePdf`.
1. Spécifiez le nom du fichier PDF qui sera converti.

1. Appelez `AsposePdf` en tant que Promise et effectuez l'opération de conversion de fichier. Recevez l'objet si réussi.
1. Appelez la fonction [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/).
1. Convertissez le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPDFtoDocX.docx". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convertir un fichier PDF en DocX et enregistrer le "ResultPDFtoDocX.docx"*/
      const json = AsposePdfModule.AsposePdfToDocX(pdf_file, "ResultPDFtoDocX.docx");
      console.log("AsposePdfToDocX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importez le module `asposepdfnodejs`.
1. Spécifiez le nom du fichier PDF qui sera converti.

1. Initialiser le module AsposePdf. Recevez l'objet si réussi.
1. Appelez la fonction [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/).
1. Convertir le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPDFtoDocX.docx". Si le paramètre json.errorCode n'est pas 0 et qu'une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convertir un fichier PDF en DocX et enregistrer le "ResultPDFtoDocX.docx"*/
  const json = AsposePdfModule.AsposePdfToDocX(pdf_file, "ResultPDFtoDocX.docx");
  console.log("AsposePdfToDocX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```