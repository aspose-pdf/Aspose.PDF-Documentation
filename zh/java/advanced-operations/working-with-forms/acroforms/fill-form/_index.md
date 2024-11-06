---
title: 填写 AcroForms
linktitle: 填写 AcroForms
type: docs
weight: 20
url: zh/java/fill-form/
description: 本节说明如何使用 Aspose.PDF for Java 在 PDF 文档中填写表单字段。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF 文档非常出色，并且确实是创建表单的首选文件类型。

Aspose.PDF for Java 允许您填写表单字段，从 Document 对象的 Form 集合中获取字段。

让我们看看下面的例子如何解决这个任务：

```java
public class ExamplesFillForm {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void FillFormFieldPDFDocument() {
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

    
}
```