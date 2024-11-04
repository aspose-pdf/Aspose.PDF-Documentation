---
title: Optimiser les ressources PDF en utilisant JavaScript via C++
linktitle: Optimiser les ressources PDF
type: docs
weight: 15
url: /javascript-cpp/optimize-pdf-resources/
description: Optimiser les ressources des fichiers PDF pour une vue web rapide en utilisant un outil JavaScript.
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Optimiser les ressources PDF

Optimiser les ressources dans le document :

  1. Les ressources qui ne sont pas utilisées sur les pages du document sont supprimées
  1. Les ressources égales sont regroupées en un seul objet
  1. Les objets inutilisés sont supprimés
 
1. Sélectionnez un fichier PDF pour l'optimisation.
1. Créez un 'FileReader'.
1. La fonction [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfoptimizeresource/) est exécutée.
1. Le nom du fichier résultant est défini, dans cet exemple "ResultPdfOptimizeResource.pdf".

1. Ensuite, si le 'json.errorCode' est 0, alors votre DownloadFile est nommé comme vous l'avez spécifié précédemment. Si le paramètre 'json.errorCode' n'est pas égal à 0 et, par conséquent, il y aura une erreur dans votre fichier, alors l'information sur cette erreur sera contenue dans le fichier 'json.errorText'.
1. En conséquence, la fonction [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) génère un lien et vous permet de télécharger le fichier résultant sur le système d'exploitation de l'utilisateur.

Le code suivant montre comment optimiser un document PDF.

```js

    var ffilePdfOptimizeResource = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Optimiser les ressources d'un fichier PDF et sauvegarder le "ResultPdfOptimizeResource.pdf"*/
        const json = AsposePdfOptimizeResource(event.target.result, e.target.files[0].name, "ResultPdfOptimizeResource.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Créer un lien pour télécharger le fichier résultant*/
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
        (evt.data.json.errorCode == 0) ? `Résultat:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `Erreur : ${evt.data.json.errorText}`;

    /*Gestionnaire d'événements*/
    const ffilePdfOptimizeResource = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Optimiser les ressources d'un fichier PDF et enregistrer le "ResultPdfOptimizeResource.pdf" - Demander au Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfOptimizeResource', "params": [event.target.result, e.target.files[0].name, "ResultPdfOptimizeResource.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Extrait de code]

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