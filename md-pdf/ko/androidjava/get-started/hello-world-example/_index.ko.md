---
title: 헬로 월드 자바 예제
linktitle: 헬로 월드 예제
type: docs
weight: 20
url: /androidjava/hello-world-example/
description: 이 페이지는 Aspose.PDF for Android를 사용하여 텍스트 - 헬로 월드를 포함하는 PDF 문서를 생성하기 위한 간단한 프로그래밍 방법을 보여줍니다.
lastmod: "2021-08-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 헬로 월드 예제

"헬로 월드" 예제는 전통적으로 프로그래밍 언어나 소프트웨어의 기능을 간단한 사용 사례로 소개하는 데 사용됩니다.

Aspose.PDF for Android via Java API는 Java 애플리케이션 개발자가 애플리케이션 내에서 PDF 파일을 생성, 읽기, 편집 및 조작할 수 있도록 합니다. 여러 다른 파일 형식을 PDF 파일 형식으로 읽고 변환할 수 있습니다. 이 헬로 월드 문서는 Aspose.PDF for Android via Java API를 사용하여 Java에서 PDF 파일을 생성하는 방법을 보여줍니다.
환경에서 [Aspose.PDF for Android via Java 설치](/pdf/androidjava/installation/) 후, 아래 코드 샘플을 실행하여 Aspose.PDF API가 어떻게 작동하는지 확인할 수 있습니다.

아래 코드 스니펫은 다음 단계를 따릅니다:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document) 객체 인스턴스화
1. 문서 객체에 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/page) 추가
1. [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment) 객체 생성
1. 페이지의 [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) 컬렉션에 TextFragment 추가
1. 결과 PDF 문서 저장

다음 코드 스니펫은 Aspose.PDF for Android API의 기본 작동 단계를 보여줍니다.

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
                // 문서 객체 초기화
                Document document = new Document();

                // 페이지 추가
                Page page = document.getPages().add();

                myData = inputText.getText().toString().trim();
                if (myData.equals("")) {
                    myData = "Hello, world!";
                }

                // 새 페이지에 텍스트 추가
                page.getParagraphs().add(new TextFragment(myData));

                // 업데이트된 PDF 저장
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
                // 문서 객체 초기화
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