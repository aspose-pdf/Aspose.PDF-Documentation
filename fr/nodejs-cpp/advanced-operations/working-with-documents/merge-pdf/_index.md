---
title: Comment fusionner des PDF dans Node.js
linktitle: Fusionner des fichiers PDF
type: docs
weight: 20
url: /fr/nodejs-cpp/merge-pdf/
description: Cette page explique comment fusionner des documents PDF en un seul fichier PDF avec Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Fusionner ou combiner deux PDF en un seul PDF dans Node.js

Combiner et fusionner des fichiers est une tâche très courante lors du travail avec un grand nombre de documents. Parfois, lorsqu'on travaille avec des documents et des images, lorsqu'ils sont numérisés, traités et organisés, plusieurs fichiers sont créés.
Mais que faire si vous devez tout stocker dans un seul fichier ? Ou si vous ne voulez pas imprimer plusieurs documents ? Concaténez deux fichiers PDF avec Aspose.PDF for Node.js via C++.

Dans le cas où vous souhaitez fusionner deux PDF, vous pouvez utiliser [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/) fonction. 
Veuillez vérifier le snippet de code suivant afin de fusionner deux fichiers PDF dans un environnement Node.js.

**CommonJS :**

1. Appel `require` et importer `asposepdfnodejs` module en tant que `AsposePdf` variable.
1. Spécifiez le nom des fichiers PDF qui seront fusionnés.
1. Appel `AsposePdf` en tant que Promise et effectuez l'opération de fusion. Recevez l'objet si réussi.
1. Appelez la fonction [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/).
1. Fusionnez deux fichiers PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est sauvegardé dans "ResultMerge.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Merge two PDF-files and save the "ResultMerge.pdf"*/
      const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
      console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom des fichiers PDF qui seront fusionnés.
1. Initialisez le module AsposePdf. Recevez l'objet en cas de succès.
1. Appelez la fonction [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/).
1. Fusionnez deux fichiers PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est sauvegardé dans "ResultMerge.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Merge two PDF-files and save the "ResultMerge.pdf"*/
  const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
  console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```