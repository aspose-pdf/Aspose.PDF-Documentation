---
title: 在 PHP 中优化 PDF 文档以用于网络
type: docs
weight: 60
url: /zh/java/optimize-pdf-document-for-the-web-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 优化 PDF 以用于网络

要使用 **Aspose.PDF Java for PHP** 优化 PDF 文档以用于网络，只需调用 **Optimize** 类的 **optimize_web** 方法。

PHP 代码

```php

 public static function optimize_web($dataDir=null)

{

    # 打开一个 pdf 文档。

    $doc = new Document($dataDir . "input1.pdf");

    # 优化以用于网络

    $doc->optimize();

    # 保存输出文档

    $doc->save($dataDir . "Optimized_Web.pdf");

    print "已优化 PDF 以用于网络，请检查输出文件。" . PHP_EOL;

}    
```

**下载运行代码**

从以下任何一个社交编码网站下载 **Optimize PDF for Web (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/Optimize.php)