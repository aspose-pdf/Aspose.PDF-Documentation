---
title: Ajouter une Image au PDF en utilisant JavaScript via C++ 
linktitle: Ajouter une Image
type: docs
weight: 10
url: /fr/javascript-cpp/add-image-to-pdf/
description: Cette section décrit comment ajouter une image à un fichier PDF existant en utilisant Aspose.PDF pour JavaScript via C++.
lastmod: "2023-12-15"
---

## Ajouter une Image dans un Fichier PDF Existant

Avez-vous besoin d'attacher une image à un PDF ? Vous voulez améliorer la lisibilité de votre PDF ? Ajoutez des images à votre PDF et votre présentation ou CV aura l'air plus présentable.

Il est communément admis que l'ajout d'images aux fichiers PDF nécessite un outil spécial complexe. Cependant, avec Aspose.PDF pour JavaScript, vous pouvez rapidement et facilement ajouter les images dont vous avez besoin au PDF en utilisant JavaScript directement dans votre navigateur.

Pour ajouter une image à un fichier PDF existant :

1. Définir le nom de fichier image par défaut.
1. Créer un 'FileReader'.
1. Définir le nom de fichier image.
1. Préparer le fichier image à partir de BLOB.
1. La fonction [AsposePdfAddImage](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddimage/) est exécutée.

1. Ajoutez le fichier image à la fin d'un fichier PDF et enregistrez-le sous le nom "ResultImage.pdf".
1. Ensuite, si le 'json.errorCode' est 0, alors votre DownloadFile prend le nom que vous avez spécifié précédemment. Si le paramètre 'json.errorCode' n'est pas égal à 0 et, en conséquence, il y aura une erreur dans votre fichier, alors des informations sur cette erreur seront contenues dans le fichier 'json.errorText'.
1. En conséquence, la fonction [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) génère un lien et vous permet de télécharger le fichier résultant sur le système d'exploitation de l'utilisateur.

L'extrait de code suivant montre comment ajouter l'image dans un document PDF.

```js

  /*définir le nom de fichier image par défaut*/
  var fileImage = "/Aspose.jpg";

  var ffileImage = function (e) {
    const file_reader = new FileReader();
    /*définir le nom de fichier image*/
    fileImage = e.target.files[0].name;
    file_reader.onload = (event) => {
      /*préparer(enregistrer) le fichier image depuis le BLOB*/
      AsposePdfPrepare(event.target.result, fileImage);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```

Dans le prochain exemple, nous sélectionnons l'image à traiter :

```js

  var ffileAddImage = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*ajouter le fichier image à la fin d'un fichier PDF et enregistrer le "ResultImage.pdf"*/
      const json = AsposePdfAddImage(event.target.result, e.target.files[0].name, fileImage, "ResultImage.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*créer un lien pour télécharger le fichier résultat*/
      DownloadFile(json.fileNameResult, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```

## Utilisation des Web Workers

```js

    /*Créer un Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erreur du Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'chargé!' :
        (evt.data.json.errorCode == 0) ?
          `Résultat:\n${(evt.data.operation == 'AsposePdfPrepare') ?
            'image préparée!':
            DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Erreur: ${evt.data.json.errorText}`;

    /*Définir le nom de fichier image par défaut: 'Aspose.jpg' déjà chargé, voir les paramètres dans 'settings.json'*/
    var fileImage = "Aspose.jpg";

    /*Gestionnaire d'événements*/
    const ffileAddImage = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Ajouter l'image à la fin d'un fichier PDF et enregistrer le "ResultImage.pdf" - Demander au Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddImage',
            "params": [event.target.result, e.target.files[0].name, fileImage, "ResultImage.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileImage = e => {
      const file_reader = new FileReader();
      /*Définir le nom du fichier image*/
      fileImage = e.target.files[0].name;
      file_reader.onload = event => {
        /*Enregistrer le BLOB dans la mémoire FS pour traitement*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfPrepare', "params": [event.target.result, e.target.files[0].name] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Créer un lien pour télécharger le fichier résultat*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "Cliquez ici pour télécharger le fichier " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```