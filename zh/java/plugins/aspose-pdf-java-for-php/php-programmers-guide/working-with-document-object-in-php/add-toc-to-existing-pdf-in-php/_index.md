---
title: 向现有 PDF 添加目录在 PHP 中
type: docs
weight: 20
url: zh/java/add-toc-to-existing-pdf-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 添加目录

要在 Pdf 文档中使用 **Aspose.PDF Java for PHP** 添加目录，只需调用 **AddToc** 类。

PHP 代码

```php

# 打开一个 pdf 文档。
$doc = new Document($dataDir . "input1.pdf");

# 访问 PDF 文件的第一页
$toc_page = $doc->getPages()->insert(1);

# 创建对象以表示目录信息
$toc_info = new TocInfo();
$title = new TextFragment("目录");
$title->getTextState()->setFontSize(20);
#title.getTextState().setFontStyle(Rjb::import('com.aspose.pdf.FontStyles.Bold'))

# 设置目录的标题
$toc_info->setTitle($title);
$toc_page->setTocInfo($toc_info);

# 创建将用作目录元素的字符串对象
$titles = array("首页", "第二页");

$i = 0;
while ($i < 2){

    # 创建 Heading 对象
    $heading2 = new Heading(1);

    $segment2 = new TextSegment();
    $heading2->setTocPage($toc_page);
    $heading2->getSegments()->add($segment2);

    # 为标题对象指定目标页面
    $heading2->setDestinationPage($doc->getPages()->get_Item($i + 2));

    # 目标页面
    $heading2->setTop($doc->getPages()->get_Item($i + 2)->getRect()->getHeight());

    # 目标坐标
    $segment2->setText($titles[$i]);

    # 将标题添加到包含目录的页面
    $toc_page->getParagraphs()->add($heading2);

    $i +=1;

}

# 保存 PDF 文档
$doc->save($dataDir . "TOC.pdf");

print "目录添加成功，请检查输出文件。";

```


**下载运行代码**

从以下任一社交编码网站下载 **添加目录 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/AddToc.php)