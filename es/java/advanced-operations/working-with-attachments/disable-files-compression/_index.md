---
title: Desactivar la Compresión de Archivos al Añadir como Recursos Integrados
linktitle: Desactivar Compresión de Archivos
type: docs
weight: 40
url: /es/java/disable-files-compression-when-adding-as-embedded-resources/
description: Este artículo explica cómo desactivar la compresión de archivos al añadir como recursos integrados
lastmod: "2021-06-05"
---

La clase [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) permite a los desarrolladores añadir archivos adjuntos a documentos PDF. Por defecto, los archivos adjuntos están comprimidos. Hemos actualizado la API para permitir a los desarrolladores desactivar la compresión al añadir archivos como recursos integrados. Esto brinda a los desarrolladores más control sobre cómo se procesan los archivos.

Para permitir a los desarrolladores controlar la compresión de archivos, se ha añadido el método [setEncoding(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification#setEncoding-int-) a la clase [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification).
 Esta propiedad determina qué codificación se utilizará para la compresión de archivos. El método acepta un valor del enumerador [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding). Los valores posibles son [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).None y [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).Zip.

Si la codificación está configurada como [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).None, entonces el archivo adjunto no se comprime. La codificación predeterminada es [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).Zip.

El siguiente fragmento de código muestra cómo agregar un archivo adjunto a un documento PDF.

```java
    public static void DisableFilesCompressionWhenAddingAsEmbeddedResources() throws IOException{
  // obtener referencia del archivo fuente/entrada
  java.nio.file.Path path = java.nio.file.Paths.get(_dataDir+"input.pdf");
  // leer todos los contenidos del archivo fuente en ByteArray
  byte[] data = java.nio.file.Files.readAllBytes(path);
  // crear una instancia del objeto Stream a partir del contenido de ByteArray
  InputStream is = new ByteArrayInputStream(data);
  // Instanciar objeto Document a partir de la instancia de stream
  Document pdfDocument = new Document(is);
  // configurar nuevo archivo para ser agregado como adjunto
  FileSpecification fileSpecification = new FileSpecification("test.txt", "Archivo de texto de muestra");
  // Especificar la propiedad Encoding configurándola a FileEncoding.None
  fileSpecification.setEncoding(FileEncoding.None);
  // agregar adjunto a la colección de adjuntos del documento
  pdfDocument.getEmbeddedFiles().add(fileSpecification);
  // guardar nuevo resultado
  pdfDocument.save("output.pdf");
    }
```