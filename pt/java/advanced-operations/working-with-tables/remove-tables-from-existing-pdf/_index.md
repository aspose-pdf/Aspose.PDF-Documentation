---
title: Remover Tabelas de um PDF Existente
linktitle: Remover Tabelas
type: docs
weight: 40
url: pt/java/remove-tables-from-existing-pdf/
description: Aspose.PDF para Java permite que você remova tabela e múltiplas tabelas do seu documento PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Aspose.PDF para Java oferece as capacidades de inserir/criar Tabela dentro de um documento PDF enquanto está sendo gerado do zero ou você também pode adicionar o objeto de tabela em qualquer documento PDF existente. No entanto, você pode ter uma necessidade de [Manipular Tabelas em PDF Existente](https://docs.aspose.com/pdf/java/manipulate-tables-in-existing-pdf/) onde você pode atualizar os conteúdos em células de tabela existentes. No entanto, você pode se deparar com uma necessidade de remover objetos de tabela de um documento PDF existente.

{{% /alert %}}

Para remover as tabelas, precisamos usar a classe [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber) para obter as tabelas no PDF existente e, em seguida, chamar o método [Remove](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#remove-com.aspose.pdf.AbsorbedTable-).

## Remover Tabela de Documento PDF

Adicionamos uma nova função, ou seja, Remove(), à Classe [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber) existente para remover a tabela do documento PDF. Uma vez que o absorvedor encontra com sucesso as tabelas na página, ele se torna capaz de removê-las. Por favor, verifique o trecho de código a seguir mostrando como remover uma tabela de um documento PDF:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleRemoveTable {
    
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void RemoveTable() {
        // Carregar documento PDF existente
        Document pdfDocument = new Document(_dataDir + "Table_input.pdf");

        // Criar objeto TableAbsorber para encontrar tabelas
        TableAbsorber absorber = new TableAbsorber();

        // Visitar a primeira página com o absorvedor
        absorber.visit(pdfDocument.getPages().get_Item(1));

        // Obter a primeira tabela na página
        AbsorbedTable table = absorber.getTableList().get(0);

        // Remover a tabela
        absorber.remove(table);

        // Salvar PDF
        pdfDocument.save(_dataDir + "Table_out.pdf");
    }  
```


## Remover Várias Tabelas de um Documento PDF

Às vezes, um documento PDF pode conter mais de uma tabela e você pode ter a necessidade de remover várias tabelas dele. Para remover múltiplas tabelas de um documento PDF, por favor, use o seguinte trecho de código:

```java
    public static void RemoveMultipleTable() {
        // Carregar documento PDF existente
        Document pdfDocument = new Document(_dataDir + "Table_input2.pdf");

        // Criar objeto TableAbsorber para encontrar tabelas
        TableAbsorber absorber = new TableAbsorber();

        // Visitar a segunda página com o absorvedor
        absorber.visit(pdfDocument.getPages().get_Item(2));

        // Percorrer a cópia da coleção e remover tabelas
        for (AbsorbedTable table : absorber.getTableList())
            absorber.remove(table);

        // Salvar documento
        pdfDocument.save(_dataDir + "Table2_out.pdf");
    }
}
```