---
title: Dividir PDF usando JavaScript
linktitle: Dividir archivos PDF
type: docs
weight: 30
url: /es/javascript-cpp/split-pdf/
description: Este tema muestra cómo dividir páginas PDF en archivos PDF individuales con Aspose.PDF para JavaScript a través de C++.
lastmod: "2022-12-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Dividir PDF en dos archivos usando JavaScript

Este tema muestra cómo dividir páginas PDF en archivos PDF individuales usando JavaScript. Actualmente, apoyamos la división en dos partes. Esto significa que `pageToSplit` es un marcador para la división. El primer archivo contendrá todas las páginas desde 1 hasta `pageToSplit` inclusivamente, y el segundo archivo tendrá el resto de las páginas.

La operación de división depende del número de páginas en el documento y puede ser muy lenta. Por lo tanto, recomendamos encarecidamente usar Web Workers.

El fragmento de código proporcionado es un ejemplo de uso de un Web Worker en JavaScript para dividir un archivo PDF en dos archivos PDF separados y ofrecer al usuario la opción de descargar los archivos resultantes.
 Aquí están los pasos del código:

1. Creación de un Web Worker. Un web worker se inicializa utilizando el archivo de script "AsposePDFforJS.js". Este web worker manejará las tareas de división de archivos PDF en segundo plano. En nuestro ejemplo, cualquier error que ocurra en el worker se captura y se registra en la consola.
2. Manejo de Mensajes. El web worker está configurado para escuchar mensajes utilizando el controlador de eventos onmessage. Cuando recibe un mensaje de la página web, procesa la solicitud y envía una respuesta de vuelta al hilo principal.
3. Manejador de Eventos de División de Archivos. Hay un manejador de eventos ffileSplit que se activa cuando un usuario selecciona un archivo PDF para dividir. Lee el archivo PDF seleccionado usando un FileReader y envía el contenido del archivo y los parámetros relevantes (como el número de páginas para dividir y los nombres de los archivos de salida) al web worker a través de una llamada postMessage.
1. Función de Descargar Archivo. La función [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) es responsable de generar un enlace que permite al usuario descargar un archivo. Acepta el nombre del archivo, el tipo MIME y el contenido del archivo. La función crea un enlace de descarga, asocia el contenido del archivo con él, establece el nombre del archivo y lo agrega al documento. Esto permite al usuario descargar los archivos PDF resultantes.

1. Manejo de Mensajes en el Trabajador Web. A continuación, si el 'json.errorCode' es 0, entonces json.fileNameResult contendrá el nombre que especificaste anteriormente. Si el parámetro 'json.errorCode' no es igual a 0 y, en consecuencia, hay un error en tu archivo, entonces la información sobre dicho error se encontrará en la propiedad 'json.errorText'.

1. Mostrar Resultado. La página principal incluye un elemento con el ID 'output'. Cuando el trabajador web envía un mensaje con el resultado, actualiza el elemento 'output'. Si la operación es exitosa, muestra enlaces de descarga para los dos archivos PDF divididos. Si hay un error, muestra un mensaje de error.

Este código demuestra una forma de descargar tareas intensivas en recursos de división de archivos PDF a un trabajador web para evitar bloquear el hilo principal de la interfaz de usuario. También ofrece una manera amigable para el usuario de descargar los archivos PDF divididos.

```js

    /*Crear Trabajador Web*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Error del Trabajador Web: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '¡cargado!' :
        (evt.data.json.errorCode == 0) ?
          `Resultado:\n${DownloadFile(evt.data.json.fileNameResult1, "application/pdf", evt.data.params[0])}
                  \n${DownloadFile(evt.data.json.fileNameResult2, "application/pdf", evt.data.params[1])}` :
          `Error: ${evt.data.json.errorText}`;

    /*Manejador de eventos*/
    const ffileSplit = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Establecer el número de página para dividir*/
        const pageToSplit = 1;
        /*Dividir en dos archivos PDF y guardar "ResultSplit1.pdf", "ResultSplit2.pdf" - Preguntar al Trabajador Web*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfSplit2Files',
            "params": [event.target.result, e.target.files[0].name, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Crear un enlace para descargar el archivo de resultado*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "Haz clic aquí para descargar el archivo " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```

El siguiente fragmento de código JavaScript muestra un ejemplo simple de cómo dividir páginas de un PDF en archivos PDF individuales:

1. Seleccione un archivo PDF para dividir.
1. Cree un objeto 'FileReader' en el manejador.
1. Establezca el número de página para dividir.
1. Llame a [AsposePdfSplit2Files](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfsplit2files/) en el último manejador.
1. Analice el resultado. El nombre del archivo resultante se establece, en este ejemplo "ResultSplit2.pdf".
1. A continuación, si el 'json.errorCode' es 0, entonces json.fileNameResult contendrá el nombre que especificó anteriormente. Si el parámetro 'json.errorCode' no es igual a 0 y, en consecuencia, hay un error en su archivo, entonces la información sobre dicho error se encontrará en la propiedad 'json.errorText'.
1. Puede usar la función auxiliar [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/).

```js

  var ffileSplit = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*Establezca el número de página para dividir*/
      const pageToSplit = 1;
      /*Divida en dos archivos PDF y guarde el "ResultSplit1.pdf", "ResultSplit2.pdf"*/
      const json = AsposePdfSplit2Files(event.target.result, e.target.files[0].name, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = e.target.files[0].name + " dividido: " + json.fileNameResult1 + ", " + json.fileNameResult2;
      else document.getElementById('output').textContent = json.errorText;
      /*Hacer un enlace para descargar el primer archivo resultante*/
      DownloadFile(json.fileNameResult1, "application/pdf");
      /*Hacer un enlace para descargar el segundo archivo resultante*/
      DownloadFile(json.fileNameResult2, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```