---
title: Convertir PDF a texto
linktitle: Convertir PDF a texto
type: docs
weight: 120
url: /androidjava/convert-pdf-to-txt/
lastmod: "2021-06-05"
description: Con Aspose.PDF para Android a través de Java puedes convertir un documento PDF completo a un archivo de texto o convertir solo una página PDF a un archivo de texto.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}} 

Prueba en línea. Puedes comprobar la calidad de la conversión de Aspose.PDF y ver los resultados en línea en este enlace [products.aspose.app/pdf/conversion/pdf-to-txt](https://products.aspose.app/pdf/conversion/pdf-to-txt)

{{% /alert %}}

## Convertir página PDF a archivo de texto

Puedes convertir un documento PDF a un archivo TXT con Aspose.PDF para Android a través de Java. Debes utilizar el método Visit de la clase [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) para resolver esta tarea.

El siguiente fragmento de código explica cómo extraer los textos de las páginas particulares.

```java
public void convertPDFPagesToTXT() {
        // Abrir documento
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        TextAbsorber ta = new TextAbsorber();
        int[] pages = new int[] { 1, 3, 4 };

        for (int page : pages) {
            ta.visit(document.getPages().get_Item(page));
        }
        File txtFileName = new File(fileStorage, "PDF-to-Text.txt");

        // Guardar el texto extraído en un archivo de texto
        BufferedWriter writer;
        try {
            writer = new BufferedWriter(new FileWriter(txtFileName));
            writer.write(ta.getText());
            writer.close();
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```