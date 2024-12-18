---
title: Manipular Tabelas em PDF Existente
linktitle: Manipular Tabelas
type: docs
weight: 30
url: /pt/java/manipulate-tables-in-existing-pdf/
description: Manipular tabelas em arquivo PDF existente e substituir tabela antiga por uma nova no documento PDF com Aspose.PDF para Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Manipular tabelas em PDF existente

Uma das primeiras funcionalidades suportadas pelo Aspose.PDF para Java são suas capacidades de Trabalhar com Tabelas e isso fornece um ótimo suporte para adicionar tabelas em arquivos PDF sendo gerados do zero ou em qualquer arquivo PDF existente.
 Você também obtém a capacidade de integrar a Tabela com o Banco de Dados (DOM) para criar tabelas dinâmicas com base no conteúdo do banco de dados. Nesta nova versão, implementamos um novo recurso de busca e análise de tabelas simples que já existem na página de um documento PDF. Uma nova classe chamada **Aspose.PDF.Text.TableAbsorber** fornece essas capacidades. O uso do TableAbsorber é muito semelhante à classe existente TextFragmentAbsorber.

O trecho de código a seguir mostra as etapas para atualizar o conteúdo em uma célula de tabela específica.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleManipulate {

    private static String _dataDir = "/home/admin1/pdf-exemplos/Samples/";

    public static void ManipulateTables() {

        // Carregar arquivo PDF existente
        Document pdfDocument = new Document(_dataDir + "input.pdf");
        // Criar objeto TableAbsorber para encontrar tabelas
        TableAbsorber absorber = new TableAbsorber();

        // Visitar a primeira página com o absorvedor
        absorber.visit(pdfDocument.getPages().get_Item(1));

        // Obter acesso à primeira tabela na página, sua primeira célula e fragmentos de texto nela
        TextFragment fragment = absorber.getTableList().get(0).getRowList().get(0).getCellList().get(0)
                .getTextFragments().get_Item(1);

        // Alterar texto do primeiro fragmento de texto na célula
        fragment.setText("olá mundo");

        pdfDocument.save(_dataDir + "ManipulateTable_out.pdf");
    }
```

## Substituir a tabela antiga por uma nova no documento PDF

Caso você precise encontrar uma tabela específica e substituí-la pela desejada, você pode usar o método Replace() da Classe [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber) para fazer isso.

O exemplo a seguir demonstra a funcionalidade de substituir a tabela dentro do documento PDF:

```java
public static void ReplaceOldTableWithNew() {

        // Carregar documento PDF existente
        Document pdfDocument = new Document(_dataDir + "Table_input2.pdf");

        // Criar objeto TableAbsorber para encontrar tabelas
        TableAbsorber absorber = new TableAbsorber();

        Page page = pdfDocument.getPages().get_Item(1);

        // Visitar a primeira página com o absorvedor
        absorber.visit(page);

        // Obter a primeira tabela na página
        AbsorbedTable table = absorber.getTableList().get(0);

        // Criar nova tabela
        Table newTable = new Table();
        newTable.setColumnWidths("100 100 100");
        newTable.setDefaultCellBorder (new BorderInfo(BorderSide.All, 1F));

        Row row = newTable.getRows().add();
        row.getCells().add("Col 1");
        row.getCells().add("Col 2");
        row.getCells().add("Col 3");

        // Substituir a tabela pela nova
        absorber.replace(page, table, newTable);

        // Salvar documento
        pdfDocument.save(_dataDir + "TableReplaced_out.pdf");
        
    }

}
```