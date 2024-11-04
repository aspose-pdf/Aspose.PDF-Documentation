---
title: 新しいページでのテーブルレンダリングの強制
type: docs
weight: 20
url: /java/force-table-rendering-on-new-page/
lastmod: "2021-06-05"
---

## 新しいページでのテーブルレンダリング

デフォルトでは、段落はPageオブジェクトのParagraphsコレクションに追加されます。ただし、ページ上で直前に追加された段落レベルのオブジェクトの直後ではなく、新しいページにテーブルをレンダリングすることが可能です。

### テーブルの追加

新しいページでテーブルをレンダリングするには、[BaseParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/baseparagraph)クラスの[IsInNewPage](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#isInNewPage--)メソッドを使用します。以下のコードスニペットにその方法を示します。

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
        // ページを追加しました。
        Page curPage = doc.getPages().add();
        for (int i = 1; i <= 120; i++)
        {
            Row row = table.getRows().add();
            row.setFixedRowHeight (15);
            Cell cell1 = row.getCells().add();
            cell1.getParagraphs().add(new TextFragment("Content 1"));
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
        // テーブル1を次のページに移動したいです...
        paragraphs.add(table1);
        
        doc.save(_dataDir + "IsNewPageProperty_Test_out.pdf");
    }
}
```


{{% alert color="primary" %}}

com.aspose.pdf.[Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table) クラスにより、PDF ドキュメントでテーブルを作成/レンダリングすることが可能になります。類似の機能は aspose.pdf.[Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table) クラスでもサポートされていますが、最新の com.aspose.pdf パッケージのドキュメント オブジェクト モデル (DOM) の使用をお勧めします。なぜなら、新しい機能や問題の解決はすべて新しい DOM で行われているからです。しかし、古い Aspose.PDF for Java (aspose.pdf パッケージ) には、段落クラスに [isInNewPage(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#isInNewPage--) メソッドがあり、段落が新しいページにレンダリングされるようになっています。後方互換性を保つために、[isInNewPage(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#isInNewPage--) メソッドが [BaseParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph) クラスに追加されています。

{{% /alert %}}