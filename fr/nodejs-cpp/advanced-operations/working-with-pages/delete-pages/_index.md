---
title: Supprimer une page dans un PDF avec Node.js
linktitle: Supprimer les pages PDF
type: docs
weight: 30
url: /fr/nodejs-cpp/delete-pages/
description: Vous pouvez supprimer des pages de votre fichier PDF en utilisant Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Dans le cas où vous souhaitez supprimer des pages PDF, vous pouvez utiliser [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/) fonction. 

Une caractéristique de cette fonction est qu'elle peut accepter plusieurs types comme paramètre numPages :

- string : dans ce cas, nous pouvons indiquer un ensemble de pages en utilisant des pages particulières ou des intervalles. Par exemple, la chaîne "7, 20, 30-32, 34" signifie que nous voulons supprimer les pages 7, 20, de 30 à 32 et 34.
- array : dans ce cas, nous ne pouvons mentionner que des pages. Le tableau [3,7] signifie que nous voulons supprimer les pages 3 et 7.
- int : un seul numéro de page.

Veuillez vérifier le fragment de code suivant afin de supprimer des pages PDF dans un environnement Node.js.

**CommonJS:**

1. Appel `require` et importer `asposepdfnodejs` module comme `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF dont les pages seront supprimées.
1. Appel `AsposePdf` en tant que Promise et effectuez l'opération de suppression des pages. Recevez l'objet si l'opération réussit.
1. Appelez la fonction [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/). 
1. Supprime les pages spécifiques du fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultDeletePages.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*string, include number pages with interval: "7, 20, 22, 30-32, 33, 36-40, 46"*/
      /*const numPages = "1-3";*/
      /*array, array of number pages*/
      /*const numPages = [1,3];*/
      /*number, number page*/
      const numPages = 1;
      /*Delete pages from a PDF-file and save the "ResultDeletePages.pdf"*/
      const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
      console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6 :**

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF dont les pages seront supprimées.
1. Initialisez le module AsposePdf. Recevez l'objet si l'opération réussit.
1. Appelez la fonction [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/). Cette fonction permet de supprimer les pages spécifiées du fichier PDF. L'opération est déterminée par la variable numPages, qui peut être une chaîne contenant des intervalles de pages (par exemple "7, 20, 22, 30-32, 33, 36-40, 46"), un tableau de numéros de pages, ou un seul numéro de page.
1. Supprime les pages spécifiques du fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultDeletePages.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*string, include number pages with interval: "7, 20, 22, 30-32, 33, 36-40, 46"*/
  /*const numPages = "1-3";*/
  /*array, array of number pages*/
  /*const numPages = [1,3];*/
  /*number, number page*/
  const numPages = 1;
  /*Delete pages from a PDF-file and save the "ResultDeletePages.pdf"*/
  const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
  console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```