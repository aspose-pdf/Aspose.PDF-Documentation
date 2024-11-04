---
title: 将PDF转换为Microsoft PowerPoint
linktitle: 将PDF转换为PowerPoint
type: docs
weight: 30
url: /java/convert-pdf-to-powerpoint/
lastmod: "2021-11-19"
description: Aspose.PDF允许您使用Java将PDF转换为PowerPoint格式。可以将PDF转换为带有图像幻灯片的PPTX。
lastmod: "2021-10-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF for Java** 让您跟踪PDF到PPTX转换的进度。 我们有一个名为Aspose.Slides的API，它提供创建和操作PPT/PPTX演示文稿的功能。该API还提供将PPT/PPTX文件转换为PDF格式的功能。在Aspose.PDF for Java中，我们引入了将PDF文档转换为PPTX格式的功能。在此转换过程中，PDF文件的各个页面被转换为PPTX文件中的单独幻灯片。

在PDF到PPTX转换过程中，文本被渲染为可选择/更新的文本，而不是渲染为图像。
 请注意，为了将PDF文件转换为PPTX格式，Aspose.PDF提供了一个名为PptxSaveOptions的类。[PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions)类的对象作为第二个参数传递给[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..)方法。

查看下一个代码片段，以解决将PDF转换为PowerPoint格式的任务：

```java
public final class ConvertPDFtoPPTX {

    private ConvertPDFtoPPTX() {

    }

    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void run() throws IOException {
        convertPDFtoPPTX_Simple();
        convertPDFtoPPTX_SlideAsImages();
        convertPDFtoPPTX_ProgresDetails();
    }

    public static void convertPDFtoPPTX_Simple() {
        String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX.pdf").toString();
        String pptxDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX_out.pptx").toString();

        // 加载PDF文档
        Document document = new Document(documentFileName);

        // 实例化PptxSaveOptions
        PptxSaveOptions pptx_save = new PptxSaveOptions();

        // 将输出保存为PPTX格式
        document.save(pptxDocumentFileName, pptx_save);
        document.close();
    }
}
```

## 将 PDF 转换为以图像为幻灯片的 PPTX

如果您需要将可搜索的 PDF 转换为以图像而不是可选择文本的 PPTX，Aspose.PDF 提供了这种功能，通过 [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) 类来实现。为此，将 [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) 类的属性 SlidesAsImages 设置为 'true'，如下代码示例所示。

以下代码片段展示了将 PDF 文件转换为以图像为幻灯片的 PPTX 格式的过程。

```java
public static void convertPDFtoPPTX_SlideAsImages() {
    String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX.pdf").toString();
    String pptxDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX_out.pptx").toString();

    // 加载 PDF 文档
    Document document = new Document(documentFileName);
    // 实例化 PptxSaveOptions 实例
    PptxSaveOptions pptxSaveOptions = new PptxSaveOptions();
    // 将输出保存为 PPTX 格式
    pptxSaveOptions.setSlidesAsImages(true);

    document.save(pptxDocumentFileName, pptxSaveOptions);
    document.close();
}
```


## 在控制台显示进度与 Aspose.PDF for Java 看起来像这样：

```java
package com.aspose.pdf.examples.conversion;

import com.aspose.pdf.Document;
import com.aspose.pdf.PptxSaveOptions;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * 将 PDF 转换为 PPTX。
 */
public final class ConvertPDFtoPPTX {

    private ConvertPDFtoPPTX() {

    }

    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void run() throws IOException {
        convertPDFtoPPTX_ProgressDetails();
    }

    public static void convertPDFtoPPTX_ProgressDetails() {
        String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX.pdf").toString();
        String pptxDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToPPTX_out.pptx").toString();

        // 加载 PDF 文档
        Document document = new Document(documentFileName);

        // 实例化 PptxSaveOptions 实例
        PptxSaveOptions pptx_save = new PptxSaveOptions();

        // 指定自定义进度处理程序
        pptx_save.setCustomProgressHandler(new ShowProgressOnConsole());

        // 以 PPTX 格式保存输出
        document.save(pptxDocumentFileName, pptx_save);
        document.close();
    }
}
```


## PPTX 转换的进度详情

Aspose.PDF for Java 允许您跟踪 PDF 到 PPTX 的转换进度。[Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) 类提供了 [CustomProgressHandler](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlSaveOptions) 属性，可以指定为自定义方法以跟踪转换进度，如以下代码示例所示。

```java
package com.aspose.pdf.examples;

import java.time.LocalDateTime;

import com.aspose.pdf.ProgressEventType;
import com.aspose.pdf.UnifiedSaveOptions.ConversionProgressEventHandler;
import com.aspose.pdf.UnifiedSaveOptions.ProgressEventHandlerInfo;

class ShowProgressOnConsole extends ConversionProgressEventHandler{

    @Override
    public void invoke(ProgressEventHandlerInfo eventInfo) {        
        switch (eventInfo.EventType) {
            case ProgressEventType.TotalProgress:
                System.out.println(
                        String.format("%s  - 转换进度 : %d %%.", LocalDateTime.now().toString(), eventInfo.Value));
                break;
            case ProgressEventType.ResultPageCreated:
                System.out.println(String.format("%s  - 结果页面的 %s 在 %d 布局中创建。", LocalDateTime.now().toString(),
                        eventInfo.Value, eventInfo.MaxValue));
                break;
            case ProgressEventType.ResultPageSaved:
                System.out.println(String.format("%s  - 结果页面 %d 在 %d 中导出。", LocalDateTime.now(), eventInfo.Value, eventInfo.MaxValue));
                break;
            case ProgressEventType.SourcePageAnalysed:
                System.out.println(String.format("%s  - 源页面 %d 在 %d 中分析。", LocalDateTime.now(),  eventInfo.Value, eventInfo.MaxValue));
                break;
            default:
                break;
        }
    }
```


{{% alert color="success" %}}
**尝试在线将 PDF 转换为 PowerPoint**

Aspose.PDF for Java 为您提供了在线免费应用程序["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)，您可以在此尝试研究其功能和工作质量。

[![Aspose.PDF 转换 PDF 到 PPTX 免费应用](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}