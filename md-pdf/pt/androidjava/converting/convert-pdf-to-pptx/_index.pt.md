---
title: Converter PDF para PowerPoint
linktitle: Converter PDF para PowerPoint
type: docs
weight: 110
url: /androidjava/convert-pdf-to-powerpoint/
description: Aspose.PDF permite que você converta PDF para o formato PowerPoint. Uma maneira é a possibilidade de converter PDF para PPTX com Slides como Imagens.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Nós temos uma API chamada Aspose.Slides que oferece o recurso de criar e também manipular apresentações PPT/PPTX. Esta API também fornece o recurso de converter arquivos PPT/PPTX para o formato PDF. No Aspose.PDF para Java, introduzimos um recurso para transformar documentos PDF em formato PPTX. Durante esta conversão, as páginas individuais do arquivo PDF são convertidas em slides separados no arquivo PPTX.

{{% alert color="primary" %}}

Experimente online. Você pode verificar a qualidade da conversão do Aspose.PDF e visualizar os resultados online neste link [products.aspose.app/pdf/conversion/pdf-to-pptx](https://products.aspose.app/pdf/conversion/pdf-to-pptx)

{{% /alert %}}

Durante a conversão de PDF para PPTX, o texto é renderizado como Texto onde você pode selecioná-lo/atualizá-lo, em vez de ser renderizado como uma imagem. Por favor, note que para converter arquivos PDF para o formato PPTX, Aspose.PDF fornece uma classe chamada PptxSaveOptions. Um objeto da classe [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) é passado como segundo argumento para o método [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..).

Confira o próximo trecho de código para resolver suas tarefas com a conversão de PDF para o formato PowerPoint:

```java
 public void convertPDFtoPowerPoint() {
        // Carregar documento PDF
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instanciar objeto ExcelSave Option
        PptxSaveOptions pptxSaveOptions = new PptxSaveOptions();


        // Salvar a saída em PPTX
        File xlsFileName = new File(fileStorage, "PDF-to-Powerpoint.pptx");
        try {
            // Salvar o arquivo no formato PPTX
            document.save(xlsFileName.toString(), pptxSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```