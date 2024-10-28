---
title: 强制表格在新页面渲染
type: docs
weight: 20
url: /java/force-table-rendering-on-new-page/
lastmod: "2021-06-05"
---

## 在新页面渲染表格

默认情况下，段落会被添加到页面对象的段落集合中。然而，可以在新页面上渲染表格，而不是直接在页面上已添加的段落级对象之后。

### 添加表格

要在新页面上渲染表格，请使用 [BaseParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/baseparagraph) 类中的 [IsInNewPage](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#isInNewPage--) 方法。以下代码片段展示了如何实现。

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
        // 添加页面。
        Page curPage = doc.getPages().add();
        for (int i = 1; i <= 120; i++)
        {
            Row row = table.getRows().add();
            row.setFixedRowHeight (15);
            Cell cell1 = row.getCells().add();
            cell1.getParagraphs().add(new TextFragment("内容 1"));
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
        // 我想保持表格1在下一页...
        paragraphs.add(table1);
        
        doc.save(_dataDir + "IsNewPageProperty_Test_out.pdf");
    }
}
```


{{% alert color="primary" %}}

com.aspose.pdf.[Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table) 类提供了在 PDF 文档中创建/渲染表格的功能。aspose.pdf.[Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table) 类也支持类似的功能，但我们鼓励客户尝试使用 com.aspose.pdf 包的最新文档对象模型 (DOM)，因为所有的新功能和问题解决都是在新的 DOM 中进行的。然而，旧版的 Aspose.PDF for Java（aspose.pdf 包）在段落类中有一个方法 [isInNewPage(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#isInNewPage--)，以便段落在新页面上渲染。为了向后兼容，[isInNewPage(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#isInNewPage--) 方法已被添加到 [BaseParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph) 类中。

{{% /alert %}}