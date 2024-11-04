---
title: Extraer y Guardar un Adjunto
linktitle: Extraer y Guardar un Adjunto
type: docs
weight: 20
url: /java/extract-and-save-an-attachment/
description: Aspose.PDF para Java le permite obtener todos los adjuntos de un documento PDF. Además, puede obtener un adjunto individual de su documento.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtener Adjuntos de un Documento PDF

Con Aspose.PDF, es posible obtener todos los adjuntos de un documento PDF. Esto es útil cuando desea guardar los documentos por separado del PDF o si necesita eliminar los adjuntos de un PDF.

Los siguientes fragmentos de código muestran cómo obtener todos los adjuntos de un documento PDF.

```java
   public static void GetAttachmentsFromPDFDocument() {
// Abrir documento
Document pdfDocument = new Document(_dataDir+"input.pdf");
  // Obtener archivo incrustado particular
  FileSpecification fileSpecification = pdfDocument.getEmbeddedFiles().get_Item(1);
  // Obtener las propiedades del archivo
  System.out.printf("Nombre: - " + fileSpecification.getName());
  System.out.printf("\nDescripción: - " + fileSpecification.getDescription());
  System.out.printf("\nTipo MIME: - " + fileSpecification.getMIMEType());
  // Obtener adjunto del archivo PDF
  try {
   InputStream input = fileSpecification.getContents();
   File file = new File(fileSpecification.getName());
   // Crear ruta para el archivo desde el PDF
   file.getParentFile().mkdirs();
   // Crear y extraer archivo desde el PDF
   java.io.FileOutputStream output = new java.io.FileOutputStream(fileSpecification.getName(), true);
   byte[] buffer = new byte[4096];
   int n = 0;
   while (-1 != (n = input.read(buffer)))
    output.write(buffer, 0, n);
   // Cerrar objeto InputStream
   input.close();
   output.close();
  } catch (IOException e) {
   e.printStackTrace();
  }
  // Cerrar objeto Document
  pdfDocument.dispose();
        
    }

```


## Obtener Información del Adjunto

Como se menciona en [Obtener Adjuntos de un Documento PDF](/pdf/java/get-attachments-from-a-pdf-document/), la información del adjunto se mantiene en el objeto [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification), recopilado con otros adjuntos en la colección EmbeddedFiles del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

El objeto [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) proporciona métodos que obtienen información sobre el adjunto, por ejemplo:

- getName() – obtiene el nombre del archivo.
- [getDescription()](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification#getDescription--) – obtiene la descripción del archivo.
- getMIMEType() – obtiene el tipo MIME del archivo.
- getParams() – información sobre los parámetros del archivo, por ejemplo, CheckSum, CreationDate, ModDate y Size.

Para obtener estos parámetros, primero asegúrese de que el método getParams() no devuelva nulo.

Puede iterar a través de todos los adjuntos en la colección EmbeddedFiles utilizando un bucle for, o obtener un adjunto individual especificando su valor de índice.
 El siguiente fragmento de código muestra cómo obtener información sobre un archivo adjunto específico.

```java
    public static void GetAttachmentInformation() {
  // Abrir documento
  Document pdfDocument = new Document(_dataDir+"input.pdf");
  // Obtener un archivo incrustado en particular
  FileSpecification fileSpecification = pdfDocument.getEmbeddedFiles().get_Item(1);
  // Obtener las propiedades del archivo
  System.out.println("Nombre:-" + fileSpecification.getName());
  System.out.println("Descripción:- " + fileSpecification.getDescription());
  System.out.println("Tipo Mime:-" + fileSpecification.getMIMEType());
  // Verificar si el objeto parámetro contiene los parámetros
  if (fileSpecification.getParams() != null) {
   System.out.println("Suma de verificación:- " + fileSpecification.getParams().getCheckSum());
   System.out.println("Fecha de creación:- " + fileSpecification.getParams().getCreationDate());
   System.out.println("Fecha de modificación:- " + fileSpecification.getParams().getModDate());
   System.out.println("Tamaño:- " + fileSpecification.getParams().getSize());
  } 
```