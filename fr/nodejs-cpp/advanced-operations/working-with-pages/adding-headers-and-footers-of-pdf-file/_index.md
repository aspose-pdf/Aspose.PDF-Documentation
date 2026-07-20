---
title: Ajouter un en-tête et un pied de page au PDF dans Node.js
linktitle: Ajouter un en-tête et un pied de page au PDF
type: docs
weight: 70
url: /fr/nodejs-cpp/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for Node.js via C++ vous permet d'ajouter des en-têtes et des pieds de page à votre fichier PDF en utilisant AsposePdfAddTextHeaderFooter.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF for Node.js via C++** vous permet d'ajouter un en-tête et un pied de page dans votre fichier PDF existant. 

Dans le cas où vous souhaitez ajouter un en-tête et un pied de page, vous pouvez utiliser [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/) fonction. 

Veuillez vérifier le fragment de code suivant afin d'ajouter un en‑tête et un pied de page à un fichier PDF dans un environnement Node.js.

**CommonJS:**

1. Appeler `require` et importer `asposepdfnodejs` module comme `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF dans lequel l'en‑tête et le pied de page seront ajoutés.
1. Appeler `AsposePdf` en tant que Promise et effectuer l'opération d'ajout d'en-tête et de pied de page. Recevoir l'objet si succès.
1. Appeler la fonction [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/).
1. Ajoutez du texte dans l'en-tête et le pied de page d'un fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultAddHeaderFooter.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Add text in Header/Footer of a PDF-file and save the "ResultAddHeaderFooter.pdf"*/
      const json = AsposePdfModule.AsposePdfAddTextHeaderFooter(pdf_file, "Aspose.PDF for Node.js via C++ via C++", "ASPOSE", "ResultAddHeaderFooter.pdf");
      console.log("AsposePdfAddTextHeaderFooter => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6 :**

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF dans lequel l'en‑tête et le pied de page seront ajoutés.
1. Initialisez le module AsposePdf. Recevez l'objet si l'opération réussit.
1. Appeler la fonction [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/).
1. Ajoutez du texte dans l'en-tête et le pied de page d'un fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultAddHeaderFooter.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Add text in Header/Footer of a PDF-file and save the "ResultAddHeaderFooter.pdf"*/
  const json = AsposePdfModule.AsposePdfAddTextHeaderFooter(pdf_file, "Aspose.PDF for Node.js via C++ via C++", "ASPOSE", "ResultAddHeaderFooter.pdf");
  console.log("AsposePdfAddTextHeaderFooter => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```