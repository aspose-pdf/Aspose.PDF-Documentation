---
title: 修改 AcroForms
linktitle: 修改 AcroForms
type: docs
weight: 40
url: /zh/java/modifing-form/
description: 本节解释如何使用 Aspose.PDF for Java 修改 PDF 文档中的表单。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 设置自定义表单字段字体

Adobe PDF 文件中的表单字段可以配置为使用特定的默认字体。Aspose.PDF 允许开发人员将任何字体应用为字段默认字体，无论是 14 种核心字体之一还是自定义字体。
要设置和更新用于表单字段的默认字体，Aspose.PDF 提供了 DefaultAppearance (Font font, double size, Color color) 类。可以使用 com.aspose.pdf.DefaultAppearance 访问此类。要使用此对象，请使用 Field 类的 setDefaultAppearance(..) 方法。

以下代码片段向您展示如何为 PDF 表单字段设置默认字体。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.DefaultAppearance;
import com.aspose.pdf.Document;
import com.aspose.pdf.Field;
import com.aspose.pdf.Font;
import com.aspose.pdf.FontRepository;
import com.aspose.pdf.Rectangle;
import com.aspose.pdf.TextBoxField;

public class ExamplesModifying {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void SetFormFieldFontOtherThan14CorePDFFonts() {
        // 打开文档
        Document pdfDocument = new Document(_dataDir + "FormFieldFont14.pdf");
        // 从文档中获取特定的表单字段
        Field field = (Field) pdfDocument.getForm().get("textbox1");

        // 创建字体对象
        Font font = FontRepository.findFont("ComicSansMS");

        // 为表单字段设置字体信息
        field.setDefaultAppearance (new DefaultAppearance(font, 10, java.awt.Color.BLACK));
        
        // 保存更新的文档
        pdfDocument.save(_dataDir + "FormFieldFont14_out.pdf");
    }
```


## 获取/设置 FieldLimit

FormEditor 类的 SetFieldLimit 方法允许您设置字段限制，即可以输入到字段中的最大字符数。

```java
    public static void GettingMaximumFieldLimit()
    {
        // 使用 DOM 获取最大字段限制
        Document doc = new Document(_dataDir + "FieldLimit.pdf");
        TextBoxField field = (TextBoxField)doc.getForm().get("textbox1");
        System.out.println("限制: " +field.getMaxLen());
    }
```

您还可以使用以下代码片段，通过 Aspose.PDF.Facades 命名空间获取相同的值。

```java
    public static void GettingMaximumFieldLimitFacades()
    {
        // 使用 Facades 获取最大字段限制
        com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form();
        form.bindPdf(_dataDir + "FieldLimit.pdf");
        System.out.println("限制: " + form.getFieldLimit("textbox1"));
    }
```

同样，Aspose.PDF 还有一个使用 DOM 方法获取字段限制的方法。
 以下代码片段展示了步骤。

```java
    public static void SettingMaximumFieldLimit()
    {
        // 使用DOM获取最大字段限制
        Document doc = new Document(_dataDir + "FieldLimit.pdf");
        TextBoxField field = (TextBoxField)doc.getForm().get("textbox1");
        field.setMaxLen(10);
        System.out.println("Limit: " +field.getMaxLen());       
    }
```

## 从PDF文档中删除特定的表单字段

所有的表单字段都包含在[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)对象的Form集合中。该集合提供了管理表单字段的不同方法，包括删除方法。如果你想删除一个特定的字段，将字段名称作为参数传递给删除方法，然后保存更新的PDF文档。

以下代码片段展示了如何从PDF文档中删除一个命名字段。

```java
    public static void DeleteParticularFormField()
    {    
        // 打开文档
        Document pdfDocument = new Document("input.pdf");

        // 按名称删除命名字段
        pdfDocument.getForm().delete("textbox1");

        // 保存修改后的PDF
        pdfDocument.save("output.pdf");
    }
```

## 修改 PDF 文档中的表单字段

[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象的 Form 集合允许您管理 PDF 文档中的表单字段。

要修改表单字段，请从 Form 集合中获取字段并设置其属性。然后保存更新后的 PDF 文档。

以下代码片段显示了如何修改 PDF 文档中现有的表单字段。

```java
    public static void ModifyFormField()
    {
        Document pdfDocument = new Document("input.pdf");
        // 获取一个字段
        TextBoxField textBoxField = (TextBoxField) pdfDocument.getForm().get("textbox1");

        // 修改字段值
        textBoxField.setValue("Updated Value");

        // 将字段设置为只读
        textBoxField.setReadOnly(true);

        // 保存更新后的文档
        pdfDocument.save("output.pdf");
    }
```

### 将表单字段移动到 PDF 文件中的新位置

如果您想将表单字段移动到 PDF 页面上的新位置，请首先获取字段对象，然后为其 setRect 方法指定一个新值。
 A [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) 对象与新坐标一起分配给 setRect(..) 方法。然后使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象的 save 方法保存更新后的 PDF。

以下代码片段向您展示如何将表单字段移动到新位置。

```java
    public static void ModifyMoveFormFieldNewLocation()
    {    
        // 打开文档
        Document pdfDocument = new Document(_dataDir+"input.pdf");
        // 获取一个字段
        TextBoxField textBoxField = (TextBoxField) pdfDocument.getForm().get("textbox1");

        // 修改字段位置
        textBoxField.setRect(new Rectangle(300, 400, 600, 500));

        // 保存修改后的文档
        pdfDocument.save("output.pdf");
    }
}
```