---
title: FDF、XML 和 XFDF 格式之间有什么区别
type: docs
weight: 30
url: zh/net/whats-the-difference-between-xml-fdf-and-xfdf/
description: 本节介绍使用 Aspose.PDF Facades 的 Form 类在 XML、FDF 和 XFDF 表单之间的区别。
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

我们混合了许多不同的术语，如 FDF、XML 和 XFDF。所有这些术语在某种程度上是相互关联的。本文探讨了这些概念及其相互关系。

{{% /alert %}}

## 解开表单

Aspose.PDF for .NET 用于操作由 Adobe 标准化的 PDF 文档。而 PDF 文档包含称为 AcroForms 的交互式表单。这些交互式表单具有多个表单字段，如组合框、文本框和单选按钮。Adobe 的交互式表单及其表单字段的工作方式与 HTML 表单及其表单字段相同。

可以将表单字段的值存储在一个单独的文件中：一个 FDF（表单数据格式）文件。
``` 这包含以键/值对形式的表单字段的值。FDF文件仍然用于此目的。但Adobe也提供了一种称为XFDF的XML编码类型的FDF。XFDF文件使用XML标签以层次结构方式存储表单字段的值。

通过Aspose.PDF，开发人员不仅可以将PDF表单字段的值导出到FDF或XFDF文件，还可以导出到XML文件。所有这些文件使用不同的语法来保存PDF表单字段值。下面的示例解释了这些差异。

假设有一些PDF表单字段，其值需要以FDF、XML和XFDF形式表示。这些假设的表单字段及其字段名称和值如下所示：

|**字段名称**|**字段值**|
| :- | :- |
|Company|Aspose.com|
|Address.1|悉尼，澳大利亚|
|Address.2|附加地址行|
让我们看看如何在FDF、XML和XFDF格式中表示这些值。

### 什么是FDF格式？

正如我们所知，FDF文件以键/值对形式存储数据，其中/T代表键，/V代表值，括号()中的数据代表键或值的内容。 例如，/T(Company) 表示 Company 是字段键，/V(Aspose.com) 表示字段值。

/T(Company) /V(Aspose.com)
/T(Address.1) /V( Sydney , Australia )
/T(Address.2) /V(Additional Address Line)

### 什么是 XML 格式？

开发者可以将每个 PDF 表单字段表示为一个字段标签，`<field>`。每个字段标签都有一个名为 name 的属性显示字段名称，还有一个子标签，`<value>` 表示字段值，如下所示：

```xml
 <?xml version="1.0" ?>
 <fields>
  <field name="Company">
    <value>Aspose.com</value>
  </field>
  <field name="Address.1">
    <value>Sydney, Australia</value>
  </field>
  <field name="Address.2">
    <value>Additional Address Line</value>
  </field>
 </fields>
```

### ### 什么是 XFDF 格式？

上述数据在 XFDF 格式中的表示与 XML 格式类似，但有一些区别。 在XFDF文件中，我们添加了它们的XML命名空间，即<http://ns.adpbe.com/xfdf/>，并且有一个额外的标签`<f>`用于指向包含这些PDF表单字段的PDF文档。与XML一样，XFDF也包含以字段标签`<field>`形式的字段，如下所示：

```xml

<?xml version="1.0" encoding="UTF-8"?>
<xfdf xmlns="http://ns.adobe.com/xfdf/" xml:space="preserve">   
   <f href="CompanyForm.pdf"/> 
   <fields>
      <field name="Company">
         <value>Aspose.com</value>
      </field>
      <field name="Address">
         <field name="1">
            <value>Sydney, Australia</value>
         </field>
         <field name="2">
            <value>Additional Address Line</value>
         </field>
      </field>
   </fields>
 </xfdf>
```

### 识别表单字段名称

Aspose.PDF for .NET提供了创建、编辑和填写已创建PDF表单的功能。 它包含 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) 类，其中有一个名为 [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index) 的函数，该函数接受两个参数，即需要填写的字段名称和字段值。因此，为了填写表单字段，您必须知道确切的表单字段名称。我们经常遇到需要填写用某些工具创建的表单的情形，即。 Adobe Designer，我们不确定表单字段的名称。为了满足我们的需求，我们需要读取所有 PDF 表单字段的名称。[Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) 类提供了一个名为 [FieldsNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/properties/fieldnames) 的属性，该属性返回所有字段的名称，如果 PDF 没有字段，则返回 null。但是这个属性将返回所有 PDF 表单字段的名称，我们无法确定哪个名称对应表单上的哪个字段。

作为解决此问题的方法，我们需要每个字段的外观属性。 [Form](http://www.aspose.com/documentation/file-format-components/aspose.pdf.kit-for-.net-and-java/aspose.pdf.kit.form.html) 类有一个名为 GetFieldFacade 的函数，它返回属性，包括位置、颜色、边框样式、字体、列表项等。为了保存这些值，我们将使用 [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) 类，该类用于记录字段的视觉属性。一旦我们拥有这些属性，我们可以在每个字段下添加一个文本字段，该字段将显示字段名称。这里出现了一个问题，我们如何确定添加文本字段的位置？这个问题的解决方案是 [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) 类中的 Box 属性，它保存字段的位置。我们将这些值保存到一个矩形类型的数组中，并使用这些值来识别添加新文本字段的位置。在 Aspose.Pdf.Facades 命名空间中，我们有一个名为 [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) 的类，它提供了操作 PDF 表单的功能。 打开一个 PDF 表单，在每个现有表单字段下方添加一个文本字段，并以新名称保存 PDF 表单。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-DifferenceBetweenFile-DifferenceBetweenFile.cs" >}}