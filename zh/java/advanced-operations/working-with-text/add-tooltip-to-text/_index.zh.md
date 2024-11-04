---
title: 使用工具提示
linktitle: PDF 工具提示
type: docs
weight: 20
url: /java/pdf-tooltip/
description: 了解如何使用 Java 和 Aspose.PDF 在 PDF 中为文本片段添加工具提示。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 通过添加不可见按钮为搜索文本添加工具提示

在 PDF 文档中通常需要为短语或特定单词添加一些详细信息作为工具提示，以便当用户将鼠标光标悬停在文本上时可以弹出。Aspose.PDF for Java 提供了通过在搜索文本上添加不可见按钮来创建工具提示的功能。以下代码段将向您展示如何实现此功能：

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.ButtonField;
import com.aspose.pdf.Document;
import com.aspose.pdf.TextFragment;
import com.aspose.pdf.TextFragmentAbsorber;
import com.aspose.pdf.TextFragmentCollection;

public class ExampleToolTip {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddToolTip() {
        String outputFile = _dataDir + "Tooltip_out.pdf";

        // 创建带有文本的示例文档
        Document doc = new Document();
        doc.getPages().add().getParagraphs().add(new TextFragment("将鼠标光标移到此处以显示工具提示"));
        doc.getPages().get_Item(1).getParagraphs().add(new TextFragment("将鼠标光标移到此处以显示非常长的工具提示"));
        doc.save(outputFile);

        // 打开带有文本的文档
        Document document = new Document(outputFile);
        // 创建 TextAbsorber 对象以查找所有与正则表达式匹配的短语
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("将鼠标光标移到此处以显示工具提示");
        // 为文档页面接受吸收器
        document.getPages().accept(absorber);
        // 获取提取的文本片段
        TextFragmentCollection textFragments = absorber.getTextFragments();

        // 遍历片段
        for(TextFragment fragment : textFragments)
        {
            // 在文本片段位置创建不可见按钮
            ButtonField field = new ButtonField(fragment.getPage(), fragment.getRectangle());
            // AlternateName 值将作为工具提示由查看应用程序显示
            field.setAlternateName ("文本的工具提示。");
            // 将按钮字段添加到文档
            document.getForm().add(field);
        }

        // 接下来将是非常长的工具提示示例
        absorber = new TextFragmentAbsorber("将鼠标光标移到此处以显示非常长的工具提示");
        document.getPages().accept(absorber);
        textFragments = absorber.getTextFragments();

        for(TextFragment fragment : textFragments)
        {
            ButtonField field = new ButtonField(fragment.getPage(), fragment.getRectangle());
            // 设置非常长的文本
            field.setAlternateName ("Lorem ipsum dolor sit amet, consectetur adipiscing elit," +
                                    " sed do eiusmod tempor incididunt ut labore et dolore magna" +
                                    " aliqua. Ut enim ad minim veniam, quis nostrud exercitation" +
                                    " ullamco laboris nisi ut aliquip ex ea commodo consequat." +
                                    " Duis aute irure dolor in reprehenderit in voluptate velit" +
                                    " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint" +
                                    " occaecat cupidatat non proident, sunt in culpa qui officia" +
                                    " deserunt mollit anim id est laborum.");
            document.getForm().add(field);
        }

        // 保存文档
        document.save(outputFile);
    }
}
```


{{% alert color="primary" %}}

关于工具提示的长度，工具提示文本作为 PDF 字符串类型包含在 PDF 文档中，位于内容流之外。PDF 文件中的此类字符串没有有效限制（参见 PDF 参考附录 C.）。然而，运行在特定处理器和特定操作环境中的合规阅读器（例如 Adobe Acrobat）确实有这样的限制。请参阅您的 PDF 阅读器应用程序文档。

{{% /alert %}}

## 创建一个隐藏文本块并在鼠标悬停时显示

在 Aspose.PDF 中，实现了一项隐藏动作的功能，可以在鼠标进入/退出某些不可见按钮时显示/隐藏文本框字段（或任何其他类型的注释）。为此，使用 Aspose.Pdf.Annotations.HideAction 类来分配隐藏/显示文本块的动作。请使用以下代码片段在鼠标进入/退出时显示/隐藏文本块。

还请注意，文档中的 PDF 动作在合规阅读器中运行良好（例如。
 Adobe Reader）但不保证其他PDF阅读器（例如，Web浏览器插件）。我们进行了简要调查，发现：

- 所有的隐藏动作在Internet Explorer v.11.0中工作正常。
- 所有隐藏动作在Opera v.12.14中也能正常工作，但我们发现首次打开文档时有一些响应延迟。
- 只有使用接受字段名称的HideAction构造函数的实现才能在Google Chrome v.61.0浏览文档时工作；如果在Google Chrome中浏览很重要，请使用相应的构造函数：

>buttonField.Actions.OnEnter = new HideAction(floatingField.FullName, false);
>buttonField.Actions.OnExit = new HideAction(floatingField.FullName);

```java
    public static void name() {
        String outputFile = _dataDir + "TextBlock_HideShow_MouseOverOut_out.pdf";

        // 创建含有文本的示例文档
        Document doc = new Document();
        doc.getPages().add().getParagraphs().add(new TextFragment("将鼠标光标移动到此处以显示浮动文本"));
        doc.save(outputFile);

        // 打开含有文本的文档
        Document document = new Document(outputFile);
        // 创建TextAbsorber对象以查找所有匹配正则表达式的短语
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("将鼠标光标移动到此处以显示浮动文本");
        // 接受文档页面的吸收器
        document.getPages().accept(absorber);
        // 获取第一个提取的文本片段
        TextFragmentCollection textFragments = absorber.getTextFragments();
        TextFragment fragment = textFragments.get_Item(1);

        // 在页面的指定矩形中创建用于浮动文本的隐藏文本字段
        TextBoxField floatingField = new TextBoxField(fragment.getPage(), new Rectangle(100, 700, 220, 740));
        // 设置要显示为字段值的文本
        floatingField.setValue ("这是\"浮动文本字段\"。");
        // 我们建议在此场景中将字段设为“只读”
        floatingField.setReadOnly(true);

        // 设置“隐藏”标志以使字段在打开文档时不可见
        floatingField.setFlags( floatingField.getFlags() | AnnotationFlags.Hidden);

        // 设置唯一字段名称不是必须的，但允许
        floatingField.setPartialName ("FloatingField_1");

        // 设置字段外观的特征不是必须的，但会更好
        DefaultAppearance da = new DefaultAppearance("Helvetica", 16, java.awt.Color.RED);
        floatingField.setDefaultAppearance(da);
        //new DefaultAppearance("Helv", 10, Color.getBlue()
        floatingField.getCharacteristics().setBackground(Color.getLightBlue());
        floatingField.getCharacteristics().setBorder(Color.getDarkBlue());
        floatingField.setBorder(new Border(floatingField));
        floatingField.getBorder().setWidth(1);
        floatingField.setMultiline(true);

        // 将文本字段添加到文档
        document.getForm().add(floatingField);

        // 在文本片段位置创建不可见按钮
        Field buttonField = new ButtonField(fragment.getPage(), fragment.getRectangle());
        // 为指定字段（注释）和不可见标志创建新的隐藏动作。
        // （如果您在上面指定了名称，也可以通过名称引用浮动字段。）
        // 在不可见按钮字段上添加鼠标进入/退出动作
        buttonField.getActions().setOnEnter(new HideAction(floatingField, false));
        buttonField.getActions().setOnExit (new HideAction(floatingField));

        // 将按钮字段添加到文档
        document.getForm().add(buttonField);

        // 保存文档
        document.save(outputFile);
    }
```