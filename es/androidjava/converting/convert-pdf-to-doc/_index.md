---
title: Convertir PDF a DOC 
linktitle: Convertir PDF a DOC
type: docs
weight: 70
url: /es/androidjava/convert-pdf-to-doc/
lastmod: "2021-06-05"
description: Convierta archivos PDF a formato DOC con facilidad y control total con Aspose.PDF para Android a través de Java. Aprenda más sobre cómo ajustar la conversión de archivos Microsoft Word Doc a PDF.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Una de las características más populares es la conversión de PDF a Microsoft Word DOC, lo que hace que el contenido sea fácil de manipular. Aspose.PDF para Android a través de Java le permite convertir archivos PDF a DOC.

**Aspose.PDF para Android a través de Java** puede crear documentos PDF desde cero y es un gran conjunto de herramientas para actualizar, editar y manipular documentos PDF existentes.
 Una característica importante es la capacidad de convertir páginas y documentos PDF completos en imágenes. Otra característica popular es la conversión de PDF a Microsoft Word DOC, lo que hace que el contenido sea fácil de manipular. (La mayoría de los usuarios no pueden editar documentos PDF, pero pueden trabajar fácilmente con tablas, texto e imágenes en Microsoft Word).

Para simplificar y hacer comprensible, Aspose.PDF para Android a través de Java proporciona un código de dos líneas para transformar un archivo PDF fuente en un archivo DOC.

{{% alert color="primary" %}}

Prueba en línea. Puedes comprobar la calidad de la conversión de Aspose.PDF y ver los resultados en línea en este enlace [products.aspose.app/pdf/conversion/pdf-to-doc](https://products.aspose.app/pdf/conversion/pdf-to-doc)

{{% /alert %}}

El siguiente fragmento de código muestra el proceso de conversión de un archivo PDF a formato DOC.

```java
 public void convertPDFtoDOC() {
        // Abrir el documento PDF fuente
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File docFileName = new File(fileStorage, "PDF-to-Word.doc");

        try {
            // Guardar el archivo en formato de documento MS
            document.save(docFileName.toString(), SaveFormat.Doc);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```