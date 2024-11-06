---
title: 将 PDF 转换为文本
linktitle: 将 PDF 转换为文本
type: docs
weight: 120
url: zh/androidjava/convert-pdf-to-txt/
lastmod: "2021-06-05"
description: 使用 Aspose.PDF for Android via Java，您可以将整个 PDF 文档转换为文本文件，或仅将 PDF 页转换为文本文件。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

在线尝试。您可以在此链接 [products.aspose.app/pdf/conversion/pdf-to-txt](https://products.aspose.app/pdf/conversion/pdf-to-txt) 上查看 Aspose.PDF 转换的质量并在线查看结果

{{% /alert %}}

## 将 PDF 页转换为文本文件

您可以使用 Aspose.PDF for Android via Java 将 PDF 文档转换为 TXT 文件。您应该使用 [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) 类的 Visit 方法来解决这个任务。

以下代码片段说明了如何从特定页面中提取文本。

```java
public void convertPDFPagesToTXT() {
        // 打开文档
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        TextAbsorber ta = new TextAbsorber();
        int[] pages = new int[] { 1, 3, 4 };

        for (int page : pages) {
            ta.visit(document.getPages().get_Item(page));
        }
        File txtFileName = new File(fileStorage, "PDF-to-Text.txt");

        // 将提取的文本保存到文本文件中
        BufferedWriter writer;
        try {
            writer = new BufferedWriter(new FileWriter(txtFileName));
            writer.write(ta.getText());
            writer.close();
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```