---
title: 提取数据 AcroForms
linktitle: 提取数据 AcroForms
type: docs
weight: 30
url: zh/java/extract-form/
description: 本节解释如何使用 Aspose.PDF for Java 从 PDF 文档中提取表单。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 从 PDF 文档中的单个字段获取值

表单字段的[getValue() 方法](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--)允许您获取特定字段的值。

要获取该值，请从[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)对象的 Form 集合中获取表单字段。

此示例选择一个[TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField)并使用[getValue() 方法](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--)检索其值。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Document;
import com.aspose.pdf.Field;
import com.aspose.pdf.TextBoxField;

public class ExamplesExtractFormData {
    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void GetValueFromIndividualFieldPDFDocument() {
        // 打开文档
        Document pdfDocument = new Document(_dataDir+"GetValueFromField.pdf");

        // 获取字段
        TextBoxField textBoxField = (TextBoxField) pdfDocument.getForm().get("textbox1");

        // 获取字段名称
        System.out.printf("PartialName :-" + textBoxField.getPartialName());

        // 获取字段值
        System.out.printf("Value :-" + textBoxField.getValue());
    }
```


## 从 PDF 文档中获取所有字段的值

要从 PDF 文档中获取所有字段的值，您需要遍历所有表单字段，然后使用[getValue() 方法](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--)获取值。使用[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)对象的[getForm() 方法](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--)从 Form 集合中获取每个字段，并使用 getFields() 将表单字段的列表存入 Field 数组中，然后遍历数组以获取字段的值。

以下代码片段演示如何获取 PDF 文档中所有字段的值。

```java
    public static void GetValuesFromAllFieldsPDFDocument() {
        // 打开文档
        Document document = new Document(_dataDir + "GetValuesFromAllFields.pdf");

        Field[] fields = document.getForm().getFields();
        for (int i = 0; i < fields.length; i++) {

            System.out.println("表单字段: " + fields[i].getFullName());
            System.out.println("表单字段: " + fields[i].getValue());
        }

    }
}
```


## 从 PDF 文件的特定区域获取表单字段

在某些情况下，需要获取的数据并不是来自整个表单，而是例如只来自打印页的左上四分之一区域。使用 Aspose.PDF for Java，这不是问题。您可以指定一个区域来过滤掉给定 PDF 文件区域之外的字段。要从 PDF 文件的特定区域获取表单字段：

1. 使用 Document 对象打开 PDF 文件。
1. 从文档的 Forms 集合中获取表单。
1. 指定矩形区域并将其传递给 Form 对象的 [getFieldsInRect](https://reference.aspose.com/pdf/java/com.aspose.pdf/Form#getFieldsInRect-com.aspose.pdf.Rectangle-) 方法。返回一个 [Fields](https://reference.aspose.com/pdf/java/com.aspose.pdf/Field) 集合。
1. 使用此集合来操作字段。

以下代码片段显示了如何在 PDF 文件的特定矩形区域中获取表单字段。

```java
public static void GetValuesFromSpecificRegion() {
    // 打开 pdf 文件
    Document doc = new Document(_dataDir + "GetFieldsFromRegion.pdf");

    // 创建矩形对象以获取该区域中的字段
    Rectangle rectangle = new Rectangle(35, 30, 500, 500);

    // 获取 PDF 表单
    com.aspose.pdf.Form form = doc.getForm();

    // 获取矩形区域中的字段
    Field[] fields = form.getFieldsInRect(rectangle);

    // 显示字段名称和值
    for (Field field : fields)
    {
        // 显示所有放置的图像放置属性
        System.out.println("Field Name: " + field.getFullName() + "-" + "Field Value: " + field.getValue());
    }
}
```