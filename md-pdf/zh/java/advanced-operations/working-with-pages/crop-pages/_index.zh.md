---

title: 程序化地裁剪PDF页面  
linktitle: 裁剪页面  
type: docs  
weight: 80  
url: /java/crop-pages/  
description: 您可以使用Aspose.PDF for Java获取页面属性，例如宽度、高度、出血框、裁剪框和修整框。  
lastmod: "2021-06-05"  
sitemap:  
    changefreq: "weekly"  
    priority: 0.7  
---
## 获取页面属性

PDF文件中的每一页都有许多属性，例如宽度、高度、出血框、裁剪框和修整框。Aspose.PDF for Java允许您访问这些属性。

- **媒体框**：媒体框是最大的页面框。它对应于打印到PostScript或PDF时选择的页面尺寸（例如A4、A5、美国信纸等）。换句话说，媒体框决定了显示或打印PDF文档的媒体的物理大小。
- **出血框**：如果文档有出血，PDF也会有一个出血框。
 出血是超出页面边缘的颜色（或艺术作品）的量。它用于确保当文件打印并切割到合适大小（“修整”）时，墨水会一直到页面的边缘。即使页面被错误修整 - 稍微偏离修整标记切割 - 页面上也不会出现白边。
- **修整框**：修整框表示文件在打印和修整后的最终尺寸。
- **艺术框**：艺术框是在文档页面的实际内容周围绘制的框。此页面框在其他应用中导入PDF文档时使用。
- **裁剪框**：裁剪框是您的PDF文档在Adobe Acrobat中显示的“页面”大小。在正常视图中，Adobe Acrobat中仅显示裁剪框的内容。有关这些属性的详细描述，请阅读Adobe.Pdf规范，特别是10.10.1页面边界。
- **页面.矩形**：是媒体框和投影框的交集（通常是可见矩形）。 下面的图片展示了这些属性。  
有关更多详细信息，请访问[此页面](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html)。

下面的代码片段展示了如何裁剪页面：

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleCropPages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    // 打开文档
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    public static void CropPagesPDF() {
        Document pdfDocument = new Document("crop_page.pdf");
        Page page = pdfDocument.getPages().get_Item(1);

        System.out.println(page.getCropBox());
        System.out.println(page.getTrimBox());
        System.out.println(page.getArtBox());
        System.out.println(page.getBleedBox());
        System.out.println(page.getMediaBox());

        // 创建新的 Box 矩形
        Rectangle newBox = new Rectangle(200, 220, 2170, 1520);

        page.setCropBox(newBox);
        page.setTrimBox(newBox);
        page.setArtBox(newBox);
        page.setBleedBox(newBox);

        // 保存输出文档
        pdfDocument.save(_dataDir + "crop_page_modified.pdf");
    }
}
```

In this example we used a sample file [here](crop_page.pdf). Initially our page looks like shown on the Figure 1.  
在这个例子中，我们使用了一个示例文件[这里](crop_page.pdf)。最初我们的页面如图1所示。  
![Figure 1. Cropped Page](crop_page.png)  

After the change, the page will look like Figure 2.  
更改后，页面将如图2所示。  
![Figure 2. Cropped Page](crop_page2.png)