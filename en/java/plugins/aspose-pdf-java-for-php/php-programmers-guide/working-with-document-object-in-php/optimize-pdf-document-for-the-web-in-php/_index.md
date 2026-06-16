---
title: Optimize PDF Document for the Web in PHP
linktitle: Optimize PDF Document for the Web in PHP
type: docs
weight: 60
url: /java/optimize-pdf-document-for-the-web-in-php/
description: Learn how to optimize a PDF document for faster web performance and reduced file size in PHP with Aspose.PDF.
lastmod: "2026-06-09"
---
## Aspose.PDF - Optimize PDF for Web

To optimize PDF document for the web using **Aspose.PDF Java for PHP**, simply invoke **optimize_web** method ofВ  **Optimize** class.

PHP Code

```php

 public static function optimize_web($dataDir=null)

{

    # Open a pdf document.

    $doc = new Document($dataDir . "input1.pdf");

    # Optimize for web

    $doc->optimize();

    #Save output document

    $doc->save($dataDir . "Optimized_Web.pdf");

    print "Optimized PDF for the Web, please check output file." . PHP_EOL;

}В В В
```

**Download Running Code**

DownloadВ **Optimize PDF for Web (Aspose.PDF)**В fromВ any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/Optimize.php)
