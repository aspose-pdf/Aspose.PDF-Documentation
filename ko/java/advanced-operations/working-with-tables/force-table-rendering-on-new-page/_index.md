---
title: 강제 테이블 렌더링을 새 페이지에서 시작하기
type: docs
weight: 20
url: /ko/java/force-table-rendering-on-new-page/
lastmod: "2021-06-05"
---

## 새 페이지에서 테이블 렌더링

기본적으로, 단락은 Page 객체의 Paragraphs 컬렉션에 추가됩니다. 하지만 페이지의 이전에 추가된 단락 수준 객체 바로 뒤가 아닌 새 페이지에 테이블을 렌더링할 수 있습니다.

### 테이블 추가하기

새 페이지에 테이블을 렌더링하려면, [BaseParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/baseparagraph) 클래스의 [IsInNewPage](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#isInNewPage--) 메서드를 사용하세요. 아래의 코드 스니펫은 그 방법을 보여줍니다.

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
        // 페이지 추가됨.
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
        // 테이블 1을 다음 페이지에 유지하고 싶습니다...
        paragraphs.add(table1);
        
        doc.save(_dataDir + "IsNewPageProperty_Test_out.pdf");
    }
}
```


{{% alert color="primary" %}}

com.aspose.pdf.[Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table) 클래스는 PDF 문서에서 테이블을 생성/렌더링할 수 있게 해줍니다. 유사한 기능은 aspose.pdf.[Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table) 클래스에서도 지원되지만, 저희는 고객들이 com.aspose.pdf 패키지의 최신 문서 객체 모델(DOM)을 사용해 보시기를 권장합니다. 왜냐하면 모든 새로운 기능과 문제 해결이 새로운 DOM에서 수행되고 있기 때문입니다. 그러나 레거시 Aspose.PDF for Java(aspose.pdf 패키지)에는 단락 클래스에서 [isInNewPage(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#isInNewPage--) 메서드를 통해 단락이 새 페이지에 렌더링되도록 하는 메서드가 있습니다. 하위 호환성을 위해 [isInNewPage(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#isInNewPage--) 메서드가 [BaseParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph) 클래스에 추가되었습니다.

{{% /alert %}}