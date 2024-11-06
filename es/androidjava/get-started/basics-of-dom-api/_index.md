---
title: Conceptos básicos de la API DOM de Aspose.PDF
linktitle: Conceptos básicos de la API DOM
type: docs
weight: 10
url: es/androidjava/basics-of-dom-api/
description: Aspose.PDF para Android a través de Java también utiliza la idea de DOM para representar la estructura de un documento PDF en términos de objetos. Aquí puedes leer la descripción de esta estructura.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Introducción a la API DOM

Document Object Model (DOM) es una forma de representación de documentos estructurados como un modelo orientado a objetos. DOM es el estándar oficial del World Wide Web Consortium (W3C) para representar documentos estructurados de una manera neutral en cuanto a plataforma e idioma.

En pocas palabras, DOM es un árbol de objetos que representan la estructura de algún documento.
 Aspose.PDF para Android a través de Java también utiliza la idea de DOM para representar la estructura de un documento PDF en términos de objetos. Sin embargo, los aspectos del DOM (como sus Elementos) se manipulan dentro de la sintaxis del lenguaje de programación en uso. La interfaz pública de un DOM se especifica en su interfaz de programación de aplicaciones (API).

### Introducción al Documento PDF

El Formato de Documento Portátil (PDF) es un estándar abierto para el intercambio de documentos. Un documento PDF es una combinación de texto y datos binarios. Si lo abres en un editor de texto, verás los objetos en bruto que definen la estructura y el contenido del documento.

La estructura lógica de un archivo PDF es jerárquica y determina la secuencia por la cual una aplicación de visualización dibuja las páginas del documento y sus contenidos. Un PDF se compone de cuatro componentes: objetos, estructura de archivo, estructura del documento y flujos de contenido.

### Estructura del Documento PDF

Dado que la estructura de un archivo PDF es jerárquica, Aspose.PDF para Java también accede a los elementos de la misma manera. La siguiente jerarquía le muestra cómo el documento PDF está estructurado lógicamente y cómo Aspose.PDF para Java DOM API lo construye.

![Estructura del Documento PDF](https://docs.aspose.com/pdf/java/images/structure.png)

### Accediendo a los Elementos del Documento PDF

El objeto Document está en el nivel raíz del modelo de objetos. La API Aspose.PDF para Android a través de Java DOM le permite crear un objeto Document y luego acceder a todos los demás objetos en la jerarquía. Puede acceder a cualquiera de las colecciones como Pages o a un elemento individual como Page, etc. La API DOM proporciona puntos de entrada y salida únicos para manipular el documento PDF como se muestra a continuación:

- Abrir documento PDF
- Acceder a la estructura del documento PDF en estilo DOM
- Actualizar datos en el documento PDF
- Validar documento PDF
- Exportar documento PDF a diferentes formatos
- Finalmente, guardar el documento PDF actualizado

## Cómo Usar la Nueva API Aspose.PDF para Android vía Java

Este tema explicará la nueva API Aspose.PDF para Android a través de Java y le guiará para comenzar rápida y fácilmente. Por favor, tenga en cuenta que los detalles sobre el uso de las características particulares no son parte de este artículo.

Aspose.PDF para Android a través de Java se compone de dos partes:

- Aspose.PDF para Android a través de Java DOM API
- Aspose.PDF.Facades 

Encontrará los detalles de cada una de estas áreas a continuación.

### Aspose.PDF para Android a través de Java DOM API

El nuevo Aspose.PDF para Android a través de Java DOM API corresponde a la estructura del documento PDF, lo que le ayuda a trabajar con los documentos PDF no solo a nivel de archivo y documento, sino también a nivel de objeto. Hemos proporcionado más flexibilidad a los desarrolladores para acceder a todos los elementos y objetos del documento PDF. Usando las clases del API DOM de Aspose.PDF, puede obtener acceso programático a los elementos y el formato del documento. Este nuevo API DOM está compuesto por varios espacios de nombres como se indica a continuación:

### com.aspose.pdf

Este espacio de nombres proporciona la clase Document que le permite abrir y guardar un documento PDF. La clase License también es parte de este espacio de nombres. También proporciona clases relacionadas con páginas PDF, adjuntos y marcadores como com.aspose.pdf.Page, com.aspose.pdf.PageCollection, com.aspose.pdf.FileSpecification, com.aspose.pdf.EmbeddedFileCollection, com.aspose.pdf.OutlineItemCollection, y com.aspose.pdf.OutlineCollection, etc.

#### com.aspose.pdf.text

Este espacio de nombres proporciona clases que te ayudan a trabajar con el texto y sus diversos aspectos, por ejemplo, com.aspose.pdf.Font, com.aspose.pdf.FontCollection, com.aspose.pdf.FontRepository, com.aspose.pdf.FontStyles, com.aspose.pdf.TextAbsorber, com.aspose.pdf.TextFragment, com.aspose.pdf.TextFragmentAbsorber, com.aspose.pdf.TextFragmentCollection, com.aspose.pdf.TextFragmentState, com.aspose.pdf.TextSegment y com.aspose.pdf.TextSegmentCollection, etc.

#### com.aspose.pdf.TextOptions

Este espacio de nombres proporciona clases que te permiten establecer diferentes opciones para buscar, editar o reemplazar texto, por ejemplo, com.aspose.pdf.TextEditOptions, com.aspose.pdf.TextReplaceOptions, y com.aspose.pdf.TextSearchOptions.
#### com.aspose.pdf.PdfAction

Este espacio de nombres contiene clases que te ayudan a trabajar con las funciones interactivas del documento PDF, por ejemplo, trabajar con el documento y otras acciones. Este espacio de nombres contiene clases como com.aspose.pdf.GoToAction, com.aspose.pdf.GoToRemoteAction y com.aspose.pdf.GoToURIAction, etc.

#### com.aspose.pdf.Annotation

Las anotaciones son una parte de las funciones interactivas de un documento PDF. Hemos dedicado un espacio de nombres para las anotaciones. Este espacio de nombres contiene clases que te ayudan a trabajar con las anotaciones, por ejemplo, com.aspose.pdf.Annotation, com.aspose.pdf.AnnotationCollection, com.aspose.pdf.CircleAnnotation y com.aspose.pdf.LinkAnnotation, etc.

#### com.aspose.pdf.Form

Este espacio de nombres contiene clases que te ayudan a trabajar con formularios PDF y campos de formulario, por ejemplo, com.aspose.pdf.Form, com.aspose.pdf.Field, com.aspose.pdf.TextBoxField y com.aspose.pdf.OptionCollection, etc.

#### com.aspose.pdf.devices

Podemos realizar varias operaciones en los documentos PDF, como convertir un documento PDF a varios formatos de imagen.
 Sin embargo, tales operaciones no pertenecen al objeto Document y no podemos extender la clase Document para tales operaciones. Por eso hemos introducido el concepto de Device en la nueva API DOM.

##### com.aspose.pdf.facades

Antes de Aspose.PDF para Java t.o.o, necesitabas Aspose.PDF.Kit para Java para manipular archivos PDF existentes. Para ejecutar el antiguo código de Aspose.PDF.Kit, puedes usar el espacio de nombres com.aspose.pdf.facades.