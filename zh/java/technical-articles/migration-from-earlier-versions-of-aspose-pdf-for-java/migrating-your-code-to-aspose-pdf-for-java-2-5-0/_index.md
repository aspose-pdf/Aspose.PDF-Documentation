---
title: 将您的代码迁移到 Aspose.PDF for Java 2.5.0
type: docs
weight: 10
url: /zh/java/migrating-your-code-to-aspose-pdf-for-java-2-5-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

在本文中，我们尝试突出显示 Aspose.PDF for Java 的现有代码中的一些区域，以使其与最新版本兼容。

{{% /alert %}}

## 详细信息

随着 Aspose.PDF for Java 2.5.0 的发布，API 结构和类的构造发生了很多变化。大多数类成员的名称已更新，一些现有的类成员被删除，并且还向现有类添加了一些方法和属性。为了给您简要介绍这些变化，我们将查看以下基于早期发布的 Aspose.PDF for Java 版本的简单代码。

在这个简单的代码中，我们将在同一个 PDF 文档中添加超链接和链接到页面。

```java
import com.aspose.pdf.elements.*;
com.aspose.pdf.License lic = new com.aspose.pdf.License();

try {

lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));

    } catch (Exception e)

{

System.out.println(e.getMessage());

}


//通过调用其空构造函数实例化一个 Pdf 对象

Pdf pdf1 = new Pdf();

//在 Pdf 对象中创建一个部分

Section sec1 = pdf1.getSections().add();

//使用部分的引用创建文本段落

Text text1 = new Text(sec1);

//将文本段落添加到部分的段落集合中

sec1.getParagraphs().add(text1);

//在文本段落中添加一个文本段

Segment segment1 = text1.getSegments().add("this is a local link");

//设置文本段的文本为下划线

segment1.getTextInfo().setUnderLine(true);


//将文本段的链接类型设置为本地

//将目标段落的 ID 分配为文本段的目标 ID

segment1.setHyperLink(new HyperLinkToLocalPdf("product1"));

//创建一个与文本段链接的文本段落

Text text3 = new Text(sec1,"product 1 info ...");

//将文本段落添加到部分的段落集合中

sec1.getParagraphs().add(text3);

//将此段落设置为第一个，以便可以在文档的单独页面中显示

text3.setFirstParagraph(true);

//将此文本段的 ID 设置为 "product1"

text3.setID("product1"); 


// 保存 PDF 文件

FileOutputStream out = new FileOutputStream(new File("UpdateOfCode_Test.pdf"));

pdf1.save(out);
```


当使用早于 Aspose.PDF for Java 2.5.0 的版本时，代码可以成功执行，并且可以生成一个包含指向同一文档内页面的超链接的 PDF 文档。但是，当使用 2.5.0 编译相同代码时，您会注意到出现许多错误，因为类成员发生了变化，并且某些类中的方法已被移除。现在让我们开始对版本 2.5.0 的代码进行修改。

使用 `import aspose.pdf.*`；代替 `import com.aspose.pdf.elements.*`；来包含包。

对于许可证初始化，请将现有代码更新为

{{% alert color="primary" %}}
**com.aspose.pdf.License lic = new com.aspose.pdf.License();**

```java

 try
{
lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));
}

```

{{% /alert %}}

更新为

{{% alert color="primary" %}}
**aspose.pdf.License lic = new aspose.pdf.License();**

```java

 try
{
lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));
}

```


{{% /alert %}}

**TextInfo** 不再包含方法 **setUnderLine(...)**。请尝试使用 **TextInfo.setIsUnderline(...)** **代替**。

名为 **HyperLinkToLocalPdf** 的类已被移除。因此，请更新您现有的代码，如

{{% alert color="primary" %}}
**//将文本段的链接类型设置为本地**

```java

 //将所需段落的ID分配为文本段的目标ID

segment1.setHyperLink(new HyperLinkToLocalPdf("product1"));

```

{{% /alert %}}

至

{{% alert color="primary" %}}
**segment1.getHyperlink().setLinkType(HyperlinkType.Local);**

```java

 segment1.getHyperlink().setTargetID("product1");

```

{{% /alert %}}

方法名 **setFirstParagraph** 已从 Text 类中移除。
 为了在新页面上显示文本段，您需要创建一个新的 Section 对象并将文本对象添加到新创建的部分中。由于默认情况下每个部分都会在新页面上显示，因此不需要调用类似 **sec2.setIsNewPage(true**)** 的方法。

## 更新后的保存方法

Pdf 类中的 save 方法以前需要使用 FileOutputStream 对象作为参数，现已被移除。在新版本中，您可以使用以下重载的 save 方法之一。

- save(BasicStream stream)
- save(java.lang.String pdfFile)
- save(java.lang.String fileName, SaveType saveType, aspose.pdf.HttpResponse response)

在进行上述所有指定更改后，使用 Aspose.PDF for Java 2.5.0 时，代码将被编译并执行，而不会显示任何错误消息。完整的更新代码片段如下所示。

```java
import aspose.pdf.*;
aspose.pdf.License lic = new aspose.pdf.License();

try {

lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));

    } catch (Exception e)

{

System.out.println(e.getMessage());

}

try {

//通过调用其空构造函数实例化一个 Pdf 对象

Pdf pdf1 = new Pdf();

//在 Pdf 对象中创建一个部分

Section sec1 = pdf1.getSections().add();

//使用段落的引用创建文本段落

Text text1 = new Text(sec1);

//在部分的段落集合中添加文本段落

sec1.getParagraphs().add(text1);

//在文本段落中添加一个文本段

Segment segment1 = text1.getSegments().add("this is a local link");

//设置文本段中的文本为下划线

segment1.getTextInfo().setIsUnderline(true);


//将文本段的链接类型设置为本地

//将所需段落的 ID 分配为文本段的目标 ID

segment1.getHyperlink().setLinkType(HyperlinkType.Local);

segment1.getHyperlink().setTargetID("product1");

// 添加一个新部分，该部分将保存带有 ID "Product 1" 的文本对象

Section sec2 = pdf1.getSections().add();

//创建一个与文本段链接的文本段落

Text text3 = new Text(sec1,"product 1 info ...");

//将文本段落添加到该部分的段落集合中

sec2.getParagraphs().add(text3);

//将此文本段的 ID 设置为 "product1"

text3.setID("product1");


// 保存 PDF 文件

pdf1.save("UpdateOfCode_Test.pdf");


     }catch(Exception e)

{

System.out.println(e.getMessage());

}
```

## Conclusion

在上述主题中，我们解释了一些在新版本中已更改的类和方法。要查看所有类及其成员的完整列表，请访问 [Aspose.PDF for Java API Reference](http://www.aspose.com/documentation/java-components/aspose.pdf-for-java/aspose.pdf-for-java-api-reference.html)

要了解有关 Aspose 及其产品的更多信息，请点击这里 <http://www.aspose.com/>