---
title: Add Image to Existing PDF File 
linktitle: Add Image
type: docs
weight: 10
url: /php-java/add-image-to-existing-pdf-file/
description: This section describes how to add image to existing PDF file using PHP.
lastmod: "2024-06-05"
---

Every PDF page contains Resources and Contents properties. Resources can be images and forms for example, while content is represented by a set of PDF operators. Each operator has its name and argument. This example uses operators to add an image to a PDF file.

To add an image to an existing PDF file:

- Create a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object and open the input PDF document.
- Get the page you want to add an image to.
- Add a new page to the document.
- Set the size of the page to 1190.7 x 841.995.
- Add an image to the page using the specified image file and the crop box of the page.
- Save the file.

The following code snippet shows how to add the image in a PDF document.

```php

    // Open the document using the specified input file.
    $document = new Document($inputFile);
    
    // Add a new page to the document.
    $page = $document->getPages()->add();
    
    // Set the size of the page to 1190.7 x 841.995.
    $page->setPageSize(1190.7, 841.995);
    
    // Add an image to the page using the specified image file and the crop box of the page.
    $page->addImage($imageFileName, $page->getCropBox());
    
    // Save the modified document to the specified output file.
    $document->save($outputFile);
    
    // Close the document.
    $document->close();
```

