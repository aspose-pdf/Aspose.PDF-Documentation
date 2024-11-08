---
title: PDF 工具提示使用 Python
linktitle: PDF 工具提示
type: docs
weight: 20
url: /zh/python-net/pdf-tooltip/
description: 学习如何使用 Python 和 Aspose.PDF 向 PDF 中的文本片段添加工具提示
lastmod: "2024-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF 工具提示使用 Python",
    "alternativeHeadline": "向文本添加 PDF 工具提示",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 文档生成",
    "keywords": "pdf, python, 添加 pdf 工具提示",
    "wordcount": "302",
    "proficiencyLevel":"初学者",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF 文档团队",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/pdf-tooltip/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/pdf-tooltip/"
    },
    "dateModified": "2024-02-04",
    "description": "学习如何使用 Python 和 Aspose.PDF 向 PDF 中的文本片段添加工具提示"
}
</script>


## 通过添加不可见按钮为搜索文本添加工具提示

此代码演示了如何使用 Aspose.PDF 为 PDF 文档中的特定文本片段添加工具提示。当鼠标光标悬停在相应文本上时，将显示工具提示。

以下代码片段将向您展示如何实现此功能：

```python

    import aspose.pdf as ap

    document = ap.Document()
    document.pages.add().paragraphs.add(
        ap.text.TextFragment("将鼠标光标移到这里以显示工具提示")
    )
    document.pages[1].paragraphs.add(
        ap.text.TextFragment(
            "将鼠标光标移到这里以显示一个非常长的工具提示"
        )
    )
    document.save(output_pdf)

    # 打开带有文本的文档
    document = ap.Document(output_pdf)
    # 创建 TextAbsorber 对象以查找所有匹配正则表达式的短语
    absorber = ap.text.TextFragmentAbsorber(
        "将鼠标光标移到这里以显示工具提示"
    )
    # 接受文档页面的吸收器
    document.pages.accept(absorber)
    # 获取提取的文本片段
    text_fragments = absorber.text_fragments

    # 循环遍历片段
    for fragment in text_fragments:
        # 在文本片段位置创建不可见按钮
        field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
        # alternate_name 值将在查看器应用程序中显示为工具提示
        field.alternate_name = "文本的工具提示。"
        # 将按钮字段添加到文档
        document.form.add(field)

    # 接下来是非常长的工具提示的示例
    absorber = ap.text.TextFragmentAbsorber(
        "将鼠标光标移到这里以显示一个非常长的工具提示"
    )
    document.pages.accept(absorber)
    text_fragments = absorber.text_fragments

    for fragment in text_fragments:
        field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
        # 设置非常长的文本
        field.alternate_name = (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit,"
            " sed do eiusmod tempor incididunt ut labore et dolore magna"
            " aliqua. Ut enim ad minim veniam, quis nostrud exercitation"
            " ullamco laboris nisi ut aliquip ex ea commodo consequat."
            " Duis aute irure dolor in reprehenderit in voluptate velit"
            " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint"
            " occaecat cupidatat non proident, sunt in culpa qui officia"
            " deserunt mollit anim id est laborum."
        )
        document.form.add(field)

    # 保存文档
    document.save(output_pdf)
```


## 创建隐藏文本块并在鼠标悬停时显示

这个Python代码片段展示了如何在PDF文档中添加浮动文本，当鼠标光标悬停在特定区域时显示。

首先，创建一个新的PDF文档，并向其中添加包含文本“将鼠标光标移到这里以显示浮动文本”的段落。然后保存文档。

接下来，重新打开保存的文档，并创建一个TextAbsorber对象来查找之前添加的文本片段。然后使用这个文本片段来定义浮动文本字段的位置和特征。

创建一个TextBoxField对象来表示浮动文本字段，并相应地设置其属性，如位置、值、只读状态和可见性。此外，为字段分配唯一名称和外观特征。

将浮动文本字段添加到文档的表单中，并在原始文本片段的位置创建一个不可见的按钮字段。
  HideAction 事件被分配给按钮字段，指定当鼠标光标进入其附近时，浮动文本字段应出现，并在光标退出时消失。

最后，将按钮字段添加到文档的表单中，并保存修改后的文档。

此代码片段提供了一种使用 Aspose.PDF for Python 在 PDF 文档中创建交互式浮动文本元素的方法。

```python

    import aspose.pdf as ap

    document = ap.Document()
    document.pages.add().paragraphs.add(
        ap.text.TextFragment("将鼠标光标移动到此处以显示浮动文本")
    )
    document.save(output_pdf)

    # 打开带有文本的文档
    document = ap.Document(output_pdf)
    # 创建 TextAbsorber 对象以查找与正则表达式匹配的所有短语
    absorber = ap.text.TextFragmentAbsorber(
        "将鼠标光标移动到此处以显示浮动文本"
    )
    # 接受文档页面的吸收器
    document.pages.accept(absorber)
    # 获取第一个提取的文本片段
    text_fragments = absorber.text_fragments
    fragment = text_fragments[1]

    # 在页面的指定矩形中为浮动文本创建隐藏文本字段
    floating_field = ap.forms.TextBoxField(
        fragment.page, ap.Rectangle(100.0, 700.0, 220.0, 740.0, False)
    )
    # 设置要显示的文本作为字段值
    floating_field.value = '这是“浮动文本字段”。'
    # 我们建议在此方案中将字段设置为“只读”
    floating_field.read_only = True
    # 设置“隐藏”标志以使字段在文档打开时不可见
    floating_field.flags |= ap.annotations.AnnotationFlags.HIDDEN

    # 设置唯一字段名称不是必须的，但允许
    floating_field.partial_name = "FloatingField_1"

    # 设置字段外观特征不是必须的，但会更好
    floating_field.default_appearance = ap.annotations.DefaultAppearance(
        "Helv", 10, ap.Color.blue.to_rgb()
    )
    floating_field.characteristics.background = ap.Color.light_blue.to_rgb()
    floating_field.characteristics.border = ap.Color.dark_blue.to_rgb()
    floating_field.border = ap.annotations.Border(floating_field)
    floating_field.border.width = 1
    floating_field.multiline = True

    # 将文本字段添加到文档中
    document.form.add(floating_field)
    # 在文本片段位置创建不可见按钮
    button_field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
    # 为指定字段（注释）和不可见性标志创建新的隐藏动作。
    # （如果之前指定了名称，您也可以通过名称引用浮动字段。）
    # 在不可见按钮字段上添加鼠标进入/退出动作

    button_field.actions.on_enter = ap.annotations.HideAction(
        floating_field.partial_name, False
    )
    button_field.actions.on_exit = ap.annotations.HideAction(
        floating_field.partial_name
    )

    # 将按钮字段添加到文档中
    document.form.add(button_field)

    # 保存文档
    document.save(output_pdf)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF 操作库 for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>