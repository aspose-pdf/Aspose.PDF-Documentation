---
title: Supprimer des Pages PDF avec JavaScript via C++ 
linktitle: Supprimer des Pages PDF
type: docs
weight: 30
url: /fr/javascript-cpp/delete-pages/
description: Vous pouvez supprimer des pages de votre fichier PDF en utilisant Aspose.PDF pour JavaScript via C++.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Vous pouvez supprimer des pages d'un fichier PDF en utilisant Aspose.PDF pour JavaScript via C++. Vous pouvez obtenir le résultat directement dans votre navigateur.

1. Créez un 'FileReader'.
1. Spécifiez les numéros de pages à supprimer.
1. La fonction [AsposePdfDeletePages](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfdeletepages/) est exécutée.
1. Le nom du fichier résultant est défini, dans cet exemple "ResultDeletePages.pdf".
1. Ensuite, si le 'json.errorCode' est 0, alors votre DownloadFile est donné le nom que vous avez spécifié précédemment. Si le paramètre 'json.errorCode' n'est pas égal à 0 et, en conséquence, il y aura une erreur dans votre fichier, alors les informations sur une telle erreur seront contenues dans le fichier 'json.errorText'.

1. En conséquence, la fonction [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) génère un lien et vous permet de télécharger le fichier résultant sur le système d'exploitation de l'utilisateur.

```js

  var ffileDeletePages = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*chaîne, inclure les numéros de pages avec intervalle : "7, 20, 22, 30-32, 33, 36-40, 46"*/
      const numPages = "1-3";
      /*tableau, tableau des numéros de pages*/
      /*const numPages = [1,3];*/
      /*nombre, numéro de page*/
      /*const numPages = 1;*/
      /*supprimer les pages 1-3 d'un fichier PDF et enregistrer le "ResultOptimize.pdf"*/
      const json = AsposePdfDeletePages(event.target.result, e.target.files[0].name, "ResultDeletePages.pdf", numPages);
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*créer un lien pour télécharger le fichier résultant*/
      DownloadFile(json.fileNameResult, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


## Utilisation des Web Workers

```js

    /*Créer un Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erreur du Web Worker : ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'chargé!' :
        (evt.data.json.errorCode == 0) ?
          `Résultat:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Erreur : ${evt.data.json.errorText}`;

    /*Gestionnaire d'événements*/
    const ffileDeletePages = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*chaîne, inclut numéro de pages avec intervalle: "7, 20, 22, 30-32, 33, 36-40, 46"*/
        const numPages = "1-3";
        /*tableau, tableau de numéros de pages*/
        /*const numPages = [1,3];*/
        /*numéro, numéro de page*/
        /*const numPages = 1;*/
        /*Supprimer des pages d'un fichier PDF et enregistrer le "ResultDeletePages.pdf - Demander à Web Worker"*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfDeletePages',
            "params": [event.target.result, e.target.files[0].name, "ResultDeletePages.pdf", numPages] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Créer un lien pour télécharger le fichier résultant*/
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