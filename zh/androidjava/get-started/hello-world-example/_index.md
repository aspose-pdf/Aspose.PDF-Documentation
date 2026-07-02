---
title: Hello World Java 示例
linktitle: Hello World 示例
type: docs
weight: 20
url: /zh/androidjava/hello-world-example/
description: 本页展示如何使用简单的编程创建包含文本 “Hello World” 的 PDF 文档，使用 Aspose.PDF for Android。
lastmod: "2026-07-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Hello World 示例

“Hello World” 示例传统上用于通过一个简单的用例来介绍编程语言或软件的特性。

Aspose.PDF for Android via Java API 为 Java 应用程序开发人员提供了在其应用中创建、读取、编辑和操作 PDF 文件的能力。它允许您读取并在 PDF 文件格式之间相互转换多种不同的文件类型。本文的 Hello World 示例展示了如何使用 Aspose.PDF for Android via Java API 在 Java 中创建 PDF 文件。
之后 [通过 Java 安装 Aspose.PDF for Android](/pdf/zh/androidjava/installation/) 在您的环境中，您可以执行以下代码示例，以了解 Aspose.PDF API 的工作方式。

下面的代码片段遵循以下步骤：

1. 实例化一个 [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document) 对象
1. 添加一个 [页面](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/page) 到文档对象
1. 创建一个 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment) 对象
1. 将 TextFragment 添加到 [段落](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) 页面的集合
1. 保存生成的 PDF 文档

下面的代码片段展示了 Aspose.PDF for Android API 的工作基本步骤。

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

