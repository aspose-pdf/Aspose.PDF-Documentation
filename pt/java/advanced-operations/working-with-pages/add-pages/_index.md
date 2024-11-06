---
title: Adicionar Páginas em PDF 
linktitle: Adicionar Páginas
type: docs
weight: 10
url: pt/java/add-pages/
description: Este artigo ensina como inserir (adicionar) uma página na localização desejada no arquivo PDF. Aprenda como mover, remover (excluir) páginas de um arquivo PDF usando a biblioteca Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Adicionar ou Inserir Página em um Arquivo PDF

Aspose.PDF para Java permite que você insira uma página em um documento PDF em qualquer local no arquivo, bem como adicione páginas ao final de um arquivo PDF. Você precisa passar a localização onde deseja inserir a página em branco para o método de inserção. Esta seção mostra como adicionar páginas a um PDF com Aspose.PDF para Java.

### Inserir Página Vazia em um Arquivo PDF na Localização Desejada

O trecho de código a seguir mostra como inserir uma página vazia em um arquivo PDF:

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) com o arquivo PDF de entrada.

1. Chame o método Insert da coleção [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection) com o índice especificado.
1. Salve o PDF de saída usando o método Save.

O trecho de código a seguir mostra como inserir uma página em um arquivo PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleAddPages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void InsertEmptyPageInPDFFileAtDesiredLocation() {
        Document document = new Document();

        // Adicionar página
        document.getPages().add();

        // Inserir uma página vazia em um PDF
        document.getPages().insert(2);

        // Salvar PDF atualizado
        document.save(_dataDir + "InsertEmptyPage_out.pdf");
    }
```

No exemplo acima, adicionamos uma página vazia com parâmetros padrão. Se você precisar fazer o tamanho da página o mesmo que outra página no documento, você deve adicionar algumas linhas de código:

```java
    public static void InsertEmptyPageInPDFFileAtDesiredLocation01() {
        Document document = new Document();

        // Adicionar página
        Page page1 = document.getPages().add();

        // Inserir uma página vazia em um PDF
        Page page2 = document.getPages().insert(2);
        ;
        // copiar parâmetros da página da página 1
        page2.setArtBox(page1.getArtBox());
        page2.setBleedBox(page1.getBleedBox());
        page2.setCropBox(page1.getCropBox());
        page2.setMediaBox(page1.getMediaBox());
        page2.setTrimBox(page1.getTrimBox());

        // Salvar PDF atualizado
        document.save(_dataDir + "InsertEmptyPage_out.pdf");
    }
```


### Adicionar uma Página Vazia ao Final de um Arquivo PDF

Às vezes, você deseja garantir que um documento termine em uma página vazia. Este tópico explica como inserir uma página vazia no final do documento PDF.

Para inserir uma página vazia no final de um arquivo PDF:

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) com o arquivo PDF de entrada.
1. Chame o método Add da coleção [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection), sem parâmetros.
1. Salve o PDF de saída usando o método Save.

O snippet de código a seguir mostra como inserir uma página vazia no final de um arquivo PDF.

```java
public static void AddAnEmptyPageAtTheEndOfAPDFFile() {

        Document document = new Document();
        // Adicionar página
        document.getPages().add();

        // Inserir uma página vazia no final de um arquivo PDF
        document.getPages().add();

        // Salvar PDF atualizado
        document.save(_dataDir + "InsertEmptyPageAtEnd_out.pdf");
    }

}
```