---
title: Conceptos básicos del API DOM de Aspose.PDF
linktitle: Conceptos básicos del API DOM
type: docs
weight: 10
url: /es/androidjava/basics-of-dom-api/
description: Aspose.PDF for Android via Java también utiliza la idea de DOM para representar la estructura de un documento PDF en términos de objetos. Aquí puedes leer la descripción de esta estructura.
lastmod: "2026-06-30"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Introducción al API DOM

El Modelo de Objetos de Documento (DOM) es una forma de representación de documentos estructurados como un modelo orientado a objetos. DOM es el estándar oficial del World Wide Web Consortium (W3C) para representar documentos estructurados de manera neutral respecto a la plataforma y al lenguaje.

En palabras simples, DOM es un árbol de objetos que representa la estructura de algún documento. Aspose.PDF for Android via Java también utiliza la idea de DOM para representar la estructura de un documento PDF en términos de objetos. Sin embargo, los aspectos de DOM (como sus Elements) se manipulan dentro de la sintaxis del lenguaje de programación en uso. La interfaz pública de un DOM se especifica en su interfaz de programación de aplicaciones (API).

### Introducción al documento PDF

Portable Document Format (PDF) es un estándar abierto para el intercambio de documentos. Un documento PDF es una combinación de texto y datos binarios. Si lo abre en un editor de texto, verá los objetos sin procesar que definen la estructura y el contenido del documento.

La estructura lógica de un archivo PDF es jerárquica y determina la secuencia con la que una aplicación de visualización dibuja las páginas del documento y su contenido. Un PDF se compone de cuatro componentes: objetos, estructura del archivo, estructura del documento y flujos de contenido.

### Estructura del documento PDF

Dado que la estructura de un archivo PDF es jerárquica, Aspose.PDF for Java también accede a los elementos de la misma manera. La siguiente jerarquía le muestra cómo está estructurado lógicamente el documento PDF y cómo la API DOM de Aspose.PDF for Java lo construye.

![Estructura del documento PDF](https://docs.aspose.com/pdf/java/images/structure.png)

### Accediendo a los elementos del documento PDF

El objeto Document está en el nivel raíz del modelo de objetos. La API DOM de Aspose.PDF for Android via Java le permite crear un objeto Document y luego acceder a todos los demás objetos en la jerarquía. Puede acceder a cualquiera de las colecciones, como Pages, o a elementos individuales, como Page, etc. La API DOM proporciona puntos de entrada y salida únicos para manipular el documento PDF como se muestra a continuación:

- Abrir documento PDF
- Acceder a la estructura del documento PDF al estilo DOM
- Actualizar datos en el documento PDF
- Validar documento PDF
- Exportar documento PDF a diferentes formatos
- Finalmente, guarde el documento PDF actualizado

## Cómo usar el nuevo Aspose.PDF for Android a través de la API Java

Este tema explicará el nuevo Aspose.PDF for Android a través de la API Java y le guiará para comenzar rápida y fácilmente. Tenga en cuenta que los detalles sobre el uso de las funciones particulares no forman parte de este artículo.

El Aspose.PDF for Android a través de Java se compone de dos partes:

- Aspose.PDF for Android a través de la API DOM Java
- Aspose.PDF.Facades 

Encontrarás los detalles de cada una de estas áreas a continuación.

### Aspose.PDF for Android a través de la API DOM Java

La nueva Aspose.PDF for Android via Java DOM API corresponde a la estructura del documento PDF, lo que le ayuda a trabajar con los documentos PDF no solo a nivel de archivo y documento, sino también a nivel de objeto. Hemos brindado más flexibilidad a los desarrolladores para acceder a todos los elementos y objetos del documento PDF. Usando las clases de la Aspose.PDF DOM API’s, puede obtener acceso programático a los elementos y el formato del documento. Esta nueva DOM API está compuesta por varios espacios de nombres como se indica a continuación:

### com.aspose.pdf

Este espacio de nombres proporciona la clase Document que le permite abrir y guardar un documento PDF. La clase License también forma parte de este espacio de nombres. También proporciona clases relacionadas con páginas PDF, adjuntos y marcadores como com.aspose.pdf.Page, com.aspose.pdf.PageCollection, com.aspose.pdf.FileSpecification, com.aspose.pdf.EmbeddedFileCollection, com.aspose.pdf.OutlineItemCollection y com.aspose.pdf.OutlineCollection, etc.

#### com.aspose.pdf.text

Este espacio de nombres proporciona clases que le ayudan a trabajar con el texto y sus diversos aspectos, por ejemplo com.aspose.pdf.Font, com.aspose.pdf.FontCollection, com.aspose.pdf.FontRepository, com.aspose.pdf.FontStyles, com.aspose.pdf.TextAbsorber, com.aspose.pdf.TextFragment, com.aspose.pdf.TextFragmentAbsorber, com.aspose.pdf.TextFragmentCollection, com.aspose.pdf.TextFragmentState, com.aspose.pdf.TextSegment y com.aspose.pdf.TextSegmentCollection, etc.

#### com.aspose.pdf.TextOptions

Este espacio de nombres proporciona clases que le permiten establecer diferentes opciones para buscar, editar o reemplazar texto, por ejemplo com.aspose.pdf.TextEditOptions, com.aspose.pdf.TextReplaceOptions y com.aspose.pdf.TextSearchOptions.

#### com.aspose.pdf.PdfAction

Este espacio de nombres contiene clases que le ayudan a trabajar con las funciones interactivas del documento PDF, por ejemplo trabajando con el documento y otras acciones. Este espacio de nombres contiene clases como com.aspose.pdf.GoToAction, com.aspose.pdf.GoToRemoteAction y com.aspose.pdf.GoToURIAction, etc.

#### com.aspose.pdf.Annotation

Las anotaciones son una parte de las funciones interactivas de un documento PDF. Hemos dedicado un espacio de nombres para anotaciones. Este espacio de nombres contiene clases que le ayudan a trabajar con las anotaciones, por ejemplo, com.aspose.pdf.Annotation, com.aspose.pdf.AnnotationCollection, com.aspose.pdf.CircleAnnotation y com.aspose.pdf.LinkAnnotation, etc.

#### com.aspose.pdf.Form

Este espacio de nombres contiene clases que le ayudan a trabajar con formularios PDF y campos de formulario, por ejemplo com.aspose.pdf.Form, com.aspose.pdf.Field, com.aspose.pdf.TextBoxField y com.aspose.pdf.OptionCollection, etc.

#### com.aspose.pdf.devices 

Podemos realizar varias operaciones en los documentos PDF, como convertir un documento PDF a varios formatos de imagen. Sin embargo, esas operaciones no pertenecen al objeto Document y no podemos extender la clase Document para dichas operaciones. Por eso hemos introducido el concepto de Device en la nueva API DOM.

##### com.aspose.pdf.facades

Antes de Aspose.PDF for Java t.o.o, necesitabas Aspose.PDF.Kit for Java para manipular archivos PDF existentes. Para ejecutar el código antiguo de Aspose.PDF.Kit, puedes usar el espacio de nombres com.aspose.pdf.facades.

