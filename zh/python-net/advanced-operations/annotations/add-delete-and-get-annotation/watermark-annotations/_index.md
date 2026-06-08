---
title: 使用 Python 的水印注释
linktitle: 水印注释
type: docs
weight: 70
url: /zh/python-net/watermark-annotations/
description: 了解如何使用 Aspose.PDF for Python via .NET 在 PDF 文档中添加、检查和删除水印注释。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 处理 PDF 文件中的水印批注。
Abstract: 本文说明了如何使用 Aspose.PDF for Python via .NET 在 PDF 文档中创建、读取和删除水印批注。它涵盖了添加带自定义文字状态和不透明度的文字水印批注、检查已有的水印批注，以及从 PDF 页面删除水印批注。
---

本文展示了如何使用 Aspose.PDF for Python via .NET 在 PDF 文档中处理水印批注。

示例脚本演示了三种常见的工作流程：

- 添加水印注释
- 获取水印注释矩形
- 删除水印注释

## 添加水印注释

此示例在 PDF 文档的首页添加水印注释。水印使用文本状态来控制字体设置，并应用自定义不透明度以实现半透明外观。

### 打开 PDF 并获取目标页面

```python
document = ap.Document(infile)
page = document.pages[1]
```

### 创建水印注释

定义注释矩形并将其追加到页面注释集合中。

```python
watermark_annotation = ap.annotations.WatermarkAnnotation(
    page,
    ap.Rectangle(100, 100, 400, 200, True),
)

page.annotations.append(watermark_annotation)
```

### 配置文本外观

创建一个 `TextState` 用于控制文本颜色、字体大小和字体族的对象。

```python
text_state = ap.text.TextState()
text_state.foreground_color = ap.Color.blue
text_state.font_size = 25
text_state.font = ap.text.FontRepository.find_font("Arial")
```

### 设置不透明度和水印文本

示例使用 50% 不透明度，并将三行文本写入水印批注。

```python
watermark_annotation.opacity = 0.5
watermark_annotation.set_text_and_state(["HELLO", "Line 1", "Line 2"], text_state)
```

### 保存 PDF

```python
document.save(outfile)
```

### 完整示例

```python
def watermark_add(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    watermark_annotation = ap.annotations.WatermarkAnnotation(
        page,
        ap.Rectangle(100, 100, 400, 200, True),
    )

    page.annotations.append(watermark_annotation)

    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.blue
    text_state.font_size = 25
    text_state.font = ap.text.FontRepository.find_font("Arial")

    watermark_annotation.opacity = 0.5
    watermark_annotation.set_text_and_state(["HELLO", "Line 1", "Line 2"], text_state)

    document.save(outfile)
```

## 获取水印注释

要检查现有的水印注释，请通过以下方式过滤第一页的注释 `WATERMARK` 键入并打印它们的矩形。

### 加载文档并收集水印注释

```python
document = ap.Document(infile)
watermark_annotations = [
    a
    for a in document.pages[1].annotations
    if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
]
```

### 打印注释矩形

```python
for watermark_annotation in watermark_annotations:
    print(watermark_annotation.rect)
```

### 完整示例

```python
def watermark_get(infile, outfile):
    document = ap.Document(infile)
    watermark_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
    ]

    for watermark_annotation in watermark_annotations:
        print(watermark_annotation.rect)
```

## 删除水印批注

此工作流会从第一页删除所有水印注释并保存更新后的 PDF。

### 查找要删除的水印批注

```python
document = ap.Document(infile)
watermark_annotations = [
    a
    for a in document.pages[1].annotations
    if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
]
```

### 删除注释并保存 PDF

```python
for watermark_annotation in watermark_annotations:
    document.pages[1].annotations.delete(watermark_annotation)

document.save(outfile)
```

### 完整示例

```python
def watermark_delete(infile, outfile):
    document = ap.Document(infile)
    watermark_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
    ]

    for watermark_annotation in watermark_annotations:
        document.pages[1].annotations.delete(watermark_annotation)

    document.save(outfile)
```

## 相关主题

- [导入和导出注释](/python-net/import-export-annotations/)
- [交互式注释](/python-net/interactive-annotations/)
- [标记注释](/python-net/markup-annotations/)
- [媒体注释](/python-net/media-annotations/)
- [安全注释](/python-net/security-annotations/)
- [形状注释](/python-net/shape-annotations/)
- [基于文本的注释](/python-net/text-based-annotations/)
