---
title: Принудительное Рендеринг Таблицы на Новой Странице
type: docs
weight: 20
url: /java/force-table-rendering-on-new-page/
lastmod: "2021-06-05"
---

## Рендеринг Таблицы на Новой Странице

По умолчанию, абзацы добавляются в коллекцию Paragraphs объекта Page. Однако, возможно отрендерить таблицу на новой странице вместо того, чтобы добавлять её непосредственно после ранее добавленного объекта уровня абзаца на странице.

### Добавление Таблицы

Чтобы отрендерить таблицу на новой странице, используйте метод [IsInNewPage](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#isInNewPage--) в классе [BaseParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/baseparagraph). Следующий фрагмент кода показывает, как это сделать.

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
        // Добавлена страница.
        Page curPage = doc.getPages().add();
        for (int i = 1; i <= 120; i++)
        {
            Row row = table.getRows().add();
            row.setFixedRowHeight (15);
            Cell cell1 = row.getCells().add();
            cell1.getParagraphs().add(new TextFragment("Содержимое 1"));
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
        // Я хочу оставить таблицу 1 на следующей странице, пожалуйста...
        paragraphs.add(table1);
        
        doc.save(_dataDir + "IsNewPageProperty_Test_out.pdf");
    }
}
```


{{% alert color="primary" %}}

Класс com.aspose.pdf.[Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table) позволяет создавать/отображать таблицы в PDF-документах. Похожая функция также поддерживается классом aspose.pdf.[Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table), но мы рекомендуем нашим клиентам попробовать использовать последнюю модель объекта документа (DOM) из пакета com.aspose.pdf, поскольку все новые функции и исправления проблем выполняются в новом DOM. Однако в устаревшей версии Aspose.PDF для Java (пакет aspose.pdf) есть метод [isInNewPage(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#isInNewPage--) в классе параграфа, чтобы параграф отображался на новой странице. Для обратной совместимости метод [isInNewPage(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#isInNewPage--) был добавлен в класс [BaseParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph).

{{% /alert %}}