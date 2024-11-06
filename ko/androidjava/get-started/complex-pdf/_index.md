---
title: Aspose.PDF를 사용하여 복잡한 PDF 생성
linktitle: 복잡한 PDF 생성
type: docs
weight: 30
url: ko/androidjava/complex-pdf-example/
description: Aspose.PDF for Android via Java를 사용하면 하나의 문서에 이미지, 텍스트 조각 및 표를 포함하는 더욱 복잡한 문서를 생성할 수 있습니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

[Hello, World](/pdf/java/hello-world-example/) 예제는 Java와 Aspose.PDF를 사용하여 PDF 문서를 생성하는 간단한 단계를 보여주었습니다. 이 기사에서는 Java와 Aspose.PDF for Java를 사용하여 더 복잡한 문서를 만드는 방법을 살펴보겠습니다. 예를 들어, 승객 페리 서비스를 운영하는 가상의 회사의 문서를 살펴보겠습니다.
우리의 문서에는 이미지, 두 개의 텍스트 조각(헤더 및 단락), 그리고 표가 포함될 것입니다. 이러한 문서를 만들기 위해 DOM 기반 접근 방식을 사용할 것입니다. [DOM API의 기초](/pdf/java/basics-of-dom-api/) 섹션에서 더 읽어볼 수 있습니다.

문서를 처음부터 생성하려면 특정 단계를 따라야 합니다:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) 객체를 인스턴스화합니다. 이 단계에서는 메타데이터가 포함된 빈 PDF 문서를 생성하지만 페이지는 없습니다.
1. 문서 객체에 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page)를 추가합니다. 이제 문서에 한 페이지가 있게 됩니다.
1. 이미지를 추가하기 위해 FileInputStream을 생성하고, 필요한 파일의 경로를 지정합니다. 그런 다음 주어진 좌표로 사각형에 그림을 추가합니다.
1. 헤더를 위한 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment)를 생성합니다. 헤더에는 Arial 폰트와 24pt의 글꼴 크기, 중앙 정렬을 사용할 것입니다.
1. 페이지의 [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--)에 헤더를 추가합니다.
1. 설명을 위한 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment)를 생성합니다. 설명에는 Arial 폰트와 24pt의 글꼴 크기, 중앙 정렬을 사용할 것입니다.

1. 페이지 단락에 (설명)을 추가합니다. 우리의 예제에서는 "Helvetica"와 "Times Roman" 글꼴을 사용했지만, Android에는 세 가지 시스템 전역 글꼴만 있다는 것을 명심하세요:

- normal (Droid Sans);
- serif (Droid Serif);
- monospace (Droid Sans Mono).

1. 테이블을 생성하고, 테이블 속성을 추가합니다.
1. 페이지에 (테이블)을 [단락](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--)에 추가합니다.
1. 문서를 "Complex.pdf"로 저장합니다.

마지막에 "PDF 문서가 생성되었습니다!"라는 메시지가 있는 팝업이 표시됩니다.

![Aspose.PDF의 Android용 Java 복잡한 예제](complex_example.png)

```java
package com.aspose.pdf.examplecomplex;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.os.Environment;
import android.widget.Button;
import android.widget.Toast;

import com.aspose.pdf.BorderInfo;
import com.aspose.pdf.BorderSide;
import com.aspose.pdf.Cell;
import com.aspose.pdf.Color;
import com.aspose.pdf.Document;
import com.aspose.pdf.FontRepository;
import com.aspose.pdf.HorizontalAlignment;
import com.aspose.pdf.Page;
import com.aspose.pdf.Position;
import com.aspose.pdf.Rectangle;
import com.aspose.pdf.Row;
import com.aspose.pdf.Table;
import com.aspose.pdf.TextFragment;

import java.io.File;
import java.io.FileInputStream;
import java.time.Duration;
import java.time.LocalTime;

public class MainActivity extends AppCompatActivity {

    Button generate_button;
    File myExternalFile;
    String filepath;
    String filename;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        generate_button = (Button) findViewById(R.id.button);
        generate_button.setOnClickListener(v->RunComplexExample());

        if(!isExternalStorageAvailable()||isExternalStorageReadOnly()){
            generate_button.setEnabled(false);
        }
        else{
            filepath = "MyFileStorage";
            filename = "SampleFile.pdf";
            myExternalFile=new File(getExternalFilesDir(filepath), filename);
        }

    }

    private void RunComplexExample() {
        // 문서 객체 초기화
        Document document = new Document();

        // 페이지 추가
        Page page = document.getPages().add();

        // 이미지 추가
        java.io.FileInputStream imageStream = null;
        try {
            imageStream = new FileInputStream("/storage/0F03-0F02/Android/data/com.aspose.pdf.examplecomplex/files/MyFileStorage/logo.png");
        } catch (Exception e) {
            e.printStackTrace();
        }

        // 페이지에 이미지 추가
        page.addImage(imageStream, new Rectangle(20, 730, 120, 830));

        // 헤더 추가
        TextFragment header = new TextFragment("2020년 가을 새로운 페리 노선");
        header.getTextState().setFont(FontRepository.findFont("Helvetica"));
        header.getTextState().setFontSize(24);
        header.setHorizontalAlignment(HorizontalAlignment.Center);
        header.setPosition(new Position(130, 720));
        page.getParagraphs().add(header);

        // 설명 추가
        String descriptionText = "방문객은 온라인으로 티켓을 구매해야 하며, 티켓은 " +
                "하루에 5,000장으로 제한됩니다. 페리 서비스는 절반의 수용 인원으로 운영되며 " +
                "축소된 일정으로 운영됩니다. 줄을 서야 할 수도 있습니다.";

        TextFragment description = new TextFragment(descriptionText);
        description.getTextState().setFont(FontRepository.findFont("Helvetica"));
        description.getTextState().setFontSize(14);
        description.setHorizontalAlignment(HorizontalAlignment.Left);
        page.getParagraphs().add(description);

        // 테이블 추가
        Table table = new Table();
        table.setColumnWidths("200");
        table.setBorder(new BorderInfo(BorderSide.Box, 1f, Color.getDarkSlateGray()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.Box, 0.5f, Color.getBlack()));
        table.getMargin().setBottom(10);
        table.getDefaultCellTextState().setFont(FontRepository.findFont("Times Roman"));

        Row headerRow = table.getRows().add();
        headerRow.getCells().add("출발 도시");
        headerRow.getCells().add("출발 섬");

        for (Cell headerRowCell : (Iterable<? extends Cell>) headerRow.getCells())
        {
            headerRowCell.setBackgroundColor(Color.getGray());
            headerRowCell.getDefaultCellTextState()
                    .setForegroundColor(Color.getWhiteSmoke().toRgb());
        }

        LocalTime time = LocalTime.of(6,0);
        Duration incTime = Duration.ofMinutes(30);

        for (int i = 0; i < 10; i++)
        {
            Row dataRow = table.getRows().add();
            dataRow.getCells().add(time.toString());
            time=time.plus(incTime);
            dataRow.getCells().add(time.toString());
        }

        page.getParagraphs().add(table);

        document.save("/storage/0F03-0F02/Android/data/com.aspose.pdf.examplecomplex/files/MyFileStorage/sample.pdf");

        Toast toast = Toast.makeText(MainActivity.this,
                "PDF 문서가 생성되었습니다!", Toast.LENGTH_LONG);
        toast.show();
    }

    private static boolean isExternalStorageReadOnly(){
        String extStorageState= Environment.getExternalStorageState();
        return Environment.MEDIA_MOUNTED_READ_ONLY.equals(extStorageState);
    }

    private static boolean isExternalStorageAvailable(){
        String extStorageState=Environment.getExternalStorageState();
        return Environment.MEDIA_MOUNTED.equals(extStorageState);
    }

}
```


```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    tools:context=".MainActivity">

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="32dp"
        android:layout_marginLeft="32dp"
        android:layout_marginRight="32dp"
        android:text="@string/title"
        android:textSize="24sp"
        android:visibility="visible"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

    <Button
        android:id="@+id/button"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="64dp"
        android:layout_marginLeft="32dp"
        android:layout_marginRight="32dp"
        android:text="@string/generate_btn" />

</LinearLayout>
```