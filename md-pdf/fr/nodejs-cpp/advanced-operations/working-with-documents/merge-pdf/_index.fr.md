---
title: Comment Fusionner des PDF dans Node.js
linktitle: Fusionner des fichiers PDF
type: docs
weight: 20
url: /nodejs-cpp/merge-pdf/
description: Cette page explique comment fusionner des documents PDF en un seul fichier PDF avec Aspose.PDF pour Node.js via C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Fusionner ou combiner deux PDF en un seul PDF dans Node.js

La combinaison et la fusion de fichiers sont des tâches très populaires lors du travail avec un grand nombre de documents. Parfois, lors du travail avec des documents et des images, lorsqu'ils sont numérisés, traités et organisés, plusieurs fichiers sont créés. Mais que faire si vous avez besoin de tout stocker dans un seul fichier ? Ou ne voulez-vous pas imprimer plusieurs documents ? Concaténez deux fichiers PDF avec Aspose.PDF pour Node.js via C++.

Dans le cas où vous souhaitez fusionner deux PDFs, vous pouvez utiliser la fonction [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/). Veuillez consulter l'extrait de code suivant afin de fusionner deux fichiers PDFs dans l'environnement Node.js.

**CommonJS:**

1. Appelez `require` et importez le module `asposepdfnodejs` en tant que variable `AsposePdf`.
1. Spécifiez le nom des fichiers PDF qui seront fusionnés.
1. Appelez `AsposePdf` en tant que Promise et effectuez l'opération de fusion. Recevez l'objet en cas de succès.
1. Appelez la fonction [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/).
1. Fusionnez deux fichiers PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultMerge.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Fusionner deux fichiers PDF et enregistrer le "ResultMerge.pdf"*/
      const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
      console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importez le module `asposepdfnodejs`.
1. Spécifiez le nom des fichiers PDF qui seront fusionnés.
1. Initialisez le module AsposePdf. Recevez l'objet si réussi.
1. Appelez la fonction [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/).
1. Fusionnez deux fichiers PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultMerge.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Fusionner deux fichiers PDF et enregistrer le "ResultMerge.pdf"*/
  const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
  console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```