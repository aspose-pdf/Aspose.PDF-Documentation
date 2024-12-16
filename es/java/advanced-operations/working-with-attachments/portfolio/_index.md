---
title: Trabajando con el Portafolio en documentos PDF
linktitle: Portafolio
type: docs
weight: 40
url: /es/java/portfolio/
description: Cómo crear un Portafolio PDF con Java. Deberías usar un archivo de Microsoft Excel, un documento de Word y un archivo de imagen para crear un Portafolio PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Primero, averigüemos **¿Qué es un formato de archivo de Portafolio PDF?**

Por ejemplo, toma un archivo de Portafolio PDF que contiene un documento de Word, Excel, presentaciones de PowerPoint, etc., como archivos adjuntos. Aquí, cada uno de los archivos adjuntos mantiene su formato de documento original, pero está incrustado o ensamblado en un solo archivo de Portafolio PDF. Por supuesto, puedes abrir, leer o editar cada uno de los archivos individuales del Portafolio PDF como si estuviera en una unidad o carpeta. Además, al igual que un documento PDF normal, también puedes aplicar marcas de agua, establecer contraseñas y permisos de seguridad como la capacidad de ver, imprimir o realizar cambios en los archivos adjuntos del Portafolio PDF.

Podemos colocar o ensamblar archivos nativos, en su tipo o formato original, como archivos adjuntos, en un archivo de Portafolio PDF.

## Cómo Crear un Portafolio PDF

Aspose.PDF permite crear documentos de Portafolio PDF usando la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Agregue un archivo a un objeto Document.Collection después de obtenerlo con la clase [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification). Cuando los archivos hayan sido añadidos, use el método Save de la clase Document para guardar el documento del portafolio.

El siguiente ejemplo utiliza un archivo Microsoft Excel, un documento Word y un archivo de imagen para crear un Portafolio PDF.

El código a continuación da como resultado el siguiente portafolio.

### Un Portafolio PDF creado con Aspose.PDF

![Un Portafolio PDF creado con Aspose.PDF for Java](working-with-pdf-portfolio_1.jpg)

```java
    public static void CreatePortfolio() throws IOException {
        // Instanciar Objeto Document
        Document pdfDocument = new Document();

        // Instanciar objeto Collection del documento
        pdfDocument.setCollection(new Collection());

        // Obtener archivos para agregar al Portafolio
        FileSpecification excel = new FileSpecification(_dataDir + "HelloWorld.xlsx");
        FileSpecification word = new FileSpecification(_dataDir + "HelloWorld.docx");
        FileSpecification image = new FileSpecification(_dataDir + "aspose-logo.jpg");

        // Proveer descripción de los archivos
        excel.setDescription ("Archivo Excel");
        word.setDescription ("Archivo Word");
        image.setDescription ("Archivo de Imagen");

        // Agregar archivos a la colección del documento
        pdfDocument.getCollection().add(excel);
        pdfDocument.getCollection().add(word);
        pdfDocument.getCollection().add(image);

        // Guardar documento del Portafolio
        pdfDocument.save(_dataDir + "CreatePDFPortfolio_out.pdf");
    }
```


## Extraer archivos de un Portafolio PDF

Los Portafolios PDF permiten reunir contenido de una variedad de fuentes (por ejemplo, archivos PDF, Word, Excel, JPEG) en un contenedor unificado. Los archivos originales conservan sus identidades individuales pero se ensamblan en un archivo de Portafolio PDF. Los usuarios pueden abrir, leer, editar y formatear cada archivo componente independientemente de los otros archivos componentes.

Aspose.PDF permite la creación de documentos de Portafolio PDF utilizando la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). También ofrece la capacidad de extraer archivos de un portafolio PDF.

El siguiente fragmento de código muestra los pasos para extraer archivos de un portafolio PDF.

![Extraer archivos de un Portafolio PDF](working-with-pdf-portfolio_2.jpg)

```java
    public static void ExtractPortfolio() throws IOException {
        // Abrir un documento
        Document pdfDocument = new Document(_dataDir + "PDFPortfolio.pdf");
        // Obtener colección de archivos incrustados
        EmbeddedFileCollection embeddedFiles = pdfDocument.getEmbeddedFiles();

        // Iterar a través de los archivos individuales del Portafolio
        for (FileSpecification fileSpecification : embeddedFiles) {
            InputStream initialStream = fileSpecification.getContents();
            byte[] buffer = new byte[fileSpecification.getContents().available()];
            initialStream.read(buffer);

            File targetFile = new File(_dataDir + fileSpecification.getName());
            OutputStream outStream = new FileOutputStream(targetFile);
            outStream.write(buffer);
            outStream.close();
        }
    }
```


## Eliminar archivos del portafolio PDF

Para eliminar/quitar archivos del portafolio PDF, intente usar las siguientes líneas de código.

```java
public static void RemoveFilesFromPDFPortfolio() {
    // Cargar el portafolio PDF fuente
    Document pdfDocument = new Document(_dataDir + "PDFPortfolio.pdf");
    pdfDocument.getCollection().delete();
    pdfDocument.save(_dataDir + "No_PortFolio_out.pdf");
}
```