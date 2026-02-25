---
title: 使用 Python 更新 PDF 中的链接
linktitle: 更新链接
type: docs
weight: 20
url: /zh/python-net/update-links/
description: 以编程方式更新 PDF 中的链接。本指南介绍如何在 Python 语言中更新 PDF 链接。
lastmod: "2025-07-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何在 PDF 中更新链接
Abstract: Aspose.PDF for Python via .NET 更新链接指南引导开发者使用 Python 修改 PDF 文档中超链接的行为。它说明了如何将链接目标更改为指向特定页面、外部网站或其他 PDF 文件。文档还涵盖了如何调整链接注释的外观，包括文本颜色，并为每种情况提供实用的代码示例。无论是纠正过时的 URL 还是增强导航，此资源都提供了一种清晰高效的编程方式来管理链接。
---

## 更新 LinkAnnotation 文本颜色

此示例展示了如何使用 Aspose.PDF for Python 检测 PDF 首页的所有链接注释，然后通过将其字体颜色更改为红色来突出显示每个链接附近的文本。它使用 TextFragmentAbsorber 并在每个链接矩形周围稍作扩展的区域来查找并修改邻近文本。

可用于以下情况：

- 在文档中直观标记链接
- 通过强调链接内容提升可访问性
- 在审阅或导出前对 PDF 文件进行预处理

对于每个链接注释，脚本获取其矩形边界并略微扩展该区域以包含邻近文本，从而实现更广泛的视觉识别。随后在此扩展区域上应用 TextFragmentAbsorber，以提取其中的所有文本片段。这些捕获的片段通过将字体颜色改为红色进行修改，从而有效地标记周围文本以便强调和审查。完成所有更新后，修改后的文档将保存到输出路径，保留高亮的注释及其关联的文本。

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Load the input PDF document
    document = ap.Document(path_infile)

    # Filter all link annotations on the first page
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.LINK
    ]

    # Loop through each link annotation found
    for la in link_annotations:
        # Create a text absorber for extracting text fragments
        ta = ap.text.TextFragmentAbsorber()

        # Get the rectangle area of the annotation
        rect = la.rect

        # Expand the rectangle slightly to catch text near the link
        rect.llx -= 2  # Lower-left x
        rect.lly -= 2  # Lower-left y
        rect.urx += 2  # Upper-right x
        rect.ury += 2  # Upper-right y

        # Restrict text search to the adjusted rectangle
        ta.text_search_options = ap.text.TextSearchOptions(rect)

        # Apply the absorber to the first page
        ta.visit(document.pages[1])

        # Iterate through found text fragments and change their color to red
        for textFragment in ta.text_fragments:
            textFragment.text_state.foreground_color = ap.Color.red

    # Save the updated PDF document to the output path
    document.save(path_outfile)
```

## 更新边框

脚本聚焦于文档的首页，过滤掉所有注释，仅选择 LINK 类型的注释——这些通常代表交互元素，如超链接或导航触发器。对于每个此类链接注释，代码将其转换为 LinkAnnotation 类型，并将其颜色属性更新为红色，以视觉方式突出显示，使其在其他内容中脱颖而出。所有链接注释修改完成后，更新后的文档将保存到指定的输出位置，保留新的样式。

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Load the PDF document
    document = ap.Document(path_infile)

    # Get all annotations of type LINK on the first page
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    # Loop through each link annotation and change its color to red
    for la in link_annotations:
        link_annotation = cast(ap.annotations.LinkAnnotation, la)
        link_annotation.color = ap.Color.red  # Highlight the link in red

    # Save the modified PDF to the output path
    document.save(path_outfile)
```    

## 更新网页目标

路径就绪后，原始文档使用 Aspose.PDF 库加载，使其内容可供修改。随后脚本聚焦于文档的首页，过滤掉所有注释，仅选择链接类型的注释，通常代表可点击区域或超链接。为避免类型错误并确保安全处理，每个注释先通过 is_assignable 检查，然后转换为相应的 LinkAnnotation 类型。如果链接关联的是 GoToURIAction，意味着它指向网页地址，脚本会将该 URI 更新为重定向用户至 "https://www.google.com"。最后，在应用所有所需更改后，修改后的文档被保存到指定的输出路径。

```python

    import aspose.pdf as ap
    from os import path

path_infile = path.join(self.dataDir, infile)
path_outfile = path.join(self.dataDir, outfile)

# Load the PDF document
document = ap.Document(path_infile)

# Find all LINK annotations on the first page
link_annotations = [
    a
    for a in document.pages[1].annotations
    if (a.annotation_type == ap.annotations.AnnotationType.LINK)
]

# Loop through annotations and replace target URI
for la in link_annotations:
    # Ensure the annotation is a LinkAnnotation
    if is_assignable(la, ap.annotations.LinkAnnotation):
        annotation = cast(ap.annotations.LinkAnnotation, la)
        
        # Check if the action is of type GoToURIAction
        if is_assignable(annotation.action, ap.annotations.GoToURIAction):
            action = cast(ap.annotations.GoToURIAction, annotation.action)
            
            # Replace the existing URI with Google
            action.uri = "https://www.google.com"

# Save the modified document to output path
document.save(path_outfile)
```
