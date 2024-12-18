---
title:  使用 C# 从 AcroForm 提取数据
linktitle:  从 AcroForm 提取数据
type: docs
weight: 50
url: /zh/net/extract-data-from-acroform/
description: Aspose.PDF 可以轻松地从 PDF 文件中提取表单字段数据。了解如何从 AcroForms 提取数据并将其保存为 JSON、XML 或 FDF 格式。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 从 PDF 文档提取表单字段

Aspose.PDF for .NET 不仅可以帮助您生成表单字段和填充表单字段，还可以轻松地从 PDF 文件中提取表单字段数据或表单字段的信息。

在下面的示例代码中，我们演示了如何遍历 PDF 中的每个页面以提取有关 PDF 中所有 AcroForm 的信息以及表单字段值。此示例代码假设您事先不知道表单字段的名称。

以下代码片段也可以与 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库一起使用。

```csharp
public static void ExtractFormFields()
{
    var document = new Aspose.Pdf.Document(Path.Combine(_dataDir, "StudentInfoFormElectronic.pdf"));
    // 从所有字段获取值
    foreach (Field formField in document.Form)
    {
        Console.WriteLine("字段名称 : {0} ", formField.PartialName);
        Console.WriteLine("值 : {0} ", formField.Value);
    }
}
```
如果您知道希望从中提取值的表单字段的名称，则可以使用 Documents.Form 集合中的索引器快速检索此数据。请查看本文底部的示例代码，了解如何使用该功能。

## 按标题检索表单字段值

表单字段的 Value 属性允许您获取特定字段的值。要获取值，请从 Document 对象的 Form 集合中获取表单字段。此示例选择一个 TextBoxField 并使用 Value 属性检索其值。

## 从 PDF 文档提取表单字段到 JSON

以下代码片段也可以与 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库一起使用。

```csharp
public static void ExtractFormFieldsToJson()
{
    var document = new Aspose.Pdf.Document(Path.Combine(_dataDir, "StudentInfoFormElectronic.pdf"));
    var formData = document.Form.Cast<Field>().Select(f => new { Name = f.PartialName, f.Value });
    string jsonString = JsonSerializer.Serialize(formData);
    Console.WriteLine(jsonString);
}
```
## 从 PDF 文件提取数据到 XML 文件

Form 类允许您使用 ExportXml 方法从 PDF 文件导出数据到 XML 文件。为了导出数据到 XML，您需要创建一个 Form 类的对象，然后使用 FileStream 对象调用 ExportXml 方法。最后，您可以关闭 FileStream 对象并释放 Form 对象。以下代码片段展示了如何导出数据到 XML 文件。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

```csharp
// 完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

// 打开文档
Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
form.BindPdf(dataDir + "input.pdf");
// 创建 xml 文件。
System.IO.FileStream xmlOutputStream = new FileStream( dataDir + "input.xml", FileMode.Create);
// 导出数据
form.ExportXml(xmlOutputStream);
// 关闭文件流
xmlOutputStream.Close();

// 关闭文档
form.Dispose();
```
## 从 PDF 文件导出数据到 FDF 文件

Form 类允许您使用 ExportFdf 方法从 PDF 文件导出数据到 FDF 文件。为了将数据导出到 FDF，您需要创建 Form 类的一个对象，然后使用 FileStream 对象调用 ExportFdf 方法。最后，您可以使用 Form 类的 Save 方法保存 PDF 文件。以下代码片段向您展示了如何导出数据到 FDF 文件。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

```csharp
// 完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
// 打开文档
form.BindPdf(dataDir + "input.pdf");

// 创建 fdf 文件。
System.IO.FileStream fdfOutputStream = new FileStream(dataDir + "student.fdf", FileMode.Create);

// 导出数据
form.ExportFdf(fdfOutputStream);

// 关闭文件流
fdfOutputStream.Close();

// 保存更新的文档
form.Save(dataDir + "ExportDataToPdf_out.pdf");
```
## 将数据从 PDF 文件导出到 XFDF

Form 类允许您使用 ExportXfdf 方法从 PDF 文件导出数据到 XFDF 文件。为了导出数据到 XFDF，您需要创建 Form 类的一个对象，然后使用 FileStream 对象调用 ExportXfdf 方法。最后，您可以使用 Form 类的 Save 方法保存 PDF 文件。以下代码片段展示了如何将数据导出到 XFDF 文件。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

```csharp
// 完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
// 打开文档
form.BindPdf(dataDir + "input.pdf");

// 创建 xfdf 文件。
System.IO.FileStream xfdfOutputStream = new FileStream("student1.xfdf", FileMode.Create);

// 导出数据
form.ExportXfdf(xfdfOutputStream);

// 关闭文件流
xfdfOutputStream.Close();

// 保存更新的文档
form.Save(dataDir + "ExportDataToXFDF_out.pdf");
```

