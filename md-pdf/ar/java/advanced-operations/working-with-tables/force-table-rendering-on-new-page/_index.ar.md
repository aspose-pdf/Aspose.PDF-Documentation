---
title: فرض عرض الجدول في صفحة جديدة
type: docs
weight: 20
url: /java/force-table-rendering-on-new-page/
lastmod: "2021-06-05"
---

## عرض الجدول في صفحة جديدة

بشكل افتراضي، يتم إضافة الفقرات إلى مجموعة الفقرات في كائن الصفحة. ومع ذلك، من الممكن عرض جدول في صفحة جديدة بدلاً من عرضه مباشرة بعد كائن فقرة مضافة مسبقًا على الصفحة.

### إضافة جدول

لعرض الجدول في صفحة جديدة، استخدم الطريقة [IsInNewPage](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#isInNewPage--) في فئة [BaseParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/baseparagraph). يوضح مقطع الشيفرة التالي كيفية القيام بذلك.

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
        // تم إضافة الصفحة.
        Page curPage = doc.getPages().add();
        for (int i = 1; i <= 120; i++)
        {
            Row row = table.getRows().add();
            row.setFixedRowHeight (15);
            Cell cell1 = row.getCells().add();
            cell1.getParagraphs().add(new TextFragment("المحتوى 1"));
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
        // أريد الاحتفاظ بالجدول 1 في الصفحة التالية من فضلك...
        paragraphs.add(table1);
        
        doc.save(_dataDir + "IsNewPageProperty_Test_out.pdf");
    }
}
```


{{% alert color="primary" %}}

توفر الفئة com.aspose.pdf.[Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table) إمكانية إنشاء/عرض الجداول في مستندات PDF. يتم دعم ميزة مشابهة أيضًا بواسطة الفئة aspose.pdf.[Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table) ولكننا نشجع عملائنا على تجربة استخدام أحدث نموذج كائن المستند (DOM) من حزمة com.aspose.pdf، لأن جميع الميزات الجديدة وحل المشكلات يتم تنفيذها في DOM الجديد. ومع ذلك، يحتوي Aspose.PDF القديم لجافا (حزمة aspose.pdf) على طريقة [isInNewPage(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#isInNewPage--) في فئة الفقرة، بحيث يتم عرض الفقرة في صفحة جديدة. لضمان التوافق مع الإصدارات السابقة، تمت إضافة طريقة [isInNewPage(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#isInNewPage--) إلى فئة [BaseParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph).

{{% /alert %}}