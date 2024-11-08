---
title: 从AcroForm提取数据
linktitle: 从AcroForm提取数据
type: docs
weight: 50
url: /zh/java/extract-data-from-acroform/
description: AcroForms存在于许多PDF文档中。本文旨在帮助您了解如何使用Java和Aspose.PDF从AcroForms中提取数据。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 从PDF文档中提取表单字段

Aspose.PDF for Java不仅可以让您创建和填写表单字段，还可以轻松地从PDF文件中提取表单字段数据或表单字段信息。

假设我们事先不知道表单字段的名称。那么我们应该遍历PDF中的每一页，以提取PDF中所有AcroForms的信息以及表单字段的值。要访问表单，我们需要使用[getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--)方法。

```java
public static void ExtractFormFields() {
    String path= "/home/admin/pdf-examples/Samples/StudentInfoFormElectronic.pdf";
    com.aspose.pdf.Document document = new com.aspose.pdf.Document(path);
    // 从所有字段获取值
    for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
        System.out.println("Field Name :" + formField.getPartialName());
        System.out.println("Value : " + formField.getValue());
    }
}
```


如果您知道要提取值的表单字段的名称，则可以使用 Documents.Form 集合中的索引器快速检索此数据。

## 按标题检索表单字段值

表单字段的 Value 属性允许您获取特定字段的值。要获取该值，请从 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象的 [form field collection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) 获取表单字段。此示例选择一个 [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) 并使用 [getValue](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) 方法检索其值。

```java
public static void ExtractFormDataByName() {
    String fileName = _dataDir+"/StudentInfoFormElectronic.pdf";
    com.aspose.pdf.Document document = new com.aspose.pdf.Document(fileName);        
    com.aspose.pdf.TextBoxField textBoxField1 = (com.aspose.pdf.TextBoxField)document.getForm().get("Last Name");

    System.out.println("Last Name :" + textBoxField1.getValue());
}
```


## 从PDF文档提取表单字段到JSON

为了将表单数据导出为JSON，我们推荐使用像[Gson](https://github.com/google/gson)这样的第三方库。以下代码片段展示了如何将`Name`和`Value`导出为JSON：

```java
public static void ExtractFormFieldsToJson() {
    String path = "/home/admin/pdf-examples/Samples/StudentInfoFormElectronic.pdf";
    com.aspose.pdf.Document document = new com.aspose.pdf.Document(path);

    java.util.List<FormElement> formData = new java.util.ArrayList<FormElement>();
    for (com.aspose.pdf.Field formField : document.getForm().getFields()) {
        formData.add(new FormElement(formField.getPartialName(), formField.getValue()));
    }

    Gson gson = new Gson();
    String jsonString = gson.toJson(formData);
    System.out.println(jsonString);
}
```

在这个例子中，我们使用了一个额外的类

```java
public class FormElement {
    public FormElement(String partialName, String Value) {
        this.Name = partialName;
        this.Value = Value;
    }
    public String Name;
    public String Value;
}
```


## 从 PDF 文件提取数据到 XML

Form 类允许您使用 ExportXml 方法将数据导出到 XML 文件中。为了将数据导出到 XML，您需要创建一个 Form 类的对象，然后使用 FileStream 对象调用 ExportXml 方法。最后，您可以关闭 FileStream 对象并释放 Form 对象。以下代码片段向您展示如何将数据导出到 XML 文件。

```java
public static void ExtractFormFieldsToXML() {

    String dataDir = "/home/admin/pdf-examples/Samples/StudentInfoFormElectronic.pdf";

    // 打开文档
    com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form();
    form.bindPdf(dataDir + "input.pdf");

    try {
        // 创建 XML 文件。
        FileOutputStream xmlOutputStream;

        xmlOutputStream = new FileOutputStream(dataDir + "input.xml");
        // 导出数据
        form.exportXml(xmlOutputStream);

        // 关闭文件流
        xmlOutputStream.close();

    } catch (IOException e) {

        e.printStackTrace();
    }

    // 关闭文档
    form.dispose();
    ;
}
```


## 将数据从 PDF 文件导出到 FDF

要将 PDF 表单数据导出到 XFDF 文件，我们可以使用 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) 类中的 [exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-) 方法。

请注意，这是来自 `com.aspose.pdf.facades` 的一个类。尽管名称相似，这个类的用途略有不同。

为了将数据导出到 FDF，您需要创建一个 `Form` 类的对象，然后使用 `OutputStream` 对象调用 `exportXfdf` 方法。以下代码片段展示了如何将数据导出到 XFDF 文件。

```java
 public static void ExtractFormExportFDF() {
        String pdfFileName = Paths.get(_dataDir, "StudentInfoFormElectronic.pdf").toString();
        String fdfFileName = Paths.get(_dataDir, "student.fdf").toString();
        com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form(pdfFileName);

        OutputStream fdfOutputStream;
        try {

            fdfOutputStream = new FileOutputStream(fdfFileName);

            // 导出数据
            form.exportFdf(fdfOutputStream);

            // 关闭文件流
            fdfOutputStream.close();

        } catch (IOException e) {
            // TODO: 处理异常
            e.printStackTrace();
        }

    }
```


## 导出数据到 XFDF 从 PDF 文件

要将 PDF 表单数据导出到 XFDF 文件，我们可以使用 [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) 类中的 [exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-) 方法。

为了导出数据到 XFDF，您需要创建一个 `Form` 类的对象，然后使用 `OutputStream` 对象调用 `exportXfdf` 方法。 以下代码片段展示了如何将数据导出到 XFDF 文件。

```java
public static void ExtractFormExportXFDF() {
        String pdfFileName = Paths.get(_dataDir, "StudentInfoFormElectronic.pdf").toString();
        String fdfFileName = Paths.get(_dataDir, "student.xfdf").toString();
        com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form(pdfFileName);

        OutputStream fdfOutputStream;
        try {

            fdfOutputStream = new FileOutputStream(fdfFileName);

            // 导出数据
            form.exportXfdf(fdfOutputStream);

            // 关闭文件流
            fdfOutputStream.close();

        } catch (IOException e) {
            // TODO: 处理异常
            e.printStackTrace();
        }
    }
```