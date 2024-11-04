---
title: Forçar Renderização de Tabela em Nova Página
type: docs
weight: 20
url: /java/force-table-rendering-on-new-page/
lastmod: "2021-06-05"
---

## Renderizar Tabela em Nova Página

Por padrão, parágrafos são adicionados à coleção de Parágrafos de um objeto Página. No entanto, é possível renderizar uma tabela em uma nova página em vez de diretamente após o objeto de nível de parágrafo previamente adicionado na página.

### Adicionando uma Tabela

Para renderizar uma tabela em uma nova página, use o método [IsInNewPage](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#isInNewPage--) na classe [BaseParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/baseparagraph). O trecho de código a seguir mostra como.

```java
public static void RenderTableOnNewPage(){
        Document doc = new Document();
        PageInfo pageInfo = doc.getPageInfo();
        MarginInfo marginInfo = pageInfo.getMargin();

        marginInfo.setLeft (37);
        marginInfo.setRight (37);
        marginInfo.setTop (37);
        marginInfo.setBottom (37);

        pageInfo.setLandscape(true);

        Table table = new Table();
        table.setColumnWidths ("50 100");
        // Página adicionada.
        Page curPage = doc.getPages().add();
        for (int i = 1; i <= 120; i++)
        {
            Row row = table.getRows().add();
            row.setFixedRowHeight (15);
            Cell cell1 = row.getCells().add();
            cell1.getParagraphs().add(new TextFragment("Conteúdo 1"));
            Cell cell2 = row.getCells().add();
            cell2.getParagraphs().add(new TextFragment("HHHHH"));
        }
        Paragraphs paragraphs = curPage.getParagraphs();
        paragraphs.add(table);
        /********************************************/
        Table table1 = new Table();
        table.setColumnWidths ("100 100");
        for (int i = 1; i <= 10; i++)
        {
            Row row = table1.getRows().add();
            Cell cell1 = row.getCells().add();
            cell1.getParagraphs().add(new TextFragment("LAAAAAAA"));
            Cell cell2 = row.getCells().add();
            cell2.getParagraphs().add(new TextFragment("LAAGGGGGG"));
        }
        table1.setInNewPage (true);
        // Eu quero manter a tabela 1 na próxima página, por favor...
        paragraphs.add(table1);
        
        doc.save(_dataDir + "IsNewPageProperty_Test_out.pdf");
    }
}
```


{{% alert color="primary" %}}

A classe com.aspose.pdf.[Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table) possibilita a criação/renderização de tabelas em documentos PDF. Um recurso semelhante também é suportado pela classe aspose.pdf.[Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table), mas encorajamos nossos clientes a tentarem usar o mais recente Modelo de Objeto de Documento (DOM) do pacote com.aspose.pdf, porque todos os novos recursos e resolução de problemas estão sendo realizados no novo DOM. No entanto, o legado Aspose.PDF para Java (o pacote aspose.pdf) possui um método [isInNewPage(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#isInNewPage--) na classe de parágrafo, para que o parágrafo seja renderizado em uma nova página. Para compatibilidade retroativa, o método [isInNewPage(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#isInNewPage--) foi adicionado à classe [BaseParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph).

{{% /alert %}}