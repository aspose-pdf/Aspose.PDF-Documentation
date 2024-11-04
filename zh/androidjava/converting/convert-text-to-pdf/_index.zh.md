---  
title: 将文本转换为PDF  
linktitle: 将文本转换为PDF  
type: docs  
weight: 300  
url: /androidjava/convert-text-to-pdf/  
lastmod: "2021-06-05"  
description: Aspose.PDF for Android via Java允许您将纯文本文件转换为PDF或将预格式化文本文件转换为PDF。  
sitemap:  
    changefreq: "weekly"  
    priority: 0.7  
---

{{% alert color="primary" %}} 

在线试用。您可以在此链接[products.aspose.app/pdf/conversion/txt-to-pdf](https://products.aspose.app/pdf/conversion/txt-to-pdf)在线检查Aspose.PDF转换的质量并查看结果。

{{% /alert %}}

**Aspose.PDF for Android via Java** 提供将文本文件转换为PDF格式的功能。在本文中，我们演示了如何使用Aspose.PDF轻松高效地将文本文件转换为PDF。

当您需要将文本文件转换为PDF时，首先在某个阅读器中读取源文本文件。
 我们使用了StringBuilder读取文本文件的内容。实例化Document对象并在Pages集合中添加一个新页面。创建一个TextFragment的新对象，并将StringBuilder对象传递给其构造函数。使用TextFragment对象在Paragraphs集合中添加一个新段落，并使用Document类的Save方法保存生成的PDF文件。

## 将纯文本文件转换为PDF

```java
public void convertTXTtoPDF_Simple () {
        // 初始化文档对象

        File pdfDocumentFileName=new File(fileStorage, "demo_txt.pdf");
        File txtDocumentFileName=new File(fileStorage, "Conversion/rfc822.txt");

        // 调用其空构造函数实例化一个Document对象
        document=new Document();

        // 在Document的Pages集合中添加一个新页面
        Page page=document.getPages().add();

        String string;
        StringBuilder stringBuilder=new StringBuilder();
        InputStream is;
        try {
            is=new FileInputStream(txtDocumentFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        BufferedReader reader=new BufferedReader(new InputStreamReader(is));
        while (true) {
            try {
                if ((string=reader.readLine()) == null) break;
            } catch (IOException e) {
                resultMessage.setText(e.getMessage());
                return;
            }
            stringBuilder.append(string).append("\n");
        }
        try {
            is.close();
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }


        // 创建一个TextFragment的实例，并将文本从reader对象传递到其构造函数作为参数
        TextFragment text=new TextFragment(stringBuilder.toString());

        // 在段落集合中添加一个新的文本段落并传递TextFragment对象
        page.getParagraphs().add(text);

        // 保存生成的PDF文件
        try {
            document.save(pdfDocumentFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```

## 将预格式化文本文件转换为PDF

```java
    public void convertPreFormattedTextToPdf () {

        File txtDocumentFile=new File(fileStorage, "Conversion/rfc822.txt");
        File pdfDocumentFileName=new File(fileStorage, "demo_txt.pdf");
        Path txtDocumentFileName=Paths.get(txtDocumentFile.toString());

        // 将文本文件读取为字符串数组
        List<String> lines;
        try {
            lines=Files.readAllLines(txtDocumentFileName, ENCODING);
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // 通过调用空构造函数实例化一个Document对象
        document=new Document();

        // 在Document的Pages集合中添加一个新页面
        Page page=document.getPages().add();
        int count=4;

        Font font=FontRepository.findFont("Droid Sans Mono");
        // 设置左右边距以获得更好的展示
        page.getPageInfo().getMargin().setLeft(20);
        page.getPageInfo().getMargin().setRight(10);
        page.getPageInfo().getDefaultTextState().setFont(font);
        page.getPageInfo().getDefaultTextState().setFontSize(12);

        for (String line : lines) {
            // 检查行是否包含“换页”字符
            // 参见 https://en.wikipedia.org/wiki/Page_break
            if (line.startsWith("\f")) {
                page=document.getPages().add();
                page.getPageInfo().getMargin().setLeft(20);
                page.getPageInfo().getMargin().setRight(10);
                page.getPageInfo().getDefaultTextState().setFont(font);
                page.getPageInfo().getDefaultTextState().setFontSize(12);
            } else {
                // 创建一个TextFragment实例并
                // 将行传递给其
                // 构造函数作为参数
                TextFragment text=new TextFragment(line);

                // 在段落集合中添加一个新的文本段落并传递TextFragment
                // 对象
                page.getParagraphs().add(text);
            }
        }
        // 保存生成的PDF文件
        try {
            document.save(pdfDocumentFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```