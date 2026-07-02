---
title: مثال Hello World بلغة Java
linktitle: مثال Hello World
type: docs
weight: 20
url: /ar/androidjava/hello-world-example/
description: تُظهر هذه الصفحة كيفية استخدام برمجة بسيطة لإنشاء مستند PDF يحتوي على نص - Hello World باستخدام Aspose.PDF for Android.
lastmod: "2026-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## مثال Hello World

يُستخدم مثال \"Hello World\" تقليديًا لتقديم ميزات لغة برمجة أو برنامج ما من خلال حالة بسيطة.

يوفر Aspose.PDF for Android عبر Java API للمطورين الذين يستخدمون جافا القدرة على إنشاء ملفات PDF وقراءتها وتحريرها ومعالجتها في تطبيقاتهم. يتيح لك قراءة وتحويل عدة أنواع مختلفة من الملفات إلى تنسيق PDF ومنه. تُظهر مقالة Hello World هذه كيفية إنشاء ملف PDF في جافا باستخدام Aspose.PDF for Android عبر Java API.
بعد [تثبيت Aspose.PDF لـ Android عبر Java](/pdf/ar/androidjava/installation/) في بيئتك، يمكنك تنفيذ عينة الكود أدناه لمعرفة كيف يعمل Aspose.PDF API.

يتبع مقتطف الكود أدناه هذه الخطوات:

1. إنشاء كائن [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document) كائن
1. إضافة [صفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/page) إلى كائن المستند
1. إنشاء [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment) كائن
1. إضافة TextFragment إلى [فقرة](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) مجموعة من الصفحة
1. احفظ مستند PDF الناتج

يوضح مقطع الشيفرة التالي الخطوات الأساسية لعمل Aspose.PDF for Android API.

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

