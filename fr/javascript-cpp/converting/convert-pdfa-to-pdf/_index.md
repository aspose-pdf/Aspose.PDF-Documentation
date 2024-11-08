---
title: Convertir PDF/A en format PDF 
linktitle: Convertir PDF/A en format PDF
type: docs
weight: 110
url: /fr/javascript-cpp/convert-pdfa-to-pdf/
lastmod: "2023-11-01"
description: Ce sujet montre comment Aspose.PDF permet de convertir un fichier PDF/A en document PDF avec JavaScript.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Convertir PDF/A en format PDF

```js

  /*Créer un Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erreur du Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'chargé!' :
        (evt.data.json.errorCode == 0) ? `Résultat:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `Erreur: ${evt.data.json.errorText}`;

    /*Gestionnaire d'événements*/
    const ffilePdfAConvertToPDF = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*convertir un fichier PDF/A en PDF et enregistrer le "ResultConvertToPDF.pdf" - Demander au Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfAConvertToPDF', "params": [event.target.result, e.target.files[0].name, "ResultConvertToPDF.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Extrait de code]

    /*créer un lien pour télécharger le fichier résultat*/
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


Le fragment de code JavaScript suivant montre un exemple simple de conversion de PDF/A en PDF :

1. Sélectionnez un fichier PDF à convertir.
1. Créez un 'FileReader'.
1. La fonction [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaconverttopdf/) est exécutée.
1. Le nom du fichier résultant est défini, dans cet exemple "ResultConvertToPDFA.pdf".
1. Ensuite, si le 'json.errorCode' est 0, alors votre DownloadFile reçoit le nom que vous avez spécifié précédemment. Si le paramètre 'json.errorCode' n'est pas égal à 0 et, en conséquence, il y aura une erreur dans votre fichier, alors des informations sur une telle erreur seront contenues dans le fichier 'json.errorText'.
1. En conséquence, la fonction [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) génère un lien et vous permet de télécharger le fichier résultant sur le système d'exploitation de l'utilisateur.

```js

    var ffilePdfAConvertToPDF = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*convertir un fichier PDF/A en PDF et enregistrer le "ResultConvertToPDF.pdf"*/
        const json = AsposePdfAConvertToPDF(event.target.result, e.target.files[0].name, "ResultConvertToPDF.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*créer un lien pour télécharger le fichier résultat*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

```