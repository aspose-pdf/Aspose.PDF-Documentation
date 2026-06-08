---
title: 使用 Python 的基于文本的注释
linktitle: 文本注释
type: docs
weight: 10
url: /zh/python-net/text-based-annotations/
description: 了解如何使用 Aspose.PDF for Python via .NET 在 PDF 文档中添加、检查和删除自由文本、高亮、下划线、波浪线和删除线注释。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中处理文本和文本标记的 PDF 注释。
Abstract: 本文说明了如何使用 Aspose.PDF for Python via .NET 在 PDF 文档中创建、读取和删除基于文本的注释。它涵盖了自由文本注释和文本标记注释，例如高亮、下划线、波浪线和删除线，并包括诸如扁平化、四点坐标和提取标记文本等高级下划线工作流。
---

本文展示了如何在 PDF 文档中使用 Aspose.PDF for Python via .NET 处理基于文本的批注。

示例脚本演示了多个文本批注工作流：

- 自由文本注释
- 高亮注释
- 下划线注释
- 波浪线批注
- 删除线批注

## 自由文本注释

### 添加自由文本批注 

自由文本注释允许您直接在 PDF 页面上放置可见的文字评论。本示例向首页添加了一个简单的自由文本注释。

#### 打开源 PDF

```python
document = ap.Document(infile)
```

#### 创建并配置自由文本注释

```python
free_text_annotation = ap.annotations.FreeTextAnnotation(
    document.pages[1],
    ap.Rectangle(299, 713, 308, 720, True),
    ap.annotations.DefaultAppearance(),
)
free_text_annotation.title = "Aspose User"
free_text_annotation.color = ap.Color.light_green
```

#### 添加注释并保存 PDF

```python
document.pages[1].annotations.append(free_text_annotation)
document.save(outfile)
```

#### 完整示例

```python
def free_text_annotation_add(infile, outfile):
    document = ap.Document(infile)

    free_text_annotation = ap.annotations.FreeTextAnnotation(
        document.pages[1],
        ap.Rectangle(299, 713, 308, 720, True),
        ap.annotations.DefaultAppearance(),
    )
    free_text_annotation.title = "Aspose User"
    free_text_annotation.color = ap.Color.light_green

    document.pages[1].annotations.append(free_text_annotation)
    document.save(outfile)
```

### 获取自由文本批注 

要检查自由文本注释，请按以下方式过滤第一页注释 `FREE_TEXT` 键入并打印每个注释矩形。

#### 加载文档并收集自由文本批注

```python
document = ap.Document(infile)
free_text_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.FREE_TEXT
]
```

#### 打印注释矩形

```python
for annotation in free_text_annotations:
    print(annotation.rect)
```

#### 完整示例

```python
def free_text_annotation_get(infile, outfile):
    document = ap.Document(infile)
    free_text_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.FREE_TEXT
    ]

    for annotation in free_text_annotations:
        print(annotation.rect)
```

### 删除自由文本注释 

此工作流从第一页中移除所有自由文本批注，并保存更新后的 PDF。

#### 查找并删除自由文本注释

```python
document = ap.Document(infile)
free_text_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.FREE_TEXT
]

for annotation in free_text_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### 完整示例

```python
def free_text_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    free_text_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.FREE_TEXT
    ]

    for annotation in free_text_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```


## 文本标记注释

### 高亮批注

#### 添加文本高亮

高亮注释在不更改底层内容的情况下强调文档的部分内容。此示例向首页添加了一个高亮注释。

```python
document = ap.Document(infile)

highlight_annotation = ap.annotations.HighlightAnnotation(
    document.pages[1],
    ap.Rectangle(300, 750, 320, 770, True),
)

document.pages[1].annotations.append(highlight_annotation)
document.save(outfile)
```

```python
def text_highlight_annotation_add(infile, outfile):
    document = ap.Document(infile)

    highlight_annotation = ap.annotations.HighlightAnnotation(
        document.pages[1],
        ap.Rectangle(300, 750, 320, 770, True),
    )

    document.pages[1].annotations.append(highlight_annotation)
    document.save(outfile)
```

#### 获取文本高亮

要检查高亮注释，请按以下方式过滤页面注释 `HIGHLIGHT` 键入并打印它们的矩形。

```python
document = ap.Document(infile)
highlight_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT
]

for annotation in highlight_annotations:
    print(annotation.rect)
```

```python
def text_highlight_annotation_get(infile, outfile):
    document = ap.Document(infile)
    highlight_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT
    ]

    for annotation in highlight_annotations:
        print(annotation.rect)
```

#### 删除文本高亮

此工作流会从第一页中移除所有高亮批注，并保存输出的 PDF。

```python
document = ap.Document(infile)
highlight_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT
]

for annotation in highlight_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

```python
def text_highlight_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    highlight_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.HIGHLIGHT
    ]

    for annotation in highlight_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```


### 下划线注释

#### 添加文本下划线批注

下划线注释使用可见的下划线标记文本。此示例添加了一个基本的下划线注释，并设置了其元数据和颜色。

```python
document = ap.Document(infile)

underline_annotation = ap.annotations.UnderlineAnnotation(
    document.pages[1],
    ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
)
underline_annotation.title = "Aspose User"
underline_annotation.subject = "Inserted Underline 1"
underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
underline_annotation.color = ap.Color.blue

document.pages[1].annotations.append(underline_annotation)
document.save(outfile)
```

```python
def text_underline_annotation_add(infile, outfile):
    document = ap.Document(infile)

    underline_annotation = ap.annotations.UnderlineAnnotation(
        document.pages[1],
        ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
    )
    underline_annotation.title = "Aspose User"
    underline_annotation.subject = "Inserted Underline 1"
    underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    underline_annotation.color = ap.Color.blue

    document.pages[1].annotations.append(underline_annotation)
    document.save(outfile)
```

#### 添加文本下划线批注并展平 

如果您希望下划线成为页面内容的一部分，而不是保持为交互式注释，您可以在添加后将其扁平化。

```python
document = ap.Document(infile)

underline_annotation = ap.annotations.UnderlineAnnotation(
    document.pages[1],
    ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
)
underline_annotation.title = "Aspose User"
underline_annotation.subject = "Inserted Underline to Flatten"
underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
underline_annotation.color = ap.Color.blue

document.pages[1].annotations.append(underline_annotation)
underline_annotation.flatten()

document.save(outfile)
```

```python
def text_underline_flatten_add(infile, outfile):
    document = ap.Document(infile)

    underline_annotation = ap.annotations.UnderlineAnnotation(
        document.pages[1],
        ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
    )
    underline_annotation.title = "Aspose User"
    underline_annotation.subject = "Inserted Underline to Flatten"
    underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    underline_annotation.color = ap.Color.blue

    document.pages[1].annotations.append(underline_annotation)
    underline_annotation.flatten()

    document.save(outfile)
```

#### 使用四点添加文本下划线注释

四点坐标让您能够为下划线注释定义精确的标记区域。当您需要比简单矩形更精细的控制时，这非常有用。

```python
document = ap.Document(infile)
rect = ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)

underline_annotation = ap.annotations.UnderlineAnnotation(document.pages[1], rect)
underline_annotation.title = "Aspose User"
underline_annotation.subject = "Inserted Underline with Quad Points"
underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
underline_annotation.color = ap.Color.blue
underline_annotation.quad_points = [
    ap.Point(rect.llx, rect.lly),
    ap.Point(rect.urx, rect.lly),
    ap.Point(rect.urx, rect.ury),
    ap.Point(rect.llx, rect.ury),
]

document.pages[1].annotations.append(underline_annotation)
document.save(outfile)
```

```python
def text_underline_with_quad_points_add(infile, outfile):
    document = ap.Document(infile)
    rect = ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)

    underline_annotation = ap.annotations.UnderlineAnnotation(document.pages[1], rect)
    underline_annotation.title = "Aspose User"
    underline_annotation.subject = "Inserted Underline with Quad Points"
    underline_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    underline_annotation.color = ap.Color.blue
    underline_annotation.quad_points = [
        ap.Point(rect.llx, rect.lly),
        ap.Point(rect.urx, rect.lly),
        ap.Point(rect.urx, rect.ury),
        ap.Point(rect.llx, rect.ury),
    ]

    document.pages[1].annotations.append(underline_annotation)
    document.save(outfile)
```

#### 删除文本下划线注释

此工作流会删除首页上的所有下划线注释，并保存更新后的文档。

```python
document = ap.Document(infile)
underline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
]

for annotation in underline_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

```python
def text_underline_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    underline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for annotation in underline_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

#### 按标题删除文本下划线注释

此工作流展示了在检查其标题后，如何有选择地删除下划线注释。

```python
document = ap.Document(infile)

underline_annotations = [
    cast(ap.annotations.UnderlineAnnotation, annotation)
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
]

for annotation in underline_annotations:
    if annotation.title.startswith("a"):
        document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

```python
def text_underline_by_title_delete(infile, outfile):
    document = ap.Document(infile)

    underline_annotations = [
        cast(ap.annotations.UnderlineAnnotation, annotation)
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for annotation in underline_annotations:
        if annotation.title.startswith("a"):
            document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

#### 获取文本下划线注释

要检查下划线注释，请按以下方式过滤第一页的注释 `UNDERLINE` 键入并打印每个矩形。

```python
document = ap.Document(infile)
underline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
]

for annotation in underline_annotations:
    print(annotation.rect)
```

```python
def text_underline_annotation_get(infile, outfile):
    document = ap.Document(infile)
    underline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for annotation in underline_annotations:
        print(annotation.rect)
```

#### 获取带下划线注释标记的文本

此工作流将每个下划线批注转换为 `UnderlineAnnotation` 对象并提取标记的文本。

```python
document = ap.Document(infile)

underline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
]

for annotation in underline_annotations:
    ua = cast(ap.annotations.UnderlineAnnotation, annotation)
    print(f"Marked text: {ua.get_marked_text()}")
```

```python
def text_underline_marked_text_get(infile, outfile):
    document = ap.Document(infile)

    underline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for annotation in underline_annotations:
        ua = cast(ap.annotations.UnderlineAnnotation, annotation)
        print(f"Marked text: {ua.get_marked_text()}")
```

#### 获取已标记片段的文本下划线注释

如果您需要单独获取每个标记的片段，可以遍历返回的集合 `get_marked_text_fragments()`.

```python
document = ap.Document(infile)

underline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
]

for annotation in underline_annotations:
    ua = cast(ap.annotations.UnderlineAnnotation, annotation)
    for fragment in ua.get_marked_text_fragments():
        print(f"Fragment text: {fragment.text}")
```

```python
def text_underline_marked_fragments_get(infile, outfile):
    document = ap.Document(infile)

    underline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.UNDERLINE
    ]

    for annotation in underline_annotations:
        ua = cast(ap.annotations.UnderlineAnnotation, annotation)
        for fragment in ua.get_marked_text_fragments():
            print(f"Fragment text: {fragment.text}")
```


### 波浪线注释

#### 添加波浪线批注

波浪线批注常用于标记文本中的拼写、语法或需要注意的区域。此示例在首页添加了波浪线批注。

```python
document = ap.Document(infile)
page = document.pages[1]

squiggly_annotation = ap.annotations.SquigglyAnnotation(
    page,
    ap.Rectangle(67, 317, 261, 459, True),
)
squiggly_annotation.title = "John Smith"
squiggly_annotation.color = ap.Color.blue

page.annotations.append(squiggly_annotation)
document.save(outfile)
```

```python
def text_squiggly_annotation_add(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    squiggly_annotation = ap.annotations.SquigglyAnnotation(
        page,
        ap.Rectangle(67, 317, 261, 459, True),
    )
    squiggly_annotation.title = "John Smith"
    squiggly_annotation.color = ap.Color.blue

    page.annotations.append(squiggly_annotation)
    document.save(outfile)
```

#### 获取波浪线批注

要检查波浪线注释，请通过以下方式过滤页面注释 `SQUIGGLY` 键入并打印它们的矩形。

```python
document = ap.Document(infile)
squiggly_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.SQUIGGLY
]

for annotation in squiggly_annotations:
    print(annotation.rect)
```

```python
def text_squiggly_annotation_get(infile, outfile):
    document = ap.Document(infile)
    squiggly_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.SQUIGGLY
    ]

    for annotation in squiggly_annotations:
        print(annotation.rect)
```

#### 删除波浪线批注

此工作流会从首页移除所有波浪线批注并保存结果。

```python
document = ap.Document(infile)
squiggly_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.SQUIGGLY
]

for annotation in squiggly_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

```python
def text_squiggly_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    squiggly_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.SQUIGGLY
    ]

    for annotation in squiggly_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```


### 删除线注释

#### 添加文本删除线批注

删除线注释标记应视为已删除或划掉的文本。此示例添加了一个删除线注释，并设置其元数据和颜色。

```python
document = ap.Document(infile)

strikeout_annotation = ap.annotations.StrikeOutAnnotation(
    document.pages[1],
    ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
)
strikeout_annotation.title = "Aspose User"
strikeout_annotation.subject = "Inserted text 1"
strikeout_annotation.flags = ap.annotations.AnnotationFlags.PRINT
strikeout_annotation.color = ap.Color.blue

document.pages[1].annotations.append(strikeout_annotation)
document.save(outfile)
```

```python
def text_strikeout_annotation_add(infile, outfile):
    document = ap.Document(infile)

    strikeout_annotation = ap.annotations.StrikeOutAnnotation(
        document.pages[1],
        ap.Rectangle(299.988, 713.664, 308.708, 720.769, True),
    )
    strikeout_annotation.title = "Aspose User"
    strikeout_annotation.subject = "Inserted text 1"
    strikeout_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    strikeout_annotation.color = ap.Color.blue

    document.pages[1].annotations.append(strikeout_annotation)
    document.save(outfile)
```

#### 获取文本删除线批注

要检查删除线注释，请通过 `STRIKE_OUT` 键入并打印它们的矩形。

```python
document = ap.Document(infile)
strikeout_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
]

for annotation in strikeout_annotations:
    print(annotation.rect)
```

```python
def text_strikeout_annotation_get(infile, outfile):
    document = ap.Document(infile)
    strikeout_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
    ]

    for annotation in strikeout_annotations:
        print(annotation.rect)
```

#### 删除文本删除线注释

此工作流会从首页删除所有删线批注并保存更新后的文档。

```python
document = ap.Document(infile)
strikeout_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
]

for annotation in strikeout_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

```python
def text_strikeout_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    strikeout_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
    ]

    for annotation in strikeout_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

## 相关主题

- [导入和导出注释](/python-net/import-export-annotations/)
- [交互式注释](/python-net/interactive-annotations/)
- [标记注释](/python-net/markup-annotations/)
- [媒体注释](/python-net/media-annotations/)
- [安全注释](/python-net/security-annotations/)
- [形状注释](/python-net/shape-annotations/)
- [水印注释](/python-net/watermark-annotations/)
