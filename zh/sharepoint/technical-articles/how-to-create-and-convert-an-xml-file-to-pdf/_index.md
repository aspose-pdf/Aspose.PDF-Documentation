---

title: 如何创建和转换XML文件为PDF

type: docs

weight: 30

url: zh/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/

lastmod: "2020-12-16"

description: PDF SharePoint API能够创建和转换XML文件为PDF格式。

---

{{% alert color="primary" %}}

Aspose.PDF for SharePoint建立在我们屡获殊荣的Aspose.PDF for .NET组件之上。Aspose.PDF for .NET提供了从头创建PDF文档到操作现有PDF文件的显著功能。在这些功能中，XML到PDF的转换是该产品支持的一个出色功能。因此，我们相信Aspose.PDF for SharePoint也能够将XML文件转换为PDF格式。

{{% /alert %}}

## **创建XML文件并将其转换为PDF**

{{% alert color="primary" %}}

逐步地，本文将引导您完成创建XML文件并将其转换为PDF的过程：


1. [创建一个 XML 文件](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-1-create-xml-file).
2. [创建一个 PDF 模板](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-2-create-pdf-template).
3. [加载 XML 模板](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-3-load-xml-template).
4. [指定源路径](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-4-specify-source-file-path).
5. [指定文件属性](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-5-specify-file-properties).
6. [导出文件为 PDF](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-6-export-to-pdf).
7. [保存 PDF 文件](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-7-save-pdf-document).

#### **步骤 1：创建 XML 文件**
首先根据 Aspose.PDF for .NET 文档对象模型创建一个 XML 文件。

根据 Aspose.PDF for .NET DOM，一个 PDF 文档包含一组 Section 对象，一个 Section 包含一个或多个段落元素。
 文本是一个段落级对象，可能包含一个或多个片段。下面，将一个示例文本字符串添加到一个段对象，并添加到一个文本对象中。最后，将文本元素添加到段对象的段落集合中。

**XML**

{{< highlight csharp >}}



<?xml version="1.0" encoding="utf-8" ?>

  <Pdf xmlns="Aspose.PDF">

   <Section>

    <Text>

            <Segment>你好，世界</Segment>

    </Text>

   </Section>

  </Pdf>



{{< /highlight >}}
#### **步骤 2: 创建 PDF 模板**
在继续之前，请确保在将进行转换的系统上正确安装和配置了 SharePoint Foundation 服务 2010。

1. 登录到 SharePoint 网站。
1. 选择 **网站操作** 和 **所有项目**。
1. 选择 **创建** 选项，并从列表中选择 **PDF 模板**。
1. 输入模板名称。
1. 点击 **创建**。




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_1.png)
#### **步骤 3: 加载 XML 模板**

一旦模板创建完成，加载 [XML 文件](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/):
1. 在 PDF 模板页面，选择 **添加新项目**。




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_2.png)
#### **步骤 4：指定源文件路径**
在文档上传对话框中：

1. 点击 **浏览** 并在您的系统中找到 XML 文件。您可以启用复选框以覆盖现有文件选项。
1. 按 **确定** 按钮。




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_3.png)
#### **步骤 5：指定文件属性**
当文件加载后，在必填字段（标有红色星号：*）中添加信息。

在此示例中，已添加了示例描述并完成了以下字段：

1. 文档的简要描述。
1. 在 **分配的列表类型** 字段中输入 **AllListTypes**。
1. 从 **类型** 菜单中选择 **列表**。
   确保状态保持 **活动**。
1. 点击 **保存** 以保存属性。




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_4.png)
#### **步骤 6：导出为 PDF**

当 XML 文件已添加到 PDF 模板：
Either:

1. 右键点击 test.xml 文件。
1. 从菜单中选择 **导出为 PDF**。

Or:

1. 从 **库工具** 中选择 **Aspose 工具**。
1. 点击 **导出**。

![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_5.png)
#### **步骤 7：保存 PDF 文档**
1. 在导出为 PDF 对话框中，选择 **模板存储**（源文件存储的位置）。
1. 从 **模板名称** 菜单中选择要导出的文件。
1. 点击 **导出为 PDF** 以保存最终的 PDF 文档。

![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_6.png)
#### **打开 PDF**
PDF 文档已保存并可以打开。在下图中，请注意 XML 中 {segment} 标签中的短语 "Hello World"。还请注意 PDF 制作者是 Aspose.PDF for SharePoint。

![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_7.png)

{{% /alert %}}