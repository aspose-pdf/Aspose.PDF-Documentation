---
title: 从AcroForm提取数据
linktitle: 从AcroForm提取数据
type: docs
weight: 50
url: /androidjava/extract-data-from-acroform/
description: AcroForms存在于许多PDF文档中。本文旨在帮助您了解如何使用Aspose.PDF从AcroForms中提取数据。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 从PDF文档中提取表单字段

Aspose.PDF for Android via Java不仅允许您创建和填写表单字段，还使得从PDF文件中提取表单字段数据或表单字段信息变得容易。

假设我们事先不知道表单字段的名称。然后我们应该遍历PDF中的每一页，以提取关于PDF中所有AcroForms的信息以及表单字段的值。要访问表单，我们需要使用[getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--)方法。

```java
public void extractFormFields () {
    // 打开文档
    try {
        document=new Document(inputStream);
    } catch (Exception e) {
        resultMessage.setText(e.getMessage());
        return;
    }
    // 从所有字段中获取值
    StringBuilder sb=new StringBuilder();
    for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
        sb.append("字段名称: ");
        sb.append(formField.getPartialName());
        sb.append(" 值: ");
        sb.append(formField.getValue());
        sb.append('\n');
    }
    resultMessage.setText(sb);
}
```


如果您知道要提取值的表单字段的名称，那么可以使用 Documents.Form 集合中的索引器来快速检索此数据。

## 按标题检索表单字段值

表单字段的 Value 属性允许您获取特定字段的值。要获取值，请从 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象的 [form field collection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) 获取表单字段。此示例选择一个 [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) 并使用 [getValue](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) 方法检索其值。

```java

    public void extractFormDataByName () {
        // 打开文档
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        com.aspose.pdf.TextBoxField textBoxField1
                =(com.aspose.pdf.TextBoxField) document.getForm().get("Last Name");

        resultMessage.setText("Last Name: " + textBoxField1.getValue());

    }
```


## 从 PDF 文件提取数据到 XML

Form 类允许您使用 ExportXml 方法将数据从 PDF 文件导出到 XML 文件。为了将数据导出到 XML，您需要创建一个 Form 类的对象，然后使用 FileStream 对象调用 ExportXml 方法。最后，您可以关闭 FileStream 对象并释放 Form 对象。以下代码片段向您展示如何将数据导出到 XML 文件。

```java
public void extractFormFieldsToXML () {
        // 打开文档
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        com.aspose.pdf.facades.Form form=new com.aspose.pdf.facades.Form();
        form.bindPdf(document);
        File file=new File(fileStorage, "output.xml");
        try {
            // 创建 xml 文件。
            FileOutputStream xmlOutputStream;
            xmlOutputStream=new FileOutputStream(file.toString());
            // 导出数据
            form.exportXml(xmlOutputStream);

            // 关闭文件流
            xmlOutputStream.close();
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // 关闭文档
        form.dispose();
    }
```


## 导出数据到 PDF 文件的 FDF

要将 PDF 表单数据导出到 XFDF 文件，我们可以使用 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) 类中的 [exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-) 方法。

请注意，这是来自 `com.aspose.pdf.facades` 的一个类。尽管名称相似，但这个类的用途略有不同。

为了导出数据到 FDF，您需要创建一个 `Form` 类的对象，然后使用 `OutputStream` 对象调用 `exportXfdf` 方法。以下代码示例向您展示如何将数据导出到 XFDF 文件。

```java
public void extractFormExportFDF () {
        // 打开文档
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        File file=new File(fileStorage, "student.fdf");

        com.aspose.pdf.facades.Form form=new com.aspose.pdf.facades.Form(document);
        FileOutputStream fdfOutputStream;
        try {

            fdfOutputStream=new FileOutputStream(file.toString());

            // 导出数据
            form.exportFdf(fdfOutputStream);

            // 关闭文件流
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


## 将数据从 PDF 文件导出到 XFDF

要将 PDF 表单数据导出到 XFDF 文件，我们可以使用 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) 类中的 [exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-) 方法。

为了将数据导出到 XFDF，您需要创建一个 `Form` 类的对象，然后使用 `OutputStream` 对象调用 `exportXfdf` 方法。以下代码片段向您展示了如何将数据导出到 XFDF 文件。

```java
    public void extractFormExportXFDF () {
        // 打开文档
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        File file=new File(fileStorage, "student.xfdf");

        com.aspose.pdf.facades.Form form=new com.aspose.pdf.facades.Form(document);
        FileOutputStream fdfOutputStream;
        try {

            fdfOutputStream=new FileOutputStream(file.toString());

            // 导出数据
            form.exportXfdf(fdfOutputStream);

            // 关闭文件流
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```