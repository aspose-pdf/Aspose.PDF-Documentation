---
title: FDF、XML 和 XFDF 格式之间的区别是什么
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /zh/net/whats-the-difference-between-xml-fdf-and-xfdf/
description: 本节介绍了使用 Form 类的 Aspose.PDF Facades 中 XML、FDF 和 XFDF 表单之间的区别。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Whats is the difference between FDF, XML, and XFDF formats",
    "alternativeHeadline": "Understanding FDF, XML, and XFDF Formats in Aspose.PDF for .NET",
    "abstract": "通过 Aspose.PDF for .NET 发现 FDF、XML 和 XFDF 格式之间的区别。这一功能使开发人员能够无缝导出交互式表单字段值为多种格式，每种格式都有其自己的语法，同时增强对这些在 PDF 处理中的基本文件类型的理解和使用。通过详细的见解优化您的 PDF 表单处理，了解如何在不同数据格式中表示表单字段。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1045",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/whats-the-difference-between-xml-fdf-and-xfdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/whats-the-difference-between-xml-fdf-and-xfdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

{{% alert color="primary" %}}

我们混合了许多不同的术语，如 FDF、XML 和 XFDF。这些术语在某种程度上是相互关联的。本文探讨了这些概念及其相互关系。

{{% /alert %}}

## 解开表单的谜团

Aspose.PDF for .NET 用于操作由 Adobe 标准化的 PDF 文档。PDF 文档包含称为 AcroForms 的交互式表单。这些交互式表单有多个表单字段，如组合框、文本框和单选按钮。Adobe 的交互式表单和表单字段的工作方式与 HTML 表单及其表单字段相同。

可以将表单字段的值存储在单独的文件中：FDF（表单数据格式）文件。它以键/值对的方式包含表单字段的值。FDF 文件仍然用于此目的。但 Adobe 还提供了一种称为 XFDF 的 XML 编码类型的 FDF。XFDF 文件以层次结构的方式使用 XML 标签存储表单字段的值。

使用 Aspose.PDF，开发人员不仅可以将 PDF 表单字段的值导出到 FDF 或 XFDF 文件，还可以导出到 XML 文件。所有这些文件使用不同的语法来保存 PDF 表单字段的值。下面的示例解释了这些差异。

假设有一些 PDF 表单字段，其值需要以 FDF、XML 和 XFDF 格式呈现。以下是这些假设的表单字段及其字段名称和值：

|**字段名称**|**字段值**|
| :- | :- |
|公司|Aspose.com|
|地址.1|澳大利亚悉尼|
|地址.2|附加地址行|
让我们看看如何以 FDF、XML 和 XFDF 格式表示这些值。

### 什么是 FDF 格式？

我们知道 FDF 文件以键/值对的方式存储数据，其中 /T 表示键，/V 表示值，括号 () 中的数据表示键或值的内容。例如，/T(Company) 意味着 Company 是字段键，/V(Aspose.com) 是字段值。

/T(Company) /V(Aspose.com)
/T(Address.1) /V( Sydney , Australia )
/T(Address.2) /V(Additional Address Line)

### 什么是 XML 格式？

开发人员可以将每个 PDF 表单字段表示为字段标签 `<field>`。每个字段标签都有一个属性 name，显示字段名称，以及一个子标签 `<value>`，表示字段值，如下所示：

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

### 什么是 XFDF 格式？

上述数据在 XFDF 形式中的表示与 XML 形式相似，但有一些不同之处。在 XFDF 文件中，我们添加它们的 XML 命名空间，即 <http://ns.adpbe.com/xfdf/>，并且有一个额外的标签 `<f>`，用于指向包含这些 PDF 表单字段的 PDF 文档。与 XML 一样，XFDF 也以字段标签 `<field>` 的形式包含字段，如下所示：

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

Aspose.PDF for .NET 提供了创建、编辑和填写已创建 PDF 表单的能力。它包含 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) 类，该类具有名为 [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index) 的函数，它接受两个参数，即需要填写的字段名称和字段值。因此，为了填写表单字段，您必须知道确切的表单字段名称。
我们经常遇到需要填写在某个工具中创建的表单的情况，例如 Adobe Designer，而我们不确定表单字段名称。为了满足我们的需求，我们需要读取所有 PDF 表单字段的名称。[Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) 类提供了名为 [FieldsNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/properties/fieldnames) 的属性，该属性返回所有字段的名称，如果 PDF 没有字段，则返回 null。但该属性将返回所有 PDF 表单字段的名称，我们无法确定哪个名称对应于表单上的哪个字段。

为了解决这个问题，我们需要每个字段的外观属性。[Form](http://www.aspose.com/documentation/file-format-components/aspose.pdf.kit-for-.net-and-java/aspose.pdf.kit.form.html) 类具有名为 GetFieldFacade 的函数，该函数返回包括位置、颜色、边框样式、字体、列表项等属性。为了保存这些值，我们将使用 [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) 类，该类用于记录字段的视觉属性。一旦我们拥有这些属性，我们可以在每个字段下添加一个文本字段，以显示字段名称。在这里，出现了一个问题，我们如何确定添加文本字段的位置？解决此问题的方法是 [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) 类中的 Box 属性，该属性保存字段的位置。我们将这些值保存到一个矩形类型的数组中，并使用这些值来确定添加新文本字段的位置。
在 Aspose.Pdf.Facades 命名空间中，我们有一个名为 [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) 的类，它提供了操作 PDF 表单的能力。打开一个 PDF 表单，在每个现有表单字段下添加一个文本字段，并使用新名称保存 PDF 表单。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void DifferenceBetweenFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    // First a input pdf file should be assigned
    using (var form = new Aspose.Pdf.Facades.Form(dataDir + "FilledForm.pdf"))
    {
        // Get all field names
        String[] allfields = form.FieldNames;
        // Create an array which will hold the location coordinates of Form fields
        var box = new System.Drawing.Rectangle[allfields.Length];
        for (int i = 0; i < allfields.Length; i++)
        {
            // Get the appearance attributes of each field, consecutively
            var facade = form.GetFieldFacade(allfields[i]);
            // Box in FormFieldFacade class holds field's location.
            box[i] = facade.Box;
        }
        // Save PDF document
        form.Save(dataDir + "DifferenceBetweenFile_out.pdf");
            
        // Open PDF document
        using (var document = new Aspose.Pdf.Document(dataDir + "FilledForm - 2.pdf"))
        {
            // Now we need to add a textfield just upon the original one
            FormEditor editor = new Aspose.Pdf.Facades.FormEditor(document);
            for (int i = 0; i < allfields.Length; i++)
            {
                // Add text field beneath every existing form field
                editor.AddField(Aspose.Pdf.Facades.FieldType.Text, "TextField" + i, allfields[i], 1, box[i].Left, box[i].Top, box[i].Left + 50, box[i].Top + 10);
            }
            // Save PDF document
            editor.Save(dataDir + "DifferenceBetweenFile_out.pdf");
        }
    }
}
```