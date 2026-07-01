---
title: Hello World Java 예제
linktitle: Hello World 예제
type: docs
weight: 20
url: /ko/androidjava/hello-world-example/
description: 이 페이지에서는 Aspose.PDF for Android을 사용하여 텍스트 - Hello World가 포함된 PDF 문서를 만드는 간단한 프로그래밍 방법을 보여줍니다.
lastmod: "2026-07-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Hello World 예제

"Hello World" 예제는 전통적으로 간단한 사용 사례를 통해 프로그래밍 언어 또는 소프트웨어의 기능을 소개하는 데 사용됩니다.

Aspose.PDF for Android via Java API는 Java 애플리케이션 개발자가 애플리케이션에서 PDF 파일을 생성, 읽기, 편집 및 조작할 수 있도록 지원합니다. 이를 통해 여러 파일 형식을 PDF 파일 형식으로 읽고 변환할 수 있습니다. 이 Hello World 기사에서는 Aspose.PDF for Android via Java  API를 사용하여 Java에서 PDF 파일을 만드는 방법을 보여줍니다.
이후 [Java를 통해 Android용 Aspose.PDF 설치](/pdf/ko/androidjava/installation/) 환경에서 아래 코드 샘플을 실행하여 Aspose.PDF API가 어떻게 작동하는지 확인할 수 있습니다.

아래 코드 스니펫은 다음 단계들을 따릅니다:

1. 인스턴스화합니다 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document) 객체
1. 추가 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/page) 문서 객체에
1. 생성 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment) 객체
1. TextFragment를 추가 [단락](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) 페이지 컬렉션
1. 결과 PDF 문서를 저장합니다

다음 코드 조각은 Aspose.PDF for Android API의 작동 기본 단계들을 보여줍니다.

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

