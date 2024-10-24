---
title: Working with PDF File Metadata 
linktitle: PDF File Metadata
type: docs
weight: 140
url: /php-java/pdf-file-metadata/
description: This section explains how to get PDF file information, how to get XMP Metadata from a PDF file, set PDF File Information.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Get PDF File Information

To get file-specific information about a PDF file, first get the 'docInfo' object using the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) class  [getInfo()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getInfo--). Once the 'docInfo' object is retrieved, you can get the values of the individual properties.

The following code snippet shows you how to set PDF file information.

```php

    // Open document
    $document = new Document($inputFile);
    
    // Get document information
    $docInfo = $document->getInfo();

    // Show document information
    $responseData1 = "Author: " . $docInfo->getAuthor() . ", ";
    $responseData2 = "Creation Date: " . $docInfo->getCreationDate() . ", ";
    $responseData3 = "Keywords: " . $docInfo->getKeywords() . ", ";
    $responseData4 = "Modify Date: " . $docInfo->getModDate() . ", ";
    $responseData5 = "Subject: " . $docInfo->getSubject() . ", ";
    $responseData6 = "Title: " . $docInfo->getTitle() . "";

    $document->close();
```

