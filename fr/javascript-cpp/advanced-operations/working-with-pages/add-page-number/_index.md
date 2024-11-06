---
title: Ajouter un Numéro de Page au PDF avec JavaScript via C++
linktitle: Ajouter un Numéro de Page
type: docs
weight: 100
url: fr/javascript-cpp/add-page-number/
description: Aspose.PDF pour JavaScript via C++ vous permet d'ajouter un tampon de numéro de page à votre fichier PDF en utilisant AsposePdfAddPageNum.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Tous les documents doivent avoir des numéros de page. Le numéro de page facilite la localisation des différentes parties du document pour le lecteur.

**Aspose.PDF pour JavaScript via C++** vous permet d'ajouter des numéros de page avec [AsposePdfAddPageNum](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddpagenum/).

1. Créez un 'FileReader'.
1. La fonction [AsposePdfAddPageNum](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddpagenum/) est exécutée.
1. Le nom du fichier résultant est défini, dans cet exemple "ResultAddPageNum.pdf".

1. Ensuite, si le 'json.errorCode' est égal à 0, alors votre DownloadFile porte le nom que vous avez spécifié précédemment. Si le paramètre 'json.errorCode' n'est pas égal à 0 et, en conséquence, il y aura une erreur dans votre fichier, alors les informations concernant cette erreur seront contenues dans le fichier 'json.errorText'.
1. En conséquence, la fonction [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) génère un lien et vous permet de télécharger le fichier résultant sur le système d'exploitation de l'utilisateur.

```js
var ffileAddPageNum = function (e) {
  const file_reader = new FileReader();
  file_reader.onload = (event) => {
    /*ajouter un numéro de page à un fichier PDF et enregistrer le "ResultAddPageNum.pdf"*/
    const json = AsposePdfAddPageNum(event.target.result, e.target.files[0].name, "ResultAddPageNum.pdf");
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
    AsposePDFWebWorker.onerror = evt => console.log(`Erreur du Web Worker : ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'chargé!' :
        (evt.data.json.errorCode == 0) ?
          `Résultat:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Erreur: ${evt.data.json.errorText}`;

    /*Gestionnaire d'événements*/
    const ffileAddPageNum = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Ajouter un numéro de page à un fichier PDF et enregistrer le "ResultAddPageNum.pdf" - Demander au Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddPageNum', "params": [event.target.result, e.target.files[0].name, "ResultAddPageNum.pdf"] },
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