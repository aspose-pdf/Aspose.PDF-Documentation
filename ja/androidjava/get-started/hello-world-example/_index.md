---
title: Hello World Java のサンプル
linktitle: Hello World の例
type: docs
weight: 20
url: /ja/androidjava/hello-world-example/
description: このページでは、Aspose.PDF for Android を使用してテキスト - Hello World を含む PDF ドキュメントを作成するためのシンプルなプログラミング方法を示します。
lastmod: "2026-07-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Hello World の例

「Hello World」例は、プログラミング言語やソフトウェアの機能を簡単な使用例で紹介するために伝統的に使用されます。

Aspose.PDF for Android via Java API は、Java アプリケーション開発者がアプリケーション内で PDF ファイルを作成、読み取り、編集、操作できるようにします。PDF ファイル形式への変換や、さまざまなファイルタイプの読み取り・変換も可能です。この Hello World 記事では、Aspose.PDF for Android via Java API を使用して Java で PDF ファイルを作成する方法を示します。
後 [Java 経由で Android 用 Aspose.PDF をインストールする](/pdf/ja/androidjava/installation/) 環境で、以下のコードサンプルを実行して Aspose.PDF API がどのように動作するかを確認できます。

以下のコードスニペットは次の手順に従います：

1. インスタンス化する [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document) オブジェクト
1. 追加 [ページ](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/page) ドキュメントオブジェクトへ
1. 作成 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment) オブジェクト
1. TextFragmentを追加 [段落](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) ページのコレクション
1. 結果のPDFドキュメントを保存する

以下のコードスニペットは、Aspose.PDF for Android API の動作の基本的な手順を示しています。

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

