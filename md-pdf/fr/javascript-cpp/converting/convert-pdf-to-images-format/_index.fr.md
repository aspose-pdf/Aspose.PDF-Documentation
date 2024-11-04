---
title: Convertir un PDF en Formats d'Image en JavaScript
linktitle: Convertir un PDF en Images
type: docs
weight: 70
url: /javascript-cpp/convert-pdf-to-images-format/
lastmod: "2023-11-01"
description: Ce sujet vous montre comment utiliser Aspose.PDF pour convertir un PDF en divers formats d'images tels que TIFF, BMP, JPEG, PNG, SVG avec quelques lignes de code.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## JavaScript Convertir un PDF en Image

Dans cet article, nous vous montrerons les options pour convertir un PDF en formats d'image.

Les documents précédemment numérisés sont souvent enregistrés au format fichier PDF. Cependant, avez-vous besoin de l'éditer dans un éditeur graphique ou de l'envoyer sous forme d'image? Nous avons un outil universel pour vous permettre de convertir un PDF en images en utilisant 
La tâche la plus courante est lorsque vous devez enregistrer un document PDF entier ou certaines pages spécifiques d'un document sous forme d'un ensemble d'images. **Aspose pour JavaScript via C++** vous permet de convertir un PDF en formats JPG et PNG pour simplifier les étapes nécessaires pour obtenir vos images à partir d'un fichier PDF spécifique.

**Aspose.PDF pour JavaScript via C++** prend en charge la conversion de PDF en divers formats d'image.
 Veuillez vérifier la section [Formats de fichiers pris en charge par Aspose.PDF](https://docs.aspose.com/pdf/javascript-cpp/supported-file-formats/).

L'opération de conversion dépend du nombre de pages dans le document et peut être très chronophage. Par conséquent, nous recommandons fortement d'utiliser des Web Workers.

Ce code démontre une façon de déléguer les tâches de conversion de fichiers PDF gourmandes en ressources à un web worker pour éviter de bloquer le thread principal de l'interface utilisateur. Il offre également un moyen convivial de télécharger le fichier converti.

{{% alert color="success" %}}
**Essayez de convertir un PDF en JPEG en ligne**

Aspose.PDF pour JavaScript vous présente une application gratuite en ligne ["PDF to JPEG"](https://products.aspose.app/pdf/conversion/pdf-to-jpg), où vous pouvez essayer d'étudier la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF conversion PDF en JPEG avec application gratuite](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

## Convertir un PDF en JPEG

```js

  /*Créer un Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erreur du Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'chargé!' :
        (evt.data.json.errorCode == 0) ? 
          `Nombre de fichiers (pages) : ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/jpeg", element) ) ?? ""}` : 
          `Erreur: ${evt.data.json.errorText}`;

    /*Gestionnaire d'événement*/
    const ffileToJpg = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const password = 'owner';
        /*convertir un fichier PDF en fichiers jpg avec le modèle "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format numéro de page), résolution 150 DPI et enregistrer - Demander au Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToJpg', "params": [event.target.result, e.target.files[0].name, "ResultPdfToJpg{0:D2}.jpg", 150] }, [event.target.result]);
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

Le snippet de code JavaScript suivant montre un exemple simple de conversion de pages PDF en fichiers Jpeg :

1. Sélectionnez un fichier PDF à convertir.
1. Créez un 'FileReader'.
1. La fonction [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfpagestojpg/) est exécutée.
1. Le nom du fichier résultant est défini, dans cet exemple "ResultPdfToJpg{0:D2}.jpg".
1. Ensuite, si le 'json.errorCode' est 0, alors votre fichier résultant reçoit le nom que vous avez spécifié précédemment. Si le paramètre 'json.errorCode' n'est pas égal à 0 et qu'il y a donc une erreur dans votre fichier, alors l'information sur cette erreur sera contenue dans le fichier 'json.errorText'.
1. En conséquence, la fonction [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) génère un lien et vous permet de télécharger le fichier résultant sur le système d'exploitation de l'utilisateur.

```js

  var ffileToJpg = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*convertir un fichier PDF en fichiers jpg avec le modèle "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format numéro de page), résolution 150 DPI et enregistrer*/
      const json = AsposePdfPagesToJpg(event.target.result, e.target.files[0].name, "ResultPdfToJpg{0:D2}.jpg", 150);
      if (json.errorCode == 0) {
        document.getElementById('output').textContent = "Nombre de fichiers(pages) : " + json.filesCount.toString();
        /*créer des liens vers les fichiers résultants*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/jpeg");
      }
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

```


{{% alert color="success" %}}
**Essayez de convertir PDF en TIFF en ligne**

Aspose.PDF pour JavaScript vous présente une application en ligne gratuite ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Conversion Aspose.PDF PDF en TIFF avec une application gratuite](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## Convertir PDF en TIFF

```js

  /*Créer un Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erreur du Web Worker : ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'chargé!' :
        (evt.data.json.errorCode == 0) ? 
          `Nombre de fichiers (pages) : ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/tiff", element) ) ?? ""}` : 
          `Erreur : ${evt.data.json.errorText}`;

    /*Gestionnaire d'événements*/
    const ffileToTiff = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Convertir un fichier PDF en TIFF avec le modèle "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... format numéro de page), résolution 150 DPI et sauvegarder - Demander au Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToTiff', "params": [event.target.result, e.target.files[0].name, "ResultPdfToTiff{0:D2}.tiff", 150] }, [event.target.result]);
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


Le fragment de code JavaScript suivant montre un exemple simple de conversion de pages PDF en fichiers Tiff :

1. Sélectionnez un fichier PDF à convertir.
1. Créez un 'FileReader'.
1. La fonction [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestotiff/) est exécutée.
1. Le nom du fichier résultant est défini, dans cet exemple "ResultPdfToTiff{0:D2}.tiff".
1. Ensuite, si le 'json.errorCode' est 0, alors votre DownloadFile reçoit le nom que vous avez spécifié précédemment. Si le paramètre 'json.errorCode' n'est pas égal à 0 et, par conséquent, il y aura une erreur dans votre fichier, alors des informations sur une telle erreur seront contenues dans le fichier 'json.errorText'.
1. En conséquence, la fonction [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) génère un lien et vous permet de télécharger le fichier résultant sur le système d'exploitation de l'utilisateur.

```js

    var ffileToTiff = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Convertir un fichier PDF en TIFF avec le modèle "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... numéro de page au format), résolution 150 DPI et enregistrer*/
        const json = AsposePdfPagesToTiff(event.target.result, e.target.files[0].name, "ResultPdfToTiff{0:D2}.tiff", 150);
        if (json.errorCode == 0) {
          document.getElementById('output').textContent = "Nombre de fichiers(pages) : " + json.filesCount.toString();
          /*Créer des liens vers les fichiers résultants*/
          for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/tiff");
        }
        else document.getElementById('output').textContent = json.errorText;
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```


{{% alert color="success" %}}
**Essayez de convertir PDF en PNG en ligne**

À titre d'exemple de fonctionnement de nos applications gratuites, veuillez vérifier la fonctionnalité suivante.

Aspose.PDF pour JavaScript vous présente une application en ligne gratuite ["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Comment convertir PDF en PNG en utilisant l'application gratuite](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Convertir PDF en PNG

```js

  /*Créer un Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erreur du Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'chargé!' :
        (evt.data.json.errorCode == 0) ? 
          `Nombre de fichiers (pages) : ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/png", element) ) ?? ""}` : 
          `Erreur: ${evt.data.json.errorText}`;

    /*Gestionnaire d'événements*/
    const ffileToPng = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const password = 'propriétaire';
        /*convertir un fichier PDF en fichiers png avec le modèle "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... format numéro de page), résolution 150 DPI et enregistrer - Demander au Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToPng', "params": [event.target.result, e.target.files[0].name, "ResultPdfToPng{0:D2}.png", 150] }, [event.target.result]);
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


Le code JavaScript suivant montre un exemple simple de conversion de pages PDF en fichiers PNG :

1. Sélectionnez un fichier PDF à convertir.
1. Créez un 'FileReader'.
1. La fonction [AsposePdfPagesToPng](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfpagestopng/) est exécutée.
1. Le nom du fichier résultant est défini, dans cet exemple "ResultPdfToPng{0:D2}.png".
1. Ensuite, si 'json.errorCode' est 0, alors votre DownloadFile porte le nom que vous avez spécifié précédemment. Si le paramètre 'json.errorCode' n'est pas égal à 0 et, en conséquence, il y aura une erreur dans votre fichier, alors les informations sur une telle erreur seront contenues dans le fichier 'json.errorText'.
1. En conséquence, la fonction [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) génère un lien et vous permet de télécharger le fichier résultant sur le système d'exploitation de l'utilisateur.

```js

  var ffileToPng = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*convertir un fichier PDF en fichiers png avec le modèle "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... numéro de page au format), résolution 150 DPI et sauvegarder*/
      const json = AsposePdfPagesToPng(event.target.result, e.target.files[0].name, "ResultPdfToPng{0:D2}.png", 150);
      if (json.errorCode == 0) {
        document.getElementById('output').textContent = "Nombre de fichiers (pages) : " + json.filesCount.toString();
        /*créer des liens vers les fichiers résultants*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/png");
      }
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

```


{{% alert color="success" %}}
**Essayez de convertir un PDF en SVG en ligne**

Aspose.PDF pour JavaScript vous présente l'application en ligne gratuite ["PDF en SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Conversion Aspose.PDF de PDF en SVG avec l'application gratuite](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** est une famille de spécifications d'un format de fichier basé sur XML pour les graphiques vectoriels bidimensionnels, à la fois statiques et dynamiques (interactifs ou animés). La spécification SVG est un standard ouvert qui est en développement par le World Wide Web Consortium (W3C) depuis 1999.

## Convertir PDF en SVG

```js

  /*Créer un Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erreur du Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'chargé!' :
        (evt.data.json.errorCode == 0) ? 
          `Nombre de fichiers (pages): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/svg", element) ) ?? ""}` : 
          `Erreur: ${evt.data.json.errorText}`;

    /*Gestionnaire d'événements*/
    const ffileToSvg = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Convertir un fichier PDF en SVG - Demander au Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToSvg', "params": [event.target.result, e.target.files[0].name, "ResultPdfToSvg.svg"] }, [event.target.result]);
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


Le fragment de code JavaScript suivant montre un exemple simple de conversion de pages PDF en fichiers SVG :

1. Sélectionnez un fichier PDF à convertir.
2. Créez un 'FileReader'.
3. La fonction [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestosvg/) est exécutée.
4. Le nom du fichier résultant est défini, dans cet exemple "ResultPdfToSvg.svg".
5. Ensuite, si le 'json.errorCode' est 0, alors votre DownloadFile est donné le nom que vous avez spécifié précédemment. Si le paramètre 'json.errorCode' n'est pas égal à 0 et qu'il y aura donc une erreur dans votre fichier, alors des informations sur une telle erreur seront contenues dans le fichier 'json.errorText'.
6. En conséquence, la fonction [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) génère un lien et vous permet de télécharger le fichier résultant sur le système d'exploitation de l'utilisateur.

```js

    var ffileToSvg = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Convertir un fichier PDF en SVG*/
        const json = AsposePdfPagesToSvg(event.target.result, e.target.files[0].name, "ResultPdfToSvg.svg");
        if (json.errorCode == 0) {
          document.getElementById('output').textContent = "Nombre de fichiers (pages) : " + json.filesCount.toString();
          /*Créer des liens vers les fichiers résultants*/
          for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/svg");
        }
        else document.getElementById('output').textContent = json.errorText;
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


### Convertir PDF en SVG zippé

```js

  /*Créer un Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erreur du Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'chargé!' :
        (evt.data.json.errorCode == 0) ? `Résultat:\n${DownloadFile(evt.data.json.fileNameResult, "application/zip", evt.data.params[0])}` : `Erreur: ${evt.data.json.errorText}`;

    /*Gestionnaire d'événement*/
    const ffileToSvgZip = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Convertir un fichier PDF en SVG(zip) et enregistrer le "ResultPdfToSvgZip.zip" - Demander au Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToSvgZip', "params": [event.target.result, e.target.files[0].name, "ResultPdfToSvgZip.zip"] }, [event.target.result]);
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


Le code JavaScript suivant montre un exemple simple de conversion de pages PDF en fichiers SVG(zip) :

1. Sélectionnez un fichier PDF à convertir.
2. Créez un 'FileReader'.
3. La fonction [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestosvgzip/) est exécutée.
4. Le nom du fichier résultant est défini, dans cet exemple "ResultPdfToSvgZip.zip".
5. Ensuite, si le 'json.errorCode' est 0, alors votre DownloadFile reçoit le nom que vous avez spécifié précédemment. Si le paramètre 'json.errorCode' n'est pas égal à 0 et qu'il y a, en conséquence, une erreur dans votre fichier, alors l'information sur cette erreur sera contenue dans le fichier 'json.errorText'.
6. En conséquence, la fonction [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) génère un lien et vous permet de télécharger le fichier résultant sur le système d'exploitation de l'utilisateur.

```js

    var ffileToSvgZip = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Convertir un fichier PDF en SVG(zip) et enregistrer le "ResultPdfToSvgZip.zip"*/
        const json = AsposePdfPagesToSvgZip(event.target.result, e.target.files[0].name, "ResultPdfToSvgZip.zip");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Créer un lien pour télécharger le fichier résultant*/
        DownloadFile(json.fileNameResult, "application/zip");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


## Convertir PDF en DICOM

```js

  /*Créer un Web Worker*/
  const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
  AsposePDFWebWorker.onerror = evt => console.log(`Erreur du Web Worker: ${evt.message}`);
  AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
    (evt.data == 'ready') ? 'chargé!' :
      (evt.data.json.errorCode == 0) ?
        `Nombre de fichiers (pages): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
          (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "application/dicom", element) ) ?? ""}` :
        `Erreur: ${evt.data.json.errorText}`;

  /*Gestionnaire d'événement*/
  const ffileToDICOM = e => {
    const file_reader = new FileReader();
    file_reader.onload = event => {
      /*Convertir un fichier PDF en DICOM avec le modèle "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... format numéro de page), résolution 150 DPI et enregistrer - Demander au Web Worker*/
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToDICOM', "params": [event.target.result, e.target.files[0].name, "ResultPdfToDICOM{0:D2}.dcm", 150] }, [event.target.result]);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

  /*Créer un lien pour télécharger le fichier de résultat*/
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


Le fragment de code JavaScript suivant montre un exemple simple de conversion de pages PDF en fichiers DICOM :

1. Sélectionnez un fichier PDF à convertir.
2. Créez un 'FileReader'.
3. La fonction [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestodicom/) est exécutée.
4. Le nom du fichier résultant est défini, dans cet exemple "ResultPdfToDICOM{0:D2}.dcm".
5. Ensuite, si le 'json.errorCode' est 0, alors votre fichier résultant reçoit le nom que vous avez spécifié précédemment. Si le paramètre 'json.errorCode' n'est pas égal à 0 et, en conséquence, il y aura une erreur dans votre fichier, alors des informations sur une telle erreur seront contenues dans le fichier 'json.errorText'.
6. En conséquence, la fonction [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) génère un lien et vous permet de télécharger le fichier résultant sur le système d'exploitation de l'utilisateur.

```js

  var ffileToDICOM = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*Convertir un fichier PDF en DICOM avec le modèle "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... numéro de page au format), résolution 150 DPI et sauvegarder*/
      const json = AsposePdfPagesToDICOM(event.target.result, e.target.files[0].name, "ResultPdfToDICOM{0:D2}.dcm", 150);
      if (json.errorCode == 0) {
        document.getElementById('output').textContent = "Nombre de fichiers(pages) : " + json.filesCount.toString();
        /*Créer des liens vers les fichiers résultats*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "application/dicom");
      }
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


## Convertir PDF en BMP

```js

    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erreur du Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'chargé!' :
        (evt.data.json.errorCode == 0) ? 
          `Nombre de fichiers(pages): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/bmp", element) ) ?? ""}` : 
          `Erreur: ${evt.data.json.errorText}`;

    /*Gestionnaire d'événements*/
    const ffileToBmp = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Convertir un fichier PDF en BMP avec le modèle "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... numéro de page au format), résolution 150 DPI et enregistrer - Demander au Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToBmp', "params": [event.target.result, e.target.files[0].name, "ResultPdfToBmp{0:D2}.bmp", 150] }, [event.target.result]);
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


Le snippet de code JavaScript suivant montre un exemple simple de conversion de pages PDF en fichiers BMP :

1. Sélectionnez un fichier PDF à convertir.
1. Créez un 'FileReader'.
1. La fonction [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestobmp/) est exécutée.
1. Le nom du fichier résultant est défini, dans cet exemple "ResultPdfToBmp{0:D2}.bmp".
1. Ensuite, si le 'json.errorCode' est 0, alors votre DownloadFile reçoit le nom que vous avez spécifié précédemment. Si le paramètre 'json.errorCode' n'est pas égal à 0 et, en conséquence, il y aura une erreur dans votre fichier, alors des informations sur une telle erreur seront contenues dans le fichier 'json.errorText'.
1. En conséquence, la fonction [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) génère un lien et vous permet de télécharger le fichier résultant sur le système d'exploitation de l'utilisateur.

```js

    var ffileToBmp = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Convertir un fichier PDF en BMP avec le modèle "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... format numéro de page), résolution 150 DPI et enregistrer*/
        const json = AsposePdfPagesToBmp(event.target.result, e.target.files[0].name, "ResultPdfToBmp{0:D2}.bmp", 150);
        if (json.errorCode == 0) {
          document.getElementById('output').textContent = "Nombre de fichiers(pages) : " + json.filesCount.toString();
          /*Créer des liens vers les fichiers résultants*/
          for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/bmp");
        }
        else document.getElementById('output').textContent = json.errorText;
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```