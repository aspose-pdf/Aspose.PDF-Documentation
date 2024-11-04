---
title: Hello World Java Example
linktitle: Hello World Example
type: docs
weight: 20
url: /androidjava/hello-world-example/
description: هذه الصفحة تعرض كيفية استخدام البرمجة البسيطة لإنشاء مستند PDF يحتوي على نص - Hello World باستخدام Aspose.PDF لنظام Android.
lastmod: "2021-08-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## مثال Hello World

يستخدم عادةً مثال "Hello World" لتعريف ميزات لغة البرمجة أو البرنامج من خلال حالة استخدام بسيطة.

تمكن Aspose.PDF for Android عبر Java API مطوري تطبيقات Java من إنشاء وقراءة وتحرير ومعالجة ملفات PDF في تطبيقاتهم. يتيح لك قراءة وتحويل عدة أنواع ملفات مختلفة إلى ومن تنسيق ملف PDF. يوضح هذا المقال كيفية إنشاء ملف PDF في Java باستخدام Aspose.PDF لنظام Android عبر Java API.
بعد [تثبيت Aspose.PDF لنظام Android عبر Java](/pdf/androidjava/installation/) في بيئتك، يمكنك تنفيذ عينة الكود أدناه لترى كيف يعمل Aspose.PDF API.

يتبع مقطع الكود أدناه هذه الخطوات:

1. إنشاء كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document)
1. إضافة [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/page) إلى كائن المستند
1. إنشاء كائن [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment)
1. إضافة TextFragment إلى مجموعة [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) في الصفحة
1. حفظ مستند PDF الناتج

يوضح مقطع الشيفرة التالي الخطوات الأساسية لعمل Aspose.PDF لـ Android API.

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
                // تهيئة كائن المستند
                Document document = new Document();

                //إضافة صفحة
                Page page = document.getPages().add();

                myData = inputText.getText().toString().trim();
                if (myData.equals("")) {
                    myData = "Hello, world!";
                }

                // إضافة نص إلى الصفحة الجديدة
                page.getParagraphs().add(new TextFragment(myData));

                // حفظ PDF المحدث
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
                // تهيئة كائن المستند
                Document document = new Document(myExternalFile.getAbsolutePath());
                myData = "المستند يحتوي على " + document.getPages().size() + " صفحة/صفحات.";
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