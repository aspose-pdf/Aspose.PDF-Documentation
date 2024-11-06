---
title: Converter PDF para Microsoft PowerPoint 
linktitle: Converter PDF para PowerPoint
type: docs
weight: 30
url: pt/php-java/convert-pdf-to-powerpoint/
lastmod: "2024-05-20"
description: Aspose.PDF permite converter PDF para o formato PowerPoint usando PHP. Existe uma maneira de converter PDF para PPTX com slides como imagens.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF para PHP** permite acompanhar o progresso da conversão de PDF para PPTX. Temos uma API chamada Aspose.Slides que oferece o recurso de criar e manipular apresentações PPT/PPTX. Esta API também fornece o recurso de converter arquivos PPT/PPTX para o formato PDF. No Aspose.PDF para PHP, introduzimos um recurso para transformar documentos PDF em formato PPTX. Durante esta conversão, as páginas individuais do arquivo PDF são convertidas em slides separados no arquivo PPTX.

Durante a conversão de PDF para PPTX, o texto é renderizado como Texto, onde você pode selecioná-lo/atualizá-lo, em vez de ser renderizado como uma imagem.
 Por favor, note que, para converter arquivos PDF para o formato PPTX, o Aspose.PDF fornece uma classe chamada PptxSaveOptions. Um objeto da classe [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) é passado como um segundo argumento para o método [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..).

Confira o próximo trecho de código para resolver suas tarefas com a conversão de PDF para formato PowerPoint:

```php
// Carregar o documento PDF de entrada
$document = new Document($inputFile);

// Criar uma instância de PptxSaveOptions
$saveOption = new PptxSaveOptions();

// Salvar o documento PDF como um arquivo PPTX
$document->save($outputFile, $saveOption);
```

## Converter PDF para PPTX com Slides como Imagens

Caso você precise converter um PDF pesquisável para PPTX como imagens em vez de texto selecionável, o Aspose.PDF fornece tal recurso por meio da classe [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions). Para conseguir isso, defina a propriedade SlidesAsImages da classe [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) como 'true', como mostrado no exemplo de código a seguir.

O seguinte trecho de código mostra o processo para converter arquivos PDF no formato PPTX Slides como Imagens.

```php
// Carregar o documento PDF de entrada
$document = new Document($inputFile);

// Criar uma instância de PptxSaveOptions
$saveOption = new PptxSaveOptions();
$saveOption->setSlidesAsImages(true);

// Salvar o documento PDF como um arquivo PPTX
$document->save($outputFile, $saveOption);

    public static void ConvertPDFtoPPTX_SlideAsImages() {
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "PDFToPPTX.pdf").toString();
        String pptxDocumentFileName = Paths.get(_dataDir.toString(), "PDFToPPTX_out.pptx").toString();

        // Carregar documento PDF
        Document doc = new Document(pdfDocumentFileName);
        // Instanciar a instância de PptxSaveOptions
        PptxSaveOptions pptx_save = new PptxSaveOptions();
        // Salvar a saída no formato PPTX
        pptx_save.setSlidesAsImages(true);

        doc.save(pptxDocumentFileName, pptx_save);
    }
```

{{% alert color="success" %}}
**Tente converter PDF para PowerPoint online**

Aspose.PDF para PHP apresenta a você o aplicativo online gratuito ["PDF para PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Conversão Aspose.PDF PDF para PPTX com Aplicativo Gratuito](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}