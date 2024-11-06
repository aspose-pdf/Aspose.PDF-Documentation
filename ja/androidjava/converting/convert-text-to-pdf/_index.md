---
title: テキストをPDFに変換 
linktitle: テキストをPDFに変換
type: docs
weight: 300
url: ja/androidjava/convert-text-to-pdf/
lastmod: "2021-06-05"
description: Aspose.PDF for Android via Javaを使用すると、プレーンテキストファイルをPDFに変換したり、事前にフォーマットされたテキストファイルをPDFに変換したりできます。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}} 

オンラインで試すことができます。Aspose.PDFの変換品質を確認し、結果をオンラインで表示できます。このリンクで確認できます [products.aspose.app/pdf/conversion/txt-to-pdf](https://products.aspose.app/pdf/conversion/txt-to-pdf)

{{% /alert %}}

**Aspose.PDF for Android via Java** は、テキストファイルをPDF形式に変換する機能を提供します。この記事では、Aspose.PDFを使用してテキストファイルをPDFにどれほど簡単かつ効率的に変換できるかを示します。

テキストファイルをPDFに変換する必要がある場合、最初にソースのテキストファイルを何らかのリーダーで読み込みます。
 StringBuilderを使用してテキストファイルの内容を読み込みました。Documentオブジェクトをインスタンス化し、Pagesコレクションに新しいページを追加します。TextFragmentの新しいオブジェクトを作成し、そのコンストラクタにStringBuilderオブジェクトを渡します。TextFragmentオブジェクトを使用してParagraphsコレクションに新しい段落を追加し、DocumentクラスのSaveメソッドを使用して結果のPDFファイルを保存します。

## プレーンテキストファイルをPDFに変換

```java
public void convertTXTtoPDF_Simple () {
        // ドキュメントオブジェクトを初期化

        File pdfDocumentFileName=new File(fileStorage, "demo_txt.pdf");
        File txtDocumentFileName=new File(fileStorage, "Conversion/rfc822.txt");

        // 空のコンストラクタを呼び出してDocumentオブジェクトをインスタンス化
        document=new Document();

        // DocumentのPagesコレクションに新しいページを追加
        Page page=document.getPages().add();

        String string;
        StringBuilder stringBuilder=new StringBuilder();
        InputStream is;
        try {
            is=new FileInputStream(txtDocumentFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        BufferedReader reader=new BufferedReader(new InputStreamReader(is));
        while (true) {
            try {
                if ((string=reader.readLine()) == null) break;
            } catch (IOException e) {
                resultMessage.setText(e.getMessage());
                return;
            }
            stringBuilder.append(string).append("\n");
        }
        try {
            is.close();
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }


        // TextFragmentのインスタンスを作成し、readerオブジェクトからのテキストを引数として
        // コンストラクタに渡す
        TextFragment text=new TextFragment(stringBuilder.toString());

        // 段落コレクションに新しいテキスト段落を追加し、TextFragmentオブジェクトを渡す
        page.getParagraphs().add(text);

        // 結果のPDFファイルを保存
        try {
            document.save(pdfDocumentFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```

## プレフォーマットされたテキストファイルをPDFに変換する

```java
    public void convertPreFormattedTextToPdf () {

        File txtDocumentFile=new File(fileStorage, "Conversion/rfc822.txt");
        File pdfDocumentFileName=new File(fileStorage, "demo_txt.pdf");
        Path txtDocumentFileName=Paths.get(txtDocumentFile.toString());

        // テキストファイルを文字列の配列として読み込む
        List<String> lines;
        try {
            lines=Files.readAllLines(txtDocumentFileName, ENCODING);
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // 空のコンストラクタを呼び出してDocumentオブジェクトをインスタンス化する
        document=new Document();

        // DocumentのPagesコレクションに新しいページを追加する
        Page page=document.getPages().add();
        int count=4;

        Font font=FontRepository.findFont("Droid Sans Mono");
        // より良いプレゼンテーションのために左右のマージンを設定する
        page.getPageInfo().getMargin().setLeft(20);
        page.getPageInfo().getMargin().setRight(10);
        page.getPageInfo().getDefaultTextState().setFont(font);
        page.getPageInfo().getDefaultTextState().setFontSize(12);

        for (String line : lines) {
            // 行が「改ページ」文字を含むかどうかを確認する
            // https://en.wikipedia.org/wiki/Page_break を参照
            if (line.startsWith("\f")) {
                page=document.getPages().add();
                page.getPageInfo().getMargin().setLeft(20);
                page.getPageInfo().getMargin().setRight(10);
                page.getPageInfo().getDefaultTextState().setFont(font);
                page.getPageInfo().getDefaultTextState().setFontSize(12);
            } else {
                // TextFragmentのインスタンスを作成し、
                // そのコンストラクタに行を引数として渡す
                TextFragment text=new TextFragment(line);

                // 段落コレクションに新しいテキスト段落を追加し、TextFragmentオブジェクトを渡す
                page.getParagraphs().add(text);
            }
        }
        // 結果のPDFファイルを保存する
        try {
            document.save(pdfDocumentFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```