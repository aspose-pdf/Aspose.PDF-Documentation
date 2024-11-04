---
title: Hello World Java 示例
linktitle: Hello World 示例
type: docs
weight: 20
url: /androidjava/hello-world-example/
description: 本页展示如何使用简单的编程创建包含文本 - Hello World 的 PDF 文档，使用 Aspose.PDF for Android。
lastmod: "2021-08-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Hello World 示例

“Hello World” 示例传统上用于通过一个简单的用例介绍编程语言或软件的功能。

Aspose.PDF for Android via Java API 使 Java 应用程序开发人员能够在其应用程序中创建、读取、编辑和操作 PDF 文件。它允许您读取和转换多种不同的文件类型到 PDF 文件格式和从 PDF 文件格式转换。本 Hello World 文章展示了如何使用 Aspose.PDF for Android via Java API 在 Java 中创建 PDF 文件。
在您的环境中[安装 Aspose.PDF for Android via Java](/pdf/androidjava/installation/)后，您可以执行下面的代码示例，看看 Aspose.PDF API 是如何工作的。

下面的代码片段遵循这些步骤：

1. 实例化一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document) 对象
1. 向文档对象添加一个 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/page)
1. 创建一个 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment) 对象
1. 将 TextFragment 添加到页面的 [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) 集合中
1. 保存生成的 PDF 文档

以下代码片段展示了 Aspose.PDF for Android API 的基本工作步骤。

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
                // 初始化文档对象
                Document document = new Document();

                // 添加页面
                Page page = document.getPages().add();

                myData = inputText.getText().toString().trim();
                if (myData.equals("")) {
                    myData = "Hello, world!";
                }

                // 将文本添加到新页面
                page.getParagraphs().add(new TextFragment(myData));

                // 保存更新的 PDF
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
                // 初始化文档对象
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