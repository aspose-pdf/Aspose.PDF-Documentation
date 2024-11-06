---
title: Convertir des PDF en formats PDF/A 
linktitle: Convertir des PDF en formats PDF/A
type: docs
weight: 100
url: fr/javascript-cpp/convert-pdf-to-pdfa/
lastmod: "2023-11-01"
description: Ce sujet vous montre comment Aspose.PDF permet de convertir un fichier PDF en un fichier PDF conforme à PDF/A. 
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF pour JavaScript** vous permet de convertir un fichier PDF en un fichier PDF conforme à <abbr title="Portable Document Format / A">PDF/A</abbr>.

L'opération de conversion dépend du nombre de pages dans le document et peut être très chronophage. Par conséquent, nous recommandons fortement l'utilisation de Web Workers.

Ce code démontre une manière de délester les tâches de conversion de fichiers PDF gourmandes en ressources vers un web worker pour éviter de bloquer le fil principal de l'interface utilisateur. Il offre également un moyen convivial de télécharger le fichier converti.

{{% alert color="success" %}}
**Essayez de convertir un PDF en PDF/A en ligne**

Aspose.PDF pour JavaScript vous présente une application en ligne gratuite ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF to PDF/A avec Application Gratuite](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

## Convertir PDF au format PDF/A

```js

  /*Créer un Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erreur du Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'chargé!' :
        (evt.data.json.errorCode == 0) ? `Résultat:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}\n${DownloadFile(evt.data.json.fileNameLogResult, "application/xml", evt.data.params[1])}` : `Erreur: ${evt.data.json.errorText}`;

    /*Gestionnaire d'événement*/
    const ffilePdfConvertToPDFA = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const pdfFormat = 'Module.PdfFormat.PDF_A_1A';
        /*convertir un fichier PDF en PDF/A(1A) et enregistrer le "ResultConvertToPDFA.pdf"*/
        /*pendant le processus de conversion, la validation est également effectuée, "ResultConvertToPDFA.xml"- Demander au Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfConvertToPDFA', "params": [event.target.result, e.target.files[0].name, pdfFormat, "ResultConvertToPDFA.pdf", "ResultConvertToPDFA.xml"] }, [event.target.result]);
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


The following JavaScript code snippet shows simple example of coverting PDF to PDF/A files:

1. Sélectionnez un fichier PDF à convertir.
1. Créez un 'FileReader'.
1. La fonction [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfconverttopdfa/) est exécutée.
1. Le nom du fichier résultant est défini, dans cet exemple "ResultConvertToPDFA.pdf". Pendant le processus de conversion, la validation est également effectuée, "ResultConvertToPDFA.xml".
1. Ensuite, si le 'json.errorCode' est 0, alors votre DownloadFile reçoit le nom que vous avez spécifié précédemment. Si le paramètre 'json.errorCode' n'est pas égal à 0 et, en conséquence, il y aura une erreur dans votre fichier, alors des informations sur cette erreur seront contenues dans le fichier 'json.errorText'.
1. En conséquence, la fonction [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) génère un lien et vous permet de télécharger le fichier résultant, ainsi qu'un lien pour télécharger le fichier Log (xml) vers le système d'exploitation de l'utilisateur.

```js

  var ffilePdfConvertToPDFA = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*convertir un fichier PDF en PDF/A(1A) et enregistrer le "ResultConvertToPDFA.pdf"*/
      /*pendant le processus de conversion, la validation est également effectuée, "ResultConvertToPDFA.xml"*/
      const json = AsposePdfConvertToPDFA(event.target.result, e.target.files[0].name, Module.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFA.xml");
      if (json.errorCode == 0)
      {
        document.getElementById('output').textContent = json.fileNameResult + "\nFichier journal (format xml) : " + json.fileNameLogResult;
        /*créer un lien pour télécharger le fichier résultant*/
        DownloadFile(json.fileNameResult, "application/pdf");
      }
      else document.getElementById('output').textContent = json.errorText + "\nFichier journal (format xml) : " + json.fileNameLogResult;
      /*créer un lien pour télécharger le fichier journal (xml)*/
      DownloadFile(json.fileNameLogResult, "application/xml");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```