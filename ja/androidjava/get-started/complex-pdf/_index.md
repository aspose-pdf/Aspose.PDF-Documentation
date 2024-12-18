---
title: 複雑なPDFをAspose.PDFで作成する
linktitle: 複雑なPDFを作成する
type: docs
weight: 30
url: /ja/androidjava/complex-pdf-example/
description: Aspose.PDF for Android via Javaを使用すると、1つのドキュメントに画像、テキストフラグメント、テーブルを含むより複雑なドキュメントを作成できます。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

[Hello, World](/pdf/ja/java/hello-world-example/) の例では、JavaとAspose.PDFを使用してPDFドキュメントを作成する簡単なステップを示しました。この記事では、JavaとAspose.PDF for Javaを使用して、より複雑なドキュメントを作成する方法を見ていきます。例として、架空の会社が運営する旅客フェリーサービスのドキュメントを取り上げます。
私たちのドキュメントには、画像、2つのテキストフラグメント（ヘッダーと段落）、およびテーブルが含まれます。このようなドキュメントを作成するために、DOMベースのアプローチを使用します。詳細は、[DOM APIの基本](/pdf/ja/java/basics-of-dom-api/)のセクションで読むことができます。

ドキュメントをゼロから作成する場合、特定の手順に従う必要があります：

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) オブジェクトをインスタンス化します。このステップでは、メタデータはあるがページのない空のPDFドキュメントを作成します。
1. ドキュメントオブジェクトに [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page) を追加します。これで、ドキュメントには1ページが含まれます。
1. 画像を追加するために、FileInputStreamを作成し、必要なファイルへのパスを指定します。次に、指定された座標の矩形に画像を追加します。
1. ヘッダー用の [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) を作成します。ヘッダーには、フォントサイズ24ptのArialフォントと中央揃えを使用します。
1. ヘッダーをページの [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--) に追加します。
1. 説明用の [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) を作成します。説明には、フォントサイズ24ptのArialフォントと中央揃えを使用します。

1. ページの段落に（説明）を追加します。例では「Helvetica」と「Times Roman」フォントを使用しましたが、Androidにはシステム全体で使用できるフォントが3つしかないことを忘れないでください。

- normal (Droid Sans);
- serif (Droid Serif);
- monospace (Droid Sans Mono).

1. テーブルを作成し、テーブルのプロパティを追加します。
1. ページに（テーブル）を[段落](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--)として追加します。
1. ドキュメントを「Complex.pdf」として保存します。

最後に、「PDFドキュメントが生成されました！」というメッセージのポップアップが表示されます。

![Aspose.PDFの複雑な例（Java経由のAndroid）](complex_example.png)

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
        // ドキュメントオブジェクトを初期化
        Document document = new Document();

        // ページを追加
        Page page = document.getPages().add();

        // 画像を追加
        java.io.FileInputStream imageStream = null;
        try {
            imageStream = new FileInputStream("/storage/0F03-0F02/Android/data/com.aspose.pdf.examplecomplex/files/MyFileStorage/logo.png");
        } catch (Exception e) {
            e.printStackTrace();
        }

        // 画像をページに追加
        page.addImage(imageStream, new Rectangle(20, 730, 120, 830));

        // ヘッダーを追加
        TextFragment header = new TextFragment("2020年秋の新しいフェリー路線");
        header.getTextState().setFont(FontRepository.findFont("Helvetica"));
        header.getTextState().setFontSize(24);
        header.setHorizontalAlignment (HorizontalAlignment.Center);
        header.setPosition(new Position(130, 720));
        page.getParagraphs().add(header);

        // 説明を追加
        String descriptionText = "訪問者はオンラインでチケットを購入する必要があり、チケットは1日あたり5,000枚に制限されています。フェリーサービスは半分の容量で運行されており、" +
                "スケジュールが削減されています。行列が予想されます。";

        TextFragment description = new TextFragment(descriptionText);
        description.getTextState().setFont(FontRepository.findFont("Helvetica"));
        description.getTextState().setFontSize(14);
        description.setHorizontalAlignment(HorizontalAlignment.Left);
        page.getParagraphs().add(description);

        // テーブルを追加
        Table table = new Table();
        table.setColumnWidths("200");
        table.setBorder(new BorderInfo(BorderSide.Box, 1f, Color.getDarkSlateGray()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.Box, 0.5f, Color.getBlack()));
        table.getMargin().setBottom(10);
        table.getDefaultCellTextState().setFont(FontRepository.findFont("Times Roman"));

        Row headerRow = table.getRows().add();
        headerRow.getCells().add("出発都市");
        headerRow.getCells().add("出発島");

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
                "PDFドキュメントが生成されました！", Toast.LENGTH_LONG);
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