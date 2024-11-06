title: Hello World Java Example
linktitle: Hello World Example
type: docs
weight: 20
url: ja/androidjava/hello-world-example/
description: このページは、Aspose.PDF for Androidを使用してテキスト - Hello Worldを含むPDFドキュメントを作成するための簡単なプログラミングの使用方法を示します。
lastmod: "2021-08-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Hello World Example

「Hello World」例は、プログラミング言語またはソフトウェアの機能を簡単なユースケースで紹介するために伝統的に使用されます。

Aspose.PDF for Android via Java APIは、Javaアプリケーション開発者がアプリケーション内でPDFファイルを作成、読み取り、編集、操作することを可能にします。これにより、PDFファイル形式への、またはPDFファイル形式からのいくつかの異なるファイルタイプを読み取り、変換することができます。このHello World記事では、Aspose.PDF for Android via Java APIを使用してJavaでPDFファイルを作成する方法を示します。
あなたの環境に[Installing Aspose.PDF for Android via Java](/pdf/androidjava/installation/)をインストールした後、以下のコードサンプルを実行して、Aspose.PDF APIがどのように機能するかを確認できます。

以下のコードスニペットはこれらのステップに従います:


1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document) オブジェクトをインスタンス化する
1. ドキュメントオブジェクトに[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/page)を追加する
1. [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment) オブジェクトを作成する
1. TextFragmentをページの[Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs)コレクションに追加する
1. 結果のPDFドキュメントを保存する

次のコードスニペットは、Aspose.PDF for Android APIの基本的な動作手順を示しています。

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
                // ドキュメントオブジェクトを初期化する
                Document document = new Document();

                // ページを追加する
                Page page = document.getPages().add();

                myData = inputText.getText().toString().trim();
                if (myData.equals("")) {
                    myData = "Hello, world!";
                }

                // 新しいページにテキストを追加する
                page.getParagraphs().add(new TextFragment(myData));

                // 更新されたPDFを保存する
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
                // ドキュメントオブジェクトを初期化する
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