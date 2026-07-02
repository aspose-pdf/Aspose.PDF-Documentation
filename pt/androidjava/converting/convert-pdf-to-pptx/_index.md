---
title: Converter PDF para PowerPoint
linktitle: Converter PDF para PowerPoint
type: docs
weight: 110
url: /pt/androidjava/convert-pdf-to-powerpoint/
description: Aspose.PDF permite que você converta PDF para o formato PowerPoint. Uma maneira é que há a possibilidade de converter PDF para PPTX com slides como imagens.
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Temos uma API chamada Aspose.Slides que oferece o recurso de criar e manipular apresentações PPT/PPTX. Esta API também fornece o recurso de converter arquivos PPT/PPTX para o formato PDF. No Aspose.PDF for Java, introduzimos um recurso para transformar documentos PDF em formato PPTX. Durante essa conversão, as páginas individuais do arquivo PDF são convertidas em slides separados no arquivo PPTX.

{{% alert color="primary" %}}

Experimente online. Você pode verificar a qualidade da conversão Aspose.PDF e visualizar os resultados online neste link [products.aspose.app/pdf/conversion/pdf-to-pptx](https://products.aspose.app/pdf/conversion/pdf-to-pptx)

{{% /alert %}}

Durante a conversão de PDF para PPTX, o texto é renderizado como Texto onde você pode selecionar/atualizar, em vez de ser renderizado como uma imagem. Observe que, para converter arquivos PDF para o formato PPTX, o Aspose.PDF fornece uma classe chamada PptxSaveOptions. Um objeto da [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) a classe é passada como segundo argumento para o [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)método .save(..).

Confira o próximo trecho de código para resolver suas tarefas com a conversão de PDF para formato PowerPoint:

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

