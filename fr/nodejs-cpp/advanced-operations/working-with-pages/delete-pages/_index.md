const asposepdf = require("asposepdfcloud");

const config = {"appKey": "your-app-key", "appSid": "your-app-sid"};
const pdfApi = new asposepdf.PdfApi(config);

// Supprimer les pages en utilisant la chaîne
pdfApi.deletePages("example.pdf", "7, 20, 30-32, 34", null, null)
    .then((result) => {
        console.log("Pages supprimées avec succès: ", result.body);
    })
    .catch((error) => {
        console.log("Erreur lors de la suppression des pages: ", error);
    });

// Supprimer les pages en utilisant un tableau
pdfApi.deletePages("example.pdf", [3, 7], null, null)
    .then((result) => {
        console.log("Pages supprimées avec succès: ", result.body);
    })
    .catch((error) => {
        console.log("Erreur lors de la suppression des pages: ", error);
    });

// Supprimer une seule page
pdfApi.deletePages("example.pdf", 2, null, null)
    .then((result) => {
        console.log("Page supprimée avec succès: ", result.body);
    })
    .catch((error) => {
        console.log("Erreur lors de la suppression de la page: ", error);
    });
```

**ES6:**

```
import { PdfApi } from "asposepdfcloud";

const config = {"appKey": "your-app-key", "appSid": "your-app-sid"};
const pdfApi = new PdfApi(config);

// Supprimer les pages en utilisant la chaîne
pdfApi.deletePages("example.pdf", "7, 20, 30-32, 34", null, null)
    .then((result) => {
        console.log("Pages supprimées avec succès: ", result.body);
    })
    .catch((error) => {
        console.log("Erreur lors de la suppression des pages: ", error);
    });

// Supprimer les pages en utilisant un tableau
pdfApi.deletePages("example.pdf", [3, 7], null, null)
    .then((result) => {
        console.log("Pages supprimées avec succès: ", result.body);
    })
    .catch((error) => {
        console.log("Erreur lors de la suppression des pages: ", error);
    });

// Supprimer une seule page
pdfApi.deletePages("example.pdf", 2, null, null)
    .then((result) => {
        console.log("Page supprimée avec succès: ", result.body);
    })
    .catch((error) => {
        console.log("Erreur lors de la suppression de la page: ", error);
    });
```

Les extraits de code ci-dessus montrent comment supprimer des pages de fichiers PDF à l'aide de la bibliothèque Aspose.PDF pour Node.js via C++.

1. Appelez `require` et importez le module `asposepdfnodejs` en tant que variable `AsposePdf`.
1. Spécifiez le nom du fichier PDF à partir duquel les pages seront supprimées.
1. Appelez `AsposePdf` en tant que Promise et effectuez l'opération pour supprimer les pages. Recevez l'objet en cas de succès.
1. Appelez la fonction [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/).
1. Supprime les pages particulières du fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultDeletePages.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*string, inclut les numéros de pages avec intervalle : "7, 20, 22, 30-32, 33, 36-40, 46"*/
      /*const numPages = "1-3";*/
      /*array, tableau de numéros de pages*/
      /*const numPages = [1,3];*/
      /*number, numéro de page*/
      const numPages = 1;
      /*Supprime les pages d'un fichier PDF et enregistre le "ResultDeletePages.pdf"*/
      const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
      console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importez le module `asposepdfnodejs`.
1. Spécifiez le nom du fichier PDF à partir duquel les pages seront supprimées.
1. Initialisez le module AsposePdf. Recevez l'objet en cas de succès.
1. Appelez la fonction [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/). Cette fonction aide à supprimer les pages spécifiées du fichier PDF. L'opération est déterminée par la variable numPages, qui peut être une chaîne avec des intervalles de pages (par exemple, "7, 20, 22, 30-32, 33, 36-40, 46"), un tableau de numéros de pages, ou un seul numéro de page.
1. Supprime les pages particulières du fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultDeletePages.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*chaîne, inclure les numéros de pages avec intervalle: "7, 20, 22, 30-32, 33, 36-40, 46"*/
  /*const numPages = "1-3";*/
  /*tableau, tableau de numéros de pages*/
  /*const numPages = [1,3];*/
  /*nombre, numéro de page*/
  const numPages = 1;
  /*Supprimez les pages d'un fichier PDF et enregistrez le "ResultDeletePages.pdf"*/
  const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
  console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```