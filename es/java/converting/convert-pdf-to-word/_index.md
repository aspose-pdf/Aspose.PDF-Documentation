---
title: Convertir PDF a Documentos de Microsoft Word en Java
linktitle: Convertir PDF a Word
type: docs
weight: 10
url: /es/java/convert-pdf-to-word/
lastmod: "2021-11-19"
description: Convierta archivos PDF a formato DOC y DOCX con facilidad y control total con Aspose.PDF para Java. Aprenda más sobre cómo ajustar la conversión de PDF a documentos de Microsoft Word.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Resumen

Este artículo explica cómo convertir PDF a Word usando Java. El código es muy simple, solo cargue el PDF en la clase Document y guárdelo como resultado en formato Microsoft Word DOC o DOCX. Cubre los siguientes temas

- [Java PDF a Word](#convert-pdf-to-doc)
- [Java PDF a DOC](#convert-pdf-to-doc)
- [Java PDF a DOCX](#convert-pdf-to-docx)
- [Java Convertir PDF a Word](#convert-pdf-to-docx)
- [Java Convertir PDF a DOC](#convert-pdf-to-doc)
- [Java Convertir PDF a DOCX](#convert-pdf-to-docx)
- [Java Cómo convertir un archivo PDF a Word DOC](#convert-pdf-to-doc) o [Word DOCX](#convert-pdf-to-docx)

- [Java Biblioteca PDF a Word, API o Código para Guardar, Generar o Crear Documentos Word Programáticamente desde PDF](#convert-pdf-to-docx)

## Convertir PDF a DOC

Una de las características más populares es la conversión de PDF a Microsoft Word DOC, lo que facilita la manipulación del contenido. Aspose.PDF para Java te permite convertir archivos PDF a DOC.

**Aspose.PDF para Java** puede crear documentos PDF desde cero y es una gran herramienta para actualizar, editar y manipular documentos PDF existentes. Una característica importante es la capacidad de convertir páginas y documentos PDF completos a imágenes. Otra característica popular es la conversión de PDF a Microsoft Word DOC, lo que hace que el contenido sea fácil de manipular. (La mayoría de los usuarios no pueden editar documentos PDF, pero pueden trabajar fácilmente con tablas, texto e imágenes en Microsoft Word).

Para simplificar y hacer comprensible, Aspose.PDF para Java proporciona un código de dos líneas para transformar un archivo PDF de origen en un archivo DOC.

El siguiente fragmento de código Java muestra el proceso de convertir un archivo PDF en formato DOC.

1. Cree una instancia del objeto [Document](https://reference.aspose.com/page/java/com.aspose.page/document) con el documento PDF de origen.
2. Guárdelo en formato **SaveFormat.Doc** llamando al método **Document.save()**.

```java
public static void convertPDFtoWord() {
    // Abrir el documento PDF de origen
    Document document = new Document(DATA_DIR + "PDFToDOC.pdf");
    // Guardar el archivo en formato de documento de MS
    document.save(DATA_DIR + "PDFToDOC_out.doc", SaveFormat.Doc);
    document.close();
}
```

## Usando la Clase DocSaveOptions

La [clase DocSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocSaveOptions) proporciona numerosas propiedades que mejoran el proceso de conversión de archivos PDF a formato DOC. Entre estas propiedades, Mode le permite especificar el modo de reconocimiento para el contenido del PDF. Puede especificar cualquier valor de la enumeración RecognitionMode para esta propiedad. Cada uno de estos valores tiene beneficios y limitaciones específicas:

- El modo [Textbox](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) es rápido y bueno para preservar la apariencia original de un archivo PDF, pero la editabilidad del documento resultante podría ser limitada.
 Cada bloque de texto visualmente agrupado en el PDF original se convierte en un cuadro de texto en el documento de salida. Esto logra una máxima semejanza con el original, de modo que el documento de salida se ve bien, pero consiste enteramente en cuadros de texto y podría dificultar la edición en Microsoft Word.

- Flow es el modo de reconocimiento completo, donde el motor realiza agrupamiento y análisis multinivel para restaurar el documento original según la intención del autor mientras produce un documento fácilmente editable. La limitación es que el documento de salida podría verse diferente del original.

- La propiedad RelativeHorizontalProximity se puede usar para controlar la proximidad relativa entre elementos textuales y significa que la distancia está normalizada por el tamaño de la fuente. Las fuentes más grandes pueden tener distancias mayores entre sílabas y aún considerarse un solo conjunto. Se especifica como un porcentaje del tamaño de la fuente, por ejemplo, 1 = 100%. Esto significa que dos caracteres de 12pt que se colocan a 12 pt de distancia son próximos.

- RecognitionBullets se utiliza para activar el reconocimiento de viñetas durante la conversión.
```java
public static void convertPDFtoWordDocAdvanced() {
    Path pdfFile = Paths.get(DATA_DIR.toString(), "PDF-to-DOC.pdf");
    Path docFile = Paths.get(DATA_DIR.toString(), "PDF-to-DOC.doc");
    Document document = new Document(pdfFile.toString());
    DocSaveOptions saveOptions = new DocSaveOptions();

    // Especificar el formato de salida como DOC
    saveOptions.setFormat(DocSaveOptions.DocFormat.Doc);
    // Establecer el modo de reconocimiento como Flujo
    saveOptions.setMode(DocSaveOptions.RecognitionMode.Flow);

    // Establecer la proximidad horizontal como 2.5
    saveOptions.setRelativeHorizontalProximity(2.5f);

    // Habilitar el valor para reconocer viñetas durante el proceso de conversión
    saveOptions.setRecognizeBullets(true);

    document.save(docFile.toString(), saveOptions);
    document.close();
}
```

{{% alert color="success" %}}
**Intenta convertir PDF a DOC en línea**

Aspose.PDF para Java te presenta la aplicación en línea gratuita ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-doc), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.

[![Convert PDF to DOC](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Convertir PDF a DOCX

La enumeración DocFormat también proporciona la opción de elegir DOCX como el formato de salida para documentos de Word. Para renderizar el archivo PDF de origen en formato DOCX, utilice el fragmento de código especificado a continuación.

## Cómo convertir PDF a DOCX

El siguiente fragmento de código Java muestra el proceso de conversión de un archivo PDF en formato DOCX.

1. Cree una instancia del objeto [Document](https://reference.aspose.com/page/java/com.aspose.page/document) con el documento PDF de origen.
2. Guárdelo en formato **SaveFormat.DocX** llamando al método **Document.save()**.

```java
public static void convertPDFtoWord_DOCX_Format() {
    // Abrir el documento PDF de origen
    Document document = new Document(DATA_DIR + "PDFToDOC.pdf");
    // Guardar el archivo DOC resultante
    document.save(DATA_DIR + "saveOptionsOutput_out.doc", SaveFormat.DocX);
    document.close();
}
```

La clase [DocSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions) tiene una propiedad llamada Format que proporciona la capacidad de especificar el formato del documento resultante, es decir, DOC o DOCX.
 Para convertir un archivo PDF al formato DOCX, pase el valor Docx de la enumeración DocSaveOptions.DocFormat.

Por favor, observe el siguiente fragmento de código que proporciona la capacidad de convertir un archivo PDF al formato DOCX con Java.

```java
public static void convertPDFtoWord_Advanced_DOCX_Format() {
    // Abrir el documento PDF de origen
    Document document = new Document(DATA_DIR + "PDFToDOC.pdf");

    // Instanciar objeto DocSaveOptions
    DocSaveOptions saveOptions = new DocSaveOptions();
    // Especificar el formato de salida como DOCX
    saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
    // Establecer otros parámetros de DocSaveOptions
    // ....

    // Guardar el documento en formato docx
    document.save("ConvertToDOCX_out.docx", saveOptions);
    document.close();
}
```

{{% alert color="warning" %}}
**Intenta convertir PDF a DOCX en línea**

Aspose.PDF para Java te presenta la aplicación en línea gratuita ["PDF a DOCX"](https://products.aspose.app/pdf/conversion/pdf-to-docx), donde puedes intentar investigar la funcionalidad y la calidad con la que trabaja.
[![Aspose.PDF Conversión PDF a DOCX App Gratuita](pdf_to_docx.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}