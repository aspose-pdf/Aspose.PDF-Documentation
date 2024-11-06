---
title: Conceptos básicos de la API DOM de Aspose.PDF
linktitle: Conceptos básicos de la API DOM
type: docs
weight: 140
url: es/net/basics-of-dom-api/
description: Aspose.PDF para .NET también utiliza la idea de DOM para representar la estructura de un documento PDF en términos de objetos.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Introducción a la API DOM

El Modelo de Objetos de Documento (DOM) es una forma de representación de documentos estructurados como un modelo orientado a objetos. DOM es el estándar oficial del World Wide Web Consortium (W3C) para representar documentos estructurados de manera neutral con respecto a la plataforma y el lenguaje.

En palabras simples, DOM es un árbol de objetos que representa la estructura de algún documento.
En palabras simples, DOM es un árbol de objetos que representa la estructura de algún documento.

### Introducción al Documento PDF

El Formato de Documento Portátil (PDF) es un estándar abierto para el intercambio de documentos. Un documento PDF es una combinación de texto y datos binarios. Si lo abres en un editor de texto, verás los objetos crudos que definen la estructura y contenidos del documento.

La estructura lógica de un archivo PDF es jerárquica y determina la secuencia por la cual una aplicación de visualización dibuja las páginas del documento y sus contenidos. Un PDF está compuesto por cuatro componentes: objetos, estructura de archivo, estructura de documento y flujos de contenido.

### Estructura del Documento PDF

Como la estructura de un archivo PDF es jerárquica, Aspose.PDF para .NET también accede a los elementos de la misma manera. La siguiente jerarquía muestra cómo está estructurado lógicamente el documento PDF y cómo la API DOM de Aspose.PDF para .NET lo construye.

![Estructura del Documento PDF](../images/structure.png)

### Accediendo a los Elementos del Documento PDF

El objeto Document está en el nivel raíz del modelo de objeto.
El objeto Document se encuentra en el nivel raíz del modelo de objeto.

- Abrir documento PDF
- Acceder a la estructura del documento PDF en estilo DOM
- Actualizar datos en el documento PDF
- Validar documento PDF
- Exportar documento PDF en diferentes formatos
- Finalmente, guardar el documento PDF actualizado

## Cómo usar la nueva API de Aspose.PDF para .NET

Este tema explicará la nueva API de Aspose.PDF para .NET y te guiará para comenzar rápidamente y de manera fácil. Tenga en cuenta que los detalles sobre el uso de las características particulares no son parte de este artículo.

Aspose.PDF para .NET se compone de dos partes:

- API DOM de Aspose.PDF para .NET
- Aspose.PDF.Facades (anteriormente Aspose.PDF.Kit para .NET)
Encontrarás los detalles de cada una de estas áreas a continuación.

### API DOM de Aspose.PDF para .NET

La API DOM de Aspose.PDF para .NET corresponde a la estructura del documento PDF, lo que te ayuda a trabajar con los documentos PDF no solo a nivel de archivo y documento, sino también a nivel de objeto.
### Aspose.PDF

Este espacio de nombres proporciona la clase Document que le permite abrir y guardar un documento PDF. La clase License también es parte de este espacio de nombres. También proporciona clases relacionadas con páginas PDF, adjuntos y marcadores como Page, PageCollection, FileSpecification, EmbeddedFileCollection, OutlineItemCollection y OutlineCollection, etc.

#### Aspose.Text

Este espacio de nombres proporciona clases que ayudan a trabajar con el texto y sus diversos aspectos, por ejemplo, Font, FontCollection, FontRepository, FontStyles, TextAbsorber, TextFragment, TextFragmentAbsorber, TextFragmentCollection, TextFragmentState, TextSegment y TextSegmentCollection, etc.

#### Aspose.Text.TextOptions

Este espacio de nombres proporciona clases que le permiten establecer diferentes opciones para buscar, editar o reemplazar texto, por ejemplo, TextEditOptions, TextReplaceOptions y TextSearchOptions.
Este espacio de nombres proporciona clases que le permiten establecer diferentes opciones para buscar, editar o reemplazar texto, por ejemplo, TextEditOptions, TextReplaceOptions y TextSearchOptions.

#### Aspose.InteractiveFeatures

Este espacio de nombres contiene clases que le ayudan a trabajar con las características interactivas del documento PDF, por ejemplo, trabajar con el documento y otras acciones. Este espacio de nombres contiene clases como GoToAction, GoToRemoteAction y GoToURIAction, etc.

#### Aspose.InteractiveFeatures.Annotations

Las anotaciones son parte de las características interactivas de un documento PDF. Hemos dedicado un espacio de nombres para las anotaciones. Este espacio de nombres contiene clases que ayudan a trabajar con las anotaciones, por ejemplo, Annotation, AnnotationCollection, CircleAnnotation y LinkAnnotation, etc.

#### Aspose.InteractiveFeatures.Forms

Este espacio de nombres contiene clases que ayudan a trabajar con formularios PDF y campos de formulario, por ejemplo, Form, Field, TextBoxField y OptionCollection, etc.

#### Aspose.PDF.Devices

Podemos realizar varias operaciones en los documentos PDF, como convertir un documento PDF a varios formatos de imagen.
Podemos realizar diversas operaciones en los documentos PDF, como convertir un documento PDF a varios formatos de imagen.

##### Aspose.PDF.Facades

Antes de Aspose.PDF para .NET, necesitabas Aspose.PDF.Kit para .NET para manipular archivos PDF existentes. Para ejecutar código antiguo de Aspose.PDF.Kit, puedes usar el espacio de nombres Aspose.PDF.Facades.
