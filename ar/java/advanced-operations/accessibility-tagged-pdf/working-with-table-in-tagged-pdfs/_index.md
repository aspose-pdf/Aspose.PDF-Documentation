---
title: العمل مع الجداول في ملفات PDF الموسومة في جافا
linktitle: العمل مع الجدول في ملفات PDF الموسومة
type: docs
weight: 40
url: /ar/java/working-with-table-in-tagged-pdfs/
description: تعلم كيفية العمل مع الجداول القابلة للوصول في ملفات PDF ذات العلامات بلغة Java باستخدام Aspose.PDF، بما في ذلك هيكل الجدول، امتدادات الخلايا، التنسيق، إعدادات الصفوف، وتحديد المواقع.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
تسمح لك Tagged table APIs بإنشاء هياكل جداول قابلة للوصول مع رؤوس صريحة، وصفوف جسم، وتذييلات، ومعاني لكل خلية.

## إنشاء جدول موسوم

استخدم هذا المثال عندما تحتاج إلى جدول أساسي يمكن الوصول إليه يتضمن رأسًا، وجسمًا، وتذييلًا، وبيانات ملخص الجدول الوصفية.

1. إنشاء ملف PDF معلم جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف a [TableElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.logicalstructure/tableelement/).
1. قم بتكوين حد الجدول وملء المحتوى باستخدام طريقة المساعد المشتركة.
1. قم بتعيين خاصية ملخص الجدول واحفظ المستند.

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

## تنسيق جدول معلم

يطبق هذا المثال تنسيقًا على مستوى الجدول مثل الألوان والحدود وتحديد حجم الأعمدة والصفوف المتكررة والمحاذاة.

1. إنشاء ملف PDF معلم جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف عنصر جدول.
1. قم بتكوين إعدادات العرض وتخطيط مستوى الجدول.
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

## تنسيق صفوف الجدول الموسومة

استخدم هذا المثال عندما يجب أن يحتوي كل صف على بياناته الوصفية الخاصة، والحدود، وإعدادات الارتفاع، والقيم الافتراضية للخلية.

1. إنشاء ملف PDF معلم جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف أقسام الجدول للرأس والجسم والتذييل.
1. إنشاء صفوف وتكوين إعدادات مستوى الصف مثل الحد، والهوامش، والارتفاع، وسلوك الصفحة.
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

## تنسيق خلايا الجدول الموسومة

يستخدم هذا المثال الطريقة المساعدة المشتركة لإنشاء جدول بتنسيق على مستوى الخلية وخلايا مدمجة.

1. إنشاء ملف PDF معلم جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. أضف عنصر جدول واملأه من خلال طريقة المساعدة مع تمكين تنسيق الخلايا.
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

استخدم هذا المثال عندما يجب وضع جدول معلم صراحةً على الصفحة.

1. إنشاء ملف PDF معلم جديد [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) وأضف عنصر جدول.
1. تكوين [PositionSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure/positionsettings/) للجدول.
1. قم بتطبيق إعدادات الموقع، واملأ الجدول، واحفظ المستند.

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

## امِل جدولًا موسومًا بمحتوى منظم

تنشئ هذه الدالة المساعدة صفوف العنوان والجسم والتذييل للجدول، وتطبق اختياريًا تنسيق الخلايا والامتدادات.

1. إنشاء أقسام رأس الجدول، والجسم، والقدم.
1. املأ صفوف الرأس، والجزء الرئيسي، وتذييل الصفوف بعناصر خلايا قابلة للوصول.
1. اختياريًا، قم بتكوين الخلايا ذات الأنماط، الخلايا المدمجة، وقيم حالة النص.

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
