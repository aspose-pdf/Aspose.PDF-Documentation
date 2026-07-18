---
title: Extraire des images du PDF dans Node.js
linktitle: Extraire des images du PDF
type: docs
weight: 20
url: /fr/nodejs-cpp/extract-images-from-the-pdf-file/
description: Comment extraire une partie de l'image du PDF en utilisant Aspose.PDF for Node.js via C++ toolkit.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraire des images des fichiers PDF dans l'environnement Node.js

Dans le cas où vous souhaitez extraire des images d'un document PDF, vous pouvez utiliser [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/) fonction. 
Nous devons passer trois arguments à cette fonction : le nom du fichier d'entrée et de sortie ainsi que la résolution.
Veuillez vérifier le fragment de code suivant pour extraire des images d'un fichier PDF en utilisant Node.js.

**CommonJS:**

1. Appel `require` et importer `asposepdfnodejs` module comme `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF à partir duquel l'image sera extraite.
1. Appel `AsposePdf` en tant que Promise et effectuer l'opération d'extraction d'image. Recevoir l'objet en cas de succès.
1. Appelez la fonction [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/).
1. Extrayez les images du fichier PDF. Ainsi, si ‘json.errorCode’ est 0, le résultat de l'opération est sauvegardé dans "ResultPdfExtractImage{0:D2}.jpg". Où {0:D2} représente le numéro de page avec un format à deux chiffres. Les images sont sauvegardées avec une résolution de 150 DPI. Si le paramètre json.errorCode n’est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d’erreur seront contenues dans ‘json.errorText’.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Extract image from a PDF-file with template "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfModule.AsposePdfExtractImage(pdf_file, "ResultPdfExtractImage{0:D2}.jpg", 150);
      console.log("AsposePdfExtractImage => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF à partir duquel l'image sera extraite.
1. Initialisez le module AsposePdf. Recevez l'objet en cas de succès.
1. Appelez la fonction [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/).
1. Extrayez les images du fichier PDF. Ainsi, si ‘json.errorCode’ est 0, le résultat de l'opération est sauvegardé dans "ResultPdfExtractImage{0:D2}.jpg". Où {0:D2} représente le numéro de page avec un format à deux chiffres. Les images sont sauvegardées avec une résolution de 150 DPI. Si le paramètre json.errorCode n’est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d’erreur seront contenues dans ‘json.errorText’.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Extract image from a PDF-file with template "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
    const json = AsposePdfModule.AsposePdfExtractImage(pdf_file, "ResultPdfExtractImage{0:D2}.jpg", 150);
    console.log("AsposePdfExtractImage => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```
