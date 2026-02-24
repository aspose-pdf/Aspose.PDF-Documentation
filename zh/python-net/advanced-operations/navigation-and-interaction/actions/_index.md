---
title: 在 PDF 文档中处理操作
linktitle: 操作
type: docs
weight: 20
url: /zh/python-net/actions/
description: 探索如何在 Python 中使用 Aspose.PDF 提取和管理 PDF 元数据，如作者和标题。
lastmod: "2025-07-10"
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: 使用 Python 处理 PDF 文档中的操作
Abstract: 本文探讨了使用 Aspose.PDF 库在 PDF 文档中处理操作的方法，涵盖文档级、页面级和表单级交互。PDF 操作是预定义或可自定义的触发器，响应用户事件，实现导航、JavaScript 执行、多媒体播放、表单提交等功能。指南演示了如何添加、定制和移除操作，如在文档事件时打开 URL、创建页面特定的导航或缩放效果、添加用于打印和导航的交互按钮、动态隐藏表单元素以及将表单数据提交到网络端点。通过详细的 Python 代码示例，读者学习如何增强 PDF 的交互性、简化工作流程，并在了解查看器兼容性考虑的前提下，将 PDF 与外部系统集成。
---

PDF 中的操作是预定义的任务，由用户交互或文档事件触发。它们可以用于：

- 导航到特定页面或外部文件
- 打开网页链接
- 播放多媒体内容
- 运行 JavaScript
- 提交或重置表单
- 显示/隐藏字段
- 更改缩放级别或视图模式

几乎所有操作都使用内置参数，但也有一些可以自定义。例如 - JavaScript 操作。

## 文档级别操作

### 向 PDF 文档添加操作

PDF 文档支持多种文档级别的操作，包括在打开文档时或响应特定事件时运行的代码。使用 `open_action` 属性来处理打开时的操作；其他操作在 `actions` 集合中管理。

让我们考虑如何使用 `open_action`。

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

document = ap.Document(path_infile)
document.open_action = ap.annotations.JavascriptAction(
    "app.launchURL('http://localhost:3000/open');"
)
document.save(path_outfile)
```

在本例中，我们调用 `app` 对象的 `launchURL` 方法并打开网站（用于演示）。

其他操作可以以相同方式添加，只需进行少量更改：

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

document = ap.Document(path_infile)
document.actions.before_saving = ap.annotations.JavascriptAction(
    "app.launchURL('http://localhost:3000/save');"
)
document.actions.before_printing = ap.annotations.JavascriptAction(
    "app.launchURL('http://localhost:3000/print');"
)
```

您可以为以下事件添加操作： `before_saving`、`before_printing`、`before_closing`、`after_saving`、`after_printing`。

此代码片段演示了如何将 JavaScript 操作附加到 PDF 中的各种文档级别事件。首先，它从指定的输入文件路径加载现有的 PDF 文档。`document.open_action` 属性被设置为在文档打开时启动 URL 的 JavaScript 操作，提示 PDF 查看器在用户的浏览器中打开 `http://localhost:3000/open`。

接下来，另外两个 JavaScript 操作被分配给文档的 `before_saving` 和 `before_printing` 事件。这些操作会在用户尝试保存或打印文档时触发，分别在浏览器中打开不同的 URL（`/save` 或 `/print`）。这对于跟踪用户交互或与基于 Web 的工作流集成非常有用。

### 从 PDF 文档中移除操作

要清除（或移除）操作，只需将处理程序设置为 `None`。

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

document = ap.Document(path_infile)
document.open_action = None
document.actions.before_saving = None
document.actions.before_printing = None
document.save(path_outfile)
```

## 页面级别操作

### 向 PDF 文档的页面添加操作

页面也提供了类似的触发器：`on_open`、`on_close`。

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...

def add_page_actions(self, infile, outfile):
    """
    Add actions to the third page of the PDF.

    Adds two actions to page 3:
    - On page open: Navigate to the top of the page with specific zoom
    - On page close: Launch a URL with page-specific information

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Raises:
        ValueError: If document has fewer than 3 pages

    Example:
        >>> actions.add_page_actions("multipage.pdf", "page_actions.pdf")
    """
    path_infile, path_outfile = self._get_file_paths(infile, outfile)

    document = ap.Document(path_infile)

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

    document.save(path_outfile)

```

我们向此页面添加了两个操作。首先，它创建一个在页面打开时触发的 "GoTo" 操作。该操作使用显式目标跳转到页面左上角的特定缩放级别。其次，它附加一个在页面关闭时运行的 JavaScript 操作，指示 PDF 查看器在浏览器中打开特定 URL。最后，修改后的文档保存到指定的输出路径。

需要注意的一个细微点是页面索引，因为使用错误的索引可能导致意外行为或错误。此外，PDF 中的 JavaScript 操作可能并非所有 PDF 查看器都支持，因此此功能在某些环境下可能无法使用。

### 从 PDF 页面中移除操作

使用 `remove_actions` 可以移除页面上的操作。

```python

import aspose.pdf as ap
from os import path

document = ap.Document(path_infile)

if len(document.pages) < 3:
    print("Error: The document does not have at least 3 pages.")
    return

page = document.pages[3]
page.actions.remove_actions()

document.save(path_outfile)

```

## AcroForms 中的操作

### 使用导航操作

PDF 标准提供了一组命名操作。此类操作的含义由其名称决定。
在下面的代码中，我们将使用导航操作。

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...

def add_navigation_buttons(self, infile, outfile):
    """
    Add navigation buttons to each page of the PDF.

    Creates four navigation buttons on each page:
    - First Page: Navigate to the first page
    - Previous Page: Navigate to the previous page
    - Next Page: Navigate to the next page
    - Last Page: Navigate to the last page

    Buttons are automatically disabled when not applicable (e.g.,
    "Previous" is disabled on the first page).

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Example:
        >>> actions.add_navigation_buttons("multipage.pdf", "nav_buttons.pdf")
    """
    path_infile, path_outfile = self._get_file_paths(infile, outfile)

    # Configuration for each navigation button
    button_config = [
        ("First Page", 10.0, PredefinedAction.FIRST_PAGE, lambda p, t: p == 1),
        ("Previous Page", 120.0, PredefinedAction.PREV_PAGE, lambda p, t: p == 1),
        ("Next Page", 230.0, PredefinedAction.NEXT_PAGE, lambda p, t: p == t),
        ("Last Page", 340.0, PredefinedAction.LAST_PAGE, lambda p, t: p == t),
    ]

    try:
        document = ap.Document(path_infile)
        total_pages = len(document.pages)

        # Add navigation buttons to each page
        for page in document.pages:
            page_number = page.number

            for name, x_pos, action, is_readonly_fn in button_config:
                # Create button rectangle
                rect = Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
                button = ButtonField(page, rect)
                button.partial_name = name

                # Disable button when not applicable
                button.read_only = is_readonly_fn(page_number, total_pages)
                button.actions.on_release_mouse_btn = NamedAction(action)

                document.form.add(button)

        document.save(path_outfile)

    except Exception as e:
        print(f"Error adding navigation buttons: {e}")

```

此代码为 PDF 文档的每一页添加导航按钮，便于用户在页面之间切换。它首先使用辅助方法确定输入和输出文件的完整路径。`button_config` 列表定义了四种导航按钮——首页、上一页、下一页、末页——以及它们的水平位置、触发的预定义导航操作和一个 lambda 函数，用于判断每个按钮在给定页面上是否应设为只读（例如，“首页”和“上一页”按钮在第一页上为只读）。

代码随后加载 PDF 并遍历每一页。对于每页，它循环遍历按钮配置，在每个按钮的位置创建矩形区域并实例化一个 ButtonField。为每个按钮设置名称，根据当前页设置只读状态，并将点击操作分配给相应的导航操作。随后将按钮添加到 PDF 表单字段中。

在所有页面的所有按钮添加完毕后，保存修改后的文档。如果在此过程中出现任何错误，会被捕获并打印。此方法确保每页都有一致的导航控件集合，提升多页 PDF 的可用性。一个细节是使用 `is_readonly_fn` lambda 在按钮不适用时（如最后一页的“下一页”）将其禁用，从而避免用户混淆。

### 使用打印操作

在使用 PDF 表单时，通常需要打印此类 PDF 文档。此操作可以通过 PDF 阅读器完成，但有时直接在文档中使用专用按钮更为方便。

事实上，这又是一个使用命名操作的示例。我们将使用 `PredefinedAction.FILE_PRINT`（模拟 File->Print 菜单项的使用），但也可以根据自己的需求使用 `PredefinedAction.PRINT` 或 `PredefinedAction.PRINT_DIALOG`。

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...

def add_named_action_print(self, infile, outfile):
    """
    Add a print button to the first page of the PDF.

    Creates a button labeled "Print" that triggers the system print dialog
    when clicked. The button is positioned at the bottom-left corner of
    the first page with a 1-pixel border.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Example:
        >>> actions.add_named_action_print("input.pdf", "output.pdf")
    """
    path_infile, path_outfile = self._get_file_paths(infile, outfile)

    document = ap.Document(path_infile)
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
    document.save(path_outfile)

```

此代码片段演示了如何在 PDF 文档的首页添加一个"Print"按钮。它首先从指定的输入文件路径加载 PDF，并选择第一页 (document.pages[1])。

在页面上为按钮的位置和大小定义了一个矩形区域。随后在此位置创建了一个 ButtonField，命名为 "printButton"，其显示值设为 "Print"。该按钮被配置为在点击时（具体来说，在鼠标按钮释放时），触发预定义的 “Print File” 动作，提示 PDF 查看器打开打印对话框。

为了增强按钮的外观，创建了一个边框并将其分配给按钮，宽度设为 1 单位。然后将按钮添加到首页的 PDF 表单字段中。最后，将修改后的文档保存到输出文件路径。这种方法为用户提供了直接在 PDF 中打印文档的便捷方式。请注意，此功能的有效性取决于 PDF 查看器对交互式表单字段和预定义动作的支持。

### 使用隐藏动作

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...

def add_named_action_hide(self, infile, outfile):
    """
    Add a hide button that toggles visibility of all checkbox fields.

    Creates a button labeled "Hide Checkboxes" that can hide or show
    all checkbox fields in the document. Useful for forms with many
    checkboxes that might clutter the interface.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Example:
        >>> actions.add_named_action_hide("form.pdf", "form_with_hide.pdf")
    """
    path_infile, path_outfile = self._get_file_paths(infile, outfile)

    try:
        document = ap.Document(path_infile)
        # Collect all checkbox fields in the document
        checkboxes = [field for field in document.form if isinstance(field, ap.CheckboxField)]

        # Create the hide button
        rect = Rectangle(10, 510, 100, 540)
        hide_button = ButtonField(document.pages[1], rect)
        hide_button.partial_name = "HideButton"
        hide_button.value = "Hide Checkboxes"

        # Add HideAction to button - will hide all checkboxes when clicked
        hide_button.actions.on_release_mouse_btn = ap.HideAction(checkboxes, True)

        # Add button to the form on page 1
        document.form.add(hide_button, 1)

        # Save the modified PDF
        document.save(path_outfile)

    except Exception as e:
        print(f"Error adding hide button: {e}")

```

此代码片段在 PDF 的首页添加一个按钮，点击后隐藏文档中所有的复选框字段。它首先使用辅助方法解析完整的输入和输出文件路径。加载 PDF 后，通过过滤表单字段中 `ap.CheckboxField` 实例来收集所有复选框字段。

在页面顶部附近为新按钮的位置定义了一个矩形区域。随后在此位置创建了一个 ButtonField，命名为 "HideButton"，标签为 "Hide Checkboxes"。该按钮被配置为在点击时（鼠标按钮释放时），触发一个 HideAction，隐藏所有已收集的复选框。

然后将按钮添加到首页的表单字段中，并将修改后的 PDF 保存到输出文件。如果在此过程中出现任何错误，它们会被捕获并打印。此功能为用户提供了一种快速隐藏 PDF 中所有复选框的方法，可用于自定义文档外观或工作流。

### 应用提交动作

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...

def add_submit_action(self, infile, outfile):
    """
    Submit form.

    Parameters:
    - infile (str): The name of the input PDF file.
    - outfile (str): The name of the output PDF file.
    """
    path_infile = self.dataDir + infile
    path_outfile = self.dataDir + outfile

    try:
        document = ap.Document(path_infile)

        # Create the submit action
        submit_action = ap.SubmitFormAction()
        submit_action.url = FileSpecification("http://localhost:3000/submit")
        submit_action.flags = (
            SubmitFormAction.EXPORT_FORMAT | SubmitFormAction.SUBMIT_COORDINATES
        )

        # Create the submit button
        rect = Rectangle(10, 10, 100, 40)
        submit_button = ButtonField(document.pages[1], rect)
        submit_button.partial_name = "SubmitButton"
        submit_button.value = "Submit"
        submit_button.actions.on_release_mouse_btn = submit_action

        # Add the button to the form on page 1
        document.form.add(submit_button, 1)

        # Save the document
        document.save(path_outfile)

    except Exception as e:
        print(f"Error adding submit button: {e}")

```

此函数在 PDF 表单的首页添加一个 "Submit" 按钮，允许用户将表单数据提交到指定的 Web 端点。它首先构建输入和输出 PDF 文件的完整路径，然后使用 Aspose.PDF 库加载输入 PDF。

`SubmitFormAction` 被创建以定义按钮点击时的行为。该动作的 url 通过指向 http://localhost:3000/submit 的 `FileSpecification` 设置，这意味着表单数据将发送到此 URL。flags 属性结合了 `EXPORT_FORMAT` 和 `SUBMIT_COORDINATES`，确保表单数据以标准格式导出，并且在提交中包含按钮点击的坐标。

为按钮在页面上的位置和大小定义了一个矩形区域。在首页的此位置创建了一个 ButtonField，命名为 "SubmitButton"，其显示值设为 "Submit"。提交动作被分配给按钮的鼠标释放事件，因此在用户点击按钮时触发该动作。

最后，将按钮添加到首页的表单字段中，并将修改后的 PDF 保存到输出文件。如果在此过程中出现任何错误，它们会被捕获并打印。这种方法为 PDF 用户提供了一种友好的方式，可将表单数据直接提交到服务器端点。

