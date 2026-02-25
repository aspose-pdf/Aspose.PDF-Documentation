---
title: 使用 Python 从 PDF 文件中提取链接
linktitle: 提取链接
type: docs
weight: 30
url: /zh/python-net/extract-links/
description: 了解如何使用 Aspose.PDF 在 Python 中提取 PDF 文档中的超链接，以进行内容管理和链接分析。
lastmod: "2025-07-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何从 PDF 中提取链接
Abstract: Aspose.PDF for Python via .NET 的链接提取指南解释了如何使用 Python 编程方式从 PDF 文档中检索超链接注释。文档包含实用的代码示例，且突出显示该功能可用于链接审计、导航分析或构建交互式文档功能等任务。无论是处理单页 PDF 还是大批量文档，本指南都提供了清晰高效的超链接提取方法。
---

## 从 PDF 文件中提取链接

本示例演示了如何使用 Aspose.PDF for Python 遍历 PDF 首页的所有链接注释。它会过滤注释以识别 LinkAnnotation 类型的注释，安全地进行类型转换，然后打印它们的页索引和在页面上的矩形位置。

这可用于调试、分析或对 PDF 中现有链接注释进行自动更新。

1. 加载 PDF 文档。使用 ap.Document(path_infile) 打开文件。
1. 访问首页的注释。使用 document.pages[1].annotations 获取所有注释。
1. 仅过滤 LinkAnnotation 类型。检查每个注释的 annotation_type。
1. 转换并处理 LinkAnnotation。使用 is_assignable() 和 cast() 确保安全访问 LinkAnnotation 属性。
1. 打印注释详情。输出每个链接的页索引和矩形（位置）。

```python

    import aspose.pdf as ap
    from os import path

    # Construct full path for the input PDF file
    path_infile = path.join(self.dataDir, infile)

    # (Optional) You can construct the output file path if needed later
    # path_outfile = path.join(self.dataDir, outfile)

    # Load the PDF document
    document = ap.Document(path_infile)

    # Retrieve all annotations from the first page and filter only LinkAnnotations
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    # Iterate over each link annotation
    for la in link_annotations:
        # Check if the annotation is a LinkAnnotation (type-safe check)
        if is_assignable(la, ap.annotations.LinkAnnotation):
            # Safely cast the annotation to LinkAnnotation type
            annotation = cast(ap.annotations.LinkAnnotation, la)
            
            # Print annotation location and page index
            print(f"Page: {annotation.page_index}, location: {annotation.rect}")
            print(annotation.page_index)
```

## 从 PDF 文件中提取超链接

此代码演示了如何使用 Aspose.PDF for Python 从 PDF 文档的首页提取所有 LinkAnnotation 对象，并识别其中包含 GoToURIAction 的链接。对于每个此类链接，打印其页索引和目标 URI。

这对于以下任务很有用：

- 审计 PDF 中的外部链接
- 提取文档或支持 URL
- 检测失效或过时的超链接

1. 加载 PDF 文档。使用 ap.Document 打开文件。
1. 获取首页的所有链接注释。过滤注释，仅保留类型为 AnnotationType.LINK 的注释。
1. 类型检查并转换为 LinkAnnotation。确保每个注释确实是 LinkAnnotation 后再访问其属性。
1. 检查链接的操作类型。过滤使用 GoToURIAction 的链接（即指向网页 URL 的链接）。
1. 提取并打印 URI 和页索引。使用 .uri 获取外部链接，使用 .page_index 获取上下文。

```python

    import aspose.pdf as ap
    from os import path

    # Construct the full path for the input PDF file
    path_infile = path.join(self.dataDir, infile)

    # Optional: construct output file path if needed
    # path_outfile = path.join(self.dataDir, outfile)

    # Load the input PDF document
    document = ap.Document(path_infile)

    # Retrieve all annotations from the first page and filter only link annotations
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.LINK
    ]

    # Iterate through filtered link annotations
    for la in link_annotations:
        # Check if the annotation is a LinkAnnotation (safe type check)
        if is_assignable(la, ap.annotations.LinkAnnotation):
            # Cast the annotation to LinkAnnotation to access link-specific properties
            annotation = cast(ap.annotations.LinkAnnotation, la)

            # Check if the link's action is of type GoToURIAction (external web link)
            if is_assignable(annotation.action, ap.annotations.GoToURIAction):
                # Cast the action to GoToURIAction to access the URI property
                action = cast(ap.annotations.GoToURIAction, annotation.action)

                # Print the page number and the link's URI
                print(f"Page {annotation.page_index}, URI: {action.uri}")
```
