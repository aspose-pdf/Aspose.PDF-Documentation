---
title: Пример Hello World на Java
linktitle: Пример Hello World
type: docs
weight: 20
url: /androidjava/hello-world-example/
description: Эта страница показывает, как использовать простое программирование для создания PDF-документа, содержащего текст - Hello World, с использованием Aspose.PDF для Android.
lastmod: "2021-08-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Пример Hello World

Пример "Hello World" традиционно используется для введения в особенности языка программирования или программного обеспечения с простым примером использования.

Aspose.PDF для Android через Java API позволяет разработчикам Java-приложений создавать, читать, редактировать и манипулировать PDF-файлами в своих приложениях. Он позволяет читать и конвертировать различные типы файлов в формат PDF и из него. Эта статья Hello World показывает, как создать PDF-файл на Java, используя Aspose.PDF для Android через Java API.
После [установки Aspose.PDF для Android через Java](/pdf/androidjava/installation/) в вашей среде, вы можете выполнить приведенный ниже пример кода, чтобы увидеть, как работает API Aspose.PDF.

Пример кода ниже следует этим шагам:

1. Создайте объект [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document)
1. Добавьте [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/page) к объекту документа
1. Создайте объект [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment)
1. Добавьте TextFragment в коллекцию [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) страницы
1. Сохраните итоговый PDF документ

Следующий фрагмент кода показывает основные шаги работы Aspose.PDF для Android API.

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
                // Инициализация объекта документа
                Document document = new Document();

                //Добавить страницу
                Page page = document.getPages().add();

                myData = inputText.getText().toString().trim();
                if (myData.equals("")) {
                    myData = "Привет, мир!";
                }

                // Добавить текст на новую страницу
                page.getParagraphs().add(new TextFragment(myData));

                // Сохранить обновленный PDF
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
                // Инициализация объекта документа
                Document document = new Document(myExternalFile.getAbsolutePath());
                myData = "Документ содержит "+document.getPages().size()+" страницу(ы).";
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