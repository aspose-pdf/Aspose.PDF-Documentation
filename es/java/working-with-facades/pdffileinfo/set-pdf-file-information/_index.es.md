---
title: Establecer información del archivo PDF - fachadas
type: docs
weight: 20
url: /java/set-pdf-information/
description: Esta sección explica cómo establecer la información del archivo PDF con Aspose.PDF Facades usando la clase PdfFileInfo.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

La clase [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo) te permite establecer información específica del archivo de un documento PDF. Necesitas crear un objeto de la clase [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo) y luego establecer diferentes propiedades específicas del archivo como Autor, Título, Palabra clave y Creador, etc. Finalmente, guarda el archivo PDF actualizado usando el método [saveNewInfo(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo#saveNewInfo-java.io.OutputStream-) del objeto [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo).

El siguiente fragmento de código te muestra cómo establecer la información del archivo PDF.

```java
 public static void SetPdfInfo()
    {
        PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf");
        // Establecer información del PDF
        fileInfo.setAuthor("Aspose");
        fileInfo.setTitle ("Hello World!");
        fileInfo.setKeywords("Peace and Development");
        fileInfo.setCreator ("Aspose");
        
        // Guardar archivo actualizado
        fileInfo.saveNewInfo(_dataDir + "SetfileInfo_out.pdf");
    }
```


## Establecer Información Meta

[setMetaInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo#setMetaInfo-java.lang.String-java.lang.String-) método le permite agregar cualquier información. En nuestro ejemplo, agregamos un campo. Verifique el siguiente fragmento de código:

```java
   public static void SetMetaInfo()
    {
        // Crear instancia del objeto PdffileInfo
        PdfFileInfo fInfo = new PdfFileInfo(_dataDir + "sample.pdf");
       
        // Establecer nuevo atributo de cliente como información meta
        fInfo.setMetaInfo("Reviewer", "usuario de Aspose.PDF");

        // Guardar archivo actualizado
        fInfo.saveNewInfo(_dataDir + "SetMetaInfo_out.pdf");

    }
```