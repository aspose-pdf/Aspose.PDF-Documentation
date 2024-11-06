---
title: Conceptos básicos de Aspose.PDF DOM API
linktitle: Conceptos básicos de DOM API
type: docs
weight: 120
url: es/cpp/basics-of-dom-api/
description: Aspose.PDF para C++ también utiliza la idea de DOM para representar la estructura de un documento PDF en términos de objetos. Aquí puede leer la descripción de esta estructura.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Introducción a la API DOM

Document Object Model (DOM) es una forma de representación de documentos estructurados como un modelo orientado a objetos. DOM es el estándar oficial del Consorcio World Wide Web (W3C) para representar documentos estructurados de manera neutral en cuanto a plataforma y lenguaje.

En palabras simples, DOM es un árbol de objetos que representa la estructura de algún documento. Aspose.PDF for C++ también utiliza la idea de DOM para representar la estructura de un documento PDF en términos de objetos. Sin embargo, los aspectos del DOM (como sus Elementos) se manipulan dentro de la sintaxis del lenguaje de programación en uso. La interfaz pública de un DOM se especifica en su interfaz de programación de aplicaciones (API).

### Introducción al Documento PDF

El Formato de Documento Portátil (PDF) es un estándar abierto para el intercambio de documentos. Un documento PDF es una combinación de texto y datos binarios. Si lo abres en un editor de texto, verás los objetos en bruto que definen la estructura y el contenido del documento.

La estructura lógica de un archivo PDF es jerárquica y determina la secuencia por la cual una aplicación de visualización dibuja las páginas del documento y su contenido. Un PDF se compone de cuatro componentes: objetos, estructura de archivo, estructura de documento y flujos de contenido.

### Estructura del Documento PDF

Dado que la estructura de un archivo PDF es jerárquica, Aspose.PDF para C++ también accede a los elementos de la misma manera. La siguiente jerarquía te muestra cómo está estructurado lógicamente el documento PDF y cómo Aspose.PDF para C++ DOM API lo construye.

![Estructura del Documento PDF](../images/structure.png)

### Accediendo a los Elementos del Documento PDF

El objeto Document está en el nivel raíz del modelo de objetos. La API DOM de Aspose.PDF para C++ te permite crear un objeto Document y luego acceder a todos los demás objetos en la jerarquía. Puedes acceder a cualquiera de las colecciones como Pages o a elementos individuales como Page, etc. La API DOM proporciona puntos de entrada y salida únicos para manipular el documento PDF como se muestra a continuación:

- Abrir documento PDF
- Acceder a la estructura del documento PDF al estilo DOM
- Actualizar datos en el documento PDF
- Validar documento PDF
- Exportar documento PDF a diferentes formatos
- Finalmente, guardar el documento PDF actualizado

## Cómo Usar la Nueva API de Aspose.PDF para C++

Este tema explicará la nueva API de Aspose.PDF para C++ y te guiará para comenzar rápida y fácilmente. Por favor, tenga en cuenta que los detalles sobre el uso de las características particulares no son parte de este artículo.

Aspose.PDF para C++ se compone de dos partes:

- Aspose.PDF para C++ DOM API
- Aspose.PDF.Facades

Encontrará los detalles de cada una de estas áreas a continuación.

### Aspose.PDF para C++ DOM API

El Aspose.PDF para C++ DOM API corresponde a la estructura del documento PDF, lo que le ayuda a trabajar con los documentos PDF no solo a nivel de archivo y documento, sino también a nivel de objeto. Hemos proporcionado más flexibilidad a los desarrolladores para acceder a todos los elementos y objetos del documento PDF. Usando las clases del Aspose.PDF DOM API, puede obtener acceso programático a los elementos y formato del documento. Esta nueva DOM API está compuesta de varios espacios de nombres como se indica a continuación:

### Referencia del Espacio de Nombres Aspose::Pdf

Este espacio de nombres proporciona la clase Document que le permite abrir y guardar un documento PDF.

#### Referencia del Espacio de Nombres Aspose::Pdf::Text

Este espacio de nombres proporciona clases que le ayudan a trabajar con el texto y sus diversos aspectos, por ejemplo, Font, FontCollection, FontRepository, FontSource, TextAbsorber, TextFragment, TextFragmentAbsorber, TextFragmentCollection, TextFragmentState, TextSegment y TextSegmentCollection, etc.
#### Aspose::Pdf::Collections Namespace Reference

Este espacio de nombres proporciona la clase AsposeHashDictionary.

#### Aspose::Pdf::CommonData Namespace Reference

#### Aspose::Pdf::Diagnostics Namespace Reference

#### Aspose::Pdf::Drawing Namespace Reference

Este espacio de nombres proporciona las clases: Curve, Circle, Arc, Rectangle, Graph, etc., para añadir elementos gráficos a su archivo PDF.

#### Aspose::Pdf::Engine Namespace Reference

Este espacio de nombres proporciona las clases Addressing, Interactive, Security, CommonData, IO, Presentation.

#### Aspose::Pdf::GroupProcessor Namespace Reference

Este espacio de nombres proporciona las clases: ExtractorFactory - representa una fábrica para crear objetos IPdfTypeExtractor, IDocumentPageTextExtractor, IDocumentTextExtractor, clases IPdfTypeExtractor - representa una interfaz para interactuar con el extractor.

#### Aspose::Pdf::Interchange Namespace Reference

#### Aspose::Pdf::LogicalStructure Namespace Reference

Este espacio de nombres proporciona las clases: AnnotationElement, AttributeOwnerStandard, CaptionElement, DocumentElement, FormElement, GroupingElement, ILSTextElement, PrivateElement, WarichuWTElement, etc.

#### Aspose::Pdf::Operators Namespace Reference

Este espacio de nombres proporciona clases de los siguientes operadores: BasicSetColorAndPatternOperator, BlockTextOperator, SetCharWidthBoundingBox, SetColorStroke, SetHorizontalTextScaling, SetTextRenderingMode, TextShowOperator, etc.

#### Aspose::Pdf::Optimization Namespace Reference

Este espacio de nombres proporciona dos clases - ImageCompressionOptions y OptimizationOptions.

#### Aspose::Pdf::PageModel Namespace Reference

#### Aspose::Pdf::PdfAOptionClasses Namespace Reference

Este espacio de nombres proporciona dos clases: FontEmbeddingOptions - El estándar PDF/A requiere que todas las fuentes deben estar incrustadas en el documento. Esta clase incluye banderas para casos cuando no es posible incrustar alguna fuente porque esta fuente está ausente en la PC de destino. ToUnicodeProcessingRules - Esta clase describe reglas que se pueden usar para resolver el error de Adobe Preflight "El texto no se puede mapear a Unicode".

#### Aspose::Pdf::Sanitization Namespace Reference

Este espacio de nombres proporciona dos clases: Details_SanitizationException e IRecovery.

#### Aspose::Pdf::Tagged Namespace Reference

Este espacio de nombres proporciona clases Details_TaggedException - Representa una excepción para el contenido TaggedPDF del documento. ITaggedContent - Representa una interfaz para trabajar con el contenido TaggedPdf del documento? y TaggedPdfExceptionCode.

#### Aspose::Pdf::Validation Namespace Reference

#### Aspose::Pdf::XfaConverter Namespace Reference

Este espacio de nombres proporciona la clase XfaParserOptions - clase para manejar la encapsulación de datos relacionados.

#### Aspose::Pdf::Annotations Namespace Reference

Las anotaciones son parte de las características interactivas de un documento PDF. Hemos dedicado un espacio de nombres para las anotaciones. Este espacio de nombres contiene clases que te ayudan a trabajar con las anotaciones, por ejemplo, Annotation, AnnotationCollection, CircleAnnotation y LinkAnnotation, etc.

#### Aspose::Pdf::Forms Namespace Reference

Este espacio de nombres contiene clases que te ayudan a trabajar con formularios PDF y campos de formulario, por ejemplo Form, Field, TextBoxField y OptionCollection, etc.

#### Aspose::Pdf::Devices Namespace Reference

We can perform various operations on the PDF documents such as converting PDF document to various image formats. However, such operations do not belong to the Document object and we cannot extend the Document class for such operations. That's why we have introduced the concept of the Device in the new DOM API.

##### Aspose::Pdf::Facades Namespace Reference

You can use Aspose.PDF.Facades namespace. This Namespace provides classes AutoFiller - represents a class to receive data from database or other datasource. Bookmark, Form, Stamp, PdfConverter anr more classes.

Podemos realizar varias operaciones en los documentos PDF, como convertir un documento PDF a varios formatos de imagen. Sin embargo, tales operaciones no pertenecen al objeto Document y no podemos extender la clase Document para tales operaciones. Es por eso que hemos introducido el concepto de Device en la nueva API DOM.

##### Referencia del Espacio de Nombres Aspose::Pdf::Facades

Puede usar el espacio de nombres Aspose.PDF.Facades. Este espacio de nombres proporciona clases como AutoFiller, que representa una clase para recibir datos de una base de datos u otra fuente de datos. Bookmark, Form, Stamp, PdfConverter y más clases.