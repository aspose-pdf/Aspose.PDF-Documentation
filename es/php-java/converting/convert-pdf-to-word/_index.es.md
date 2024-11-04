---
title: Convertir PDF a Microsoft Word
linktitle: Convertir PDF a Word
type: docs
weight: 10
url: /php-java/convert-pdf-to-word/
lastmod: "2024-05-20"
description: Convierta archivos PDF a formato DOC y DOCX con facilidad y control total con Aspose.PDF para PHP. Aprenda más sobre cómo ajustar la conversión de documentos PDF a Microsoft Word.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Visión general

Este artículo explica cómo convertir PDF a Word usando PHP. El código es muy simple, solo cargue el PDF en la clase Document y guárdelo como salida en formato Microsoft Word DOC o DOCX. Cubre los siguientes temas

- [PDF a Word en PHP](#convert-pdf-to-doc)
- [PDF a DOC en PHP](#convert-pdf-to-doc)
- [PDF a DOCX en PHP](#convert-pdf-to-docx)
- [Convertir PDF a Word en PHP](#convert-pdf-to-docx)
- [Convertir PDF a DOC en PHP](#convert-pdf-to-doc)
- [Convertir PDF a DOCX en PHP](#convert-pdf-to-docx)
- [Cómo convertir archivo PDF a Word DOC en PHP](#convert-pdf-to-doc) o [Word DOCX](#convert-pdf-to-docx)

- [Biblioteca de PDF a Word en PHP, API o código para guardar, generar o crear documentos de Word programáticamente desde PDF](#convert-pdf-to-docx)

## Convertir PDF a DOC

Una de las características más populares es la conversión de PDF a Microsoft Word DOC, lo que hace que el contenido sea fácil de manipular. Aspose.PDF para PHP te permite convertir archivos PDF a DOC.

**Aspose.PDF para PHP** puede crear documentos PDF desde cero y es una excelente herramienta para actualizar, editar y manipular documentos PDF existentes. Una característica importante es la capacidad de convertir páginas y documentos PDF completos a imágenes. Otra característica popular es la conversión de PDF a Microsoft Word DOC, lo que hace que el contenido sea fácil de manipular. (La mayoría de los usuarios no pueden editar documentos PDF pero pueden trabajar fácilmente con tablas, texto e imágenes en Microsoft Word).

Para hacer las cosas simples y comprensibles, Aspose.PDF para PHP proporciona un código de dos líneas para transformar un archivo PDF de origen en un archivo DOC.

El siguiente fragmento de código Java muestra el proceso de convertir un archivo PDF en formato DOC.

1. Crea una instancia del objeto [Document](https://reference.aspose.com/page/java/com.aspose.page/document) con el documento PDF de origen.

2. Guárdalo en formato **SaveFormat.Doc** llamando al método **Document.save()**.

```php
// Cargar el documento PDF
$document = new Document($inputFile);

// Crear un nuevo objeto DocSaveOptions
$saveOption = new DocSaveOptions();

// Establecer el formato de salida a DOC
$saveOption->setFormat(DocSaveOptions_DocFormat::$Doc);

// Guardar el documento como DOC
$document->save($outputFile, $saveOption);
```

## Usando la Clase DocSaveOptions

La [clase DocSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocSaveOptions) proporciona numerosas propiedades que mejoran el proceso de conversión de archivos PDF a formato DOC. Entre estas propiedades, Mode te permite especificar el modo de reconocimiento para el contenido del PDF. Puedes especificar cualquier valor de la enumeración RecognitionMode para esta propiedad. Cada uno de estos valores tiene beneficios y limitaciones específicas:

- El modo [Textbox](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) es rápido y bueno para preservar la apariencia original de un archivo PDF, pero la capacidad de edición del documento resultante podría ser limitada.
 Cada bloque de texto visualmente agrupado en el PDF original se convierte en un cuadro de texto en el documento de salida. Esto logra una máxima semejanza con el original para que el documento de salida se vea bien, pero consiste enteramente en cuadros de texto y podría hacer que la edición en Microsoft Word sea difícil.

- Flow es el modo de reconocimiento completo, donde el motor realiza agrupación y análisis multinivel para restaurar el documento original según la intención del autor mientras produce un documento fácil de editar. La limitación es que el documento de salida podría verse diferente del original.

- La propiedad RelativeHorizontalProximity se puede usar para controlar la proximidad relativa entre elementos textuales y significa que la distancia es normalizada por el tamaño de la fuente. Las fuentes más grandes pueden tener mayores distancias entre sílabas y aún ser consideradas un todo único. Se especifica como un porcentaje del tamaño de la fuente, por ejemplo, 1 = 100%. Esto significa que dos caracteres de 12 pt que están colocados a 12 pt de distancia son proximales.

- RecognitionBullets se utiliza para activar el reconocimiento de viñetas durante la conversión.
```php
// Cargar el documento PDF
$document = new Document($inputFile);

// Crear un nuevo objeto DocSaveOptions
$saveOption = new DocSaveOptions();

// Establecer el modo de reconocimiento a EnhancedFlow
$saveOption->setMode(DocSaveOptions_RecognitionMode::$EnhancedFlow);

// Establecer el formato de salida a DOC
$saveOption->setFormat(DocSaveOptions_DocFormat::$Doc);

// Establecer el modo de reconocimiento como Flow
saveOptions->setMode(DocSaveOptions_RecognitionMode::$Flow);

// Establecer la proximidad horizontal a 2.5
saveOptions->setRelativeHorizontalProximity(2.5f);

// Habilitar el valor para reconocer viñetas durante el proceso de conversión
saveOptions->setRecognizeBullets(true);

// Guardar el documento como DOCX
$document->save($outputFile, $saveOption);
```

{{% alert color="success" %}}
**Intenta convertir PDF a DOC en línea**

Aspose.PDF para PHP te presenta la aplicación gratuita en línea ["PDF a Word"](https://products.aspose.app/pdf/conversion/pdf-to-doc), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.


[![Convertir PDF a DOC](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Convertir PDF a DOCX

La enumeración DocFormat también ofrece la opción de elegir DOCX como el formato de salida para documentos de Word. Para renderizar el archivo PDF de origen en formato DOCX, utilice el fragmento de código especificado a continuación.

## Cómo convertir PDF a DOCX

El siguiente fragmento de código Java muestra el proceso de conversión de un archivo PDF en formato DOCX.

1. Cree una instancia del objeto [Document](https://reference.aspose.com/page/java/com.aspose.page/document) con el documento PDF de origen.
2. Guárdelo en formato **SaveFormat.DocX** llamando al método **Document.save()**.

```php
    // Cargar el documento PDF
    $document = new Document($inputFile);
    
    // Guardar el documento como DOCX
    $document->save($outputFile, SaveFormat::$DocX);
```

La clase [DocSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions) tiene una propiedad llamada Format que proporciona la capacidad de especificar el formato del documento resultante, es decir, DOC o DOCX.
 Para convertir un archivo PDF a formato DOCX, por favor pase el valor Docx de la enumeración DocSaveOptions.DocFormat.

Por favor, eche un vistazo al siguiente fragmento de código que proporciona la capacidad de convertir un archivo PDF a formato DOCX con Java.

```php
// Cargar el documento PDF
$document = new Document($inputFile);

// Crear un nuevo objeto DocSaveOptions
$saveOption = new DocSaveOptions();

// Establecer el modo de reconocimiento a EnhancedFlow
$saveOption->setMode(DocSaveOptions_RecognitionMode::$EnhancedFlow);

// Establecer el formato de salida a DOCX
$saveOption->setFormat(DocSaveOptions_DocFormat::$DocX);

// Guardar el documento como DOCX
$document->save($outputFile, $saveOption);
```

{{% alert color="warning" %}}
**Intenta convertir PDF a DOCX en línea**

Aspose.PDF para PHP te presenta la aplicación en línea gratuita ["PDF a DOCX"](https://products.aspose.app/pdf/conversion/pdf-to-docx), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.


[![Aplicación gratuita de conversión de Aspose.PDF de PDF a DOCX](pdf_to_docx.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)
{{% /alert %}}