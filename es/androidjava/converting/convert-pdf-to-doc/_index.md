---
title: Convertir PDF a DOC
linktitle: Convertir PDF a DOC
type: docs
weight: 70
url: /es/androidjava/convert-pdf-to-doc/
lastmod: "2026-06-30"
description: Convierta un archivo PDF al formato DOC con facilidad y total control con Aspose.PDF for Android via Java. Obtenga más información sobre cómo optimizar la conversión de archivos Microsoft Word Doc a PDF.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Una de las características más populares es la conversión de PDF a Microsoft Word DOC, lo que facilita la manipulación del contenido. Aspose.PDF for Android via Java le permite convertir archivos PDF a DOC.

**Aspose.PDF for Android via Java** puede crear documentos PDF desde cero y es una excelente herramienta para actualizar, editar y manipular documentos PDF existentes. Una característica importante es la capacidad de convertir páginas y documentos PDF completos a imágenes. Otra característica popular es la conversión de PDF a Microsoft Word DOC, lo que facilita la manipulación del contenido. (La mayoría de los usuarios no pueden editar documentos PDF, pero pueden trabajar fácilmente con tablas, texto e imágenes en Microsoft Word.)

Para simplificar y facilitar la comprensión, Aspose.PDF for Android via Java ofrece un código de dos líneas para transformar un archivo PDF de origen en un archivo DOC.

{{% alert color="primary" %}}

Prueba en línea. Puedes comprobar la calidad de la conversión de Aspose.PDF y ver los resultados en línea en este enlace [products.aspose.app/pdf/conversion/pdf-to-doc](https://products.aspose.app/pdf/conversion/pdf-to-doc)

{{% /alert %}}

El siguiente fragmento de código muestra el proceso de convertir un archivo PDF a formato DOC.

```java
 public void convertPDFtoDOC() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File docFileName = new File(fileStorage, "PDF-to-Word.doc");

        try {
            // Save the file into MS document format
            document.save(docFileName.toString(), SaveFormat.Doc);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


