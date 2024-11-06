---
title: Convertir PDF a PowerPoint 
linktitle: Convertir PDF a PowerPoint
type: docs
weight: 110
url: es/androidjava/convert-pdf-to-powerpoint/
description: Aspose.PDF permite convertir PDF a formato PowerPoint. Una forma es la posibilidad de convertir PDF a PPTX con las diapositivas como imágenes. 
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Tenemos una API llamada Aspose.Slides que ofrece la característica de crear así como manipular presentaciones PPT/PPTX. Esta API también proporciona la característica de convertir archivos PPT/PPTX a formato PDF. En Aspose.PDF para Java, hemos introducido una función para transformar documentos PDF en formato PPTX. Durante esta conversión, las páginas individuales del archivo PDF se convierten en diapositivas separadas en el archivo PPTX.

{{% alert color="primary" %}}

Prueba en línea. Puedes comprobar la calidad de la conversión de Aspose.PDF y ver los resultados en línea en este enlace [products.aspose.app/pdf/conversion/pdf-to-pptx](https://products.aspose.app/pdf/conversion/pdf-to-pptx)

{{% /alert %}}

Durante la conversión de PDF a PPTX, el texto se representa como Texto donde puedes seleccionarlo/actualizarlo, en lugar de ser representado como una imagen. Por favor, ten en cuenta que para convertir archivos PDF al formato PPTX, Aspose.PDF proporciona una clase llamada PptxSaveOptions. Un objeto de la clase [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) se pasa como segundo argumento al método [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..).

Consulta el siguiente fragmento de código para resolver tus tareas con la conversión de PDF a formato PowerPoint:

```java
 public void convertPDFtoPowerPoint() {
        // Cargar documento PDF
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instanciar objeto de opción de guardado de Excel
        PptxSaveOptions pptxSaveOptions = new PptxSaveOptions();


        // Guardar la salida en PPTX
        File xlsFileName = new File(fileStorage, "PDF-to-Powerpoint.pptx");
        try {
            // Guardar el archivo en formato PPTX
            document.save(xlsFileName.toString(), pptxSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```