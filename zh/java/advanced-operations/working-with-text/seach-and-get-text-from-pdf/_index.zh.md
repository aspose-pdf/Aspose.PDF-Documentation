---
title: 从PDF文档页面中搜索和获取文本
linktitle: 搜索和获取文本
type: docs
weight: 60
url: /java/search-and-get-text-from-pdf/
description: 本文解释了如何使用各种工具从PDF文档中搜索和获取文本。我们可以从特定或整个页面使用正则表达式进行搜索。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 从PDF文档的所有页面中搜索和获取文本

TextFragmentAbsorber允许您从PDF文档的所有页面中找到匹配特定短语的文本。

要在整个文档中搜索文本，请调用[Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page)集合的accept()方法。
 [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) 方法接受一个 TextFragmentAbsorber 对象作为参数，该对象返回一个 TextFragment 对象的集合。循环遍历所有的片段以获取其属性，例如文本、位置、XIndent、YIndent、FontName、FontSize、IsAccessible、IsEmbedded、IsSubset、ForegroundColor 等。

以下代码片段展示了如何搜索整个文档并在控制台显示所有匹配项。

```java
// 打开文档
Document pdfDocument = new Document("input.pdf");

// 创建 TextAbsorber 对象以查找输入搜索短语的所有实例
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("sample");

// 接受所有页面的吸收器
pdfDocument.getPages().accept(textFragmentAbsorber);

// 将提取的文本片段放入集合
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

// 循环遍历片段
for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
    System.out.println("文本 :- " + textFragment.getText());
    System.out.println("位置 :- " + textFragment.getPosition());
    System.out.println("X缩进 :- " + textFragment.getPosition().getXIndent());
    System.out.println("Y缩进 :- " + textFragment.getPosition().getYIndent());
    System.out.println("字体 - 名称 :- " + textFragment.getTextState().getFont().getFontName());
    System.out.println("字体 - 是否可访问 :- " + textFragment.getTextState().getFont().isAccessible());
    System.out.println("字体 - 是否嵌入 - " + textFragment.getTextState().getFont().isEmbedded());
    System.out.println("字体 - 是否子集 :- " + textFragment.getTextState().getFont().isSubset());
    System.out.println("字体大小 :- " + textFragment.getTextState().getFontSize());
    System.out.println("前景色 :- " + textFragment.getTextState().getForegroundColor());
}
```

要在特定页面上搜索文本并获取与其关联的属性，请提供页面索引：

```java
// 接受文档第一页的吸收器
pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber);
```

## 从PDF页面搜索和获取文本片段

要在文档的所有页面上搜索文本片段，请获取文档的TextFragment对象。

TextFragmentAbsorber允许您从PDF文档的所有页面中找到匹配特定短语的文本。要在整个文档中搜索文本，请调用[Pages](https://reference.aspose.com/pdf//java/com.aspose.pdf/pagecollection)集合的[accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber)方法。[accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber)方法接受一个TextFragmentAbsorber对象作为参数，该对象返回一个TextFragment对象的集合。

{{% alert color="primary" %}}

当从文档中获取到TextFragmentCollection集合后，循环遍历它以获取每个TextFragment对象的TextSegmentCollection集合。
 在那之后，你可以获取单独的 TextSegment 对象的属性。

{{% /alert %}}

以下代码片段展示了如何在所有页面上搜索文本段。

```java
// 打开文档
Document pdfDocument = new Document("input.pdf");

// 创建 TextAbsorber 对象以找到输入搜索短语的所有实例
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("sample");

// 接受文档第一页的吸收器
pdfDocument.getPages().accept(textFragmentAbsorber);

// 将提取的文本片段获取到集合中
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

// 遍历文本片段
for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
    // 遍历文本段
    for (TextSegment textSegment : (Iterable<TextSegment>) textFragment.getSegments()) {
        System.out.println("Text :- " + textSegment.getText());
        System.out.println("Position :- " + textSegment.getPosition());
        System.out.println("XIndent :- " + textSegment.getPosition().getXIndent());
        System.out.println("YIndent :- " + textSegment.getPosition().getYIndent());
        System.out.println("Font - Name :- " + textSegment.getTextState().getFont().getFontName());
        System.out.println("Font - IsAccessible :- " + textSegment.getTextState().getFont().isAccessible());
        System.out.println("Font - IsEmbedded - " + textSegment.getTextState().getFont().isEmbedded());
        System.out.println("Font - IsSubset :- " + textSegment.getTextState().getFont().isSubset());
        System.out.println("Font Size :- " + textSegment.getTextState().getFontSize());
        System.out.println("Foreground Color :- " + textSegment.getTextState().getForegroundColor());
    }
}
```

要搜索特定文本段并获取相关属性，请指定您要搜索的页面的页面索引：

```java
// 接受文档第一页的吸收器。
pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber);
```

## 使用正则表达式搜索和获取页面上的文本

TextFragmentAbsorber帮助您根据正则表达式搜索和检索文档中所有页面的文本。

要从文档中搜索和获取文本：

1. 将搜索词作为正则表达式传递给TextFragmentAbsorber构造函数。
2. 设置TextFragmentAbsorber对象的TextSearchOptions属性。
   此属性需要一个TextSearchOptions对象：在创建新对象时将true传递给其构造函数。
3. 要从所有页面检索匹配的文本，请调用[Pages](https://reference.aspose.com/pdf//java/com.aspose.pdf/pagecollection)集合的[accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber)方法。

   TextFragmentAbsorber返回一个TextFragmentCollection，其中包含所有符合正则表达式指定条件的片段。

以下代码片段展示了如何在文档中搜索所有页面并根据正则表达式获取文本。

```java
// 打开一个文档
Document pdfDocument = new Document("source.pdf");

// 创建 TextAbsorber 对象来查找输入搜索短语的所有实例
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // 例如 1999-2000

// 设置文本搜索选项以指定正则表达式的使用
TextSearchOptions textSearchOptions = new TextSearchOptions(true);
textFragmentAbsorber.setTextSearchOptions(textSearchOptions);

// 接受文档第一页的吸收器
pdfDocument.getPages().accept(textFragmentAbsorber);

// 将提取的文本片段放入集合
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

// 遍历片段
for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
    System.out.println("文本 :- " + textFragment.getText());
    System.out.println("位置 :- " + textFragment.getPosition());
    System.out.println("X偏移 :- " + textFragment.getPosition().getXIndent());
    System.out.println("Y偏移 :- " + textFragment.getPosition().getYIndent());
    System.out.println("字体 - 名称 :- " + textFragment.getTextState().getFont().getFontName());
    System.out.println("字体 - 是否可访问 :- " + textFragment.getTextState().getFont().isAccessible());
    System.out.println("字体 - 是否嵌入 - " + textFragment.getTextState().getFont().isEmbedded());
    System.out.println("字体 - 是否子集 :- " + textFragment.getTextState().getFont().isSubset());
    System.out.println("字体大小 :- " + textFragment.getTextState().getFontSize());
    System.out.println("前景颜色 :- " + textFragment.getTextState().getForegroundColor());
}
```


要在特定页面上搜索文本并获取其属性，请指定页面索引：

```java
// 接受文档第一页的吸收器。
pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber)
```

为了在大小写中搜索字符串，可以考虑使用正则表达式。

```java
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("(?i)Line", new TextSearchOptions(true));
```

示例：

```java
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("[\\S]+");
```