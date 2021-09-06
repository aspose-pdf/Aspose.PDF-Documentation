---
title: Hello World Java Example
linktitle: Hello World Example
type: docs
weight: 20
url: /androidjava/hello-world-example/
description: This page show how use simple programming for create a PDF document containing text - Hello World using Aspose.PDF for Android.
lastmod: "2021-08-05"
sitemap:
    changefreq: "montly"
    priority: 0.7
---

## Hello World Example

A "Hello World" example is traditionally used to introduce features of a programming language or software with a simple use case.

Aspose.PDF for Java API empowers Java application developers to create, read, edit and manipulate PDF files in their applications. It lets you read and convert several different file types to and from PDF file format. This Hello World article shows how to create a PDF file in Java using Aspose.PDF for Java API.
After [installing Aspose.PDF for Java](/pdf/java/installation/) in your environment, you can execute the below code sample to see how Aspose.PDF API works.

Below code snippet follows these steps:

1. Instantiate a [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document) object
1. Add a [Page](https://apireference.aspose.com/pdf/java/com.aspose.pdf.class-use/page) to document object
1. Create a [TextFragment](https://apireference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment) object
1. Add TextFragment to [Paragraph](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) collection of the page
1. Save the resultant PDF document

The following code snippet shows basic steps of the working of Aspose.PDF for Android API.

```java
// Initialize document object
Document document = new Document();
 
//Add page
Page page = document.getPages().add();
 
// Add text to new page
page.getParagraphs().add(new TextFragment("Hello World!"));
 
// Save updated PDF
document.save("HelloWorld_out.pdf");
```

The whole sample is more complex. Let's take a look at the main scene.

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="fill_parent" android:layout_height="fill_parent"
    android:orientation="vertical">

    <TextView android:layout_width="fill_parent"
        android:layout_height="wrap_content"
        android:text="@string/logo"
        android:textSize="24sp"/>

    <EditText android:id="@+id/myInputText"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:ems="10" android:lines="5"
        android:minLines="3" android:gravity="top|left"
        android:inputType="textMultiLine">

        <requestFocus />
    </EditText>

    <LinearLayout
        android:layout_width="match_parent" android:layout_height="wrap_content"
        android:orientation="horizontal"
        android:weightSum="1.0"
        android:layout_marginTop="20dp">

        <Button android:id="@+id/saveExternalStorage"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="SAVE"
            android:layout_weight="0.5"/>

        <Button android:id="@+id/getExternalStorage"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:layout_weight="0.5"
            android:text="READ" />

    </LinearLayout>

    <TextView android:id="@+id/response"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content" android:padding="5dp"
        android:text=""
        android:textAppearance="?android:attr/textAppearanceMedium" />

</LinearLayout>
```

On this scene we have text view, input box and 2 buttons. User can type own text and then write it into PDF.
Our sample app has 2 buttons. The 1st button will be used for saving created PDF, and 2nd one - for reading data from PDF.

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
