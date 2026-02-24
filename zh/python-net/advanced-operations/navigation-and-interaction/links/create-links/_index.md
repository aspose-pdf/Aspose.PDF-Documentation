---
title: 使用 Python 在 PDF 文件中创建链接
linktitle: 创建链接
type: docs
weight: 10
url: /zh/python-net/create-links/
description: 本节解释如何使用 Python 在 PDF 文档中创建链接。
lastmod: "2025-07-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何在 PDF 中创建链接
Abstract: Aspose.PDF for Python via .NET 的链接创建指南为开发者提供了使用 Python 向 PDF 文档添加交互式超链接的实用说明。它涵盖了如何创建各种类型的链接，包括启动外部应用程序、在同一文档内导航至特定页面或打开其他 PDF 文件的链接。文档解释了如何使用 LinkAnnotation 对象、使用 Rectangle 定义可点击区域，并分配诸如 LaunchAction 或 GoToRemoteAction 等操作。通过清晰的代码示例和一步一步的指导，此资源帮助开发者在其 Python 应用程序中增强 PDF 的导航和交互性。
---

## PDF 文档中的链接

根据 PDF 1.7 规范（ISO 32000-1:2008），**链接注释**可以触发多种操作类型，以定义注释被激活时的行为。以下是支持的主要操作：

1. **GoTo** – 导航到同一文档中的目标位置。
1. **GoToR** – 跳转到另一个 PDF 文件中的目标（远程跳转）。
1. **URI** – 打开统一资源标识符，通常是网页链接。
1. **Launch** – 启动应用程序或打开文件（取决于平台，出于安全考虑通常受限制）。
1. **Named** – 执行预定义操作，例如跳转到下一页或打印文档。
1. **JavaScript** – 执行嵌入的 JavaScript 代码（因安全问题需谨慎使用）。
1. **SubmitForm** – 将表单数据提交到指定的 URL。
1. **ResetForm** – 将表单字段重置为默认值。
1. **ImportData** – 从外部文件导入数据到文档中。

通过在文档中添加指向应用程序的链接，可以实现从文档链接到应用程序。这在例如希望读者在教程的特定位置执行某些操作，或创建功能丰富的文档时非常有用。

使用 'LaunchAction' 创建应用程序链接：

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Open the input PDF document
    document = ap.Document(path_infile)

    # Select the second page (index 1)
    page = document.pages[1]

    # Create a link annotation with specific dimensions and position
    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))

    # Configure the link's border
    border = ap.annotations.Border(link)
    border.width = 5  # Border width of 5 units
    border.dash = ap.annotations.Dash(1, 1)  # Dashed border style

    # Set link appearance
    link.color = ap.Color.green  # Green color for the link

    # Set the action to launch another PDF file
    # Note: Commented out system command demonstrates potential alternative launch actions
    # link.action = ap.annotations.LaunchAction(document, "start %windir%\explorer.exe")
    link.action = ap.annotations.LaunchAction(document, "sample.pdf")

    # Add the link annotation to the page
    page.annotations.append(link)

    # Save the modified document
    document.save(path_outfile)
```

## 在 PDF 文件中创建 PDF 文档链接

### 使用 GoToRemoteAction

此代码片段演示如何使用 Python PDF 库在 PDF 文档的特定页面添加链接注释。

1. 打开 PDF 文档
1. 选择文档的第二页（索引 1）
1. 创建链接注释：
1. 位于坐标 (10, 580, 120, 600) 处
1. 颜色为绿色
1. 链接到 'sample.pdf' 的第一页
1. 将链接注释添加到页面
1. 将修改后的文档保存到输出文件路径

使用 'GoToRemoteAction' 创建 PDF 文档链接：

```python

import aspose.pdf as ap
from os import path

path_infile = path.join(self.dataDir, infile)
path_outfile = path.join(self.dataDir, outfile)

# Load the input PDF document
document = ap.Document(path_infile)

# Access the first page of the document (Aspose uses 1-based indexing)
page = document.pages[1]

# Create a link annotation in the specified rectangle area on the page
link = ap.annotations.LinkAnnotation(
    page, ap.Rectangle(10, 580, 120, 600, True)  # (left, bottom, right, top, isEmpty)
)

# Set the color of the link annotation to green
link.color = ap.Color.green

# Define a remote action to open "sample.pdf" and navigate to its first page
link.action = ap.annotations.GoToRemoteAction("sample.pdf", 1)

# Add the link annotation to the current page
page.annotations.append(link)

# Save the updated PDF to the specified output path
document.save(path_outfile)
```

### 使用 GoToAction

此代码演示如何使用 Aspose.PDF for Python 在 PDF 文档的特定页面添加链接注释。该链接显示为绿色、虚线边框的矩形，允许用户在同一 PDF 内导航到另一页。使用 'GoToAction' 创建 PDF 文档链接：

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Open the PDF document
    document = ap.Document(path_infile)

    # Select the second page (index 1)
    page = document.pages[1]

    # Create a link annotation with specific coordinates
    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))

    # Customize link annotation border
    border = ap.annotations.Border(link)
    border.width = 5  # Border width
    border.dash = ap.annotations.Dash(1, 1)  # Dashed border style

    # Set link color to green
    link.color = ap.Color.green

    # Set link destination
    if document.pages.count >= 4:
        # Link to 4th page if document has 4 or more pages
        link.action = ap.annotations.GoToAction(document.pages[4])
    else:
        # Fallback: link to the last page if less than 4 pages
        link.action = ap.annotations.GoToAction(document.pages[document.pages.count])

    # Add the link annotation to the page
    page.annotations.append(link)

    # Save the modified document
    document.save(path_outfile)
```

### 应用 GoToURIAction

下一个示例演示如何使用 Aspose.PDF for Python 向 PDF 文档添加链接注释。该链接显示为第一页的绿色可点击区域，点击后通过 GoToURIAction 在网页浏览器中打开 Aspose.PDF for Python 文档。

此功能可用于在 PDF 中直接嵌入有用的外部参考、文档或支持链接。

1. 加载 PDF 文档。使用 ap.Document 打开现有的 PDF 文件。
1. 访问首页。使用 document.pages[1] 访问第一页（Aspose 使用基于 1 的索引）。
1. 创建链接注释。创建 LinkAnnotation 对象，并使用 ap.Rectangle 指定可点击的矩形区域。
1. 设置注释外观。使用 link.color = ap.Color.green 将注释颜色设为绿色。
1. 分配 URI 操作。使用 GoToURIAction 将注释链接到外部 URL。
1. 将注释添加到页面。将配置好的链接注释追加到第一页的 annotations 集合中。
1. 保存修改后的文档。将更新后的 PDF 文档保存到指定的输出路径。

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Load the input PDF document
    document = ap.Document(path_infile)

    # Access the first page (Aspose uses 1-based indexing)
    page = document.pages[1]

    # Create a link annotation at the specified rectangle position
    link = ap.annotations.LinkAnnotation(
        page, ap.Rectangle(10, 580, 120, 600, True)  # (left, bottom, right, top, isEmpty)
    )

    # Set the color of the link annotation to green
    link.color = ap.Color.green

    # Define a URI action that navigates to the Aspose.PDF Python documentation
    link.action = ap.annotations.GoToURIAction("https://docs.aspose.com/pdf/python")

    # Add the link annotation to the page
    page.annotations.append(link)

    # Save the modified PDF to the output path
    document.save(path_outfile)
```

