---
title: Create PDF Document 
linktitle: Create
type: docs
weight: 10
url: /php-java/create-document/
description: Learn how to create PDF file in Aspose.PDF for PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for PHP via Java** API lets application developers to embed PDF documents processing functionality in their applications. It can be used to create and read PDF files without the need of any other software installed on the underlying machine. Aspose.PDF for PHP via Java can be used in a variety of application types such as Desktop, JSP, and JSF applications.

## How to create PDF File using PHP via Java

To create a PDF file using PHP via Java, the following steps can be used.

1. Instantiate a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object
1. Add a [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) to document object
1. Create a [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment) object
1. Add [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment) to [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) collection of the page
1. Save the resultant PDF document

```php

    $document = new Document();    
    $page = $document->getPages()->add();
    $textFragment = new TextFragment("Hello World!");    
    $page->getParagraphs()->add($textFragment);
    $document->save($outputFile);
```
