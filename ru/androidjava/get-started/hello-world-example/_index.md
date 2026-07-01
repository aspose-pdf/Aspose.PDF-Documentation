---
title: Пример Hello World на Java
linktitle: Пример Hello World
type: docs
weight: 20
url: /ru/androidjava/hello-world-example/
description: Эта страница показывает, как использовать простое программирование для создания PDF‑документа, содержащего текст - Hello World с помощью Aspose.PDF for Android.
lastmod: "2026-07-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Пример Hello World

Пример “Hello World” традиционно используется для представления возможностей языка программирования или программного обеспечения с простым вариантом использования.

Aspose.PDF for Android via Java API предоставляет разработчикам Java‑приложений возможности создавать, читать, редактировать и обрабатывать PDF‑файлы в своих приложениях. Он позволяет читать и конвертировать различные типы файлов в формат PDF и из него. Эта статья Hello World показывает, как создать PDF‑файл на Java с использованием Aspose.PDF for Android via Java API.
После [установка Aspose.PDF for Android через Java](/pdf/ru/androidjava/installation/) в вашей среде вы можете выполнить приведённый ниже пример кода, чтобы увидеть, как работает API Aspose.PDF.

Ниже приведённый фрагмент кода следует этим шагам:

1. Создайте экземпляр [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document) объект
1. Добавьте [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/page) к объекту документа
1. Создайте [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment) объект
1. Добавьте TextFragment к [Параграф](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) коллекция страницы
1. Сохраните полученный PDF‑документ

Ниже приведён фрагмент кода, показывающий базовые шаги работы Aspose.PDF for Android API.

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


