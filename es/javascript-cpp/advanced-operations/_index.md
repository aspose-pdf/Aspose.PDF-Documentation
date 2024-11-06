---
title: Operaciones avanzadas usando JavaScript a través de C++
linktitle: Operaciones avanzadas
type: docs
weight: 60
url: es/javascript-cpp/advanced-operations/
description: Aspose.PDF para JavaScript a través de C++ no solo puede realizar tareas simples y fáciles, sino también abordar objetivos más complejos. Consulta la siguiente sección para usuarios avanzados y desarrolladores.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Operaciones Avanzadas** es una sección sobre cómo manejar archivos PDF existentes de manera programática, ya sean documentos creados con Aspose.PDF como se discutió en [Operaciones Básicas](/pdf/javascript-cpp/basic-operations/), o PDFs creados con Adobe Acrobat, Google Docs, Microsoft Office, Open Office o cualquier otro productor de PDF.

## Usando Web Workers

La versión 23.6 añadió la capacidad de usar Web Workers:

```js
const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
```

El uso de Web Workers desde JavaScript a través de C++, te permite realizar operaciones sin bloquear la interfaz, en un hilo de trabajo separado.

Web Workers es una herramienta simple para ejecutar scripts en segundo plano. Lo que permite realizar tareas sin interferir con la interfaz de usuario, en un hilo de trabajo separado.

Aprenderás diferentes maneras de:

- [Trabajar con Documentos](/pdf/javascript-cpp/working-with-documents/) - comprimir, dividir y combinar documentos y realizar otras operaciones con el documento completo.
- [Trabajar con Páginas](/pdf/javascript-cpp/working-with-pages/) - agregar, mover o eliminar, recortar páginas, sellos.
- [Metadatos en PDFs](/pdf/javascript-cpp/pdf-file-metadata/) - obtener o establecer metadatos en documentos.
- [Trabajar con Imágenes](/pdf/javascript-cpp/working-with-images/) - insertar, eliminar, extraer imagen en documento
- [Navegación e Interacción](/pdf/javascript-cpp/navigation-and-interaction/) - manejar acciones, marcadores, navegar páginas
- [Anotaciones](/pdf/javascript-cpp/annotations/) - Las anotaciones permiten a los usuarios agregar contenido personalizado en las páginas PDF. Puedes agregar, eliminar y modificar la anotación de los documentos PDF.

- [Protección y Firma](/pdf/javascript-cpp/securing-and-signing/) - proteger y firmar tu documento PDF programáticamente
- [Attachments](/pdf/javascript-cpp/attachments/) - Los documentos PDF pueden contener archivos adjuntos. Estos archivos adjuntos pueden ser otros documentos PDF, o cualquier tipo de archivo, como archivos de audio, documentos de Microsoft Office, etc. Aprenderás cómo añadir archivos adjuntos a un PDF, obtener la información de un archivo adjunto, guardarlo en un archivo, y eliminar el archivo adjunto del PDF programáticamente con JavaScript.