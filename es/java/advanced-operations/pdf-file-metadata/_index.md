---
title: Trabajando con Metadatos de Archivos PDF 
linktitle: Metadatos de Archivos PDF
type: docs
weight: 140
url: es/java/pdf-file-metadata/
description: Esta sección explica cómo obtener información de archivos PDF, cómo obtener Metadatos XMP de un archivo PDF, establecer Información de Archivos PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtener Información del Archivo PDF

Para obtener información específica de un archivo sobre un archivo PDF, primero obtenga el objeto [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocumentInfo) usando la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) [getInfo()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getInfo--). Una vez que se recupera el objeto [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocumentInfo), puede obtener los valores de las propiedades individuales.

El siguiente fragmento de código muestra cómo establecer la información del archivo PDF.

```java
public class ExampleMetadata {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Metadata/";

    public static void GetPDFFileInformation() {
        // Crear un nuevo documento PDF
        Document pdfDocument = new Document(_dataDir + "sample.pdf");
        // Obtener información del documento
        DocumentInfo docInfo = pdfDocument.getInfo();
        // Mostrar información del documento
        System.out.println("Autor: " + docInfo.getAuthor());
        System.out.println("Fecha de Creación: " + docInfo.getCreationDate());
        System.out.println("Palabras Clave: " + docInfo.getKeywords());
        System.out.println("Fecha de Modificación: " + docInfo.getModDate());
        System.out.println("Asunto: " + docInfo.getSubject());
        System.out.println("Título: " + docInfo.getTitle());
    }
```


## Establecer Información del Archivo PDF

Aspose.PDF para Java te permite establecer información específica del archivo para un PDF, como autor, fecha de creación, asunto y título.

Para establecer esta información:

1. Crea un objeto [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocumentInfo).
1. Establece los valores de las propiedades.
1. Guarda el documento actualizado usando el método [save()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save-com.aspose.ms.System.IO.FileStream-) de la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

{{% alert color="primary" %}}

Por favor, ten en cuenta que no puedes establecer valores para los campos **Producer** y **Creator**, porque Aspose.PDF para Java x.x.x se mostrará en estos campos.

{{% /alert %}}

El siguiente fragmento de código te muestra cómo establecer la información del archivo PDF.

```java
 public static void SetPDFFileInformation() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // Especificar información del documento
        DocumentInfo docInfo = new DocumentInfo(pdfDocument);

        docInfo.setAuthor("Aspose");
        docInfo.setCreationDate(new java.util.Date());
        docInfo.setKeywords("Aspose.Pdf, DOM, API");
        docInfo.setModDate(new java.util.Date());
        docInfo.setSubject("Información del PDF");
        docInfo.setTitle("Estableciendo Información del Documento PDF");

        // Guardar documento de salida
        pdfDocument.save(_dataDir + "SetFileInfo_out.pdf");
    }
```


## Obtener Metadatos XMP de un Archivo PDF

Aspose.PDF para Java te permite acceder a los metadatos XMP de un archivo PDF.

Para obtener los metadatos de un archivo PDF,

1. Crea un objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) y abre el archivo PDF de entrada.
1. Usa la propiedad [getMetadata()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getMetadata--) para obtener los metadatos.

El siguiente fragmento de código te muestra cómo obtener los metadatos del archivo PDF.

```java
   public static void GetXMPMetadata() {

        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "SetXMPMetadata.pdf");

        System.out.println("xmp:CreateDate: " + pdfDocument.getMetadata().get_Item("xmp:CreateDate"));
        System.out.println("xmp:Nickname: " + pdfDocument.getMetadata().get_Item("xmp:Nickname"));
        System.out.println("xmp:CustomProperty: " + pdfDocument.getMetadata().get_Item("xmp:CustomProperty"));

    }
```

## Establecer Metadatos XMP en un Archivo PDF

Aspose.PDF para Java te permite establecer metadatos en un archivo PDF.
 Para establecer metadatos:

1. Cree un objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Establezca valores de metadatos utilizando la propiedad [getMetadata()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getMetadata--).
1. Guarde el documento actualizado usando el método [save()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save-com.aspose.ms.System.IO.FileStream-) del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

El siguiente fragmento de código le muestra cómo establecer metadatos en un archivo PDF.

```java
    public static void SetXMPMetadata() {

        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // Establecer propiedades
        pdfDocument.getMetadata().set_Item("xmp:CreateDate", new XmpValue(new java.util.Date()));
        pdfDocument.getMetadata().set_Item("xmp:Nickname", new XmpValue("Nickname"));
        pdfDocument.getMetadata().set_Item("xmp:CustomProperty", new XmpValue("Custom Value"));

        // Guardar documento
        pdfDocument.save(_dataDir + "SetXMPMetadata.pdf");
    }
```

## Insertar Metadatos con Prefijo

Algunos desarrolladores necesitan crear un nuevo espacio de nombres de metadatos con un prefijo. El siguiente fragmento de código muestra cómo insertar metadatos con prefijo.

```java
    public static void InsertMetadataWithPrefix() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "SetXMPMetadata.pdf");
        pdfDocument.getMetadata().registerNamespaceUri("adc", "http://tempuri.org/adc/1.0");
        pdfDocument.getMetadata().set_Item("adc:format", new XmpValue("application/pdf"));
        pdfDocument.getMetadata().set_Item("adc:title", new XmpValue("alternative title"));        
        // Guardar documento
        pdfDocument.save(_dataDir + "SetPrefixMetadata_out.pdf");
    }
}
```