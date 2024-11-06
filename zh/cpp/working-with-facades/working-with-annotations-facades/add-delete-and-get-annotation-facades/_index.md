---
title: 添加、删除和获取注释 - Facades
type: docs
weight: 10
url: zh/cpp/add-delete-and-get-annotation-facades/
---

## <ins>**在现有的 PDF 文件中添加注释使用 PdfContentEditor**
**PdfContentEditor** 允许您在现有的 PDF 文件中添加不同类型的注释。您可以使用 **PdfContentEditor** 类的相应方法，在现有 PDF 文档中添加特定类型的注释。例如，在以下代码片段中，我们使用了 **CreateText(...)** 和 **CreateFreeText(...)** 方法，分别在现有 PDF 中添加注释和自由文本注释。为了使用 **PdfContentEditor** 类添加注释，您需要执行以下步骤：

- 创建一个 Facades::PdfContentEditor 对象。
- 使用 **BindPdf(...)** 方法加载现有的 PDF。
- 调用相应的方法来创建注释。例如 **CreateText(...)、CreateFreeText(...)** 等。
- 使用 **Save(...)** 方法保存 PDF 文档。
### **向现有的 PDF 文档添加注释**

以下代码片段向您展示了如何在现有 PDF 文件中添加注释。
```

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-AddAnnotation-AddAnnotation.cpp" >}}
## <ins>**从现有 PDF 删除所有注释**
Aspose.PDF for C++ 还提供了 **PdfAnnotationEditor** 类，该类使您能够删除 PDF 文档中的所有注释。为了删除现有 PDF 中的所有注释，您需要创建一个 **PdfAnnotationEditor** 类的对象并打开现有文档。之后，您可以使用 PdfAnnotationEditor 类的 **DeleteAnnotations(...)** 方法来删除注释。以下代码片段向您展示了使用 PdfAnnotationEditor 来实现此目的：

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-DeleteAllAnnotations-1.cpp" >}}
## <ins>**按指定类型删除所有注释**
您可以使用 **PdfAnnotationEditor** 类按指定的注释类型删除现有 PDF 文件中的所有注释。 为了做到这一点，您需要创建一个**PdfAnnotationEditor**对象，并使用**BindPdf**方法绑定输入PDF文件。之后，调用**DeleteAnnotations**方法，并传入字符串参数，以从文件中删除所有注释；字符串参数表示要删除的注释类型。最后，使用**Save**方法保存更新后的PDF文件。以下代码段向您展示如何通过指定的注释类型删除所有注释。

## <ins>**更新/修改现有PDF文件中的注释**
为了更新修改PDF文档中的注释，您可以使用**PdfAnnotationEditor**类的**ModifyAnnotations(...)**方法，该方法需要传入一个注释对象以及注释的起始和结束索引。以下代码段将演示**ModifyAnnotations(...)**方法的用法：## <ins>**从XFDF导入注释到PDF文件**
**PdfAnnotationEditor**类的**ImportAnnotationFromXfdf**方法，允许您将注释导入到PDF文件中。为了导入注释，您需要创建一个**PdfAnnotationEditor**对象，并使用**BindPdf**方法绑定PDF文件。之后，您需要创建一个要导入到PDF文件中的注释类型的枚举。然后，您可以使用**ImportAnnotationFromXfdf**方法来导入注释。最后，使用**PdfAnnotationEditor**对象的**Save**方法保存更新后的PDF文件。以下代码片段展示了如何从XFDF文件导入注释。

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-ImportAnnotations-1.cpp" >}}
## **从PDF文件导出注释到XFDF**
**ExportAnnotationXfdf**方法允许您从PDF文件中导出注释。 为了导出注释，您需要创建一个**PdfAnnotationEditor**对象并使用**BindPdf**方法绑定PDF文件。之后，您需要创建一个要从PDF文件中导出的注释类型的枚举。然后，您可以使用**ExportAnnotationXfdf**方法导入注释。最后，使用**PdfAnnotationEditor**对象的**Save**方法保存更新后的PDF文件。以下代码片段向您展示如何将注释导出到XFDF文件。

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-ExportAnnotations-1.cpp" >}}
## <ins>**从现有PDF文件中提取注释**
**ExtractAnnotations**方法允许您从PDF文件中提取注释。 为了提取注释，您需要创建一个**PdfAnnotationEditor**对象，并使用**BindPdf**方法绑定PDF文件。之后，您需要创建一个枚举，以列出您想从PDF文件中提取的注释类型。然后，您可以使用**Extract Annotations**方法将注释提取到ArrayPtr中。接下来，您可以遍历此列表并获取单个注释。最后，使用**PdfAnnotationEditor**对象的**Save**方法保存更新后的PDF文件。以下代码片段展示了如何从PDF文件中提取注释。

{{< gist "aspose-pdf" "e5fb9ddf5bd6460bb13d47fe5a83d86d" "Examples-PdfCPP-Annotations-ExtractAnnotations-1.cpp" >}}