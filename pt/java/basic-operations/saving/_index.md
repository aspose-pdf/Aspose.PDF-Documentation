---
title: Salvar Documento PDF
linktitle: Salvar
type: docs
weight: 30
url: /pt/java/save-pdf-document/
description: Aprenda como salvar um arquivo PDF com a biblioteca Aspose.PDF para Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Salvar documento PDF no sistema de arquivos

Você pode salvar o documento PDF criado ou manipulado no sistema de arquivos usando o método Save da classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
Quando você não fornece o tipo de formato (opções), o documento é salvo no formato Aspose.PDF v.1.7 (*.pdf).

```java
package com.aspose.pdf.examples;


import java.io.FileOutputStream;

import java.nio.file.Path;
import java.nio.file.Paths;
import com.aspose.pdf.*;

public final class BasicOperationsSave {

    private BasicOperationsSave() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) {
        SaveDocument();
        SaveDocumentStream();
        SaveDocumentAsPDFx();
    }

    public static void SaveDocument() {
        String originalFileName = _dataDir + "/SimpleResume.pdf";
        String modifiedFileName = _dataDir + "/SimpleResumeModified.pdf";

        Document pdfDocument = new Document(originalFileName);
        // fazer alguma manipulação, por exemplo, adicionar nova página vazia
        pdfDocument.getPages().add();
        pdfDocument.save(modifiedFileName);
    }
```


## Salvar documento PDF para stream

Você também pode salvar o documento PDF criado ou manipulado para stream usando sobrecargas dos métodos Save.

```java
public static void SaveDocumentStream() {
        String originalFileName = _dataDir + "/SimpleResume.pdf";
        String modifiedFileName = _dataDir + "/SimpleResumeModified.pdf";

        Document pdfDocument = new Document(originalFileName);
        // faça alguma manipulação, por exemplo, adicionar uma nova página vazia
        pdfDocument.getPages().add();
        try {
            pdfDocument.save(new FileOutputStream(modifiedFileName));
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

    }

```

## Salvar documento PDF em aplicações Web

Para salvar documentos em aplicações Web, você pode usar as maneiras propostas acima. Além disso, a classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) tem um método sobrecarregado Save.
```java
    // @RequestMapping(value = "/files/{file_name}", method = RequestMethod.GET)
    // public void getFile(@PathVariable("file_name") String fileName, HttpServletResponse response) {
    //     try {
    //         response.setContentType("application/pdf");
    //         // obtenha seu arquivo como InputStream
    //         InputStream is = new FileInputStream(_dataDir + fileName);
    //         // copie-o para o OutputStream da resposta
    //         org.apache.commons.io.IOUtils.copy(is, response.getOutputStream());
    //         response.flushBuffer();
    //     } catch (IOException ex) {
    //         log.info("Erro ao escrever o arquivo no stream de saída. O nome do arquivo era '{}'", fileName, ex);
    //         throw new RuntimeException("Erro de E/S ao escrever o arquivo no stream de saída");
    //     }
    // }
```


Para uma explicação mais detalhada, siga para a seção [Showcase]().

## Salvar no formato PDF/A ou PDF/X

O PDF/A é uma versão do Formato de Documento Portátil (PDF) padronizada pela ISO para uso em arquivamento e preservação a longo prazo de documentos eletrônicos. O PDF/A difere do PDF em que proíbe recursos não adequados para arquivamento a longo prazo, como vinculação de fontes (em oposição à incorporação de fontes) e criptografia. Os requisitos ISO para visualizadores de PDF/A incluem diretrizes de gestão de cores, suporte a fontes incorporadas e uma interface de usuário para leitura de anotações incorporadas.

O PDF/X é um subconjunto do padrão ISO para PDF. O propósito do PDF/X é facilitar a troca de gráficos, e por isso tem uma série de requisitos relacionados à impressão que não se aplicam aos arquivos PDF padrão.

Em ambos os casos, o método Save é usado para armazenar os documentos, enquanto os documentos devem ser preparados usando o método Convert.

```java
public static void SaveDocumentAsPDFx() {
        Document pdfDocument = new Document("../../../Samples/SimpleResume.pdf");
        pdfDocument.getPages().add();
        pdfDocument.convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
        pdfDocument.save("../../../Samples/SimpleResume_X3.pdf");
    }

}
```