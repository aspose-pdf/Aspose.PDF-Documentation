---
title: PdfFileEditor Class
type: docs
weight: 10
url: /es/net/pdffileeditor-class/
description: Esta sección explica cómo trabajar con Aspose.PDF Facades usando la clase PdfFileEditor.
lastmod: "2021-06-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Trabajar con documentos PDF incluye varias funciones. Gestionar las páginas de un archivo PDF es una parte importante de este trabajo. Aspose.PDF.Facaded proporciona la clase `PdfFileEditor` para este propósito.

La clase PdfFileEditor contiene los métodos que ayudan a manipular páginas individuales; esta clase no edita ni manipula los contenidos de una página. Puedes insertar una nueva página, eliminar una página existente, dividir las páginas o puedes especificar la imposición de las páginas usando PdfFileEditor.

Las características proporcionadas por esta clase se pueden dividir en tres categorías principales, es decir, Edición de Archivos, Imposición de PDF y División. Vamos a discutir estas secciones en detalle a continuación:

## Edición de Archivos

Las características que podemos incluir en esta sección son Insertar, Añadir, Eliminar, Concatenar y Extraer. Puedes insertar una nueva página en una ubicación especificada usando el método Insert, o agregar las páginas al final del archivo. También puedes eliminar cualquier número de páginas del archivo usando el método Delete, especificando un array de enteros que contenga los números de las páginas a eliminar. El método Concatenate te ayuda a unir páginas de múltiples archivos PDF. Puedes extraer cualquier número de páginas usando el método Extract, y guardar estas páginas en otro archivo PDF o flujo de memoria.

Esta sección explora las capacidades de esta clase y explica el propósito de sus métodos.

- [Concatenar documentos PDF](/pdf/es/net/concatenate-pdf-documents/)
- [Extraer páginas de PDF](/pdf/es/net/extract-pdf-pages/)
- [Insertar páginas de PDF](/pdf/es/net/insert-pdf-pages/)
- [Eliminar páginas de PDF](/pdf/es/net/delete-pdf-pages/)

## Usando Saltos de Página

El Salto de Página es una característica especial que permite el reflujo del documento.

- [Salto de Página en PDF existente](/pdf/es/net/page-break-in-existing-pdf/)

## Imposición de PDF

La imposición es el proceso de organizar las páginas correctamente antes de imprimir. `PdfFileEditor` proporciona dos métodos para este propósito, es decir, `MakeBooklet` y `MakeNUp`. El método MakeBooklet ayuda a organizar las páginas de manera que sea fácil doblarlas o encuadernarlas después de imprimirlas, sin embargo, el método MakeNUp permite imprimir múltiples páginas en una sola página del archivo PDF.

- [Crear folleto de PDF](/pdf/es/net/make-booklet-of-pdf/)
- [Crear NUp de archivos PDF](/pdf/es/net/make-nup-of-pdf-files/)

## División

La función de división te permite dividir un archivo PDF existente en diferentes partes. Puedes dividir la parte frontal del archivo PDF o la parte trasera. Como PdfFileEditor proporciona una variedad de métodos para propósitos de división, también puedes dividir un archivo en páginas individuales o en muchos conjuntos de múltiples páginas.

- [Dividir páginas de PDF](/pdf/es/net/split-pdf-pages/)