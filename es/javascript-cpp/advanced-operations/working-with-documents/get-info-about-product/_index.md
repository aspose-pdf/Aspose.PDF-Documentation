---
title: Obtener información sobre el Producto usando JavaScript
linktitle: Obtener información sobre el Producto
type: docs
weight: 70
url: /es/javascript-cpp/get-info-about-product/
description: Este tema muestra cómo obtener información sobre el Producto con Aspose.PDF para JavaScript vía C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Este tema explica cómo obtener información sobre el Producto usando JavaScript.

```js

    /*Crear Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Error desde Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '¡cargado!' :
        (evt.data.json.errorCode !== 0) ? `Error: ${evt.data.json.errorText}` :
                          "Producto     : " + evt.data.json.product
                      + "\nFamilia      : " + evt.data.json.family
                      + "\nVersión      : " + evt.data.json.version
                      + "\nFecha de lanzamiento : " + evt.data.json.releasedate
                      + "\nProductor    : " + evt.data.json.producer
                      + "\nEstá licenciado : " + evt.data.json.islicensed;

    /*Manejador de eventos*/
    const onAsposePdfAbout = e => {
      /*Obtener información sobre el Producto - Preguntar al Web Worker*/
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfAbout', "params": [] }, []);
    };
```


El siguiente fragmento de código JavaScript muestra un ejemplo simple de cómo obtener información sobre el Producto:

1. Se ejecuta la función [AsposePdfAbout](https://reference.aspose.com/pdf/javascript-cpp/misc/asposepdfabout/).
1. Información del Producto que se puede obtener:
- Nombre del producto
- Familia del producto
- Versión del producto
- Fecha de lanzamiento
- Nombre completo/productor
- El producto está licenciado
1. A continuación, si el 'json.errorCode' es 0, entonces puedes obtener información sobre el Producto. Si el parámetro 'json.errorCode' no es igual a 0 y, en consecuencia, hay un error en tu archivo, entonces la información sobre dicho error se encontrará en el archivo 'json.errorText'.

```js

  var onAsposePdfAbout = function () {
    /*Obtener información sobre el Producto*/
    const json = AsposePdfAbout();
    /* JSON
    Nombre del producto       : json.product
    Familia del producto      : json.family
    Versión del producto      : json.version
    Fecha de lanzamiento      : json.releasedate
    Nombre completo/productor : json.producer
    El producto está licenciado: json.islicensed
    */
    if (json.errorCode == 0) document.getElementById('output').textContent = 
                    "Producto     : " + json.product
                + "\nFamilia      : " + json.family
                + "\nVersión      : " + json.version
                + "\nFecha de lanzamiento : " + json.releasedate
                + "\nProductor    : " + json.producer
                + "\nEstá licenciado  : " + json.islicensed;
    else document.getElementById('output').textContent = json.errorText;
  }
```