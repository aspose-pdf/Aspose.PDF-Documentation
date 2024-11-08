---
title: ドキュメントを作成
type: docs
weight: 10
url: /ja/java/create-pdf-document/
description: Aspose.PDF for Java は、簡単なステップで PDF ドキュメントと検索可能な PDF ファイルを作成するのに役立ちます。
lastmod: "2021-06-05"
---

この記事では、Aspose.PDF for Java API を使用して Java アプリケーションで PDF ファイルを簡単に生成および読み取る方法を紹介します。

Aspose.PDF for Java API は、Java アプリケーション開発者がアプリケーションに PDF ドキュメント処理機能を組み込むことを可能にします。これにより、基盤となるマシンに他のソフトウェアをインストールすることなく、PDF ファイルを作成および読み取ることができます。Aspose.PDF for Java は、デスクトップ、JSP、JSF アプリケーションなど、さまざまな Java アプリケーションタイプで使用できます。

## Java を使用して PDF ファイルを作成する方法

Java を使用して PDF ファイルを作成するには、次の手順を使用します。

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) クラスのオブジェクトを作成します。

1. [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page) オブジェクトを Document オブジェクトの Pages コレクションに追加します
1. [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment) をページの [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/paragraphs) コレクションに追加します
1. 結果の PDF ドキュメントを保存します

```java
package com.aspose.pdf.examples;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Scanner;

import javax.imageio.ImageIO;

import com.aspose.pdf.*;
import com.aspose.pdf.Document.CallBackGetHocr;

public class ExampleCreate {
    
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    
    public static void Create() {        
        Document document = new Document();
 
        // ページを追加
        Page page = document.getPages().add();
         
        // 新しいページにテキストを追加
        page.getParagraphs().add(new TextFragment("Hello World!"));
         
        // 更新された PDF を保存
        document.save(_dataDir+"HelloWorld_out.pdf");
    }
```


この場合、A4サイズのページ、縦向きで1ページのPDFドキュメントを作成します。ページの左上には「Hello, World」が含まれます。

また、Aspose.PDF for Javaは検索可能なPDFを作成する機能を提供しています。次のコードスニペットを学びましょう:

```java
public static void CreateSearchablePDF() {                
        Document doc = new Document(_dataDir + "sample1.pdf");
        
        // コールバックを作成 - PDF画像のテキストを認識するロジック。外部のOCRはHOCR標準(http://en.wikipedia.org/wiki/HOCR)をサポートします。
        // 無料のGoogle Tesseract OCR(http://en.wikipedia.org/wiki/Tesseract_%28software%29)を使用しました。
        
        CallBackGetHocr cbgh = new CallBackGetHocr() {
            @Override
            public String invoke(java.awt.image.BufferedImage img) {
                File outputfile = new File(_dataDir + "test.jpg");
                try {
                    ImageIO.write(img, "jpg", outputfile);
                } catch (IOException e1) {
                    e1.printStackTrace();
                }
        
                try {
                    java.lang.Process process = Runtime.getRuntime().exec("tesseract" + " " + _dataDir + "test.jpg" + " " + _dataDir + "out hocr");
                    System.out.println("tesseract" + " " + _dataDir + "test.jpg" + " " + _dataDir + "out hocr");
                    process.waitFor();
        
                } catch (IOException e) {
                    e.printStackTrace();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
        
                // out.htmlを文字列に読み込む
                File file = new File(_dataDir + "out.hocr");
                StringBuilder fileContents = new StringBuilder((int) file.length());
                Scanner scanner = null;
                try {
                    scanner = new Scanner(file);
                    String lineSeparator = System.getProperty("line.separator");
        
                    while (scanner.hasNextLine()) {
                        fileContents.append(scanner.nextLine() + lineSeparator);
                    }
                } catch (FileNotFoundException e) {
                    e.printStackTrace();
                } finally {
                    if (scanner != null)
                        scanner.close();
                }
        
                // 一時ファイルを削除
                File fileOut = new File(_dataDir + "out.hocr");
                if (fileOut.exists()) {
                    fileOut.delete();
                }
                File fileTest = new File(_dataDir + "test.jpg");
                if (fileTest.exists()) {
                    fileTest.delete();
                }
        
                return fileContents.toString();
            }
        };
        // コールバック終了
        
        doc.convert(cbgh);
        doc.save(_dataDir + "output971.pdf");        
    }
}
```