---
title: 使用 Python 的安全注释
linktitle: 安全注释
type: docs
weight: 75
url: /zh/python-net/security-annotations/
description: 了解如何使用 Aspose.PDF for Python via .NET 标记要进行编辑的文本、应用编辑注释，以及在 PDF 文件中编辑图像区域。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中使用安全注释对敏感 PDF 内容进行脱敏处理。
Abstract: 本文解释了如何使用 Aspose.PDF for Python via .NET 在 PDF 文档中处理安全注释。它涵盖了使用脱敏注释标记匹配的文本、永久应用脱敏以及基于检测到的图像放置矩形对选定的图像区域进行脱敏。
---

本文展示了如何在 PDF 文档中使用 Aspose.PDF for Python via .NET 的安全注释。

示例脚本演示了三种常见的编辑工作流：

- 使用编辑注释标记文本片段
- 永久应用现有的遮蔽注释
- 在页面上遮蔽检测到的图像区域

## 标记文本涂黑

此工作流在文档中搜索匹配的文本，并在每个匹配项上放置编辑注释。它不会立即删除内容；仅标记文本以供以后进行编辑。

### 打开 PDF 并搜索目标文本

创建一个 `TextFragmentAbsorber` 针对搜索词，在扫描所有页面之前启用常规文本搜索选项。

```python
document = ap.Document(infile)
text_fragment_absorber = ap.text.TextFragmentAbsorber(search_term)

text_search_options = ap.text.TextSearchOptions(True)
text_fragment_absorber.text_search_options = text_search_options
document.pages.accept(text_fragment_absorber)
```

### 为每个匹配项创建涂黑注释

对于每个匹配的文本片段，创建一个 `RedactionAnnotation` 使用片段矩形并配置其视觉外观。

```python
for text_fragment in text_fragment_absorber.text_fragments:
    page = text_fragment.page
    annotation_rectangle = text_fragment.rectangle
    redaction_annotation = ap.annotations.RedactionAnnotation(
        page, annotation_rectangle
    )
    redaction_annotation.fill_color = ap.Color.gray
    redaction_annotation.border_color = ap.Color.red
    redaction_annotation.color = ap.Color.white
    redaction_annotation.overlay_text = "REDACTED"
    redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
    redaction_annotation.repeat = True
    page.annotations.add(redaction_annotation, True)
```

### 保存标记的 PDF

```python
document.save(outfile)
```

### 完整示例

```python
def mark_text_redaction(infile, outfile, search_term):
    document = ap.Document(infile)
    text_fragment_absorber = ap.text.TextFragmentAbsorber(search_term)

    text_search_options = ap.text.TextSearchOptions(True)
    text_fragment_absorber.text_search_options = text_search_options
    document.pages.accept(text_fragment_absorber)

    for text_fragment in text_fragment_absorber.text_fragments:
        page = text_fragment.page
        annotation_rectangle = text_fragment.rectangle
        redaction_annotation = ap.annotations.RedactionAnnotation(
            page, annotation_rectangle
        )
        redaction_annotation.fill_color = ap.Color.gray
        redaction_annotation.border_color = ap.Color.red
        redaction_annotation.color = ap.Color.white
        redaction_annotation.overlay_text = "REDACTED"
        redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
        redaction_annotation.repeat = True
        page.annotations.add(redaction_annotation, True)

    document.save(outfile)
```



## 应用遮蔽

在添加了编辑遮盖注释后，此工作流会在第一页永久应用它们。应用后，原始内容将从文档输出中删除。

### 加载 PDF 并收集编辑注释

```python
document = ap.Document(infile)
redaction_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.REDACTION
]
```

### 应用每个编辑注释

该示例检查每个注释都可以被视为 a `RedactionAnnotation` 调用之前 `redact()`.

```python
for redaction_annotation in redaction_annotations:
    if is_assignable(redaction_annotation, ap.annotations.RedactionAnnotation):
        cast(ap.annotations.RedactionAnnotation, redaction_annotation).redact()
```

### 保存已遮蔽的 PDF

```python
document.save(outfile)
```

### 完整示例

```python
def apply_redaction(infile, outfile):
    document = ap.Document(infile)
    redaction_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.REDACTION
    ]

    for redaction_annotation in redaction_annotations:
        if is_assignable(redaction_annotation, ap.annotations.RedactionAnnotation):
            cast(ap.annotations.RedactionAnnotation, redaction_annotation).redact()

    document.save(outfile)
```



## 编辑区域

此示例对检测到的图像区域进行遮蔽，而不是对文本进行遮蔽。它扫描页面中的图像放置位置，选择一个放置矩形，并在该区域上添加遮蔽注释。

### 打开 PDF 并检测图像放置

使用 `ImagePlacementAbsorber` 在首页查找图像位置。

```python
document = ap.Document(infile)

image_placement_absorber = ap.ImagePlacementAbsorber()
page = document.pages[1]
page.accept(image_placement_absorber)
```

### 为所选图像区域创建遮蔽注释

该示例使用检测到的第三个图像放置，并应用与文本标记示例中相同的遮蔽样式。

```python
target_rect = image_placement_absorber.image_placements[2].rectangle
redaction_annotation = ap.annotations.RedactionAnnotation(page, target_rect)
redaction_annotation.fill_color = ap.Color.gray
redaction_annotation.border_color = ap.Color.red
redaction_annotation.color = ap.Color.white
redaction_annotation.overlay_text = "REDACTED"
redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
redaction_annotation.repeat = True
```

### 添加注释并保存 PDF

```python
page.annotations.add(redaction_annotation, True)
document.save(outfile)
```

### 完整示例

```python
def redact_area(infile, outfile):
    document = ap.Document(infile)

    image_placement_absorber = ap.ImagePlacementAbsorber()
    page = document.pages[1]
    page.accept(image_placement_absorber)

    target_rect = image_placement_absorber.image_placements[2].rectangle
    redaction_annotation = ap.annotations.RedactionAnnotation(page, target_rect)
    redaction_annotation.fill_color = ap.Color.gray
    redaction_annotation.border_color = ap.Color.red
    redaction_annotation.color = ap.Color.white
    redaction_annotation.overlay_text = "REDACTED"
    redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
    redaction_annotation.repeat = True

    page.annotations.add(redaction_annotation, True)
    document.save(outfile)
```

## 相关主题

- [导入和导出注释](/python-net/import-export-annotations/)
- [交互式注释](/python-net/interactive-annotations/)
- [标记注释](/python-net/markup-annotations/)
- [媒体注释](/python-net/media-annotations/)
- [形状注释](/python-net/shape-annotations/)
- [基于文本的注释](/python-net/text-based-annotations/)
- [水印注释](/python-net/watermark-annotations/)
