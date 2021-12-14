---
title: Create Links in PDF file with Java
linktitle: Create Links
type: docs
weight: 10
url: /androidjava/create-links/
description: This section explains how to create links in your PDF document with Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Create Links

Aspose.PDF for Java allows you to add a link to an external PDF file so that you can link several documents together.
By adding a link to an application into a document, it is possible to link to applications from a document. This is useful when you want readers to take a certain action at a specific point in a tutorial, for example, or to create a feature-rich document. To create an application link:

1. [Create a Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document) object.
1. Get the [Page](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Page) you want to add link to.
1. Create a [LinkAnnotation](https://apireference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) object using the [Page](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Page) and [Rectangle](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) objects.
1. Set the link attributes using the [LinkAnnotation](https://apireference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) object.
1. Also, set the to [LaunchAction](https://apireference.aspose.com/pdf/java/com.aspose.pdf/LaunchAction) object’s and call setAction(..) method.
1. When creating the [LaunchAction](https://apireference.aspose.com/pdf/java/com.aspose.pdf/LaunchAction) object, specify the application you want to launch.
1. Add the link to the Page object’s [Annotations](https://apireference.aspose.com/pdf/java/com.aspose.pdf/AnnotationCollection) collection.
1. Finally, save the updated PDF using the [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document) object’s Save method.

The following code snippet shows how to create a link to an application in a PDF file.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;


public class ExampleLinks {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    private static String GetDataDir() {
        String os = System.getProperty("os.name");
        if (os.startsWith("Windows"))
            _dataDir = "C:\\Samples\\Links-Actions";
        return _dataDir;
    }

    public static void CreateLink() {

        // Open document
        Document document = new Document(GetDataDir() + "CreateApplicationLink.pdf");

        // Create link
        Page page = document.getPages().get_Item(1);
        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(100, 200, 300, 300));
        link.setColor(Color.getGreen());
        link.setAction(new LaunchAction(document, _dataDir + "sample.pdf"));
        page.getAnnotations().add(link);

        // Save updated document
        document.save(_dataDir + "CreateApplicationLink_out.pdf");
    }
```

### Create PDF Document Link in a PDF File

Aspose.PDF for Java allows you to add a link to an external PDF file so that you can link several documents together. To create a PDF document link:

1. First, create a [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document) object.
1. Then, get the particular [Page](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Page) you want to add the link to.
1. Create a [LinkAnnotation](https://apireference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) object using the [Page](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Page and [Rectangle](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) objects.
1. Set the link attributes using the [LinkAnnotation](https://apireference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) object.
1. Call setAction(..) method and pass [GoToRemoteAction](https://apireference.aspose.com/pdf/java/com.aspose.pdf/GoToRemoteAction) object.
1. While creating the [GoToRemoteAction](https://apireference.aspose.com/pdf/java/com.aspose.pdf/GoToRemoteAction) object, specify the PDF file that should launch, as well as the page number it should open on.
1. Add the link to the Page object’s [Annotations](https://apireference.aspose.com/pdf/java/com.aspose.pdf/AnnotationCollection) collection.
1. Finally, save the updated PDF using the [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document) object’s Save method.

The following code snippet shows how to create PDF document link in a PDF file.

 ```java
    public static void CreatePDFDocumentLink() {

        // Open document
        Document document = new Document(_dataDir + "CreateDocumentLink.pdf");

        // Create link
        Page page = document.getPages().get_Item(1);
        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(100, 200, 300, 300));
        link.setColor(Color.getGreen());
        link.setAction(new GoToRemoteAction(_dataDir + "sample.pdf", 1));
        page.getAnnotations().add(link);

        // Save updated document
        document.save(_dataDir + "CreateDocumentLink_out.pdf");
    }
```