title: Ajouter des tampons d'image au PDF dans Node.js
linktitle: Tampons d'image dans le fichier PDF
type: docs
weight: 60
url: /nodejs-cpp/stamping/
description: Ajouter le tampon d'image dans votre document PDF en utilisant AsposePdfAddStamp avec l'outil Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ajouter un tampon d'image dans un fichier PDF

Tamponner un document PDF est similaire à tamponner un document papier. Un tampon dans un fichier PDF fournit des informations supplémentaires au fichier PDF, telles que la protection du fichier PDF pour l'utilisation par d'autres et la confirmation de la sécurité du contenu du fichier PDF.
Vous pouvez utiliser la fonction [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/) pour ajouter un tampon d'image à un fichier PDF en utilisant Node.js.

Veuillez vérifier l'extrait de code suivant afin d'ajouter un tampon d'image à un fichier PDF dans l'environnement Node.js.

**CommonJS :**

1. Appelez `require` et importez le module `asposepdfnodejs` en tant que variable `AsposePdf`.

1. Spécifiez le nom du fichier PDF dans lequel le tampon d'image sera ajouté.
1. Appelez `AsposePdf` en tant que Promise et effectuez l'opération d'ajout de tampon d'image. Recevez l'objet si cela réussit.
1. Appelez la fonction [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/).
1. Ajoutez un tampon à un fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultImage.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const stamp_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Ajouter un tampon à un fichier PDF et enregistrer le "ResultImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddStamp(pdf_file, stamp_file, 0, 5, 5, 40, 40, AsposePdfModule.Rotation.on270, 0.5, "ResultAddStamp.pdf");
      console.log("AsposePdfAddStamp => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importez le module `asposepdfnodejs`.
1. Spécifiez le nom du fichier PDF dans lequel le tampon d'image sera ajouté.
1. Initialisez le module AsposePdf. Recevez l'objet si réussi.
1. Appelez la fonction [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/).
1. Ajoutez un tampon à un fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultImage.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const stamp_file = 'Aspose.jpg';
  /*Ajoutez un tampon à un fichier PDF et enregistrez le "ResultImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddStamp(pdf_file, stamp_file, 0, 5, 5, 40, 40, AsposePdfModule.Rotation.on270, 0.5, "ResultAddStamp.pdf");
  console.log("AsposePdfAddStamp => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```