---
title: Extraire des images du PDF JavaScript
linktitle: Extraire des images du PDF
type: docs
weight: 20
url: fr/javascript-cpp/extract-images-from-the-pdf-file/
description: Comment extraire une partie de l'image d'un PDF en utilisant l'outil Aspose.PDF pour JavaScript.
lastmod: "2023-09-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

L'outil Web d'Aspose.PDF vous permet d'extraire facilement des images des fichiers PDF.

Si vous souhaitez extraire des images d'un document PDF, vous pouvez utiliser la fonction [AsposePdfExtractImage](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextractimage/).
Veuillez consulter l'extrait de code suivant afin d'extraire des images d'un fichier PDF en utilisant JavaScript via C++.

1. Créez un 'FileReader'.
1. La fonction [AsposePdfExtractImage](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextractimage/) est exécutée.
1. Le nom du fichier résultant est défini, dans cet exemple "ResultPdfExtractImage{0:D2}.jpg".

1. Ensuite, si le 'json.errorCode' est 0, vous pouvez obtenir des liens vers les fichiers résultants. Si le paramètre 'json.errorCode' n'est pas égal à 0 et, en conséquence, il y aura une erreur dans votre fichier, alors des informations sur cette erreur seront contenues dans le fichier 'json.errorText'.
1. En conséquence, la fonction [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) génère un lien et vous permet de télécharger le fichier résultant sur le système d'exploitation de l'utilisateur.

```js

    var ffileExtractImage = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
    /*Extraire l'image à partir d'un fichier PDF avec le modèle "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format numéro de page), résolution 150 DPI et sauvegarder*/
    const json = AsposePdfExtractImage(event.target.result, e.target.files[0].name, "ResultPdfExtractImage{0:D2}.jpg", 150);
    if (json.errorCode == 0) {
        document.getElementById('output').textContent = "Nombre de fichiers(images) : " + json.filesCount.toString();
        /*Créer des liens vers les fichiers résultants*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/jpeg");
    }
    else document.getElementById('output').textContent = json.errorText;
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


## Utilisation des Web Workers

```js

  /*Créer un Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erreur du Web Worker : ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'chargé!' :
        (evt.data.json.errorCode == 0) ? 
          `Nombre de fichiers(images) : ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/jpeg", element) ) ?? ""}` : 
          `Erreur : ${evt.data.json.errorText}`;

    /*Gestionnaire d'événements*/
    const ffileExtractImage = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Extraire l'image d'un fichier PDF avec le modèle "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format du numéro de page), résolution 150 DPI et enregistrer*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfExtractImage', "params": [event.target.result, e.target.files[0].name, "ResultPdfExtractImage{0:D2}.jpg", 150] }, [event.target.result]);
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