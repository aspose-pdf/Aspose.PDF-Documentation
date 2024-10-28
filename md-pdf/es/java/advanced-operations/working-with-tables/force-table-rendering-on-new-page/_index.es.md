---
title: Forzar el Renderizado de la Tabla en una Nueva Página
type: docs
weight: 20
url: /java/force-table-rendering-on-new-page/
lastmod: "2021-06-05"
---

## Renderizar Tabla en una Nueva Página

Por defecto, los párrafos se agregan a la colección de Párrafos de un objeto Página. Sin embargo, es posible renderizar una tabla en una nueva página en lugar de directamente después del objeto de nivel de párrafo agregado previamente en la página.

### Agregar una Tabla

Para renderizar una tabla en una nueva página, use el método [IsInNewPage](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#isInNewPage--) en la clase [BaseParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/baseparagraph). El siguiente fragmento de código muestra cómo.

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
        // Página añadida.
        Page curPage = doc.getPages().add();
        for (int i = 1; i <= 120; i++)
        {
            Row row = table.getRows().add();
            row.setFixedRowHeight (15);
            Cell cell1 = row.getCells().add();
            cell1.getParagraphs().add(new TextFragment("Contenido 1"));
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
        // Quiero mantener la tabla 1 en la siguiente página por favor...
        paragraphs.add(table1);
        
        doc.save(_dataDir + "IsNewPageProperty_Test_out.pdf");
    }
}
```


{{% alert color="primary" %}}

La clase com.aspose.pdf.[Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table) hace posible crear/renderizar tablas en documentos PDF. Una característica similar también es compatible con la clase aspose.pdf.[Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table), pero animamos a nuestros clientes a intentar usar el último Modelo de Objetos de Documento (DOM) del paquete com.aspose.pdf, porque todas las nuevas características y la resolución de problemas se están llevando a cabo en el nuevo DOM. Sin embargo, el legado Aspose.PDF para Java (el paquete aspose.pdf) tiene un método [isInNewPage(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#isInNewPage--) en la clase de párrafo, para que el párrafo se renderice en una nueva página. Para la compatibilidad con versiones anteriores, el método [isInNewPage(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#isInNewPage--) ha sido añadido a la clase [BaseParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph).

{{% /alert %}}