---
title: 快速提示
type: docs
weight: 50
url: zh/java/quick-tips/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

此页面包含一些与 Aspose.PDF for Java API 相关的快速提示

{{% /alert %}}

## 向 PDF 添加 JavaScript

以下代码片段可用于设置/添加 JavaScript 到 PDF 文件。

```java

String path = "D:\\";
String fileOut = path + "JavaScript.pdf";
IDocument document = null;
try
{

    document = new Document();
    document.getPages().add();
    document.getPages().add();

    //在文档级别添加 JavaScript
    //使用所需的 JavaScript 语句实例化 JavascriptAction
    JavascriptAction javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

    //将 JavascriptAction 对象分配给文档的所需动作
    document.setOpenAction(javaScript);
    document.setOpenAction(new JavascriptAction("app.alert('Hello PDF')"));

    //在页面级别添加 JavaScript
    document.getActions().setBeforeClosing(new JavascriptAction("app.alert('document is closing')"));

    document.getPages().get_Item(1).getActions().setOnOpen(new JavascriptAction("app.alert('page 1 is opened')"));

    document.getPages().get_Item(2).getActions().setOnOpen(new JavascriptAction("app.alert('page 2 is opened')"));

    document.getPages().get_Item(2).getActions().setOnClose(new JavascriptAction("app.alert('page 2 is closed')"));

    document.save(fileOut);

}
finally { if (document != null) document.dispose(); document = null; }

```


**一些更多的例子**

```java

// 打印后
document.getActions().setAfterPrinting(new JavascriptAction("app.alert('文件已打印')"));

// 保存后
document.getActions().setAfterSaving(new JavascriptAction("app.alert('文件已保存')"));


```

## 释放已用内存

如果您已经完成了使用 Aspose.PDF for Java 的工作，并想要清除不同静态实例中的内存，以便为其他进程提供最大内存，您应该执行以下代码行：

```java

com.aspose.pdf.MemoryCleaner.clear();

```

## 从 ByteArrayInputStream 加载 PDF

以下代码片段显示了将 PDF 文件加载到 ByteArray 中的步骤，然后用 ByteArrayInputStream 实例化 Document 对象。

```java

// 源 PDF 文件

java.io.File file = new java.io.File("c:/pdftest/result.pdf");

java.io.FileInputStream fis = new java.io.FileInputStream(file);

//System.out.println(file.exists() + "!!");

//InputStream in = resource.openStream();

java.io.ByteArrayOutputStream bos = new java.io.ByteArrayOutputStream();

byte[] buf = new byte[1024];

try {

    for (int readNum; (readNum = fis.read(buf)) != -1;) {

        bos.write(buf, 0, readNum); //毫无疑问这里是0

        //从指定的字节数组的偏移量 off 开始将 len 个字节写入此字节数组输出流。

        System.out.println("读取了 " + readNum + " 字节,");

    }

} catch (java.io.IOException ex) {


}

byte[] bytes = bos.toByteArray();

// 在传递字节数组作为参数时，用 ByteArrayInputStream 实例化 Document 对象

com.aspose.pdf.Document doc = new
com.aspose.pdf.Document(new java.io.ByteArrayInputStream(bytes));

// 获取 PDF 文件的页数

System.out.println(doc.getPages().size());

```


## 保存 PDF 到 ByteArrayOutputStream

以下代码片段展示了将生成的 PDF 文件保存到 ByteArrayOutputStream 的步骤。

```java

 com.aspose.pdf.Document pdfDocument = new 
com.aspose.pdf.Document("source.pdf");

java.io.InputStream is = null;

java.io.ByteArrayOutputStream os = new java.io.ByteArrayOutputStream();

try{

pdfDocument.save(os,com.aspose.pdf.SaveFormat.Doc);

System.out.println(os.size());

is = new java.io.ByteArrayInputStream(os.toByteArray());

            os.close();

            os.flush();

pdfDocument.close();

}catch (Throwable e) {}

```