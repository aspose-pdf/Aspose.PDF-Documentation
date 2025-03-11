---
title: Fundamentos de la API DOM de Aspose.PDF
linktitle: Fundamentos de la API DOM
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 130
url: /es/net/basics-of-dom-api/
description: Aspose.PDF for .NET también utiliza la idea de DOM para representar la estructura de un documento PDF en términos de objetos.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Basics of Aspose.PDF DOM API",
    "alternativeHeadline": "Enhanced PDF Manipulation with Aspose.PDF DOM API in C#",
    "abstract": "La nueva API DOM Aspose.PDF for .NET proporciona un enfoque robusto orientado a objetos para manipular documentos PDF al representar su estructura como un árbol jerárquico. Esta característica permite a los desarrolladores acceder, actualizar y exportar fácilmente elementos PDF, al tiempo que mejora la flexibilidad y el control sobre la manipulación de documentos a través de una interfaz de programación intuitiva.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "891",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/basics-of-dom-api/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/basics-of-dom-api/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Introducción a la API DOM

El Modelo de Objetos del Documento (DOM) es una forma de representación de documentos estructurados como un modelo orientado a objetos. DOM es el estándar oficial del Consorcio World Wide Web (W3C) para representar documentos estructurados de manera neutral en cuanto a plataforma y lenguaje.

En palabras simples, el DOM es un árbol de objetos que representan la estructura de algún documento. Aspose.PDF for .NET también utiliza la idea de DOM para representar la estructura de un documento PDF en términos de objetos. Sin embargo, los aspectos del DOM (como sus Elementos) se manipulan dentro de la sintaxis del lenguaje de programación en uso. La interfaz pública de un DOM se especifica en su interfaz de programación de aplicaciones (API).

### Introducción al Documento PDF

El Formato de Documento Portátil (PDF) es un estándar abierto para el intercambio de documentos. Un documento PDF es una combinación de texto y datos binarios. Si lo abres en un editor de texto, verás los objetos en bruto que definen la estructura y el contenido del documento.

La estructura lógica de un archivo PDF es jerárquica y determina la secuencia por la cual una aplicación de visualización dibuja las páginas del documento y su contenido. Un PDF se compone de cuatro componentes: objetos, estructura de archivo, estructura de documento y flujos de contenido.

### Estructura del Documento PDF

Dado que la estructura de un archivo PDF es jerárquica, Aspose.PDF for .NET también accede a los elementos de la misma manera. La siguiente jerarquía te muestra cómo está estructurado lógicamente el documento PDF y cómo lo construye la API DOM de Aspose.PDF for .NET.

![Estructura del Documento PDF](../images/structure.png)

### Accediendo a los Elementos del Documento PDF

El objeto Document está en el nivel raíz del modelo de objetos. La API DOM de Aspose.PDF for .NET te permite crear un objeto Document y luego acceder a todos los demás objetos en la jerarquía. Puedes acceder a cualquiera de las colecciones como Pages o a elementos individuales como Page, etc. La API DOM proporciona puntos de entrada y salida únicos para manipular el documento PDF como se muestra a continuación:

- Abrir documento PDF.
- Acceder a la estructura del documento PDF en estilo DOM.
- Actualizar datos en el documento PDF.
- Validar documento PDF.
- Exportar documento PDF a diferentes formatos.
- Finalmente, guardar el documento PDF actualizado.

## Cómo Usar la Nueva API Aspose.PDF for .NET

Este tema explicará la nueva API Aspose.PDF for .NET y te guiará para comenzar de manera rápida y sencilla. Ten en cuenta que los detalles sobre el uso de características particulares no son parte de este artículo.

La Aspose.PDF for .NET se compone de dos partes:

- API DOM de Aspose.PDF for .NET.
- Aspose.Pdf.Facades (antiguo Aspose.PDF.Kit para .NET).

Encontrarás los detalles de cada una de estas áreas a continuación.

### API DOM de Aspose.PDF for .NET

La API DOM de Aspose.PDF for .NET corresponde a la estructura del documento PDF, que te ayuda a trabajar con los documentos PDF no solo a nivel de archivo y documento, sino también a nivel de objeto. Hemos proporcionado más flexibilidad a los desarrolladores para acceder a todos los elementos y objetos del documento PDF. Usando las clases de la API DOM de Aspose.PDF, puedes obtener acceso programático a los elementos y formato del documento. Esta nueva API DOM está compuesta por varios espacios de nombres como se indica a continuación:

### Aspose.PDF

Este espacio de nombres proporciona la clase Document que te permite abrir y guardar un documento PDF. La clase License también es parte de este espacio de nombres. También proporciona clases relacionadas con páginas PDF, adjuntos y marcadores como Page, PageCollection, FileSpecification, EmbeddedFileCollection, OutlineItemCollection y OutlineCollection, etc.

#### Aspose.Text

Este espacio de nombres proporciona clases que te ayudan a trabajar con el texto y sus varios aspectos, por ejemplo Font, FontCollection, FontRepository, FontStyles, TextAbsorber, TextFragment, TextFragmentAbsorber, TextFragmentCollection, TextFragmentState, TextSegment y TextSegmentCollection, etc.

#### Aspose.Text.TextOptions

Este espacio de nombres proporciona clases que te permiten establecer diferentes opciones para buscar, editar o reemplazar texto, por ejemplo TextEditOptions, TextReplaceOptions y TextSearchOptions.

#### Aspose.InteractiveFeatures

Este espacio de nombres contiene clases que te ayudan a trabajar con las características interactivas del documento PDF, por ejemplo, trabajar con el documento y otras acciones. Este espacio de nombres contiene clases como GoToAction, GoToRemoteAction y GoToURIAction, etc.

#### Aspose.InteractiveFeatures.Annotations

Las anotaciones son parte de las características interactivas de un documento PDF. Hemos dedicado un espacio de nombres para anotaciones. Este espacio de nombres contiene clases que te ayudan a trabajar con las anotaciones, por ejemplo, Annotation, AnnotationCollection, CircleAnnotation y LinkAnnotation, etc.

#### Aspose.InteractiveFeatures.Forms

Este espacio de nombres contiene clases que te ayudan a trabajar con formularios PDF y campos de formulario, por ejemplo Form, Field, TextBoxField y OptionCollection, etc.

#### Aspose.Pdf.Devices

Podemos realizar varias operaciones en los documentos PDF, como convertir un documento PDF a varios formatos de imagen. Sin embargo, tales operaciones no pertenecen al objeto Document y no podemos extender la clase Document para tales operaciones. Por eso hemos introducido el concepto de Device en la nueva API DOM.

#### Aspose.Pdf.Facades

Antes de Aspose.PDF for .NET, necesitabas Aspose.PDF.Kit para .NET para manipular archivos PDF existentes. Para ejecutar el código antiguo de Aspose.PDF.Kit, puedes usar el espacio de nombres Aspose.PDF.Facades.