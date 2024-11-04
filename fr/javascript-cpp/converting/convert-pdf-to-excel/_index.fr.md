---
title: Convertir un PDF en Excel en JavaScript
linktitle: Convertir un PDF en Excel
type: docs
weight: 20
url: /javascript-cpp/convert-pdf-to-xlsx/
lastmod: "2023-11-01"
keywords: convertir PDF en Excel en utilisant javascript, convertir PDF en XLSX, convertir PDF en CSV.
description: Aspose.PDF pour JavaScript vous permet de convertir des PDF en formats XLSX et CSV.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Création de feuilles de calcul à partir de PDF en utilisant JavaScript

**Aspose.PDF pour JavaScript** prend en charge la fonctionnalité de conversion de fichiers PDF en formats Excel et CSV.

{{% alert color="success" %}}
**Essayez de convertir un PDF en Excel en ligne**

Aspose.PDF pour JavaScript vous présente l'application en ligne gratuite ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), où vous pouvez essayer d'étudier la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en Excel avec l'application gratuite](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

L'opération de conversion dépend du nombre de pages dans le document et peut être très chronophage.
 Par conséquent, nous recommandons fortement d'utiliser les Web Workers.

Ce code démontre une façon de décharger les tâches de conversion de fichiers PDF gourmandes en ressources vers un web worker pour éviter de bloquer le thread principal de l'interface utilisateur. Il offre également un moyen convivial de télécharger le fichier converti.

## Convertir PDF en XLSX

```js

  /*Créer un Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erreur du Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'chargé!' :
        (evt.data.json.errorCode == 0) ? `Résultat:\n${DownloadFile(evt.data.json.fileNameResult, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", evt.data.params[0])}` : `Erreur: ${evt.data.json.errorText}`;

    /*Gestionnaire d'événements*/
    const ffileToXlsX = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*convertir un fichier PDF en XlsX et enregistrer "ResultPDFtoXlsX.xlsx" - Demander au Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToXlsX', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoXlsX.xlsx"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Extrait de code]

    /*créer un lien pour télécharger le fichier résultant*/
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

Le fragment de code JavaScript suivant montre un exemple simple de conversion de pages PDF en fichiers XlsX :

1. Sélectionnez un fichier PDF à convertir.
1. Créez un 'FileReader'.
1. La fonction [AsposePdfToXlsX](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdftoxlsx/) est exécutée.
1. Le nom du fichier résultant est défini, dans cet exemple "ResultPDFtoXlsX.xlsx".
1. Ensuite, si le 'json.errorCode' est 0, alors votre fichier résultat reçoit le nom que vous avez spécifié précédemment. Si le paramètre 'json.errorCode' n'est pas égal à 0 et, en conséquence, il y aura une erreur dans votre fichier, alors les informations sur cette erreur seront contenues dans le fichier 'json.errorText'.
1. En conséquence, la fonction [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) génère un lien et vous permet de télécharger le fichier résultant sur le système d'exploitation de l'utilisateur.

```js

  var ffileToXlsX = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*convertir un fichier PDF en XlsX et enregistrer le "ResultPDFtoXlsX.xlsx"*/
      const json = AsposePdfToXlsX(event.target.result, e.target.files[0].name, "ResultPDFtoXlsX.xlsx");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*créer un lien pour télécharger le fichier résultat*/
      DownloadFile(json.fileNameResult, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```


## Convertir PDF en CSV

```js

    /*Créer Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erreur de Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'chargé!' :
        (evt.data.json.errorCode == 0) ? 
          `Nombre de fichiers (tables) : ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "text/csv", element) ) ?? ""}` : 
          `Erreur : ${evt.data.json.errorText}`;

    /*Gestionnaire d'événements*/
    const ffileToCSV = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Convertir un fichier PDF en CSV (extraire les tables) avec le modèle "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... numéro de page formaté), TAB comme délimiteur et sauvegarder - Demander au Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfTablesToCSV', "params": [event.target.result, e.target.files[0].name, "ResultPdfTablesToCSV{0:D2}.csv", "\t"] }, [event.target.result]);
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


Le fragment de code JavaScript suivant montre un exemple simple de conversion de PDF en CSV :

1. Sélectionnez un fichier PDF à convertir.
1. Créez un 'FileReader'.
1. La fonction [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftablestocsv/) est exécutée.
1. Le nom du fichier résultant est défini, dans cet exemple "ResultPdfTablesToCSV{0:D2}.csv".
1. Ensuite, si le 'json.errorCode' est 0, alors votre fichier résultat reçoit le nom que vous avez spécifié précédemment. Si le paramètre 'json.errorCode' n'est pas égal à 0 et, par conséquent, il y aura une erreur dans votre fichier, alors les informations sur cette erreur seront contenues dans le fichier 'json.errorText'.
1. En conséquence, la fonction [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) génère un lien et vous permet de télécharger le fichier résultant sur le système d'exploitation de l'utilisateur.

```js

  var ffileToCSV = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Convertir un fichier PDF en CSV (extraire les tables) avec le modèle "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... numéro de page au format), TAB comme délimiteur*/
        const json = AsposePdfTablesToCSV(event.target.result, e.target.files[0].name, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
        if (json.errorCode == 0) {
          document.getElementById('output').textContent = "Nombre de fichiers (tables) : " + json.filesCount.toString();
          /*Créer des liens vers les fichiers résultants*/
          for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "text/csv");
        }
        else document.getElementById('output').textContent = json.errorText;
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```