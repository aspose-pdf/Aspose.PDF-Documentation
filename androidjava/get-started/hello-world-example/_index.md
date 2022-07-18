---
title: Hello World Java Example
linktitle: Hello World Example
type: docs
weight: 20
url: /androidjava/hello-world-example/
description: This page show how use simple programming for create a PDF document containing text - Hello World using Aspose.PDF for Android.
lastmod: "2021-08-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Hello World Example

A "Hello World" example is traditionally used to introduce features of a programming language or software with a simple use case.

Aspose.PDF for Android via Java API empowers Java application developers to create, read, edit and manipulate PDF files in their applications. It lets you read and convert several different file types to and from PDF file format. This Hello World article shows how to create a PDF file in Java using Aspose.PDF for Android via Java  API.
After [installing Aspose.PDF for Android via Java](/pdf/androidjava/installation/) in your environment, you can execute the below code sample to see how Aspose.PDF API works.

Below code snippet follows these steps:

1. Instantiate a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document) object
1. Add a [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/page) to document object
1. Create a [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment) object
1. Add TextFragment to [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) collection of the page
1. Save the resultant PDF document

The following code snippet shows basic steps of the working of Aspose.PDF for Android API.

```java
package com.aspose.pdf.examplesimple;

import android.app.Activity;
import android.os.Bundle;
import android.os.Environment;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import com.aspose.pdf.Document;
import com.aspose.pdf.Page;
import com.aspose.pdf.TextFragment;

import java.io.File;


public class MainActivity extends Activity {
    EditText inputText;
    TextView response;
    Button saveButton,readButton;

    File myExternalFile;
    String myData = "";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        inputText = (EditText) findViewById(R.id.myInputText);
        response = (TextView) findViewById(R.id.response);


        saveButton =
                (Button) findViewById(R.id.saveExternalStorage);
        saveButton.setOnClickListener(v -> {
            try {
                // Initialize document object
                Document document = new Document();

                //Add page
                Page page = document.getPages().add();

                myData = inputText.getText().toString().trim();
                if (myData.equals("")) {
                    myData = "Hello, world!";
                }

                // Add text to new page
                page.getParagraphs().add(new TextFragment(myData));

                // Save updated PDF
                document.save(myExternalFile.getAbsolutePath());

            } catch (Exception e) {
                e.printStackTrace();
            }
            inputText.setText("");
            response.setText(R.string.save_message);
        });

        readButton = (Button) findViewById(R.id.getExternalStorage);
        readButton.setOnClickListener(v -> {
            try {
                // Initialize document object
                Document document = new Document(myExternalFile.getAbsolutePath());
                myData = "Document contain "+document.getPages().size()+" page(s).";
            } catch (Exception e) {
                e.printStackTrace();
            }
            inputText.setText(myData);
            response.setText(R.string.read_message);
        });

        if (!isExternalStorageAvailable() || isExternalStorageReadOnly()) {
            saveButton.setEnabled(false);
        }
        else {
            String filename = "SampleFile.pdf";
            String filepath = "MyFileStorage";
            myExternalFile = new File(getExternalFilesDir(filepath), filename);
        }
    }
    private static boolean isExternalStorageReadOnly() {
        String extStorageState = Environment.getExternalStorageState();
        return Environment.MEDIA_MOUNTED_READ_ONLY.equals(extStorageState);
    }

    private static boolean isExternalStorageAvailable() {
        String extStorageState = Environment.getExternalStorageState();
        return Environment.MEDIA_MOUNTED.equals(extStorageState);
    }
}
```
