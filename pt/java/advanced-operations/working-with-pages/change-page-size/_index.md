---
title: Alterar Tamanho da Página do PDF Programaticamente 
linktitle: Alterar Tamanho da Página
type: docs
weight: 50
url: /pt/java/change-page-size/
description: Alterar o Tamanho da Página do seu arquivo PDF usando a biblioteca Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Alterar Tamanho da Página do PDF

Aspose.PDF para Java permite que você altere o tamanho da página do PDF com linhas simples de código em suas aplicações Java. Este tópico explica como atualizar/alterar as dimensões (tamanho) da página de um arquivo PDF existente.

A classe [Page](https://reference.aspose.com/pdf//java/com.aspose.pdf/page) contém o método SetPageSize(...) que permite definir o tamanho da página. O trecho de código abaixo atualiza as dimensões da página em alguns passos fáceis:

1. Carregue o arquivo PDF de origem.
1. Obtenha as páginas no objeto [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection).
1. Obtenha uma determinada página.
1. Chame o método SetPageSize(..) para atualizar suas dimensões.

1. Chame o método Save(..) da classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) para gerar o arquivo PDF com as dimensões de página atualizadas.

{{% alert color="primary" %}}

Por favor, note que as propriedades de altura e largura usam pontos como unidade básica, onde 1 polegada = 72 pontos e 1 cm = 1/2.54 polegada = 0.3937 polegada = 28.3 pontos.

{{% /alert %}}

O snippet de código a seguir mostra como alterar as dimensões da página PDF para o tamanho A4.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleChangePDFPageSize {
    // O caminho para o diretório de documentos.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ChangePDFPageSize() {
        
        // Abrir o primeiro documento
        Document pdfDocument = new Document(_dataDir + "sample.pdf");
                
        // Obter coleção de páginas
        PageCollection pageCollection = pdfDocument.getPages();

        // Obter página específica
        Page pdfPage = pageCollection.get_Item(1);

        // Definir o tamanho da página como A4 (11.7 x 8.3 pol) e no Aspose.Pdf, 1 polegada = 72 pontos
        // Portanto, as dimensões A4 em pontos serão (842.4, 597.6)
        pdfPage.setPageSize(597.6, 842.4);

        _dataDir = _dataDir + "UpdateDimensions_out.pdf";
        
        // Salvar o documento atualizado
        pdfDocument.save(_dataDir);
    }
```


## Obter Tamanho da Página PDF

Você pode ler o tamanho da página de um arquivo PDF existente usando Aspose.PDF para Java. O exemplo de código a seguir mostra como ler as dimensões da página PDF usando Java.

```java
    public static void GetPDFPageSize() {
        
        // Abrir o primeiro documento
        Document pdfDocument = new Document(_dataDir + "sample.pdf");
                
        // Adiciona uma página em branco ao documento PDF
        Page page = pdfDocument.getPages().size() > 0 ? pdfDocument.getPages().get_Item(1) : pdfDocument.getPages().add();
        
        // Obter informações de altura e largura da página
        System.out.println(page.getPageRect(true).getWidth() + ":" + page.getPageRect(true).getHeight());
        
        // Rotacionar página em um ângulo de 90 graus
        page.setRotate (Rotation.on90);

        // Obter informações de altura e largura da página
        System.out.println(page.getPageRect(true).getWidth() + ":" + page.getPageRect(true).getHeight());
        
        // Salvar o documento atualizado
        _dataDir = _dataDir + "UpdateDimensions_out.pdf";
        pdfDocument.save(_dataDir);
    }

}
```