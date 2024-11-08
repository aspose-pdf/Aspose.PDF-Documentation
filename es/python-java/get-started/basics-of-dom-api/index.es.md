---
title: Conceptos básicos de la API DOM de Aspose.PDF
linktitle: Conceptos básicos de la API DOM
type: docs
weight: 110
url: /es/python-java/basics-of-dom-api/
description: Aspose.PDF para Java también utiliza la idea de DOM para representar la estructura de un documento PDF en términos de objetos. Aquí puede leer la descripción de esta estructura.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Introducción a la API DOM

El Modelo de Objeto de Documento (DOM) es una forma de representación de documentos estructurados como un modelo orientado a objetos. DOM es el estándar oficial del Consorcio World Wide Web (W3C) para representar documentos estructurados de manera neutral en cuanto a plataforma e idioma.

En palabras simples, DOM es un árbol de objetos que representa la estructura de algún documento.
 Aspose.PDF for Java también utiliza la idea de DOM para representar la estructura de un documento PDF en términos de objetos. Sin embargo, los aspectos del DOM (como sus Elementos) se manipulan dentro de la sintaxis del lenguaje de programación en uso. La interfaz pública de un DOM se especifica en su interfaz de programación de aplicaciones (API).

### Introducción al Documento PDF

El Formato de Documento Portátil (PDF) es un estándar abierto para el intercambio de documentos. Un documento PDF es una combinación de texto y datos binarios. Si lo abres en un editor de texto, verás los objetos en bruto que definen la estructura y el contenido del documento.

La estructura lógica de un archivo PDF es jerárquica y determina la secuencia en la cual una aplicación de visualización dibuja las páginas del documento y sus contenidos. Un PDF se compone de cuatro componentes: objetos, estructura del archivo, estructura del documento y flujos de contenido.

### Estructura del Documento PDF

Como la estructura de un archivo PDF es jerárquica, Aspose.PDF para Java también accede a los elementos de la misma manera. La siguiente jerarquía te muestra cómo el documento PDF está estructurado lógicamente y cómo Aspose.PDF para Java DOM API lo construye.

![Estructura del Documento PDF](../images/structure.png)

### Accediendo a los Elementos del Documento PDF

El objeto Document está en el nivel raíz del modelo de objetos. El Aspose.PDF para Java DOM API te permite crear un objeto Document y luego acceder a todos los demás objetos en la jerarquía. Puedes acceder a cualquiera de las colecciones como Pages o a elementos individuales como Page, etc. El DOM API proporciona puntos de entrada y salida únicos para manipular el documento PDF como se muestra a continuación:

- Abrir documento PDF
- Acceder a la estructura del documento PDF en estilo DOM
- Actualizar datos en el documento PDF
- Validar documento PDF
- Exportar documento PDF a diferentes formatos
- Finalmente, guardar el documento PDF actualizado

## Cómo Usar el Nuevo Aspose.PDF para Java API

Este tema explicará el nuevo Aspose.PDF para Java API y te guiará para comenzar de manera rápida y sencilla. Por favor, tenga en cuenta que los detalles sobre el uso de las características particulares no son parte de este artículo.

El Aspose.PDF para Java se compone de dos partes:

- Aspose.PDF para Java DOM API
- Aspose.PDF.Facades

Encontrará los detalles de cada una de estas áreas a continuación.

### Aspose.PDF para Java DOM API

El nuevo Aspose.PDF para Java DOM API corresponde a la estructura del documento PDF, lo que le ayuda a trabajar con los documentos PDF no solo a nivel de archivo y documento, sino también a nivel de objeto. Hemos proporcionado más flexibilidad a los desarrolladores para acceder a todos los elementos y objetos del documento PDF. Usando las clases del API DOM de Aspose.PDF, puede obtener acceso programático a los elementos y formato del documento. Este nuevo API DOM está compuesto por varios espacios de nombres como se indica a continuación:

### com.aspose.pdf

Este espacio de nombres proporciona la clase Document que le permite abrir y guardar un documento PDF. La clase License también es parte de este espacio de nombres. También proporciona clases relacionadas con páginas PDF, archivos adjuntos y marcadores como com.aspose.pdf.Page, com.aspose.pdf.PageCollection, com.aspose.pdf.FileSpecification, com.aspose.pdf.EmbeddedFileCollection, com.aspose.pdf.OutlineItemCollection, y com.aspose.pdf.OutlineCollection, etc.

#### com.aspose.pdf.text

Este espacio de nombres proporciona clases que te ayudan a trabajar con el texto y sus varios aspectos, por ejemplo, com.aspose.pdf.Font, com.aspose.pdf.FontCollection, com.aspose.pdf.FontRepository, com.aspose.pdf.FontStyles, com.aspose.pdf.TextAbsorber, com.aspose.pdf.TextFragment, com.aspose.pdf.TextFragmentAbsorber, com.aspose.pdf.TextFragmentCollection, com.aspose.pdf.TextFragmentState, com.aspose.pdf.TextSegment y com.aspose.pdf.TextSegmentCollection, etc.

#### com.aspose.pdf.TextOptions

Este espacio de nombres proporciona clases que te permiten establecer diferentes opciones para buscar, editar o reemplazar texto, por ejemplo, com.aspose.pdf.TextEditOptions, com.aspose.pdf.TextReplaceOptions, y com.aspose.pdf.TextSearchOptions.
#### com.aspose.pdf.PdfAction

Este espacio de nombres contiene clases que te ayudan a trabajar con las características interactivas del documento PDF, por ejemplo, trabajando con el documento y otras acciones. Este espacio de nombres contiene clases como com.aspose.pdf.GoToAction, com.aspose.pdf.GoToRemoteAction y com.aspose.pdf.GoToURIAction, etc.

#### com.aspose.pdf.Annotation

Las anotaciones son parte de las características interactivas de un documento PDF. Hemos dedicado un espacio de nombres para anotaciones. Este espacio de nombres contiene clases que te ayudan a trabajar con las anotaciones, por ejemplo, com.aspose.pdf.Annotation, com.aspose.pdf.AnnotationCollection, com.aspose.pdf.CircleAnnotation y com.aspose.pdf.LinkAnnotation, etc.

#### com.aspose.pdf.Form

Este espacio de nombres contiene clases que te ayudan a trabajar con formularios PDF y campos de formulario, por ejemplo, com.aspose.pdf.Form, com.aspose.pdf.Field, com.aspose.pdf.TextBoxField y com.aspose.pdf.OptionCollection, etc.

#### com.aspose.pdf.devices

Podemos realizar varias operaciones en los documentos PDF, como convertir un documento PDF a varios formatos de imagen.
 However, such operations do not belong to the Document object and we cannot extend the Document class for such operations. That's why we have introduced the concept of the Device in the new DOM API.

##### com.aspose.pdf.facades

Anteriormente a Aspose.PDF para Java también, necesitabas Aspose.PDF.Kit para Java para manipular archivos PDF existentes. Para ejecutar el código antiguo de Aspose.PDF.Kit, puedes usar el espacio de nombres com.aspose.pdf.facades.