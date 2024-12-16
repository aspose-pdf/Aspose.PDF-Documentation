---
title: Converter PDF para texto 
linktitle: Converter PDF para texto
type: docs
weight: 120
url: /pt/androidjava/convert-pdf-to-txt/
lastmod: "2021-06-05"
description: Com o Aspose.PDF para Android via Java você pode converter um documento PDF inteiro em um arquivo de texto ou converter apenas uma página PDF em um arquivo de texto.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---


{{% alert color="primary" %}} 

Experimente online. Você pode verificar a qualidade da conversão do Aspose.PDF e visualizar os resultados online neste link [products.aspose.app/pdf/conversion/pdf-to-txt](https://products.aspose.app/pdf/conversion/pdf-to-txt)

{{% /alert %}}

## Converter página PDF para arquivo de texto

Você pode converter documento PDF para arquivo TXT com Aspose.PDF para Android via Java. Você deve usar o método Visit da classe [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) para resolver esta tarefa.

O snippet de código a seguir explica como extrair os textos das páginas específicas.

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
        File txtFileName = new File(fileStorage, "PDF-para-Texto.txt");

        // Salvar o texto extraído em arquivo de texto
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