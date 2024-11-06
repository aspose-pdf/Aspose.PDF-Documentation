---

title: 从PDF中提取段落  
linktitle: 提取段落  
type: docs  
weight: 20  
url: zh/php-java/extract-paragraph-from-pdf/  
description: 本文介绍如何使用ParagraphAbsorber——Aspose.PDF中的一个特殊工具来从PDF文档中提取文本。  
lastmod: "2024-05-20"  
sitemap:  
changefreq: "monthly"  
priority: 0.7  
---

## 以段落形式从PDF文档中提取文本

我们可以通过在单个页面或整个文档中搜索特定文本（使用“纯文本”或“正则表达式”）来获取PDF文档中的文本，或者我们可以获取单个页面、页面范围或整个文档的完整文本。然而，在某些情况下，您需要从PDF文档中提取段落或以段落形式的文本。我们已经实现了在PDF文档页面的文本中搜索章节和段落的功能。我们引入了ParagraphAbsorber类（类似于TextFragmentAbsorber和TextAbsorber），可以用于从PDF文档中提取段落。

### 遍历段落集合并获取它们的文本

```php

// 打开一个现有的PDF文件
$document = new Document($inputFile);
// 实例化 ParagraphAbsorber
$absorber = new ParagraphAbsorber();
$absorber->visit($document);
$responseData = "";

foreach ($absorber->getPageMarkups() as $markup) {
    $i = 1;

    foreach ($markup->getSections() as $section) {
        $j = 1;

        foreach ($section->getParagraphs() as $paragraph) {
            $paragraphText = "\r\n";

            foreach ($paragraph->getLines() as $line) {
                foreach ($line as $fragment) {
                    $paragraphText = $paragraphText . $fragment->getText();
                }
                $paragraphText = $paragraphText . "\r\n";
            }
            $paragraphText = $paragraphText . "\r\n";

            $responseData = $responseData . "第 " . $j++ . " 段，第 " . $i++ . " 节，第 " . markup->getNumber() . " 页:";
            $responseData = $responseData . $paragraphText;
            $j++;
        }
        $i++;
    }
}

// 将提取的文本保存到输出文件。
file_put_contents($outputFile, $responseData);
```