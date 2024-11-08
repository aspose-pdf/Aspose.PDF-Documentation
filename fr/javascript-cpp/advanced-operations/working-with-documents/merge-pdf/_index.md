---
title: Comment Fusionner des PDF en utilisant JavaScript via C++ 
linktitle: Fusionner des fichiers PDF
type: docs
weight: 20
url: /fr/javascript-cpp/merge-pdf/
description: Cette page explique comment fusionner des documents PDF en un seul fichier PDF avec Aspose.PDF pour JavaScript via C++ 
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Fusionner ou combiner deux PDF en un seul PDF en JavaScript

Combiner et fusionner des fichiers est une tâche très populaire lors du travail avec un grand nombre de documents. Parfois, lors du travail avec des documents et des images, lorsqu'ils sont numérisés, traités et organisés, plusieurs fichiers sont créés.
Mais que faire si vous devez tout stocker dans un seul fichier ? Ou vous ne voulez pas imprimer plusieurs documents ? Concaténez deux fichiers PDF avec Aspose.PDF pour JavaScript via C++.

Cet outil JavaScript permet de fusionner deux fichiers PDF en un seul document PDF en utilisant Aspose.PDF pour JavaScript via C++. L'exemple est écrit en JavaScript.

1. Sélectionnez un fichier PDF pour la fusion.
1. Créez un 'FileReader'.

1. La fonction [AsposePdfMerge2Files](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfmerge2files/) est exécutée.
1. Le nom du fichier résultant est défini, dans cet exemple "ResultMerge.pdf".
1. Ensuite, si le 'json.errorCode' est 0, alors votre DownloadFile reçoit le nom que vous avez spécifié précédemment. Si le paramètre 'json.errorCode' n'est pas égal à 0 et, en conséquence, qu'il y a une erreur dans votre fichier, alors des informations sur cette erreur seront contenues dans le fichier 'json.errorText'.
1. En conséquence, la fonction [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) génère un lien et vous permet de télécharger le fichier résultant sur le système d'exploitation de l'utilisateur.

Le snippet de code suivant montre comment concaténer des fichiers PDF :

```js

  var ffileMerge = function (e) {
    const file_reader = new FileReader();
    function readFile(index) {
      /*seulement deux fichiers*/
      if (index >= e.target.files.length || index >= 2) {
        /*fusionner deux fichiers PDF et enregistrer le "ResultMerge.pdf"*/
        const json = AsposePdfMerge2Files(undefined, undefined, e.target.files[0].name, e.target.files[1].name, "ResultMerge.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*créer un lien pour télécharger le fichier résultant*/
        DownloadFile(json.fileNameResult, "application/pdf");
        return;
      }
      const file = e.target.files[index];
      file_reader.onload = function (event) {
        /*préparer(enregistrer) le fichier à partir du BLOB*/
        AsposePdfPrepare(event.target.result, file.name);
        readFile(index + 1)
      }
      file_reader.readAsArrayBuffer(file);
    }
    readFile(0);
  }
```


### Utilisation des Web Workers

```js

    /*Créer un Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erreur du Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'chargé!' :
        (evt.data.json.errorCode == 0) ? 
          `Résultat:\n${(evt.data.operation == 'AsposePdfPrepare') ? 
                      fileProcess('AsposePdfMerge2Files', evt.data.json.optdata[0].file, {"fileName2": evt.data.json.fileNameResult}) ?? 'attendez s'il vous plaît...' : 
                      DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0]) /*AsposePdfMerge2Files*/
                    }` :
          `Erreur: ${evt.data.json.errorText}`;

    /*Gestionnaire d'événements. Seuls deux fichiers sont fusionnés. Si un seul fichier est sélectionné, alors utilisez-le. Pour le second fichier, vous devez effectuer AsposePdfPrepare */
    const ffileMerge = evt => fileProcess('AsposePdfPrepare',  evt.target.files[(evt.target.files.length == 1) ? 0 : 1],
                                          [{"operation": 'AsposePdfMerge2Files', "file": evt.target.files[0]}])
    /* Demander au Web Worker */
    const fileProcess = (operation, ffile, optdata) => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        if (operation == 'AsposePdfPrepare')
          return AsposePDFWebWorker.postMessage(
                  { "operation": operation, "params": [event.target.result, ffile.name, optdata] },
                  [event.target.result]
                );
        else if (operation == 'AsposePdfMerge2Files')
          return AsposePDFWebWorker.postMessage(
                  { "operation": operation, 
                    "params": [event.target.result, undefined, ffile.name, (optdata === undefined) ? ffile.name : optdata.fileName2,
                                `Result${operation}.pdf`] },
                  [event.target.result]
                );
      }
      file_reader.readAsArrayBuffer(ffile);
    }

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