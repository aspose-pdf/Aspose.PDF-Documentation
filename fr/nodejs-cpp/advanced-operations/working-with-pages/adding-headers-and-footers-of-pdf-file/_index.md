---
title: Ajouter En-tête et Pied de page au PDF dans Node.js
linktitle: Ajouter En-tête et Pied de page au PDF
type: docs
weight: 70
url: /fr/nodejs-cpp/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF pour Node.js via C++ vous permet d'ajouter des en-têtes et des pieds de page à votre fichier PDF en utilisant AsposePdfAddTextHeaderFooter.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF pour Node.js via C++** vous permet d'ajouter un en-tête et un pied de page dans votre fichier PDF existant.

Dans le cas où vous souhaitez ajouter un en-tête et un pied de page, vous pouvez utiliser la fonction [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/).

Veuillez consulter l'extrait de code suivant afin d'ajouter un en-tête et un pied de page à un fichier PDF dans l'environnement Node.js.

**CommonJS :**

1. Appelez `require` et importez le module `asposepdfnodejs` en tant que variable `AsposePdf`.
1. Spécifiez le nom du fichier PDF dans lequel l'en-tête et le pied de page seront ajoutés.

1. Appelez `AsposePdf` en tant que promesse et effectuez l'opération pour ajouter un en-tête et un pied de page. Recevez l'objet si réussi.
1. Appelez la fonction [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/).
1. Ajoutez du texte dans l'en-tête et le pied de page d'un fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultAddHeaderFooter.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Ajoutez du texte dans l'en-tête/le pied de page d'un fichier PDF et enregistrez le "ResultAddHeaderFooter.pdf"*/
      const json = AsposePdfModule.AsposePdfAddTextHeaderFooter(pdf_file, "Aspose.PDF pour Node.js via C++ via C++", "ASPOSE", "ResultAddHeaderFooter.pdf");
      console.log("AsposePdfAddTextHeaderFooter => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importez le module `asposepdfnodejs`.
1. Spécifiez le nom du fichier PDF dans lequel l'en-tête et le pied de page seront ajoutés.
1. Initialisez le module AsposePdf. Recevez l'objet si cela réussit.
1. Appelez la fonction [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/).
1. Ajoutez du texte dans l'en-tête et le pied de page d'un fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultAddHeaderFooter.pdf". Si le paramètre json.errorCode n'est pas 0 et, par conséquent, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Ajoutez du texte dans l'en-tête/pied de page d'un fichier PDF et enregistrez le "ResultAddHeaderFooter.pdf"*/
  const json = AsposePdfModule.AsposePdfAddTextHeaderFooter(pdf_file, "Aspose.PDF pour Node.js via C++ via C++", "ASPOSE", "ResultAddHeaderFooter.pdf");
  console.log("AsposePdfAddTextHeaderFooter => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```