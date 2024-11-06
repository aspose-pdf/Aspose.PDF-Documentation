---
title: 在PDF中的表格单元格中插入图片
type: docs
weight: 20
url: zh/java/insert-an-image-into-a-table-cell-in-pdf/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

表格是显示数据的重要元素。它们为数据表示提供了一种可展示的格式。表格通常用于显示数值信息。Aspose.PDF API 提供了一个类 Table，它为您提供了在 PDF 文件中创建表格的功能。

除了创建简单的表格，您还可以设置不同的格式选项，例如表格边框样式、边距信息、对齐方式、背景颜色、列宽、标题信息、每页重复的行数值等等。

{{% /alert %}}

## Aspose.PDF 方法

根据我们的 DOM（文档对象模型），一个文档由页面组成。
 页面包含一个或多个段落，一个段落可以是图像、文本、表单字段、标题、浮动框、图表、附件或表格。表格由行的集合组成，每行包含单元格的集合。一个单元格是段落的集合。

因此，根据我们的DOM，一个表格单元格可以包含上述任意段落元素，包括图像。

## 理解单元格宽度

特别是在表格单元格中显示图像时，必须清楚理解单元格宽度，以便图像宽度固定为单元格宽度，从而正确显示。可以使用Image类的setFixedWidth()方法设置图像的宽度。

## 代码示例

```java

 String dataDir = "C:\\temp\\";

//通过调用其空构造函数实例化一个Document对象

Document pdfDocument = new Document();

//在Document对象中创建一个页面

com.aspose.pdf.Page page = pdfDocument.getPages().add();



//实例化一个表格对象

Table table = new Table();

//在所需页面的段落集合中添加表格

page.getParagraphs().add(table);

//设置表格的列宽

table.setColumnWidths("100 100 120");



//使用另一个自定义的BorderInfo对象设置表格边框

table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 1F));



//在页面中创建一个图像对象

com.aspose.pdf.Image img1 = new com.aspose.pdf.Image();

//设置图像文件的路径

img1.setFile(dataDir + "logo.jpg");



img1.setFixWidth(100);

img1.setFixHeight(100);

//在表格中创建行，然后在行中创建单元格

Row row1 = table.getRows().add();

row1.getCells().add("单元格中的示例文本");

// 添加包含图像的单元格

Cell cell2 = row1.getCells().add();

//将图像添加到表格单元格中

cell2.getParagraphs().add(img1);



row1.getCells().add("包含图像的前一个单元格");

row1.getCells().get_Item(2).setVerticalAlignment(VerticalAlignment.Center);



//保存文档

pdfDocument.save(dataDir + "Image_in_Cell.pdf");    

```