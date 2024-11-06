---
title: Creación de un PDF compatible con PDF/3-A y adjuntando factura ZUGFeRD en Java
linktitle: Adjuntar ZUGFeRD al PDF
type: docs
weight: 10
url: es/java/attach-zugferd/
description: Aprende cómo generar un documento PDF con ZUGFeRD en Aspose.PDF para Java
lastmod: "2024-01-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Adjuntar ZUGFeRD al PDF

Recomendamos los siguientes pasos para adjuntar ZUGFeRD al PDF:

* Define una variable de ruta que apunte a una carpeta donde se encuentran los archivos PDF de entrada y salida.
* Define una variable de cadena de texto que almacene la ruta al archivo PDF que será procesado. Usa el método `Paths.get` para combinar partes de la ruta completa.
* Crea una declaración try-with-resources que asegure que el objeto Document creado a partir de la variable de ruta se cerrará automáticamente después de que termine la declaración. El objeto Document representa el documento PDF que será modificado y guardado.

* Crea un objeto [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) proporcionando la ruta y descripción de otro archivo, que contiene metadatos de factura conformes con el estándar ZUGFeRD.
 * Agregar propiedades al objeto de especificación del archivo, como la descripción, el tipo MIME y AFrelationship. AFrelationship indica cómo el archivo incrustado está relacionado con el documento PDF. En este caso, se establece como "Alternative", lo que significa que el archivo incrustado es una representación alternativa del contenido del PDF.
* Agregar el objeto de especificación del archivo a la colección de archivos incrustados del documento. El nombre del archivo debe especificarse según el estándar ZUGFeRD, por ejemplo, "factor-x.xml".
* Convertir el documento al formato PDF/A-3U, un subconjunto de PDF que garantiza la preservación a largo plazo de documentos electrónicos. PDF/A-3U permite incrustar archivos de cualquier formato en documentos PDF.
* Guardar el documento convertido como un nuevo archivo PDF (por ejemplo, "ZUGFeRD-res.pdf").
* Cerrar la declaración try-with-resources y liberar el objeto Document.

```java
String _dataDir = "/home/aspose/pdf-examples/Samples/";
String path = Paths.get(_dataDir, "ZUGFeRD", "ZUGFeRD-test.pdf").toString();
try (Document document = new Document(path)) {
    String description = "Metadatos de factura conforme al estándar ZUGFeRD";
    path = Paths.get(_dataDir, "ZUGFeRD", "factur-x.xml").toString();
    FileSpecification fileSpecification = new FileSpecification(path.toString(), description);
    fileSpecification.setMIMEType("text/xml");
    fileSpecification.setAFRelationship(com.aspose.pdf.AFRelationship.Alternative);

    // Agregar el adjunto a la colección de adjuntos del documento
    document.getEmbeddedFiles().add(fileSpecification);
    path = Paths.get(_dataDir, "ZUGFeRD", "log.xml").toString();
    document.convert(path, PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);
    path = Paths.get(_dataDir, "ZUGFeRD", "ZUGFeRD-res.pdf").toString();
    document.save(path);
}
```