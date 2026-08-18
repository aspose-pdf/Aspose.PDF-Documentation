---
title: العمل مع الجداول في ملفات PDF ذات العلامات في Java
linktitle: العمل مع الجدول في ملفات PDF ذات العلامات
type: docs
weight: 40
url: /java/working-with-table-in-tagged-pdfs/
description: تعرف على كيفية العمل مع الجداول التي يمكن الوصول إليها في ملفات PDF ذات العلامات في Java باستخدام Aspose.PDF، بما في ذلك بنية الجدول، وامتدادات الخلايا، والتصميم، وإعدادات الصف، وتحديد الموضع.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
تتيح لك واجهات برمجة تطبيقات الجدول ذات العلامات إنشاء هياكل جدول يمكن الوصول إليها باستخدام رؤوس واضحة وصفوف نصية وتذييلات ودلالات لكل خلية.

## إنشاء جدول ذو علامات

استخدم هذا المثال عندما تحتاج إلى جدول أساسي يمكن الوصول إليه يحتوي على بيانات تعريف ملخصة للرأس والنص والتذييل والجدول.

1. أنشئ ملف PDF [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) بعلامة جديدة وأضف [TableElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/tableelement/).
1. قم بتكوين حدود الجدول واملأ المحتوى باستخدام أسلوب المساعد المشترك.
1. قم بتعيين سمة ملخص الجدول واحفظ المستند.

```java
public static void createTable(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Example table");
        taggedContent.setLanguage("en-US");

        TableElement tableElement = taggedContent.createTableElement();
        taggedContent.getRootElement().appendChild(tableElement, true);
        tableElement.setBorder(new BorderInfo(BorderSide.All, 1.2f, Color.getDarkBlue()));

        fillTable(tableElement, 50, 4, true);

        StructureAttributes tableAttributes = tableElement.getAttributes().getAttributes(AttributeOwnerStandard.Table);
        StructureAttribute summaryAttribute = new StructureAttribute(AttributeKey.Summary);
        summaryAttribute.setStringValue("The summary text for table");
        tableAttributes.setAttribute(summaryAttribute);

        document.save(outputFile.toString());
    }
}
```

## تصميم جدول ذو علامات

يطبق هذا المثال التنسيق على مستوى الجدول مثل الألوان والحدود وحجم الأعمدة والصفوف المتكررة والمحاذاة.

1. قم بإنشاء ملف PDF [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) بعلامة جديدة وأضف عنصر جدول.
1. قم بتكوين الإعدادات المرئية والتخطيطية على مستوى الجدول.
1. املأ الجدول واحفظ المستند.

```java
public static void styleTable(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Example table style");
        taggedContent.setLanguage("en-US");

        TableElement tableElement = taggedContent.createTableElement();
        taggedContent.getRootElement().appendChild(tableElement, true);

        tableElement.setBackgroundColor(Color.getBeige());
        tableElement.setBorder(new BorderInfo(BorderSide.All, 0.80f, Color.getGray()));
        tableElement.setAlignment(HorizontalAlignment.Center);
        tableElement.setBroken(TableBroken.Vertical);
        tableElement.setColumnAdjustment(ColumnAdjustment.AutoFitToWindow);
        tableElement.setColumnWidths("80 80 80 80 80");
        tableElement.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.50f, Color.getDarkBlue()));
        tableElement.setDefaultCellPadding(new MarginInfo(16.0, 2.0, 8.0, 2.0));
        tableElement.getDefaultCellTextState().setForegroundColor(Color.getDarkCyan());
        tableElement.getDefaultCellTextState().setFontSize(8.0f);
        tableElement.setDefaultColumnWidth("70");
        tableElement.setBordersIncluded(true);
        tableElement.setLeft(0.0f);
        tableElement.setTop(40.0f);
        tableElement.setRepeatingColumnsCount(2);
        tableElement.setRepeatingRowsCount(3);

        TextState rowStyle = new TextState();
        rowStyle.setBackgroundColor(Color.getLightCoral());
        tableElement.setRepeatingRowsStyle(rowStyle);

        fillTable(tableElement, 10, 5, false);
        document.save(outputFile.toString());
    }
}
```

## نمط صفوف الجدول الموسومة

استخدم هذا المثال عندما يجب أن يكون لكل صف بيانات التعريف والحدود وإعدادات الارتفاع والإعدادات الافتراضية للخلية الخاصة به.

1. أنشئ ملف PDF [مستند] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) بعلامة جديدة وأضف أقسام الجدول للرأس والجسم والقدم.
1. قم بإنشاء صفوف وتكوين إعدادات مستوى الصف الخاصة بها مثل الحدود والمساحة والارتفاع وسلوك الصفحة.
1. املأ الصفوف بالخلايا واحفظ المستند.

```java
public static void styleTableRow(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Example table style");
        taggedContent.setLanguage("en-US");

        TableElement tableElement = taggedContent.createTableElement();
        taggedContent.getRootElement().appendChild(tableElement, true);
        TableTHeadElement tableTHeadElement = tableElement.createTHead();
        TableTBodyElement tableTBodyElement = tableElement.createTBody();
        TableTFootElement tableTFootElement = tableElement.createTFoot();

        TableTRElement headTrElement = tableTHeadElement.createTR();
        headTrElement.setAlternativeText("Head Row");
        for (int colIndex = 0; colIndex < 3; colIndex++) {
            headTrElement.createTH().setText("Head " + colIndex);
        }

        for (int rowIndex = 0; rowIndex < 7; rowIndex++) {
            TableTRElement trElement = tableTBodyElement.createTR();
            trElement.setAlternativeText("Row " + rowIndex);
            trElement.setBackgroundColor(Color.getLightGoldenrodYellow());
            trElement.setBorder(new BorderInfo(BorderSide.All, 0.75f, Color.getDarkGray()));
            trElement.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.50f, Color.getBlue()));
            trElement.setMinRowHeight(100.0);
            trElement.setFixedRowHeight(120.0);
            trElement.setInNewPage(rowIndex % 3 == 1);
            trElement.setRowBroken(true);

            TextState cellTextState = new TextState();
            cellTextState.setForegroundColor(Color.getRed());
            trElement.setDefaultCellTextState(cellTextState);
            trElement.setDefaultCellPadding(new MarginInfo(16.0, 2.0, 8.0, 2.0));
            trElement.setVerticalAlignment(VerticalAlignment.Bottom);

            for (int colIndex = 0; colIndex < 3; colIndex++) {
                trElement.createTD().setText("Cell [" + rowIndex + ", " + colIndex + "]");
            }
        }

        TableTRElement footTrElement = tableTFootElement.createTR();
        footTrElement.setAlternativeText("Foot Row");
        for (int colIndex = 0; colIndex < 3; colIndex++) {
            footTrElement.createTD().setText("Foot " + colIndex);
        }

        document.save(outputFile.toString());
    }
}
```

## نمط خلايا الجدول ذات العلامات

يستخدم هذا المثال أسلوب المساعد المشترك لإنشاء جدول بتنسيق على مستوى الخلية وخلايا مدمجة.

1. قم بإنشاء ملف PDF [مستند] جديد بعلامات تمييز (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإضافة عنصر جدول وقم بتعبئته من خلال الأسلوب المساعد مع تمكين تصميم الخلية.
1. احفظ المستند.

```java
public static void styleTableCell(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Example table cell style");
        taggedContent.setLanguage("en-US");

        TableElement tableElement = taggedContent.createTableElement();
        taggedContent.getRootElement().appendChild(tableElement, true);
        fillTable(tableElement, 4, 4, true);

        document.save(outputFile.toString());
    }
}
```

## ضبط موضع الجدول الموسوم

استخدم هذا المثال عندما يجب وضع جدول ذو علامات بشكل واضح على الصفحة.

1. قم بإنشاء ملف PDF [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) بعلامة جديدة وأضف عنصر جدول.
1. قم بتكوين [PositionSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure/positionsettings/) للجدول.
1. قم بتطبيق إعدادات الموضع، واملأ الجدول، واحفظ المستند.

```java
public static void adjustTablePosition(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Example table position");
        taggedContent.setLanguage("en-US");

        TableElement tableElement = taggedContent.createTableElement();
        taggedContent.getRootElement().appendChild(tableElement, true);

        PositionSettings positionSettings = new PositionSettings();
        positionSettings.setHorizontalAlignment(HorizontalAlignment.None);
        positionSettings.setMargin(new MarginInfo(20, 0, 0, 0));
        positionSettings.setVerticalAlignment(VerticalAlignment.None);
        positionSettings.setFirstParagraphInColumn(false);
        positionSettings.setKeptWithNext(false);
        positionSettings.setInNewPage(false);
        positionSettings.setInLineParagraph(false);
        tableElement.adjustPosition(positionSettings);

        fillTable(tableElement, 4, 4, true);
        document.save(outputFile.toString());
    }
}
```

## املأ الجدول ذو العلامات بمحتوى منظم

يقوم هذا الأسلوب المساعد بإنشاء صفوف الرأس والنص والتذييل للجدول، ويطبق تصميم الخلايا والامتدادات بشكل اختياري.

1. قم بإنشاء أقسام رأس الجدول ونصه وقدمه.
1. قم بملء صفوف الرأس والنص والتذييل بعناصر الخلية التي يمكن الوصول إليها.
1. يمكنك اختياريًا تكوين الخلايا المصممة والخلايا المدمجة وقيم حالة النص.

```java
private static void fillTable(TableElement tableElement, int rowCount, int colCount, boolean styleCells) {
    TableTHeadElement tableTHeadElement = tableElement.createTHead();
    TableTBodyElement tableTBodyElement = tableElement.createTBody();
    TableTFootElement tableTFootElement = tableElement.createTFoot();

    TableTRElement headTrElement = tableTHeadElement.createTR();
    headTrElement.setAlternativeText("Head Row");
    headTrElement.setBackgroundColor(Color.getLightGray());

    for (int columnIndex = 0; columnIndex < colCount; columnIndex++) {
        TableTHElement thElement = headTrElement.createTH();
        thElement.setText("Head " + columnIndex);
        thElement.setBackgroundColor(Color.getGreenYellow());
        thElement.setBorder(new BorderInfo(BorderSide.All, 4.0f, Color.getGray()));
        thElement.setNoBorder(true);
        thElement.setMargin(new MarginInfo(16.0, 2.0, 8.0, 2.0));
        thElement.setAlignment(HorizontalAlignment.Right);
    }

    for (int rowIndex = 0; rowIndex < rowCount; rowIndex++) {
        TableTRElement trElement = tableTBodyElement.createTR();
        trElement.setAlternativeText("Row " + rowIndex);

        for (int columnIndex = 0; columnIndex < colCount; columnIndex++) {
            int colSpan = 1;
            int rowSpan = 1;

            if (styleCells && columnIndex == 1 && rowIndex == 1) {
                colSpan = 2;
                rowSpan = 2;
            } else if (styleCells && ((rowIndex == 1 && columnIndex == 2)
                    || (rowIndex == 2 && (columnIndex == 1 || columnIndex == 2)))) {
                continue;
            }

            TableTDElement tdElement = trElement.createTD();
            tdElement.setText("Cell [" + rowIndex + ", " + columnIndex + "]");
            tdElement.setBackgroundColor(Color.getYellow());
            tdElement.setBorder(new BorderInfo(BorderSide.All, 4.0f, Color.getGray()));
            tdElement.setNoBorder(false);
            tdElement.setMargin(new MarginInfo(8.0, 2.0, 8.0, 2.0));
            tdElement.setAlignment(HorizontalAlignment.Center);

            TextState cellTextState = new TextState();
            cellTextState.setForegroundColor(Color.getDarkBlue());
            cellTextState.setFontSize(7.5f);
            cellTextState.setFontStyle(FontStyles.Bold);
            cellTextState.setFont(FontRepository.findFont("Arial"));
            tdElement.setDefaultCellTextState(cellTextState);

            tdElement.setWordWrapped(true);
            tdElement.setVerticalAlignment(VerticalAlignment.Center);
            tdElement.setColSpan(colSpan);
            tdElement.setRowSpan(rowSpan);
        }
    }

    TableTRElement footTrElement = tableTFootElement.createTR();
    footTrElement.setAlternativeText("Foot Row");
    footTrElement.setBackgroundColor(Color.getLightSeaGreen());

    for (int columnIndex = 0; columnIndex < colCount; columnIndex++) {
        TableTDElement tdElement = footTrElement.createTD();
        tdElement.setText("Foot " + columnIndex);
        tdElement.setAlignment(HorizontalAlignment.Center);
        tdElement.getStructureTextState().setFontSize(com.aspose.pdf.Nullable.of(7.0f));
        tdElement.getStructureTextState().setFontStyle(com.aspose.pdf.Nullable.of(FontStyles.Bold));
    }
}
```
