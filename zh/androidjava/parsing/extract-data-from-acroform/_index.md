---
title:  从 AcroForm 提取数据
linktitle:  从 AcroForm 提取数据
type: docs
weight: 50
url: /zh/androidjava/extract-data-from-acroform/
description: AcroForms 在许多 PDF 文档中存在。本文旨在帮助您了解如何使用 Aspose.PDF 从 AcroForms 提取数据。
lastmod: "2026-07-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 从 PDF 文档中提取表单字段

Aspose.PDF for Android via Java 不仅可以让您创建和填写表单字段，还能轻松从 PDF 文件中提取表单字段数据或表单字段信息。

假设我们事先不知道表单字段的名称。那么我们应该遍历 PDF 中的每一页，以提取 PDF 中所有 AcroForm 的信息以及表单字段的值。要访问表单，我们需要使用 [getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) 方法。

```java
 public void extractFormFields () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Get values from all fields
        StringBuilder sb=new StringBuilder();
        for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
            sb.append("Field Name: ");
            sb.append(formField.getPartialName());
            sb.append(" Value: ");
            sb.append(formField.getValue());
            sb.append('\n');
        }
        resultMessage.setText(sb);
    }
```

如果您确实知道想要提取其值的表单字段的名称，那么您可以使用 Documents.Form 集合中的索引器来快速检索这些数据。

## 通过标题检索表单字段值

表单字段的 Value 属性允许您获取特定字段的值。要获取该值，请从 [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象的 [表单字段集合](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--). 本示例选择一个 [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) 并使用 [getValue](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) 方法。

```java

    public void extractFormDataByName () {
        // Open document
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

Form 类允许您使用 ExportXml 方法将 PDF 文件中的数据导出到 XML 文件。为了将数据导出为 XML，您需要创建 Form 类的对象，然后使用 FileStream 对象调用 ExportXml 方法。最后，您可以关闭 FileStream 对象并释放 Form 对象。下面的代码片段展示了如何将数据导出到 XML 文件。

```java
public void extractFormFieldsToXML () {
        // Open document
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
            // Create xml file.
            FileOutputStream xmlOutputStream;
            xmlOutputStream=new FileOutputStream(file.toString());
            // Export data
            form.exportXml(xmlOutputStream);

            // Close file stream
            xmlOutputStream.close();
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Close the document
        form.dispose();
    }
```

## 从 PDF 文件导出数据到 FDF

要将 PDF 表单数据导出为 XFDF 文件，我们可以使用 [exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-) 方法位于 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) 类。

请注意，它是来自 `com.aspose.pdf.facades`. 尽管名称相似，这个类的用途略有不同。

为了将数据导出到 FDF，您需要创建一个对象 `Form` 类，然后调用 `exportXfdf` 使用该方法 `OutputStream` 对象。以下代码片段向您展示如何将数据导出为 XFDF 文件。

```java
public void extractFormExportFDF () {
        // Open document
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

            // Export data
            form.exportFdf(fdfOutputStream);

            // Close file stream
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## 从 PDF 文件导出 XFDF 数据

要将 PDF 表单数据导出为 XFDF 文件，我们可以使用 [exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-) 方法位于 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) 类。

为了将数据导出为XFDF，您需要创建一个对象 `Form` 类，然后调用 `exportXfdf` 使用该方法 `OutputStream` 对象。 
以下代码片段向您展示如何将数据导出到 XFDF 文件。

```java
    public void extractFormExportXFDF () {
        // Open document
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

            // Export data
            form.exportXfdf(fdfOutputStream);

            // Close file stream
            fdfOutputStream.close();

        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

