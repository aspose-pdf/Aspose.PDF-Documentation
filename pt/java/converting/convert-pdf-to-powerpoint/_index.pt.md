---
title: Converter PDF para Microsoft PowerPoint
linktitle: Converter PDF para PowerPoint
type: docs
weight: 30
url: /java/convert-pdf-to-powerpoint/
lastmod: "2021-11-19"
description: Aspose.PDF permite converter PDF para o formato PowerPoint usando Java. Há uma possibilidade de converter PDF para PPTX com Slides como Imagens.
lastmod: "2021-10-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF para Java** permite rastrear o progresso da conversão de PDF para PPTX.
Temos uma API chamada Aspose.Slides que oferece a funcionalidade de criar e manipular apresentações PPT/PPTX. Esta API também fornece a funcionalidade de converter arquivos PPT/PPTX para o formato PDF. No Aspose.PDF para Java, introduzimos um recurso para transformar documentos PDF em formato PPTX. Durante essa conversão, as páginas individuais do arquivo PDF são convertidas em slides separados no arquivo PPTX.

Durante a conversão de PDF para PPTX, o texto é renderizado como Texto, onde você pode selecioná-lo/atualizá-lo, em vez de ser renderizado como uma imagem.
 Observe que, para converter arquivos PDF para o formato PPTX, o Aspose.PDF fornece uma classe chamada PptxSaveOptions. Um objeto da classe [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) é passado como segundo argumento para o método [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..).

Confira o próximo trecho de código para resolver suas tarefas de conversão de PDF para o formato PowerPoint:

```java
public final class ConvertPDFtoPPTX {

    private ConvertPDFtoPPTX() {

    }

    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void run() throws IOException {
        convertPDFtoPPTX_Simple();
        convertPDFtoPPTX_SlideAsImages();
        convertPDFtoPPTX_ProgresDetails();
    }

    public static void convertPDFtoPPTX_Simple() {
        String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX.pdf").toString();
        String pptxDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX_out.pptx").toString();

        // Carregar documento PDF
        Document document = new Document(documentFileName);

        // Instanciar PptxSaveOptions
        PptxSaveOptions pptx_save = new PptxSaveOptions();

        // Salvar a saída no formato PPTX
        document.save(pptxDocumentFileName, pptx_save);
        document.close();
    }
}
```

## Converter PDF para PPTX com Slides como Imagens

Caso você precise converter um PDF pesquisável para PPTX como imagens em vez de texto selecionável, o Aspose.PDF oferece esse recurso através da classe [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions). Para conseguir isso, defina a propriedade SlidesAsImages da classe [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) como 'true', conforme mostrado no exemplo de código a seguir.

O exemplo de código a seguir mostra o processo de conversão de arquivos PDF para o formato PPTX com Slides como Imagens.

```java
public static void convertPDFtoPPTX_SlideAsImages() {
    String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX.pdf").toString();
    String pptxDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX_out.pptx").toString();

    // Carregar documento PDF
    Document document = new Document(documentFileName);
    // Instanciar instância de PptxSaveOptions
    PptxSaveOptions pptxSaveOptions = new PptxSaveOptions();
    // Salvar a saída no formato PPTX
    pptxSaveOptions.setSlidesAsImages(true);

    document.save(pptxDocumentFileName, pptxSaveOptions);
    document.close();
}
```


## Mostrar Progresso no Console com Aspose.PDF para Java fica assim:

```java
package com.aspose.pdf.examples.conversion;

import com.aspose.pdf.Document;
import com.aspose.pdf.PptxSaveOptions;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * Converter PDF para PPTX.
 */
public final class ConvertPDFtoPPTX {

    private ConvertPDFtoPPTX() {

    }

    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void run() throws IOException {
        convertPDFtoPPTX_ProgressDetails();
    }

    public static void convertPDFtoPPTX_ProgressDetails() {
        String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX.pdf").toString();
        String pptxDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX_out.pptx").toString();

        // Carregar documento PDF
        Document document = new Document(documentFileName);

        // Instanciar instância de PptxSaveOptions
        PptxSaveOptions pptx_save = new PptxSaveOptions();

        // Especificar Manipulador de Progresso Personalizado
        pptx_save.setCustomProgressHandler(new ShowProgressOnConsole());

        // Salvar a saída no formato PPTX
        document.save(pptxDocumentFileName, pptx_save);
        document.close();
    }
}
```


## Detalhe de Progresso da Conversão de PPTX

Aspose.PDF para Java permite que você acompanhe o progresso da conversão de PDF para PPTX. A classe [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) fornece a propriedade [CustomProgressHandler](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlSaveOptions) que pode ser especificada para um método personalizado para rastrear o progresso da conversão, conforme mostrado no exemplo de código a seguir.

```java
package com.aspose.pdf.examples;

import java.time.LocalDateTime;

import com.aspose.pdf.ProgressEventType;
import com.aspose.pdf.UnifiedSaveOptions.ConversionProgressEventHandler;
import com.aspose.pdf.UnifiedSaveOptions.ProgressEventHandlerInfo;

class ShowProgressOnConsole extends ConversionProgressEventHandler{

    @Override
    public void invoke(ProgressEventHandlerInfo eventInfo) {        
        switch (eventInfo.EventType) {
            case ProgressEventType.TotalProgress:
                System.out.println(
                        String.format("%s  - Progresso da conversão: %d %%.", LocalDateTime.now().toString(), eventInfo.Value));
                break;
            case ProgressEventType.ResultPageCreated:
                System.out.println(String.format("%s  - Página de resultado %s de %d layout criada.", LocalDateTime.now().toString(),
                        eventInfo.Value, eventInfo.MaxValue));
                break;
            case ProgressEventType.ResultPageSaved:
                System.out.println(String.format("%s  - Página de resultado %d de %d exportada.", LocalDateTime.now(), eventInfo.Value, eventInfo.MaxValue));
                break;
            case ProgressEventType.SourcePageAnalysed:
                System.out.println(String.format("%s  - Página de origem %d de %d analisada.", LocalDateTime.now(),  eventInfo.Value, eventInfo.MaxValue));
                break;
            default:
                break;
        }
    }
```


{{% alert color="success" %}}
**Tente converter PDF para PowerPoint online**

Aspose.PDF para Java apresenta a você o aplicativo online gratuito ["PDF para PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), onde você pode tentar investigar a funcionalidade e a qualidade de seu funcionamento.

[![Conversão Aspose.PDF de PDF para PPTX com Aplicativo Grátis](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}