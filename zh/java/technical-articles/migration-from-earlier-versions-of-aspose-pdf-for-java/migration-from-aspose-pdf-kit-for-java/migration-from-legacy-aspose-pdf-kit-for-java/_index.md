---
title: 从旧版 Aspose.Pdf.Kit for Java 迁移
type: docs
weight: 10
url: zh/java/migration-from-legacy-aspose-pdf-kit-for-java/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

目前的 Aspose.PDF.Kit for Java 组件提供了操作现有 PDF 文件的功能。然而有时候，这个组件将作为单独的产品停止，因为我们已经在新的自动移植版本 Aspose.PDF for Java (4.x.x) 的 **com.aspose.pdf.facades** 包中移植了其所有的类和枚举。现在，这个单一的自动移植版本不仅可以创建还可以操作现有的 PDF 文件。

{{% /alert %}}

## 对旧代码的支持

在整个迁移过程中，我们确实考虑了此活动对现有客户的影响，并且我们尽最大努力将此影响降到最低。
 此外，我们还专注于使新的自动移植版本具有向后兼容性，以便现有客户的代码库需要最少的更改。尽管新的自动移植版本在 com.aspose.pdf 包下提供了文档对象模型 (DOM) 来创建和操作现有的 PDF 文件，但如果您希望继续使用使用 Aspose.PDF.Kit for Java 开发的旧代码，您只需导入 **com.aspose.pdf.facades** 包，您的代码应该可以工作（*除了更新显式类引用*）。

以下代码片段向您展示了如何使用新的自动移植 Aspose.PDF for Java 运行现有的 Aspose.PDF.Kit for Java 代码。

```java

 import com.aspose.pdf.facades.*;

public class template {

    public static void main(String[] args) {

        try{

            // 加载现有的 PDF 文件

            com.aspose.pdf.facades.PdfFileInfo fileInfo = new com.aspose.pdf.facades.PdfFileInfo("input.pdf");

            System.out.println("TITLE: " + fileInfo.getTitle());

            System.out.println("AUTHOR:" + fileInfo.getAuthor());

            System.out.println("CREATIONDATE:" + fileInfo.getCreationDate());

            System.out.println("CREATOR:" + fileInfo.getCreator());

            System.out.println("KeyWORDS:" + fileInfo.getKeywords());

            System.out.println("MODDATE:" + fileInfo.getModDate());

           }


catch(Exception ex)


{System.out.println(ex);}


}

}
```

## 使用 ReplaceTextStrategy 类

为了迁移 ReplaceTextStrategy 类的代码，**setScope(..)** 方法已更新为 **setReplaceScope(..)**。请查看以下代码片段。

```java

// 实例化 PdfContentEditor 对象

com.aspose.pdf.facades.PdfContentEditor editor = new com.aspose.pdf.facades.PdfContentEditor();

// 绑定源 PDF 文件

editor.bindPdf("input.pdf");

// 创建替换文本策略

com.aspose.pdf.facades.ReplaceTextStrategy strategy = new com.aspose.pdf.facades.ReplaceTextStrategy();

// 设置文本替换的对齐方式

strategy.setAlignment(com.aspose.pdf.facades.AlignmentType.Left);

// 文本替换的范围

strategy.setReplaceScope(com.aspose.pdf.facades.ReplaceTextStrategy.Scope.REPLACE_ALL);

// 设置替换策略

editor.setReplaceTextStrategy(strategy);

editor.replaceText("test", "replaced");

// 保存更新后的文件

editor.save("TxtReplaceTest.pdf");
```