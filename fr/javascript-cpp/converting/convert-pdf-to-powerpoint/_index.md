---
title: Convertir PDF en PPTX en JavaScript
linktitle: Convertir PDF en PowerPoint
type: docs
weight: 30
url: fr/javascript-cpp/convert-pdf-to-powerpoint/
lastmod: "2023-11-01"
description: Aspose.PDF vous permet de convertir les PDF en format PPTX en utilisant JavaScript directement sur le web.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

L'opération de conversion dépend du nombre de pages dans le document et peut être très chronophage. Par conséquent, nous recommandons fortement l'utilisation de Web Workers.

Ce code démontre une façon de délester les tâches de conversion de fichiers PDF gourmandes en ressources vers un web worker pour éviter de bloquer le thread principal de l'interface utilisateur. Il offre également un moyen convivial de télécharger le fichier converti.

{{% alert color="success" %}}
**Essayez de convertir un PDF en PowerPoint en ligne**

Aspose.PDF pour JavaScript vous présente l'application en ligne gratuite ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), où vous pouvez essayer de vérifier la fonctionnalité et la qualité de son fonctionnement.


[![Aspose.PDF Conversion PDF en PPTX avec application gratuite](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

## Convertir PDF en PPTX

```js

  /*Créer Web Worker*/
  const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
  AsposePDFWebWorker.onerror = evt => console.log(`Erreur du Web Worker : ${evt.message}`);
  AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
    (evt.data == 'ready') ? 'chargé!' :
      (evt.data.json.errorCode == 0) ? `Résultat:\n${DownloadFile(evt.data.json.fileNameResult, "application/vnd.openxmlformats-officedocument.presentationml.presentation", evt.data.params[0])}` : `Erreur : ${evt.data.json.errorText}`;

  /*Gestionnaire d'événements*/
  const ffileToPptX = e => {
    const file_reader = new FileReader();
    file_reader.onload = event => {
      /*Convertir un fichier PDF en PptX et enregistrer le "ResultPDFtoPptX.pptx" - Demander au Web Worker*/
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToPptX', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoPptX.pptx"] }, [event.target.result]);
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


Le fragment de code JavaScript suivant montre un exemple simple de conversion de fichiers PDF en fichiers PPTX :

1. Sélectionnez un fichier PDF pour la conversion.
1. Créez un 'FileReader'.
1. La fonction [AsposePdfToPptX](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftopptx/) est exécutée.
1. Le nom du fichier résultant est défini, dans cet exemple "ResultPDFtoPptX.pptx".
1. Ensuite, si le 'json.errorCode' est 0, alors votre fichier résultant reçoit le nom que vous avez spécifié précédemment. Si le paramètre 'json.errorCode' n'est pas égal à 0 et, en conséquence, il y aura une erreur dans votre fichier, alors les informations concernant une telle erreur seront contenues dans le fichier 'json.errorText'.
1. En conséquence, la fonction [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) génère un lien et vous permet de télécharger le fichier résultant sur le système d'exploitation de l'utilisateur.

```js

  var ffileToPptX = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*Convertir un fichier PDF en PptX et enregistrer dans "ResultPDFtoPptX.pptx"*/
      const json = AsposePdfToPptX(event.target.result, e.target.files[0].name, "ResultPDFtoPptX.pptx");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*Créer un lien pour télécharger le fichier résultant*/
      DownloadFile(json.fileNameResult, "application/vnd.openxmlformats-officedocument.presentationml.presentation");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```