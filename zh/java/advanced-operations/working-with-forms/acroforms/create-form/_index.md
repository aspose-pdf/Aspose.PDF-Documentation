---
title: 创建 AcroForms - 在 Java 中创建可填写的 PDF
linktitle: 创建 AcroForms
type: docs
weight: 10
url: /zh/java/create-forms/
description: 本节解释如何在 PDF 文档中使用 Aspose.PDF for Java 从头创建 AcroForms。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 在 PDF 文档中添加表单字段

[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类提供了一个名为 Form 的集合，帮助管理 PDF 文档中的表单字段。

要添加一个表单字段：

1. 创建要添加的表单字段。
2. 调用 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/Form) 集合的添加方法。

此示例展示如何添加一个 TextBoxField。您可以使用相同的方法添加任何表单字段：

1. 首先，创建一个字段对象并设置其属性。
2. 然后，将字段添加到 Form 集合中。

### 添加 TextBoxField

文本字段是一个允许接收者在表单中输入文本的表单元素。
 这会在您希望允许用户自由输入他们想要的内容时使用。

以下代码片段展示了如何向 PDF 文档中添加一个 TextBoxField。

```java
public class ExamplesCreateForm {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void AddingTextBoxField() {

        // 打开文档
        Document pdfDocument = new Document(_dataDir + "TextField.pdf");
        Page page = pdfDocument.getPages().get_Item(1);
        // 创建一个字段
        TextBoxField textBoxField = new TextBoxField(page, new Rectangle(100, 200, 300, 300));
        textBoxField.setPartialName("textbox1");
        textBoxField.setValue("Text Box");

        // TextBoxField.Border = new Border(
        Border border = new Border(textBoxField);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        textBoxField.setBorder(border);

        textBoxField.setColor(Color.getGreen());

        // 将字段添加到文档中
        pdfDocument.getForm().add(textBoxField, 1);

        // 保存修改后的 PDF
        pdfDocument.save(_dataDir + "TextBox_out.pdf");

    }
```

## 添加 RadioButtonField

单选按钮通常用于选择题的场景，其中只能选择一个答案。

以下代码片段展示了如何在 PDF 文档中添加 [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField)。

```java
public static void AddingRadioButton() {
        Document pdfDocument = new Document();
        // 添加页面到 PDF 文件
        pdfDocument.getPages().add();

        // 创建 RadioButtonField 对象，并传递页码作为参数
        RadioButtonField radio = new RadioButtonField(pdfDocument.getPages().get_Item(1));

        // 添加第一个单选按钮选项，并使用 Rectangle 对象指定其起始位置
        radio.addOption("Test", new Rectangle(20, 720, 40, 740));
        // 添加第二个单选按钮选项
        radio.addOption("Test1", new Rectangle(120, 720, 140, 740));
        // 将单选按钮添加到 Document 对象的表单对象中
        pdfDocument.getForm().add(radio);
        // 保存 PDF 文件
        pdfDocument.save("RadioButtonSample.pdf");

    }
```


以下代码片段显示了添加具有三个选项的[RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField)并将其放置在表格单元格中的步骤。

```java
public static void AddingRadioButtonAdvanced() {
        Document doc = new Document();
        Page page = doc.getPages().add();
        Table table = new Table();
        table.setColumnWidths("120 120 120");
        page.getParagraphs().add(table);
        Row r1 = table.getRows().add();
        Cell c1 = r1.getCells().add();
        Cell c2 = r1.getCells().add();
        Cell c3 = r1.getCells().add();

        RadioButtonField rf = new RadioButtonField(page);
        rf.setPartialName("radio");
        doc.getForm().add(rf, 1);

        RadioButtonOptionField opt1 = new RadioButtonOptionField();
        RadioButtonOptionField opt2 = new RadioButtonOptionField();
        RadioButtonOptionField opt3 = new RadioButtonOptionField();

        opt1.setOptionName("Item1");
        opt2.setOptionName("Item2");
        opt3.setOptionName("Item3");

        opt1.setWidth(15);
        opt1.setHeight(15);
        opt2.setWidth(15);
        opt2.setHeight(15);
        opt3.setWidth(15);
        opt3.setHeight(15);

        rf.add(opt1);
        rf.add(opt2);
        rf.add(opt3);

        opt1.setBorder(new Border(opt1));
        opt1.getBorder().setWidth(1);
        opt1.getBorder().setStyle(BorderStyle.Solid);
        opt1.getCharacteristics().setBorder(Color.getBlack());
        opt1.getDefaultAppearance().setTextColor(java.awt.Color.RED);
        opt1.setCaption(new TextFragment("Item1"));
        opt2.setBorder(new Border(opt2));
        opt2.getBorder().setWidth(1);
        opt2.getBorder().setStyle(BorderStyle.Solid);
        opt2.getCharacteristics().setBorder(java.awt.Color.BLACK);
        opt2.getDefaultAppearance().setTextColor(java.awt.Color.RED);
        opt2.setCaption(new TextFragment("Item2"));
        opt3.setBorder(new Border(opt3));
        opt3.getBorder().setWidth(1);
        opt3.getBorder().setStyle(BorderStyle.Solid);
        opt3.getCharacteristics().setBorder(java.awt.Color.BLACK);
        opt3.getDefaultAppearance().setTextColor(java.awt.Color.RED);
        opt3.setCaption(new TextFragment("Item3"));
        c1.getParagraphs().add(opt1);
        c2.getParagraphs().add(opt2);
        c3.getParagraphs().add(opt3);

        doc.save("RadioButtonField.pdf");
    }
```


## 为 RadioButtonField 添加标题

以下代码片段展示了如何添加将与 [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField) 关联的标题：

```java
public static void AddingCaptionToRadioButtonField() {
        // 加载源 PDF 表单
        com.aspose.pdf.facades.Form form1 = new com.aspose.pdf.facades.Form(_dataDir + "RadioButtonField.pdf");
        Document document = new Document(_dataDir + "RadioButtonField.pdf");
        for (String item : form1.getFieldNames()) {
            System.out.println(item.toString());
            if (item.contains("radio1")) {
                RadioButtonField field0 = (RadioButtonField) document.getForm().get(item);
                RadioButtonOptionField fieldoption = new RadioButtonOptionField();
                fieldoption.setOptionName("Yes");
                fieldoption.setPartialName("Yesname");

                var updatedFragment = new TextFragment("test123");
                updatedFragment.getTextState().setFont(FontRepository.findFont("Arial"));
                updatedFragment.getTextState().setFontSize(10);
                updatedFragment.getTextState().setLineSpacing(6.32f);

                // 创建 TextParagraph 对象
                TextParagraph par = new TextParagraph();

                // 设置段落位置
                par.setPosition(new Position(field0.getRect().getLLX(),
                        field0.getRect().getLLY() + updatedFragment.getTextState().getFontSize()));
                // 指定换行模式
                par.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);

                // 将新的 TextFragment 添加到段落
                par.appendLine(updatedFragment);

                // 使用 TextBuilder 添加 TextParagraph
                TextBuilder textBuilder = new TextBuilder(document.getPages().get_Item(1));
                textBuilder.appendParagraph(par);

                field0.deleteOption("item1");
            }
        }
        document.save(_dataDir + "RadioButtonField_out.pdf");

    }
```


## 添加 ComboBox 字段

组合框是一个表单字段，可以在您的文档中添加下拉菜单。

以下代码片段展示了如何在 PDF 文档中添加 [ComboBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/ComboBoxField) 字段。

```java
public static void AddingComboboxField() {
        // 创建 Document 对象
        Document doc = new Document();
        // 向文档对象添加页面
        doc.getPages().add();
        // 实例化 ComboBox 字段对象
        ComboBoxField combo = new ComboBoxField(doc.getPages().get_Item(1), new Rectangle(100, 600, 150, 616));
        // 向 ComboBox 添加选项
        combo.addOption("Red");
        combo.addOption("Yellow");
        combo.addOption("Green");
        combo.addOption("Blue");
        // 将组合框对象添加到文档对象的表单字段集合中
        doc.getForm().add(combo);
        // 保存 PDF 文档
        doc.save("ComboBox_Added.pdf");
    }
```

## 为表单添加工具提示

Document 类提供了一个名为 Form 的集合，用于管理 PDF 文档中的表单字段。
 要为表单字段添加工具提示，请使用字段类的备用名称。Adobe Acrobat 使用“备用名称”作为字段工具提示。

以下代码片段展示了如何使用 Java 为表单字段添加工具提示。

```java
public static void AddTooltipToFormField() {
        // 加载源 PDF 表单
        Document doc = new Document(_dataDir + "AddTooltipToField.pdf");

        // 获取一个字段
        TextBoxField textBoxField = (TextBoxField) doc.getForm().get("textbox1");

        // 为文本框设置工具提示
        textBoxField.setAlternateName("文本框工具提示");

        // 保存修改后的文档
        doc.save("output.pdf");
    }
```