---
title: 在 Python 中使用 PDF 操作
linktitle: 操作
type: docs
weight: 20
url: /zh/python-net/actions/
description: 了解如何使用 Python 在 PDF 文件中添加、更新和删除文档、页面和表单操作。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: 在 Python 中向 PDF 文件添加文档、页面和表单操作。
Abstract: 本文探讨了如何使用 Aspose.PDF 库在 PDF 文档中处理动作，涵盖文档级、页面级和表单级的交互。PDF 动作是预定义或可自定义的触发器，响应用户事件，实现导航、JavaScript 执行、多媒体播放、表单提交等功能。指南演示了如何添加、定制和移除动作，例如在文档事件中打开 URL、创建特定页面的导航或缩放效果、添加用于打印和导航的交互按钮、动态隐藏表单元素以及将表单数据提交到 Web 端点。通过详细的 Python 代码示例，读者可以学习提升 PDF 的交互性、简化工作流，并将 PDF 与外部系统集成，同时了解查看器兼容性注意事项。
---

PDF 中的操作是预定义的任务，当用户交互或文档事件触发时执行。它们可用于：

- 导航到特定页面或外部文件
- 打开网页链接
- 播放多媒体内容
- 运行 JavaScript
- 提交或重置表单
- 显示/隐藏字段
- 更改缩放级别或视图模式

几乎所有操作都使用内置参数，但有一些可以自定义。例如 - JavaScript 操作。

## 添加 PDF 启动操作

使用 Python 和 Aspose.PDF 向 PDF 文档添加基于 JavaScript 的启动操作。它将操作分配给关键文档事件，如打开、保存和打印，允许在受支持的 PDF 查看器中这些事件发生时自动启动 URL。

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_launch_actions(infile, outfile):
    """Add JavaScript launch actions for document events.

    Adds JavaScript actions that launch URLs when specific document events occur:
    - On document open: launches http://localhost:3000/open
    - Before saving: launches http://localhost:3000/save
    - Before printing: launches http://localhost:3000/print

    Args:
        infile (str): Path to the input PDF file.
        outfile (str): Path to save the output PDF with document actions.

    Returns:
        None

    Example:
        >>> add_launch_actions("sample_data/input/add_launch_actions_in.pdf", "sample_data/output/add_launch_actions_out.pdf")

    Notes:
        - Uses `ap.annotations.JavascriptAction` with `app.launchURL()`.
        - URLs are opened in the default browser depending on viewer support.
    """

    document = ap.Document(infile)

    # Add JavaScript actions for document events
    document.open_action = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/open');"
    )
    document.actions.before_saving = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/save');"
    )
    document.actions.before_printing = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/print');"
    )

    document.save(outfile)
```

## 从 PDF 文档中删除操作

要清除（或移除）操作，只需将处理程序设置为 `None`.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def remove_page_actions(infile, outfile):
    document = ap.Document(infile)

    if len(document.pages) < 3:
        print("Error: The document does not have at least 3 pages.")
        return

    page = document.pages[3]
    page.actions.remove_actions()

    document.save(outfile)
```

## 在 PDF 文档的页面中添加操作

类似的触发器已为页面提供： `on_open`, `on_close`.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_page_actions(infile, outfile):
    document = ap.Document(infile)

    if len(document.pages) < 3:
        print("Error: The document does not have at least 3 pages.")
        return

    page = document.pages[3]

    # Add GoTo action on page open - navigate to top of page
    action = ap.annotations.GoToAction(page)
    action.destination = ap.annotations.XYZExplicitDestination(
        page, 0, page.page_info.height, 1
    )
    page.actions.on_open = action

    # Add JavaScript action on page close
    page.actions.on_close = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/page/3');"
    )

    document.save(outfile)
```

## AcroForms 中的操作

### 使用导航操作

PDF 标准提供了一组特定的命名操作。此类操作的含义由其名称决定。
在下面的代码中，我们将使用动作进行导航。

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_navigation_buttons(infile, outfile):
    # Configuration for each navigation button
    button_config = [
        ("First Page", 10.0, PredefinedAction.FIRST_PAGE, lambda p, t: p == 1),
        ("Previous Page", 120.0, PredefinedAction.PREV_PAGE, lambda p, t: p == 1),
        ("Next Page", 230.0, PredefinedAction.NEXT_PAGE, lambda p, t: p == t),
        ("Last Page", 340.0, PredefinedAction.LAST_PAGE, lambda p, t: p == t),
    ]

    document = ap.Document(infile)
    total_pages = len(document.pages)

    # Add navigation buttons to each page
    for page in document.pages:
        for name, x_pos, action, is_readonly_fn in button_config:
            # Create button rectangle
            rect = Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
            button = ButtonField(page, rect)
            button.partial_name = name
            button.value = name
            button.characteristics.border = ap.Color.red.to_rgb()
            button.characteristics.background = ap.Color.orange.to_rgb()
            # Disable button when not applicable
            button.read_only = is_readonly_fn(page.number, total_pages)
            button.actions.on_release_mouse_btn = NamedAction(action)
            document.form.add(button)

    document.save(outfile)
```

此代码为 PDF 文档的每一页添加导航按钮，使用户更容易在页面之间移动。它首先使用辅助方法确定输入和输出文件的完整文件路径。button_config 列表定义了四种导航按钮——“首页”、“上一页”、“下一页”和“末页”——以及它们的水平位置、预定义的导航操作以及一个 lambda 函数，用于确定每个按钮在给定页面上是否应为只读（例如，“首页”和“上一页”按钮在第一页上为只读）。

代码随后加载 PDF 并遍历每一页。对于每一页，它会循环遍历按钮配置，为每个按钮创建一个矩形区域，并在该位置实例化一个 ButtonField。为每个按钮分配一个名称，其只读状态根据当前页设置，并将其点击操作指派给相应的导航操作。随后将该按钮添加到 PDF 表单字段中。

在所有按钮添加到所有页面后，修改后的文档被保存。如果在此过程中出现任何错误，它们会被捕获并打印出来。此方法确保每页都有一致的导航控件集合，提升了多页 PDF 的可用性。一个细节是使用 is_readonly_fn lambda 在按钮不合适时（例如在最后一页时禁用"Next Page"），这有助于防止用户产生困惑。

### 使用打印操作

在使用 PDF 表单时，通常需要打印此类 PDF 文档。此操作可以使用 PDF 阅读器来完成，但有时直接在文档中使用特殊按钮会更方便。

事实上，这又是一个如何使用命名动作的示例。我们将使用 `PredefinedAction.FILE_PRINT` （模拟使用 File->Print 菜单项），但您也可以使用 `PredefinedAction.PRINT` 或 `PredefinedAction.PRINT_DIALOG`，取决于您自己的目的。

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_named_action_print(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    # Create print button with specific dimensions and position
    rect = Rectangle(10, 10, 100, 40, True)
    print_button = ButtonField(page, rect)
    print_button.partial_name = "printButton"
    print_button.value = "Print"
    print_button.actions.on_release_mouse_btn = NamedAction(PredefinedAction.FILE_PRINT)

    # Add border for better visibility
    border = ap.annotations.Border(print_button)
    border.width = 1
    print_button.border = border

    # Add button to the form on page 1
    document.form.add(print_button, 1)
    document.save(outfile)
```

此代码片段演示了如何向 PDF 文档的首页添加一个 “Print” 按钮。它首先从指定的输入文件路径加载 PDF，并选择首页 (document.pages[1])。

在页面上为按钮的位置和大小定义了一个矩形区域。随后在该位置创建了一个 ButtonField，命名为 "printButton"，并将其显示值设置为 "Print"。该按钮被配置为在点击时（具体而言，在鼠标按钮释放时），触发预定义的 "Print File" 操作，促使 PDF 查看器打开打印对话框。

为了增强按钮的外观，创建了一个边框并分配给按钮，将其宽度设置为 1 个单位。然后将按钮添加到第一页的 PDF 表单字段中。最后，将修改后的文档保存到输出文件路径。此方法为用户提供了一种直接在 PDF 中打印文档的便捷方式。请注意，此功能的有效性取决于 PDF 查看器对交互式表单字段和预定义操作的支持。

### 使用隐藏操作

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_named_action_hide(infile, outfile):
    document = ap.Document(infile)
    # Collect all checkbox fields in the document
    checkboxes = [
        field for field in document.form if is_assignable(field, CheckboxField)
    ]

    # Create the hide button
    rect = Rectangle(10, 410, 140, 440, True)
    hide_button = ButtonField(document.pages[1], rect)
    hide_button.partial_name = "HideButton"
    hide_button.value = "Hide Checkboxes"

    # Add HideAction to button - will hide all checkboxes when clicked
    hide_button.actions.on_release_mouse_btn = HideAction(checkboxes, True)

    # Add button to the form on page 1
    document.form.add(hide_button, 1)

    # Save the modified PDF
    document.save(outfile)
```

此代码片段在 PDF 的首页添加了一个按钮，单击后可隐藏文档中的所有复选框字段。它首先使用辅助方法解析完整的输入和输出文件路径。加载 PDF 后，通过筛选表单字段中该类型的实例来收集所有复选框字段。 `ap.CheckboxField`.

在页面顶部附近定义了一个矩形区域，用于新按钮的位置。在此位置创建了一个 ButtonField，命名为 "HideButton,"，并标记为 "Hide Checkboxes."。按钮被配置为在点击（鼠标按钮释放时）时触发 HideAction，隐藏所有已收集的复选框。

然后将按钮添加到第一页的表单字段中，并将修改后的 PDF 保存到输出文件。如果此过程出现任何错误，它们会被捕获并打印。此功能为用户提供了一种快速隐藏 PDF 中所有复选框的方法，这对于自定义文档的外观或工作流非常有用。

### 应用提交操作

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_submit_action(infile, outfile):
    document = ap.Document(infile)

    # Create the submit action
    submit_action = SubmitFormAction()
    submit_action.url = ap.FileSpecification("http://localhost:3000/submit")
    submit_action.flags = (
        SubmitFormAction.EXPORT_FORMAT | SubmitFormAction.SUBMIT_COORDINATES
    )

    # Create the submit button
    rect = Rectangle(10, 10, 100, 40, True)
    submit_button = ButtonField(document.pages[1], rect)
    submit_button.partial_name = "SubmitButton"
    submit_button.value = "Submit"
    submit_button.actions.on_release_mouse_btn = submit_action

    # Add the button to the form on page 1
    document.form.add(submit_button, 1)

    # Save the document
    document.save(outfile)
```

此函数在 PDF 表单的首页添加一个“Submit”按钮，允许用户将表单数据提交到指定的网络端点。它首先构建输入和输出 PDF 文件的完整路径，然后使用 Aspose.PDF 库加载输入 PDF。

A `SubmitFormAction` 已创建以定义按钮被点击时的行为。操作的 URL 是使用 a 设置的 `FileSpecification` 指向 http://localhost:3000/submit, 这意味着表单数据将发送到此 URL。flags 属性组合 `EXPORT_FORMAT` 和 `SUBMIT_COORDINATES`，确保表单数据以标准格式导出，并且在提交中包含按钮点击的坐标。

在页面上为按钮的位置和大小定义了一个矩形区域。在第一页的该位置创建了一个 ButtonField，命名为 "SubmitButton"，其显示值设置为 "Submit"。提交操作被分配给按钮的鼠标释放事件，因此当用户点击按钮时会触发该操作。

最后，将按钮添加到首页的表单字段中，并将修改后的 PDF 保存到输出文件。如果在此过程中出现任何错误，会被捕获并打印。此方法为 PDF 用户提供了一种友好的方式，可将表单数据直接提交到服务器端点。

## 相关导航主题

- [使用 Python 在 PDF 中进行导航和交互](/pdf/zh/python-net/navigation-and-interaction/)
- [使用 Python 在 PDF 中处理书签](/pdf/zh/python-net/bookmarks/)
- [使用 Python 处理 PDF 中的链接](/pdf/zh/python-net/links/)
