---
title: 使用 Python 的交互式注释
linktitle: 交互式注释
type: docs
weight: 60
url: /zh/python-net/interactive-annotations/
description: 了解如何使用 Aspose.PDF for Python via .NET 在 PDF 文档中添加、读取和删除链接注释，以及创建导航和打印按钮。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中处理交互式 PDF 注释和按钮。
Abstract: 本文解释了如何使用 Aspose.PDF for Python via .NET 在 PDF 文件中处理交互式注释。它涵盖了添加链接注释、读取现有链接区域、删除链接注释、创建页面导航按钮以及向 PDF 文档添加打印按钮。
---

本文展示了如何使用 Aspose.PDF for Python via .NET 在 PDF 文档中处理交互式批注。

示例脚本演示了几种常见的工作流程：

- 在现有文本上添加链接注释
- 获取页面中的链接注释矩形
- 删除链接注释
- 创建导航按钮
- 创建一个打印按钮

## 链接注释

### 添加链接注释

此示例在第一页中搜索文本片段 `"file"` 并在匹配的文本区域上放置一个可点击的链接注释。当用户点击该注释时，PDF 将打开指定的网页地址。

#### 加载文档并查找目标文本

创建一个 `Document` 对象和使用 `TextFragmentAbsorber` 搜索将成为交互式的文本。

```python
document = ap.Document(infile)
text_fragment_absorber = ap.text.TextFragmentAbsorber("file")

document.pages[1].accept(text_fragment_absorber)
phone_number_fragment = text_fragment_absorber.text_fragments[1]
```

#### 创建链接注释

构建一个 `LinkAnnotation` 使用匹配文本片段的矩形并为其分配一个 URI 操作。

```python
link_annotation = ap.annotations.LinkAnnotation(
    document.pages[1], phone_number_fragment.rectangle
)
link_annotation.action = ap.annotations.GoToURIAction("https://www.aspose.com")
```

#### 添加注释并保存 PDF

将注释附加到页面并保存更新后的文件。

```python
document.pages[1].annotations.append(link_annotation)
document.save(outfile)
```

#### 完整示例

```python
def link_add(infile, outfile):
    document = ap.Document(infile)
    text_fragment_absorber = ap.text.TextFragmentAbsorber("file")

    document.pages[1].accept(text_fragment_absorber)
    phone_number_fragment = text_fragment_absorber.text_fragments[1]

    link_annotation = ap.annotations.LinkAnnotation(
        document.pages[1], phone_number_fragment.rectangle
    )
    link_annotation.action = ap.annotations.GoToURIAction("https://www.aspose.com")

    document.pages[1].annotations.append(link_annotation)
    document.save(outfile)
```

### 获取链接注释

要检查现有的交互式链接，请过滤第一页的注释集合，并仅保留其类型为的项目 `LINK`. 示例随后为每个匹配的注释打印矩形。

#### 加载 PDF 并收集链接注释

```python
document = ap.Document(infile)
link_annotations = [
    a
    for a in document.pages[1].annotations
    if (a.annotation_type == ap.annotations.AnnotationType.LINK)
]
```

#### 读取注释矩形

遍历过滤后的注释并打印每个链接区域的坐标。

```python
for link_annotation in link_annotations:
    print(link_annotation.rect)
```

#### 完整示例

```python
def link_get(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for link_annotation in link_annotations:
        print(link_annotation.rect)
```

### 删除链接注释

此工作流会删除第一页中的所有链接注释，并将清理后的 PDF 保存为新文件。

#### 查找要删除的链接注释

```python
document = ap.Document(infile)
link_annotations = [
    a
    for a in document.pages[1].annotations
    if (a.annotation_type == ap.annotations.AnnotationType.LINK)
]
```

#### 删除每个链接注释

```python
for link_annotation in link_annotations:
    document.pages[1].annotations.delete(link_annotation)
```

#### 保存已更新的文档

```python
document.save(outfile)
```

#### 完整示例

```python
def link_delete(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for link_annotation in link_annotations:
        document.pages[1].annotations.delete(link_annotation)

    document.save(outfile)
```

## 小部件注释

### 添加导航按钮

在多页 PDF 中，导航按钮非常有用，当您希望读者在页面之间切换而无需使用查看器界面时。本示例添加了 `Previous Page` 和 `Next Page` 按钮到每页。

#### 定义按钮设置

将按钮标题、位置和预定义操作存储在一个简单的配置列表中。

```python
button_config = [
    ("Previous Page", 120.0, ap.annotations.PredefinedAction.PREV_PAGE),
    ("Next Page", 230.0, ap.annotations.PredefinedAction.NEXT_PAGE),
]
```

#### 加载 PDF 并确保存在多个页面

该示例打开源文档并添加一页，以便导航操作至少有两个页面可供使用。

```python
document = ap.Document(infile)
document.pages.add()
```

#### 在每页上创建按钮

为每页创建一个 `ButtonField`，设置其文本和颜色，分配预定义的导航操作，并将其添加到表单。

```python
for page in document.pages:
    for name, x_pos, action in button_config:
        rect = ap.Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
        button = ap.forms.ButtonField(page, rect)
        button.partial_name = name
        button.value = name
        button.characteristics.border = ap.Color.red.to_rgb()
        button.characteristics.background = ap.Color.orange.to_rgb()
        button.actions.on_release_mouse_btn = ap.annotations.NamedAction(action)
        document.form.add(button)
```

#### 保存结果

```python
document.save(outfile)
```

#### 完整示例

```python
def navigation_buttons_add(infile, outfile):
    button_config = [
        ("Previous Page", 120.0, ap.annotations.PredefinedAction.PREV_PAGE),
        ("Next Page", 230.0, ap.annotations.PredefinedAction.NEXT_PAGE),
    ]

    document = ap.Document(infile)
    document.pages.add()

    for page in document.pages:
        for name, x_pos, action in button_config:
            rect = ap.Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
            button = ap.forms.ButtonField(page, rect)
            button.partial_name = name
            button.value = name
            button.characteristics.border = ap.Color.red.to_rgb()
            button.characteristics.background = ap.Color.orange.to_rgb()
            button.actions.on_release_mouse_btn = ap.annotations.NamedAction(action)
            document.form.add(button)

    document.save(outfile)
```

### 添加打印按钮

此示例创建一个新的一页 PDF，并在页面顶部附近放置一个打印按钮。单击该按钮将在兼容的 PDF 查看器中触发预定义的打印操作。

#### 创建一个新的 PDF 并添加页面

```python
document = ap.Document()
page = document.pages.add()
```

#### 创建并配置按钮

定义按钮矩形，创建 `ButtonField`，设置其标题，并附加打印操作。

```python
rect = ap.Rectangle(72, 748, 164, 768, True)

print_button = ap.forms.ButtonField(page, rect)
print_button.alternate_name = "Print current document"
print_button.color = ap.Color.black
print_button.partial_name = "printBtn1"
print_button.value = "Print Document"
print_button.actions.on_release_mouse_btn = ap.annotations.NamedAction(
    ap.annotations.PredefinedAction.FILE_PRINT
)
```

#### 设置边框和背景样式

该示例定义了实线边框并使用自定义颜色，使按钮在文档中可见。

```python
border = ap.annotations.Border(print_button)
border.style = ap.annotations.BorderStyle.SOLID
border.width = 2
print_button.border = border

print_button.characteristics.border = ap.Color.blue.to_rgb()
print_button.characteristics.background = ap.Color.light_blue.to_rgb()
```

#### 添加按钮并保存 PDF

```python
document.form.add(print_button)
document.save(outfile)
```

#### 完整示例

```python
def print_button_add(infile, outfile):
    document = ap.Document()
    page = document.pages.add()

    rect = ap.Rectangle(72, 748, 164, 768, True)

    print_button = ap.forms.ButtonField(page, rect)
    print_button.alternate_name = "Print current document"
    print_button.color = ap.Color.black
    print_button.partial_name = "printBtn1"
    print_button.value = "Print Document"
    print_button.actions.on_release_mouse_btn = ap.annotations.NamedAction(
        ap.annotations.PredefinedAction.FILE_PRINT
    )

    border = ap.annotations.Border(print_button)
    border.style = ap.annotations.BorderStyle.SOLID
    border.width = 2
    print_button.border = border

    print_button.characteristics.border = ap.Color.blue.to_rgb()
    print_button.characteristics.background = ap.Color.light_blue.to_rgb()

    document.form.add(print_button)
    document.save(outfile)
```

## 相关主题

- [导入和导出注释](/python-net/import-export-annotations/)
- [标记注释](/python-net/markup-annotations/)
- [媒体注释](/python-net/media-annotations/)
- [安全注释](/python-net/security-annotations/)
- [形状注释](/python-net/shape-annotations/)
- [基于文本的注释](/python-net/text-based-annotations/)
- [水印注释](/python-net/watermark-annotations/)
