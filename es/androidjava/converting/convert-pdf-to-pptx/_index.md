---
title: Convertir PDF a PowerPoint
linktitle: Convertir PDF a PowerPoint
type: docs
weight: 110
url: /es/androidjava/convert-pdf-to-powerpoint/
description: Aspose.PDF le permite convertir PDF al formato PowerPoint. Una forma es la posibilidad de convertir PDF a PPTX con diapositivas como imágenes.
lastmod: "2026-06-30"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Tenemos una API llamada Aspose.Slides que ofrece la función de crear y manipular presentaciones PPT/PPTX. Esta API también proporciona la función de convertir archivos PPT/PPTX al formato PDF. En Aspose.PDF for Java, hemos introducido una función para transformar documentos PDF al formato PPTX. Durante esta conversión, las páginas individuales del archivo PDF se convierten en diapositivas separadas en el archivo PPTX.

{{% alert color="primary" %}}

Pruebe en línea. Puede comprobar la calidad de la conversión de Aspose.PDF y ver los resultados en línea en este enlace [products.aspose.app/pdf/conversion/pdf-to-pptx](https://products.aspose.app/pdf/conversion/pdf-to-pptx)

{{% /alert %}}

Durante la conversión de PDF a PPTX, el texto se muestra como Texto donde puede seleccionarse/actualizarse, en lugar de renderizarse como una imagen. Tenga en cuenta que, para convertir archivos PDF al formato PPTX, Aspose.PDF proporciona una clase llamada PptxSaveOptions. Un objeto de la [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) la clase se pasa como segundo argumento a la [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..) método.

Revise el siguiente fragmento de código para resolver sus tareas con la conversión de PDF a formato PowerPoint:

```java
 public void convertPDFtoPowerPoint() {
        // Load PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        PptxSaveOptions pptxSaveOptions = new PptxSaveOptions();


        // Save the output in PPTX
        File xlsFileName = new File(fileStorage, "PDF-to-Powerpoint.pptx");
        try {
            // Save the file into PPTX format
            document.save(xlsFileName.toString(), pptxSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

