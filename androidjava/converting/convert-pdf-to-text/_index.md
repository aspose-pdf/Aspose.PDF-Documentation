---
title: Convert PDF to text 
linktitle: Convert PDF to text
type: docs
weight: 120
url: /androidjava/convert-pdf-to-txt/
lastmod: "2021-06-05"
description: With Aspose.PDF for Android via Java you can convert a whole PDF document to a text file or convert only a PDF page to a text file.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---


{{% alert color="primary" %}} 

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/pdf-to-txt](https://products.aspose.app/pdf/conversion/pdf-to-txt)

{{% /alert %}}

## Convert PDF page to text file

You can convert PDF document to TXT file with Aspose.PDF for Android via Java. You should use Visit method of [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) class for resolve this task.

The following code snippet explains how to extract the texts from the particular pages.

```java
public void convertPDFPagesToTXT() {
        // Open document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        TextAbsorber ta = new TextAbsorber();
        int[] pages = new int[] { 1, 3, 4 };

        for (int page : pages) {
            ta.visit(document.getPages().get_Item(page));
        }
        File txtFileName = new File(fileStorage, "PDF-to-Text.txt");

        // Save the extracted text in text file
        BufferedWriter writer;
        try {
            writer = new BufferedWriter(new FileWriter(txtFileName));
            writer.write(ta.getText());
            writer.close();
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```
