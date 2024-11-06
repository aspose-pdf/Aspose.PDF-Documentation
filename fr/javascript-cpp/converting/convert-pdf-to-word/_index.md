---
title: Convertir des documents PDF en Word en JavaScript
linktitle: Convertir PDF en Word
type: docs
weight: 10
url: fr/javascript-cpp/convert-pdf-to-doc/
lastmod: "2023-08-04"
description: Apprenez à écrire du code JavaScript pour convertir des PDF en DOC(DOCX) directement sur le Web.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

L'opération de conversion dépend du nombre de pages dans le document et peut être très chronophage. Par conséquent, nous recommandons fortement d'utiliser des Web Workers.

Ce code démontre une manière de décharger les tâches de conversion de fichiers PDF gourmandes en ressources vers un web worker pour éviter de bloquer le thread principal de l'interface utilisateur. Il offre également une manière conviviale de télécharger le fichier converti.

Pour éditer le contenu d'un fichier PDF dans Microsoft Word ou d'autres traitements de texte qui prennent en charge les formats DOC et DOCX. Les fichiers PDF sont modifiables, mais les fichiers DOC et DOCX sont plus flexibles et personnalisables.

{{% alert color="success" %}}
**Essayez de convertir PDF en DOC en ligne**

Aspose.PDF pour JavaScript vous présente une application en ligne gratuite ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Convertir PDF en DOC](/pdf/javascript-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Convertir PDF en DOC

```js

  /*Créer un Web Worker*/
  const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
  AsposePDFWebWorker.onerror = evt => console.log(`Erreur de Web Worker: ${evt.message}`);
  AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
    (evt.data == 'ready') ? 'chargé!' :
      (evt.data.json.errorCode == 0) ? `Résultat:\n${DownloadFile(evt.data.json.fileNameResult, "application/msword", evt.data.params[0])}` : `Erreur: ${evt.data.json.errorText}`;

  /*Gestionnaire d'événement*/
  const ffileToDoc = e => {
    const file_reader = new FileReader();
    file_reader.onload = event => {
      /*Convertir un fichier PDF en Doc et enregistrer le "ResultPDFtoDoc.doc" - Demander à Web Worker*/
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToDoc', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoDoc.doc"] }, [event.target.result]);
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


Le fragment de code JavaScript suivant montre un exemple simple de conversion de pages PDF en fichiers DOC :

1. Sélectionnez un fichier PDF à convertir.
2. Créez un 'FileReader'.
3. La fonction [AsposePdfToDoc](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftodoc/) est exécutée.
4. Le nom du fichier résultant est défini, dans cet exemple "ResultPDFtoDoc.doc".
5. Ensuite, si le 'json.errorCode' est 0, alors votre fichier résultant porte le nom que vous avez spécifié précédemment. Si le paramètre 'json.errorCode' n'est pas égal à 0 et, en conséquence, il y aura une erreur dans votre fichier, alors des informations sur une telle erreur seront contenues dans le fichier 'json.errorText'.
6. En conséquence, la fonction [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) génère un lien et vous permet de télécharger le fichier résultant sur le système d'exploitation de l'utilisateur.

```js

  var ffileToDoc = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*Convertir un fichier PDF en Doc et enregistrer le "ResultPDFtoDoc.doc"*/
      const json = AsposePdfToDoc(event.target.result, e.target.files[0].name, "ResultPDFtoDoc.doc");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*Créer un lien pour télécharger le fichier résultat*/
      DownloadFile(json.fileNameResult, "application/msword");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```


{{% alert color="warning" %}}
**Essayez de convertir PDF en DOCX en ligne**

Aspose.PDF pour JavaScript vous présente l'application en ligne gratuite ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), où vous pouvez essayer d'enquêter sur la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en Word Application Gratuite](/pdf/javascript-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Convertir PDF en DOCX

Aspose.PDF pour JavaScript API vous permet de lire et de convertir des documents PDF en DOCX. DOCX est un format bien connu pour les documents Microsoft Word dont la structure a été changée d'un binaire simple à une combinaison de fichiers XML et binaires. Les fichiers Docx peuvent être ouverts avec Word 2007 et les versions ultérieures, mais pas avec les versions antérieures de MS Word qui prennent en charge les extensions de fichier DOC.

```js

  /*Créer un Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erreur du Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'chargé!' :
        (evt.data.json.errorCode == 0) ? `Résultat:\n${DownloadFile(evt.data.json.fileNameResult, "application/vnd.openxmlformats-officedocument.wordprocessingml.document", evt.data.params[0])}` : `Erreur: ${evt.data.json.errorText}`;

    /*Gestionnaire d'événements*/
    const ffileToDocX = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*convertir un fichier PDF en DocX et enregistrer le "ResultPDFtoDocX.docx" - Demander au Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToDocX', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoDocX.docx"] }, [event.target.result]);
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


The following JavaScript code snippet shows simple example of coverting PDF pages into DOCX files:

1. Sélectionnez un fichier PDF à convertir.
1. Créez un 'FileReader'.
1. La fonction [AsposePdfToDocX](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdftodocx/) est exécutée.
1. Le nom du fichier résultant est défini, dans cet exemple "ResultPDFtoDocX.docx".
1. Ensuite, si le 'json.errorCode' est 0, alors votre fichier résultat porte le nom que vous avez spécifié précédemment. Si le paramètre 'json.errorCode' n'est pas égal à 0 et, par conséquent, il y aura une erreur dans votre fichier, alors des informations sur une telle erreur seront contenues dans le fichier 'json.errorText'.
1. En conséquence, la fonction [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) génère un lien et vous permet de télécharger le fichier résultant sur le système d'exploitation de l'utilisateur.

```js

  var ffileToDocX = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*convertir un fichier PDF en DocX et enregistrer le "ResultPDFtoDocX.docx"*/
      const json = AsposePdfToDocX(event.target.result, e.target.files[0].name, "ResultPDFtoDocX.docx");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*créer un lien pour télécharger le fichier résultat*/
      DownloadFile(json.fileNameResult, "application/vnd.openxmlformats-officedocument.wordprocessingml.document");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```