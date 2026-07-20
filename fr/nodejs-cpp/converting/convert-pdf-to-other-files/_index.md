---
title: Convertir le PDF en EPUB, TeX, texte, XPS dans Node.js
linktitle: Convertir le PDF en d'autres formats
type: docs
weight: 90
url: /fr/nodejs-cpp/convert-pdf-to-other-files/
lastmod: "2026-07-18"
description: Ce sujet vous montre comment convertir un fichier PDF vers d’autres formats de fichier tels que EPUB, LaTeX, Text, XPS, etc. dans l’environnement Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

{{% alert color="success" %}}
**Essayez de convertir PDF en EPUB en ligne**

Aspose.PDF for Node.js vous présente une application en ligne gratuite ["PDF vers EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), où vous pouvez essayer d’enquêter sur la fonctionnalité et la qualité avec laquelle il fonctionne.

[![Aspose.PDF Conversion PDF en EPUB avec une application gratuite](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## Convertir le PDF en EPUB

**<abbr title="Electronic Publication">EPUB</abbr>** est un standard gratuit et ouvert de livre électronique provenant de l'International Digital Publishing Forum (IDPF). Les fichiers portent l'extension .epub.
EPUB est conçu pour un contenu réflowable, ce qui signifie qu’un lecteur EPUB peut optimiser le texte pour un dispositif d’affichage particulier. EPUB prend également en charge le contenu à mise en page fixe. Le format est destiné à être un format unique que les éditeurs et les sociétés de conversion peuvent utiliser en interne, ainsi que pour la distribution et la vente. Il remplace la norme Open eBook.

Dans le cas où vous souhaitez convertir un document PDF, vous pouvez utiliser [AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/) fonction.
Veuillez vérifier le fragment de code suivant afin de le convertir dans un environnement Node.js.

**CommonJS :**

1. Appeler `require` et importer `asposepdfnodejs` module comme `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Appeler `AsposePdf` en tant que Promise et exécuter l'opération de conversion du fichier. Recevoir l'objet en cas de succès.
1. Appelez la fonction [AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/).
1. Convertir le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPDFtoEPUB.epub". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to ePub and save the "ResultPDFtoEPUB.epub"*/
      const json = AsposePdfModule.AsposePdfToEPUB(pdf_file, "ResultPDFtoEPUB.epub");
      console.log("AsposePdfToEPUB => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6 :**

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF qui sera converti
1. Initialisez le module AsposePdf. Recevez l'objet si l'opération réussit.
1. Appelez la fonction [AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/).
1. Convertir le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPDFtoEPUB.epub". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to ePub and save the "ResultPDFtoEPUB.epub"*/
  const json = AsposePdfModule.AsposePdfToEPUB(pdf_file, "ResultPDFtoEPUB.epub");
  console.log("AsposePdfToEPUB => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**Essayez de convertir PDF en LaTeX/TeX en ligne**

Aspose.PDF for Node.js vous présente une application en ligne gratuite ["PDF vers LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), où vous pouvez essayer d’enquêter sur la fonctionnalité et la qualité avec laquelle il fonctionne.

[![Aspose.PDF Conversion PDF en LaTeX/TeX avec une application gratuite](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Convertir le PDF en TeX

**Aspose.PDF for Node.js** prend en charge la conversion de PDF en TeX.
Dans le cas où vous souhaitez convertir un document PDF, vous pouvez utiliser [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/) fonction. 
Veuillez vérifier le fragment de code suivant afin de le convertir dans un environnement Node.js.

**CommonJS :**

1. Appeler `require` et importer `asposepdfnodejs` module comme `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Appeler `AsposePdf` en tant que Promise et exécuter l'opération de conversion du fichier. Recevoir l'objet en cas de succès.
1. Appelez la fonction [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/).
1. Convertir le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPDFtoTeX.tex". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to TeX and save the "ResultPDFtoTeX.tex"*/
      const json = AsposePdfModule.AsposePdfToTeX(pdf_file, "ResultPDFtoTeX.tex");
      console.log("AsposePdfToTeX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6 :**

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF qui sera converti
1. Initialisez le module AsposePdf. Recevez l'objet si l'opération réussit.
1. Appelez la fonction [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/).
1. Convertir le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPDFtoTeX.tex". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to TeX and save the "ResultPDFtoTeX.tex"*/
  const json = AsposePdfModule.AsposePdfToTeX(pdf_file, "ResultPDFtoTeX.tex");
  console.log("AsposePdfToTeX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**Essayez de convertir PDF en texte en ligne**

Aspose.PDF for Node.js vous présente une application en ligne gratuite ["PDF en texte"](https://products.aspose.app/pdf/conversion/pdf-to-txt), où vous pouvez essayer d’enquêter sur la fonctionnalité et la qualité avec laquelle il fonctionne.

[![Aspose.PDF Conversion PDF en texte avec application gratuite](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Convertir PDF en TXT

Dans le cas où vous souhaitez convertir un document PDF, vous pouvez utiliser [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/) fonction. 
Veuillez vérifier le fragment de code suivant afin de le convertir dans un environnement Node.js.

**CommonJS :**

1. Appeler `require` et importer `asposepdfnodejs` module comme `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Appeler `AsposePdf` en tant que Promise et exécuter l'opération de conversion du fichier. Recevoir l'objet en cas de succès.
1. Appelez la fonction [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/).
1. Convertir le fichier PDF. Ainsi, si 'json.errorCode' vaut 0, le résultat de l'opération est enregistré dans "ResultPDFtoTxt.txt". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to Txt and save the "ResultPDFtoTxt.txt"*/
      const json = AsposePdfModule.AsposePdfToTxt(pdf_file, "ResultPDFtoTxt.txt");
      console.log("AsposePdfToTxt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6 :**

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF qui sera converti
1. Initialisez le module AsposePdf. Recevez l'objet si l'opération réussit.
1. Appelez la fonction [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/).
1. Convertir le fichier PDF. Ainsi, si 'json.errorCode' vaut 0, le résultat de l'opération est enregistré dans "ResultPDFtoTxt.txt". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to Txt and save the "ResultPDFtoTxt.txt"*/
  const json = AsposePdfModule.AsposePdfToTxt(pdf_file, "ResultPDFtoTxt.txt");
  console.log("AsposePdfToTxt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**Essayez de convertir PDF en XPS en ligne**

Aspose.PDF for Node.js vous présente une application en ligne gratuite ["PDF vers XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), où vous pouvez essayer d’enquêter sur la fonctionnalité et la qualité avec laquelle il fonctionne.

[![Aspose.PDF Conversion PDF en XPS avec application gratuite](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## Convertir le PDF en XPS

Le type de fichier XPS est principalement associé à la XML Paper Specification de Microsoft Corporation. La XML Paper Specification (XPS), anciennement nom de code Metro et englobant le concept marketing Next Generation Print Path (NGPP), est l'initiative de Microsoft visant à intégrer la création et la visualisation de documents dans le système d'exploitation Windows.

**Aspose.PDF for Node.js** donne la possibilité de convertir des fichiers PDF en <abbr title="XML Paper Specification">XPS</abbr> format. Essayons d'utiliser l'extrait de code présenté pour convertir des fichiers PDF au format XPS avec Node.js.

Dans le cas où vous souhaitez convertir un document PDF, vous pouvez utiliser [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/) fonction. 
Veuillez vérifier le fragment de code suivant afin de le convertir dans un environnement Node.js.

**CommonJS :**

1. Appeler `require` et importer `asposepdfnodejs` module comme `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Appeler `AsposePdf` en tant que Promise et exécuter l'opération de conversion du fichier. Recevoir l'objet en cas de succès.
1. Appelez la fonction [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/).
1. Convertir le fichier PDF. Ainsi, si \u0027json.errorCode\u0027 est 0, le résultat de l'opération est enregistré dans \u0022ResultPDFtoXps.xps\u0022. Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans \u0027json.errorText\u0027.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to Xps and save the "ResultPDFtoXps.xps"*/
      const json = AsposePdfModule.AsposePdfToXps(pdf_file, "ResultPDFtoXps.xps");
      console.log("AsposePdfToXps => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6 :**

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Initialisez le module AsposePdf. Recevez l'objet si l'opération réussit.
1. Appelez la fonction [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/).
1. Convertir le fichier PDF. Ainsi, si \u0027json.errorCode\u0027 est 0, le résultat de l'opération est enregistré dans \u0022ResultPDFtoXps.xps\u0022. Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans \u0027json.errorText\u0027.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to Xps and save the "ResultPDFtoXps.xps"*/
  const json = AsposePdfModule.AsposePdfToXps(pdf_file, "ResultPDFtoXps.xps");
  console.log("AsposePdfToXps => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

## Convertir le PDF en PDF en niveaux de gris

Convertir le PDF en noir et blanc avec Aspose.PDF for Node.js via C++. 
Pourquoi devrais-je convertir un PDF en niveaux de gris ? Si le fichier PDF contient de nombreuses images couleur et que la taille du fichier est importante plutôt que la couleur, la conversion permet d'économiser de l'espace. Si vous imprimez un fichier PDF en noir et blanc, la conversion vous permettra de vérifier visuellement à quoi ressemble le résultat final. 

Dans le cas où vous souhaitez convertir un document PDF, vous pouvez utiliser [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/) fonction. 
Veuillez vérifier le fragment de code suivant afin de le convertir dans un environnement Node.js.

**CommonJS :**

1. Appeler `require` et importer `asposepdfnodejs` module comme `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Appeler `AsposePdf` en tant que Promise et exécuter l'opération de conversion du fichier. Recevoir l'objet en cas de succès.
1. Appelez la fonction [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/).
1. Convertir le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultConvertToGrayscale.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

const AsposePdf = require('asposepdfnodejs');
const pdf_file = 'Aspose.pdf';
AsposePdf().then(AsposePdfModule => {
    /*Convert a PDF-file to grayscale and save the "ResultConvertToGrayscale.pdf"*/
    const json = AsposePdfModule.AsposePdfConvertToGrayscale(pdf_file, "ResultConvertToGrayscale.pdf");
    console.log("AsposePdfConvertToGrayscale => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
});
```

**ECMAScript/ES6 :**

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Initialisez le module AsposePdf. Recevez l'objet si l'opération réussit.
1. Appelez la fonction [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/).
1. Convertir le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultConvertToGrayscale.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to grayscale and save the "ResultConvertToGrayscale.pdf"*/
  const json = AsposePdfModule.AsposePdfConvertToGrayscale(pdf_file, "ResultConvertToGrayscale.pdf");
  console.log("AsposePdfConvertToGrayscale => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```






